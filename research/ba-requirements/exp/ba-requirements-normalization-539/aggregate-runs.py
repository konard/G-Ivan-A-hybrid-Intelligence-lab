#!/usr/bin/env python3
"""Aggregate the empirical corpus of Mango BA runs for issue #539.

The script is deliberately formal: it reads `runs/<year>/RUN-*/metadata.yaml`
from a local clone of https://github.com/G-Ivan-A/mango_ba_prompts and reports
only what is written there. It does not interpret the runs and does not
classify them by meaning — interpretation lives in the research module.

Usage:
    python3 aggregate-runs.py --mango-root /path/to/mango_ba_prompts \
        --out runs-aggregate.json
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
from pathlib import Path

# Keywords traced to the normalization edge cases and to the input-quality
# spectrum. Matching is substring-based on the lowercased run text, so Russian
# stems are given without endings.
KEYWORDS = {
    "coverage": "покрыт",
    "clarification": "уточнени",
    "hallucination": "галлюцин",
    "custom": "кастом",
    "speculation": "домысл",
    "tariff": "тариф",
    "access-rights": "прав доступа",
    "already-implemented": "уже реализован",
    "discoverability": "discoverab",
    "deprecation-en": "deprecat",
    "deprecation-ru": "вывод из эксплуатации",
}

SCALAR = re.compile(r"^(\s*)([a-z_]+):\s*(.*)$")


def parse_metadata(path: Path) -> dict:
    """Flat YAML reader: top-level scalars plus the `metrics:`/`eval:` blocks.

    A real YAML parser is intentionally avoided so the container has no
    third-party dependency; the metadata files are machine-generated and use a
    fixed two-level shape.
    """
    data: dict = {}
    metrics: dict = {}
    in_metrics = False
    for line in path.read_text(encoding="utf-8").splitlines():
        # Two shapes exist in the corpus: run metrics live under `metrics:` in
        # most runs and under a top-level `eval:` mapping in the earliest ones
        # (RUN-0017, RUN-0020, RUN-0023). Both are merged into one dict.
        if line.rstrip() in {"metrics:", "eval:"}:
            in_metrics = True
            continue
        if line and not line[0].isspace() and not line.startswith("-"):
            in_metrics = False
        m = SCALAR.match(line)
        if not m:
            continue
        indent, key, raw = m.group(1), m.group(2), m.group(3).strip()
        if raw == "" or raw.startswith("#"):
            continue
        value: object = raw.strip('"').strip("'")
        if isinstance(value, str) and re.fullmatch(r"-?\d+", value):
            value = int(value)
        elif isinstance(value, str) and re.fullmatch(r"-?\d+\.\d+", value):
            value = float(value)
        if in_metrics and indent:
            metrics[key] = value
        elif not indent:
            data[key] = value
    data["metrics"] = metrics
    return data


def describe(values: list[float]) -> dict | None:
    if not values:
        return None
    return {
        "n": len(values),
        "sum": round(sum(values), 4),
        "min": min(values),
        "median": round(statistics.median(values), 4),
        "max": max(values),
    }


def repo_sha(root: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except Exception:  # noqa: BLE001 - snapshot must not fail on a non-git copy
        return "unknown"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mango-root", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    runs_root = args.mango_root / "runs"
    runs = sorted(runs_root.glob("*/RUN-*/metadata.yaml"))

    records = []
    keyword_hits = {name: [] for name in KEYWORDS}
    for meta_path in runs:
        run_dir = meta_path.parent
        data = parse_metadata(meta_path)
        text = "\n".join(
            p.read_text(encoding="utf-8", errors="ignore").lower()
            for p in run_dir.rglob("*")
            if p.is_file() and p.suffix in {".md", ".yaml", ".yml"}
        )
        run_id = data.get("run_id", run_dir.name)
        for name, needle in KEYWORDS.items():
            if needle in text:
                keyword_hits[name].append(run_id)
        records.append({
            "run_id": run_id,
            "date": str(data.get("date", "")),
            "process": data.get("process", ""),
            "status": data.get("status", ""),
            "run_type": data.get("run_type", ""),
            "metrics": data.get("metrics", {}),
        })

    def metric(name: str) -> list[float]:
        return [
            r["metrics"][name] for r in records
            if isinstance(r["metrics"].get(name), (int, float))
        ]

    def count_by(field: str) -> dict:
        out: dict = {}
        for r in records:
            out[str(r[field])] = out.get(str(r[field]), 0) + 1
        return dict(sorted(out.items(), key=lambda kv: (-kv[1], kv[0])))

    prefixes: dict = {}
    for r in records:
        head = r["process"].split("-")[0] if r["process"] else "unknown"
        prefixes[head] = prefixes.get(head, 0) + 1

    dates = sorted(r["date"] for r in records if r["date"])
    aggregate = {
        "source_repo": "https://github.com/G-Ivan-A/mango_ba_prompts",
        "repo_sha": repo_sha(args.mango_root),
        "runs_total": len(records),
        "date_range": {"from": dates[0] if dates else None,
                       "to": dates[-1] if dates else None},
        "by_run_type": count_by("run_type"),
        "by_status": count_by("status"),
        "by_process_prefix": dict(
            sorted(prefixes.items(), key=lambda kv: (-kv[1], kv[0]))),
        "metrics": {
            name: describe(metric(name))
            for name in (
                "episodes", "iterations", "ba_edits", "quality", "success_rate",
                "hallucinations", "hallucinations_shipped", "tokens_dialog_total",
                "turns", "duration_wall_clock_s",
            )
        },
        "runs_with_shipped_hallucination": sorted(
            r["run_id"] for r in records
            if isinstance(r["metrics"].get("hallucinations_shipped"), (int, float))
            and r["metrics"]["hallucinations_shipped"] > 0
        ),
        "keyword_coverage": {
            name: {"needle": KEYWORDS[name], "runs": len(hits),
                   "run_ids": sorted(hits)}
            for name, hits in keyword_hits.items()
        },
        "runs": records,
    }

    args.out.write_text(
        json.dumps(aggregate, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"runs: {aggregate['runs_total']}  sha: {aggregate['repo_sha']}")
    for name, stats in aggregate["metrics"].items():
        print(f"  {name}: {stats}")
    for name, hit in aggregate["keyword_coverage"].items():
        print(f"  keyword {name} ({hit['needle']}): {hit['runs']} runs")


if __name__ == "__main__":
    main()
