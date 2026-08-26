#!/usr/bin/env python3
"""Замер корпуса прогонов Mango под четыре RRP-модуля конвейера (issue #545).

Скрипт не зависит от внешних пакетов и не парсит YAML полноценно: из
`metadata.yaml` извлекаются только скалярные поля и списки верхнего уровня,
которых достаточно для проверяемых утверждений модулей M1-M4.

Использование:
    python3 measure-pipeline.py --mango-root /tmp/mango --out pipeline-facts.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SCALAR = re.compile(r"^([a-z_]+):\s*(.*)$")
METRIC = re.compile(r"^\s{2}([a-z_]+):\s*(.*)$")
LIST_ITEM = re.compile(r"^\s*-\s+(.*)$")
LEVEL_MARKER = re.compile(r"^L\d+[-.]")

# Операции онтологии Mango (standards/ba-ontology.md, §3), сгруппированные по
# слоям конвейера RFC: вход -> ядро -> выход -> обратная связь.
LAYER_OF_OPERATION = {
    "ingestion": "M0",
    "understanding": "M0",
    "modeling": "M1",
    "solution_design": "M1",
    "validation": "M1",
    "documentation": "M2",
    "quality": "M2",
    "reverse_requirements": "M1",
    "impact_analysis": "M3",
    "governance": "M3",
    "research": "M3",
    "risk_analysis": "M1",
    "release_readiness": "M3",
}

MODELING_MARKERS = ("us-", "user-story", "uc-", "usecase", "use-case", "modeling")
CORE_MARKERS = ("fr-", "bcreq", "glossary", "context")
RENDER_MARKERS = ("tz", "documentation", "spec", "report", "summary", "matrix")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_metadata(path: Path) -> dict:
    """Достаёт скаляры верхнего уровня, списки верхнего уровня и блок metrics."""
    data: dict = {"metrics": {}, "lists": {}}
    current_list: str | None = None
    in_metrics = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        if in_metrics:
            metric = METRIC.match(raw)
            if metric and not raw.startswith("   "):
                data["metrics"][metric.group(1)] = strip_quotes(metric.group(2))
                continue
            if raw.startswith(" "):
                continue
            in_metrics = False

        item = LIST_ITEM.match(raw)
        if item and current_list and raw.startswith(" "):
            data["lists"].setdefault(current_list, []).append(strip_quotes(item.group(1)))
            continue

        scalar = SCALAR.match(raw)
        if not scalar:
            continue

        key, value = scalar.group(1), scalar.group(2).strip()
        if key == "metrics":
            in_metrics = True
            current_list = None
            continue
        if value == "":
            current_list = key
            continue
        current_list = None
        data[key] = strip_quotes(value)

    return data


def has_any(name: str, markers) -> bool:
    lowered = name.lower()
    return any(marker in lowered for marker in markers)


def classify(run_dir: Path) -> dict:
    meta = parse_metadata(run_dir / "metadata.yaml")
    lists = meta["lists"]
    metrics = meta["metrics"]

    outputs_dir = run_dir / "outputs"
    documents = []
    if outputs_dir.is_dir():
        documents = sorted(
            p.name for p in outputs_dir.iterdir()
            if p.is_file() and p.suffix == ".md" and p.stem.upper() != "README"
        )

    process = meta.get("process", "")
    return {
        "run": run_dir.name,
        "process": process,
        "run_type": meta.get("run_type", ""),
        "status": meta.get("status", ""),
        "documents": documents,
        "document_count": len(documents),
        "levelled_documents": [d for d in documents if LEVEL_MARKER.match(d)],
        "modeling_run": has_any(process, MODELING_MARKERS),
        "core_run": has_any(process, CORE_MARKERS),
        "render_run": has_any(process, RENDER_MARKERS),
        "has_feedback": (run_dir / "feedback").is_dir(),
        "has_logs": (run_dir / "logs").is_dir(),
        "has_inputs": (run_dir / "inputs").is_dir(),
        "related_runs": lists.get("related_runs", []),
        "metric_keys": sorted(metrics),
        "has_success_rate": "success_rate" in metrics,
        "has_eval": "eval" in metrics,
        "has_verdict": "verdict" in metrics,
        "measured": metrics.get("measured", "absent"),
        "token_method": metrics.get("token_method", "absent"),
        "hallucinations_shipped": metrics.get("hallucinations_shipped", "absent"),
    }


def prompt_modes(mango_root: Path) -> dict:
    modes = {"stepwise": 0, "oneshot": 0, "legacy": 0, "other": 0}
    prompts_dir = mango_root / "prompts"
    if not prompts_dir.is_dir():
        return modes
    for prompt in prompts_dir.glob("*.md"):
        stem = prompt.stem.lower()
        for mode in ("stepwise", "oneshot", "legacy"):
            if stem.endswith(mode):
                modes[mode] += 1
                break
        else:
            modes["other"] += 1
    return modes


def summarise(runs: list[dict], modes: dict, commit: str) -> dict:
    total = len(runs)

    def share(count: int) -> float:
        return round(count / total, 4) if total else 0.0

    delivering = [r for r in runs if r["document_count"] > 0]
    multi_doc = [r for r in runs if r["document_count"] > 1]
    fan_out = [r for r in runs if len(r["levelled_documents"]) > 1]
    with_feedback = [r for r in runs if r["has_feedback"]]
    with_related = [r for r in runs if r["related_runs"]]
    measured_true = [r for r in runs if r["measured"] == "true"]
    measured_false = [r for r in runs if r["measured"] == "false"]
    measured_absent = [r for r in runs if r["measured"] == "absent"]
    shipped = [
        r for r in runs
        if r["hallucinations_shipped"] not in ("absent", "")
        and r["hallucinations_shipped"].isdigit()
        and int(r["hallucinations_shipped"]) > 0
    ]

    status_counts: dict = {}
    for run in runs:
        status_counts[run["status"] or "absent"] = status_counts.get(run["status"] or "absent", 0) + 1

    metric_key_counts: dict = {}
    for run in runs:
        for key in run["metric_keys"]:
            metric_key_counts[key] = metric_key_counts.get(key, 0) + 1

    return {
        "mango_commit": commit,
        "runs_total": total,
        "prompt_modes": modes,
        "status_counts": dict(sorted(status_counts.items(), key=lambda kv: -kv[1])),
        "m1_modeling_runs": sum(1 for r in runs if r["modeling_run"]),
        "m1_core_runs": sum(1 for r in runs if r["core_run"]),
        "m2_runs_delivering_documents": len(delivering),
        "m2_share_delivering_documents": share(len(delivering)),
        "m2_runs_multi_document": len(multi_doc),
        "m2_share_multi_document": share(len(multi_doc)),
        "m2_runs_audience_fan_out": len(fan_out),
        "m2_fan_out_runs": [r["run"] for r in fan_out],
        "m3_runs_with_feedback_dir": len(with_feedback),
        "m3_share_with_feedback_dir": share(len(with_feedback)),
        "m3_runs_with_related_runs": len(with_related),
        "m3_runs_with_success_rate": sum(1 for r in runs if r["has_success_rate"]),
        "m3_runs_with_eval": sum(1 for r in runs if r["has_eval"]),
        "m3_runs_with_verdict": sum(1 for r in runs if r["has_verdict"]),
        "m3_measured_true": len(measured_true),
        "m3_measured_false": len(measured_false),
        "m3_measured_absent": len(measured_absent),
        "m3_runs_hallucinations_shipped_positive": len(shipped),
        "m3_hallucinations_shipped_runs": [r["run"] for r in shipped],
        "m4_metric_key_frequency": dict(sorted(metric_key_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "m4_distinct_metric_keys": len(metric_key_counts),
        "m4_runs_with_inputs_dir": sum(1 for r in runs if r["has_inputs"]),
        "m4_runs_with_logs_dir": sum(1 for r in runs if r["has_logs"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mango-root", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--commit", default="unknown")
    args = parser.parse_args()

    runs_root = args.mango_root / "runs"
    run_dirs = sorted(
        p for p in runs_root.glob("*/RUN-*")
        if p.is_dir() and (p / "metadata.yaml").is_file()
    )
    runs = [classify(p) for p in run_dirs]
    payload = {"summary": summarise(runs, prompt_modes(args.mango_root), args.commit), "runs": runs}

    args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
