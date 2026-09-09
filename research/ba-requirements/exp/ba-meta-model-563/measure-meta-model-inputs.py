#!/usr/bin/env python3
"""Замер входов канонической BA Meta-Model по корпусу спицы mango_ba_prompts.

Issue #563 требует синтеза четырёх канонических таксономий (артефакты,
операции, процессы, продукты) и перевода режимов запуска `stepwise`,
`oneshot`, `legacy` в статус `deprecated`. Оба решения проверяемы только на
измеренном корпусе, поэтому скрипт отвечает на пять вопросов:

1. Сколько активных промптов в спице и во что разбирается их имя
   (`<предмет>-<операция>-<режим>`); какова кратность дублирования одной
   способности по режимам запуска.
2. Насколько варианты одной способности расходятся по скелету: если режим —
   форма доставки, скелеты вариантов должны совпадать; если режим несёт
   содержание, его нельзя снять переносом.
3. Какие промпты действительно используются прогонами (`related_artifacts`
   в `metadata.yaml`) и как распределены прогоны по режимам.
4. Какие из объявленных операций и процессов покрыты промптами и прогонами,
   а какие объявлены и не исполняются.
5. Сколько прогонов объявляют продукт или домен — то есть возможно ли
   связать артефакт с продуктовой таксономией без её формализации.

Скрипт ничего не интерпретирует: интерпретация — в датированном отчёте
research/ba-requirements/2026-09-08-meta-model-inputs-facts.md.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# Режимы запуска промптов, объявленные в docs/ba-processes/00-index.md спицы.
RUN_MODES = ("stepwise", "oneshot", "legacy")

# Словарь операций БА, объявленный в docs/taxonomy.md спицы (9 базовых + 4 расширения).
DECLARED_OPERATIONS = (
    "ingestion",
    "understanding",
    "validation",
    "modeling",
    "solution_design",
    "documentation",
    "quality",
    "research",
    "governance",
    "impact_analysis",
    "reverse_requirements",
    "risk_analysis",
    "release_readiness",
)

# Девять процессов БА, объявленных в docs/taxonomy.md спицы.
DECLARED_PROCESSES = (
    "fr-generation",
    "fr-validation",
    "tender-analysis",
    "uc-us-modeling",
    "uml-bpmn-visualization",
    "po-pm-support",
    "statistics",
    "impact-analysis",
    "risk-analysis",
)

# Домены продуктовой таксономии Манго (L2), standards/product-classification-contract.md.
PRODUCT_DOMAINS = (
    "voice-ucaas",
    "contact-center",
    "digital-channels",
    "ai-automation",
    "analytics",
    "hardware",
    "security",
)

# Лексические маркеры доменов в русскоязычных текстах прогонов.
DOMAIN_MARKERS = {
    "voice-ucaas": ("ватс", "виртуальная атс", "sip", "телефони"),
    "contact-center": ("контакт-центр", "оператор", "очеред", "ivr", "обзвон"),
    "digital-channels": ("чат", "мессенджер", "whatsapp", "telegram", "виджет"),
    "ai-automation": ("робот", "распознавани", "речевая аналитик", "бот"),
    "analytics": ("отчёт", "отчет", "статистик", "коллтрекинг", "аналитик"),
    "hardware": ("шлюз", "оборудовани", "устройств", "гарнитур"),
    "security": ("доступ", "прав", "аутентификац", "безопасност"),
}

PROMPT_NAME_RE = re.compile(r"^(?P<subject>.+)-(?P<operation>[a-z_]+)-(?P<mode>%s)$" % "|".join(RUN_MODES))

# Операции в именах промптов записаны через дефис, в словаре — через подчёркивание.
OPERATION_ALIASES = {"solution-design": "solution_design"}

SECTION_RE = re.compile(r"^\s*(?:#{1,6}\s*)?(\d+)[.)]\s*(.+?)\s*$")


def git_commit(root: Path) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def parse_prompt_name(stem: str) -> dict | None:
    match = PROMPT_NAME_RE.match(stem)
    if not match:
        return None
    operation = match.group("operation").replace("-", "_")
    subject = match.group("subject")
    # `solution-design` попадает в имя двумя словами: последнее слово ушло в operation.
    if operation == "design" and subject.endswith("-solution"):
        subject, operation = subject[: -len("-solution")], "solution_design"
    return {"subject": subject, "operation": operation, "mode": match.group("mode")}


def section_skeleton(text: str) -> list[str]:
    """Подписи нумерованных разделов промпта в порядке появления.

    Подпись огрубляется до части строки до первого двоеточия: в корпусе за
    двоеточием идёт содержание раздела, а не его имя, и сравнение полной строки
    измеряло бы совпадение текста, а не совпадение структуры.
    """
    skeleton: list[str] = []
    for line in text.splitlines():
        match = SECTION_RE.match(line)
        if not match:
            continue
        title = match.group(2).split(":", 1)[0].strip().strip("*.").lower()
        title = re.sub(r"\s+", " ", title)
        if not title or len(title) > 60:
            continue
        skeleton.append(title)
    return skeleton


def jaccard(left: set[str], right: set[str]) -> float:
    if not left and not right:
        return 1.0
    return round(len(left & right) / len(left | right), 3)


def collect_prompts(mango: Path) -> tuple[list[dict], list[str]]:
    prompts: list[dict] = []
    unparsed: list[str] = []
    for path in sorted((mango / "prompts").glob("*.md")):
        if path.name.startswith("README") or ".executable" in path.name:
            continue
        parsed = parse_prompt_name(path.stem)
        if parsed is None:
            unparsed.append(path.name)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        skeleton = section_skeleton(text)
        prompts.append(
            {
                "file": f"prompts/{path.name}",
                **parsed,
                "lines": len(text.splitlines()),
                "chars": len(text),
                "sections": len(skeleton),
                "skeleton": skeleton,
            }
        )
    return prompts, unparsed


def collect_runs(mango: Path) -> list[dict]:
    runs: list[dict] = []
    for meta in sorted((mango / "runs").rglob("metadata.yaml")):
        text = meta.read_text(encoding="utf-8", errors="replace")
        process = ""
        process_match = re.search(r"^process:\s*\"?([^\"\n]+)\"?", text, re.MULTILINE)
        if process_match:
            process = process_match.group(1).strip()
        referenced = sorted(set(re.findall(r"prompts/([a-z0-9\-_]+\.md)", text)))
        body = "\n".join(
            p.read_text(encoding="utf-8", errors="replace")
            for p in meta.parent.rglob("*.md")
        ).lower()
        domains = sorted(
            domain
            for domain, markers in DOMAIN_MARKERS.items()
            if any(marker in body for marker in markers)
        )
        declared_domain = sorted(d for d in PRODUCT_DOMAINS if d in text.lower())
        runs.append(
            {
                "run": meta.parent.name,
                "process": process,
                "prompts": referenced,
                "modes": sorted({m for m in RUN_MODES for p in referenced if p.endswith(f"-{m}.md")}),
                "lexical_domains": domains,
                "declared_domains": declared_domain,
            }
        )
    return runs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mango", required=True, type=Path, help="клон mango_ba_prompts")
    parser.add_argument("--json", type=Path, default=Path("meta-model-inputs.json"))
    args = parser.parse_args()

    mango: Path = args.mango
    if not (mango / "prompts").is_dir():
        print(f"ERROR: {mango} не похож на клон mango_ba_prompts", file=sys.stderr)
        return 2

    prompts, unparsed = collect_prompts(mango)
    runs = collect_runs(mango)

    # 1. Кратность дублирования способности по режимам запуска.
    capabilities: dict[str, dict] = {}
    for prompt in prompts:
        key = f"{prompt['subject']}-{prompt['operation']}"
        entry = capabilities.setdefault(key, {"capability": key, "operation": prompt["operation"], "variants": []})
        entry["variants"].append(prompt)

    capability_rows = []
    for key, entry in sorted(capabilities.items()):
        variants = entry["variants"]
        modes = sorted(v["mode"] for v in variants)
        pairs = []
        for i in range(len(variants)):
            for j in range(i + 1, len(variants)):
                left, right = variants[i], variants[j]
                pairs.append(
                    {
                        "modes": [left["mode"], right["mode"]],
                        "skeleton_jaccard": jaccard(set(left["skeleton"]), set(right["skeleton"])),
                        "same_order": left["skeleton"] == right["skeleton"],
                        "size_ratio": round(
                            max(left["chars"], right["chars"]) / max(1, min(left["chars"], right["chars"])), 2
                        ),
                    }
                )
        capability_rows.append(
            {
                "capability": key,
                "operation": entry["operation"],
                "modes": modes,
                "variant_count": len(variants),
                "pairs": pairs,
            }
        )

    multi_mode = [row for row in capability_rows if row["variant_count"] > 1]
    all_pairs = [p for row in capability_rows for p in row["pairs"]]
    mean_jaccard = round(sum(p["skeleton_jaccard"] for p in all_pairs) / len(all_pairs), 3) if all_pairs else None
    identical_pairs = [p for p in all_pairs if p["skeleton_jaccard"] == 1.0]

    # 2. Использование промптов и режимов прогонами.
    mode_runs = {mode: sum(1 for r in runs if mode in r["modes"]) for mode in RUN_MODES}
    runs_without_prompt = [r["run"] for r in runs if not r["prompts"]]
    referenced_prompts = sorted({p for r in runs for p in r["prompts"]})
    prompt_files = {Path(p["file"]).name for p in prompts}
    never_referenced = sorted(prompt_files - set(referenced_prompts))

    # 3. Покрытие операций и процессов.
    prompt_operations = {p["operation"] for p in prompts}
    operations_without_prompt = sorted(set(DECLARED_OPERATIONS) - prompt_operations)
    operations_outside_dictionary = sorted(prompt_operations - set(DECLARED_OPERATIONS))
    run_processes = {r["process"] for r in runs if r["process"]}
    processes_declared_hit = sorted(run_processes & set(DECLARED_PROCESSES))
    processes_never_run = sorted(set(DECLARED_PROCESSES) - run_processes)
    runs_outside_process_dictionary = sorted(run_processes - set(DECLARED_PROCESSES))

    # 4. Продуктовая привязка прогонов.
    runs_with_declared_domain = [r["run"] for r in runs if r["declared_domains"]]
    runs_single_lexical_domain = [r["run"] for r in runs if len(r["lexical_domains"]) == 1]
    runs_multi_lexical_domain = [r["run"] for r in runs if len(r["lexical_domains"]) > 1]
    runs_no_lexical_domain = [r["run"] for r in runs if not r["lexical_domains"]]

    result = {
        "corpus": {"path": str(mango), "commit": git_commit(mango), "runs": len(runs), "prompts": len(prompts)},
        "prompts": {
            "active": len(prompts),
            "unparsed_names": unparsed,
            "by_mode": {mode: sum(1 for p in prompts if p["mode"] == mode) for mode in RUN_MODES},
            "capabilities": len(capability_rows),
            "capabilities_with_multiple_modes": len(multi_mode),
            "duplication_factor": round(len(prompts) / max(1, len(capability_rows)), 2),
            "mode_pairs": len(all_pairs),
            "mean_skeleton_jaccard": mean_jaccard,
            "identical_skeleton_pairs": len(identical_pairs),
            "never_referenced_by_runs": never_referenced,
        },
        "runs": {
            "total": len(runs),
            "by_mode": mode_runs,
            "without_prompt_reference": len(runs_without_prompt),
            "distinct_prompts_referenced": len(referenced_prompts),
        },
        "operations": {
            "declared": len(DECLARED_OPERATIONS),
            "covered_by_prompts": sorted(prompt_operations & set(DECLARED_OPERATIONS)),
            "declared_without_prompt": operations_without_prompt,
            "used_outside_dictionary": operations_outside_dictionary,
        },
        "processes": {
            "declared": len(DECLARED_PROCESSES),
            "declared_seen_in_runs": processes_declared_hit,
            "declared_never_run": processes_never_run,
            "run_labels_outside_dictionary": len(runs_outside_process_dictionary),
            "run_labels_outside_dictionary_sample": runs_outside_process_dictionary[:10],
        },
        "products": {
            "domains": list(PRODUCT_DOMAINS),
            "runs_with_declared_domain": len(runs_with_declared_domain),
            "runs_with_single_lexical_domain": len(runs_single_lexical_domain),
            "runs_with_multiple_lexical_domains": len(runs_multi_lexical_domain),
            "runs_without_lexical_domain": len(runs_no_lexical_domain),
        },
        "detail": {"capability_rows": capability_rows, "run_rows": runs},
    }

    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    s = result
    print(f"corpus commit: {s['corpus']['commit']}")
    print(f"активных промптов: {s['prompts']['active']}, по режимам: {s['prompts']['by_mode']}")
    print(f"способностей (предмет+операция): {s['prompts']['capabilities']}, "
          f"с несколькими режимами: {s['prompts']['capabilities_with_multiple_modes']}, "
          f"кратность дублирования: {s['prompts']['duplication_factor']}")
    print(f"пар вариантов одной способности: {s['prompts']['mode_pairs']}, "
          f"средний Жаккар скелетов: {s['prompts']['mean_skeleton_jaccard']}, "
          f"совпадающих скелетов: {s['prompts']['identical_skeleton_pairs']}")
    print(f"промптов, ни разу не упомянутых прогонами: {len(s['prompts']['never_referenced_by_runs'])}")
    print(f"прогонов: {s['runs']['total']}, по режимам: {s['runs']['by_mode']}, "
          f"без ссылки на промпт: {s['runs']['without_prompt_reference']}")
    print(f"операций объявлено: {s['operations']['declared']}, "
          f"без промпта: {s['operations']['declared_without_prompt']}")
    print(f"процессов объявлено: {s['processes']['declared']}, "
          f"встретились в прогонах: {s['processes']['declared_seen_in_runs']}, "
          f"меток вне словаря: {s['processes']['run_labels_outside_dictionary']}")
    print(f"продукт: объявлен во frontmatter у {s['products']['runs_with_declared_domain']} прогонов; "
          f"лексически один домен у {s['products']['runs_with_single_lexical_domain']}, "
          f"несколько у {s['products']['runs_with_multiple_lexical_domains']}, "
          f"ни одного у {s['products']['runs_without_lexical_domain']}")
    print(f"результат: {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
