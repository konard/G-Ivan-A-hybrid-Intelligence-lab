#!/usr/bin/env python3
"""Сбор фактической стоимости AI-сессий по закрытым PR двух репозиториев.

Контракт: стоимость берётся ТОЛЬКО из явных числовых маркеров в теле PR или в
комментариях к нему. Никаких оценок, экстраполяций и достроек. PR без маркера
попадает в список «стоимость не указана», а не получает вычисленное значение.

Запуск:
    python3 collect-pr-costs.py --out pr-cost-dataset.json

Требуется авторизованный `gh` CLI. Сеть используется только на чтение.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import subprocess
import sys

REPOS = [
    ("G-Ivan-A/hybrid-Intelligence-lab", "Hub"),
    ("G-Ivan-A/mango_ba_prompts", "Mango"),
]

# --- Явные маркеры стоимости, встречающиеся в логах AI working session --------
# 1) актуальный формат Claude Code:  "### 💰 Cost: **$7.396399**"
RE_COST_REPORTED = re.compile(r"💰\s*Cost:\s*\*\*\$([0-9]+(?:\.[0-9]+)?)\*\*")
# 2) ранний формат: "- Calculated by Anthropic: $1.364229 USD" (цифра провайдера)
RE_COST_PROVIDER = re.compile(r"Calculated by Anthropic:\s*\$([0-9]+(?:\.[0-9]+)?)")
# 3) формат Codex и ранний Claude: "- Public pricing estimate: $1.703172 USD"
RE_COST_PUBLIC = re.compile(r"Public pricing estimate:\s*\$([0-9]+(?:\.[0-9]+)?)")

RE_MODEL_BOLD = re.compile(r"\*\*Model:\s*([^*]+)\*\*")
RE_MODEL_LINE = re.compile(r"^- Model:\s*(.+)$", re.M)
RE_TOOL = re.compile(r"^- Tool:\s*(.+)$", re.M)
RE_REQUESTED = re.compile(r"^- Requested:\s*(.+)$", re.M)

PR_FIELDS = "number,title,url,createdAt,closedAt,mergedAt,author"


def gh_json(args: list[str]):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def gh_jsonl(args: list[str]):
    out = subprocess.run(["gh", *args], check=True, capture_output=True, text=True).stdout
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def parse_session(body: str):
    """Разбирает один лог AI-сессии. Возвращает None, если стоимости в нём нет."""
    if not body or ("💰" not in body and "Cost estimation" not in body):
        return None

    cost = source = None
    for regex, label in (
        (RE_COST_REPORTED, "reported"),          # итог, напечатанный инструментом
        (RE_COST_PROVIDER, "provider-calculated"),  # цифра, посчитанная провайдером
        (RE_COST_PUBLIC, "public-pricing"),      # оценка по публичному прайсу
    ):
        m = regex.search(body)
        if m:
            cost, source = float(m.group(1)), label
            break
    if cost is None:
        return None

    m = RE_MODEL_BOLD.search(body) or RE_MODEL_LINE.search(body)
    model = m.group(1).strip() if m else None
    if model is None:
        # Ранний формат лога не печатал точное имя модели, но печатал запрошенный
        # алиас: "- Requested: `opus` (`claude-opus-4-8`)".
        m = RE_REQUESTED.search(body)
        if m:
            alias = m.group(1).strip().strip("`").split("`")[0].strip()
            if alias:
                model = "Claude " + alias.capitalize()

    m = RE_TOOL.search(body)
    tool = m.group(1).strip() if m else None
    if tool is None:
        if model and model.lower().startswith("gpt"):
            tool = "OpenAI Codex"
        elif RE_COST_REPORTED.search(body) or RE_COST_PROVIDER.search(body):
            # Обе эти цифры печатает только Claude Code.
            tool = "Anthropic Claude Code"

    return {"cost_usd": cost, "cost_source": source, "tool": tool, "model": model}


def model_family(session) -> str:
    model = (session.get("model") or "").lower()
    tool = (session.get("tool") or "").lower()
    if "codex" in tool or model.startswith("gpt"):
        return "Codex"
    if "opus" in model:
        return "Opus"
    if "claude" in tool or "claude" in model:
        return "Claude (иные модели)"
    return "Не определено"


def collect(repo: str, label: str):
    prs = gh_json(["pr", "list", "--repo", repo, "--state", "closed",
                   "--limit", "2000", "--json", PR_FIELDS + ",body"])
    by_number = {}
    for pr in prs:
        pr["repo"] = label
        pr["sessions"] = []
        session = parse_session(pr.pop("body", "") or "")
        if session:
            pr["sessions"].append(session)
        by_number[pr["number"]] = pr

    # Один запрос на весь репозиторий вместо запроса на каждый PR.
    comments = gh_jsonl(["api", f"repos/{repo}/issues/comments", "--paginate",
                         "--jq", ".[] | {issue: .issue_url, body: .body}"])
    for comment in comments:
        number = int(comment["issue"].rsplit("/", 1)[1])
        pr = by_number.get(number)
        if pr is None:
            continue  # комментарий к issue или к ещё открытому PR
        session = parse_session(comment["body"] or "")
        if session:
            pr["sessions"].append(session)

    for pr in by_number.values():
        pr["author"] = (pr.get("author") or {}).get("login")
        pr["total_cost_usd"] = round(sum(s["cost_usd"] for s in pr["sessions"]), 6)
        for session in pr["sessions"]:
            session["family"] = model_family(session)
    return sorted(by_number.values(), key=lambda p: p["number"])


def summarize(prs):
    by_family = collections.defaultdict(lambda: {"sessions": 0, "cost_usd": 0.0})
    by_model = collections.defaultdict(lambda: {"sessions": 0, "cost_usd": 0.0})
    by_month = collections.defaultdict(lambda: collections.Counter())
    by_source = collections.Counter()
    for pr in prs:
        for key, stamp in (("created", pr["createdAt"]), ("closed", pr["closedAt"])):
            bucket = by_month[(key, (stamp or "")[:7], pr["repo"])]
            bucket["prs"] += 1
            if not pr["sessions"]:
                bucket["prs_without_cost"] += 1
            for session in pr["sessions"]:
                bucket["sessions"] += 1
                bucket["cost_usd"] += session["cost_usd"]
                bucket["sessions_" + session["family"]] += 1
                bucket["cost_" + session["family"]] += session["cost_usd"]
        for session in pr["sessions"]:
            fam = by_family[(pr["repo"], session["family"])]
            fam["sessions"] += 1
            fam["cost_usd"] += session["cost_usd"]
            mod = by_model[session["model"] or "не указана"]
            mod["sessions"] += 1
            mod["cost_usd"] += session["cost_usd"]
            by_source[session["cost_source"]] += 1

    def rnd(d):
        return {k: (round(v, 6) if isinstance(v, float) else v) for k, v in d.items()}

    session_costs = sorted(s["cost_usd"] for p in prs for s in p["sessions"])
    pr_costs = sorted(p["total_cost_usd"] for p in prs if p["sessions"])
    top = sorted((p for p in prs if p["sessions"]), key=lambda p: -p["total_cost_usd"])[:10]

    return {
        "data_horizon": {
            "earliest_created_at": min((p["createdAt"] or "") for p in prs),
            "earliest_closed_at": min((p["closedAt"] or "") for p in prs),
            "latest_closed_at": max((p["closedAt"] or "") for p in prs),
        },
        "cost_stats": {
            "prs_with_cost": len(pr_costs),
            "sessions": len(session_costs),
            "total_usd": round(sum(session_costs), 6),
            "avg_per_pr_usd": round(sum(pr_costs) / len(pr_costs), 6) if pr_costs else 0.0,
            "median_pr_usd": round(pr_costs[len(pr_costs) // 2], 6) if pr_costs else 0.0,
            "avg_per_session_usd": round(sum(session_costs) / len(session_costs), 6) if session_costs else 0.0,
            "median_session_usd": round(session_costs[len(session_costs) // 2], 6) if session_costs else 0.0,
            "min_session_usd": session_costs[0] if session_costs else 0.0,
            "max_session_usd": session_costs[-1] if session_costs else 0.0,
            "prs_with_multiple_sessions": sum(1 for p in prs if len(p["sessions"]) > 1),
        },
        "top_prs_by_cost": [
            {"repo": p["repo"], "number": p["number"], "url": p["url"],
             "cost_usd": p["total_cost_usd"], "sessions": len(p["sessions"]),
             "title": p["title"]}
            for p in top
        ],
        "totals": {
            repo: {
                "closed_prs": sum(1 for p in prs if p["repo"] == repo),
                "merged": sum(1 for p in prs if p["repo"] == repo and p["mergedAt"]),
                "closed_unmerged": sum(1 for p in prs if p["repo"] == repo and not p["mergedAt"]),
                "prs_with_cost": sum(1 for p in prs if p["repo"] == repo and p["sessions"]),
                "prs_without_cost": sum(1 for p in prs if p["repo"] == repo and not p["sessions"]),
                "sessions": sum(len(p["sessions"]) for p in prs if p["repo"] == repo),
                "cost_usd": round(sum(p["total_cost_usd"] for p in prs if p["repo"] == repo), 6),
            }
            for repo in dict.fromkeys(p["repo"] for p in prs)
        },
        "by_family": {f"{k[0]}|{k[1]}": rnd(v) for k, v in sorted(by_family.items())},
        "by_model": {k: rnd(v) for k, v in sorted(by_model.items(), key=lambda kv: -kv[1]["cost_usd"])},
        "by_month": {f"{k[0]}|{k[1]}|{k[2]}": rnd(dict(v)) for k, v in sorted(by_month.items())},
        "by_cost_source": dict(by_source),
        "prs_without_cost": [
            {"repo": p["repo"], "number": p["number"], "url": p["url"],
             "closed_month": (p["closedAt"] or "")[:7],
             "merged": bool(p["mergedAt"]), "title": p["title"]}
            for p in prs if not p["sessions"]
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="pr-cost-dataset.json")
    args = parser.parse_args()

    prs = []
    for repo, label in REPOS:
        print(f"fetching {repo} ...", file=sys.stderr)
        prs.extend(collect(repo, label))

    dataset = {"summary": summarize(prs), "pull_requests": prs}
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(dataset, fh, ensure_ascii=False, indent=2, sort_keys=False)
        fh.write("\n")

    s = dataset["summary"]
    for repo, t in s["totals"].items():
        print(f"{repo}: закрытых PR={t['closed_prs']} (merged={t['merged']}, "
              f"closed-unmerged={t['closed_unmerged']}), со стоимостью={t['prs_with_cost']}, "
              f"без стоимости={t['prs_without_cost']}, сессий={t['sessions']}, "
              f"сумма=${t['cost_usd']:.2f}")
    print("\nмодельные семейства:")
    for key, v in s["by_family"].items():
        print(f"  {key:34} сессий={v['sessions']:4} ${v['cost_usd']:.2f}")
    print("\nмодели:")
    for key, v in s["by_model"].items():
        print(f"  {key:22} сессий={v['sessions']:4} ${v['cost_usd']:.2f}")
    print("\nмесяцы:")
    for key, v in s["by_month"].items():
        print(f"  {key:22} PR={v['prs']:4} без стоимости={v.get('prs_without_cost', 0):3} "
              f"сессий={v.get('sessions', 0):4} ${v.get('cost_usd', 0.0):.2f} "
              f"Codex=${v.get('cost_Codex', 0.0):.2f}/{v.get('sessions_Codex', 0)} "
              f"Opus=${v.get('cost_Opus', 0.0):.2f}/{v.get('sessions_Opus', 0)} "
              f"Claude-иные=${v.get('cost_Claude (иные модели)', 0.0):.2f}/"
              f"{v.get('sessions_Claude (иные модели)', 0)}")
    print("\nгоризонт данных:", s["data_horizon"])
    print("статистика:", s["cost_stats"])
    print("\nисточник цифры:", s["by_cost_source"])
    print("\nPR без данных о стоимости:")
    for pr in s["prs_without_cost"]:
        print(f"  {pr['repo']:6} #{pr['number']:<4} {pr['closed_month']} {pr['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
