#!/usr/bin/env python3
"""Measure the M0/M1/M2 layering hypothesis against the Mango runs corpus.

Context: comment by the process owner on PR #542
(https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/542) proposes to read
the first three roadmap modules as layers rather than as document-type stages:

    M0 — data on input          (normalization of whatever arrives)
    M1 — solution modelling     (the core is fixed; priority is readability)
    M2 — data on output         (documentation format; strictness may be
                                 imposed, or the M1 format may be kept; the
                                 choice of process may be left to the user)

The owner asks to test this as a hypothesis and to accept it only if it wins in
at least 80% of cases.

This script does not decide anything. It extracts, per run, the formal facts the
two competing decompositions disagree about:

  * does the run terminate in a ТЗ (the only terminal contract `C-TZ` of the
    linear ФТ→ТЗ decomposition);
  * does the run emit at least one output document at all (the terminal
    contract `C-OUT` of the layered decomposition);
  * does the run emit SEVERAL documents from one analysis (a fan-out, which a
    single-valued «target artifact» axis cannot express).

Classification is keyword-based and every rule is stated here, so a reader can
disagree with a rule rather than with a verdict.

Usage:
    python3 classify-runs.py --mango-root /path/to/mango_ba_prompts \
        --out runs-routing.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

# Files that are containers or machine-generated bookkeeping rather than a
# delivered document. `prompt-usage`/`steps`/`episodes`/`prompts-chain` are
# emitted by experiments/issue_309_fixate_runs.py, not authored by the BA.
NON_ARTIFACT_STEMS = {
    "README",
    "prompt-usage",
    "prompts-chain",
    "steps",
    "episodes",
}

# Companion reports ABOUT the delivered artifact (a review verdict), not another
# rendering of the same core for another audience. Kept apart so that the
# fan-out count is not inflated by the standard artifact+findings pair.
COMPANION_STEMS = {"quality-findings"}

# A rendered document carries an audience/strictness level marker Lx in Mango
# practice (RUN-0056, RUN-0057). Used only to detect fan-out, not to score it.
LEVEL_MARKER = re.compile(r"^L\d+[-.]")

# Substrings that indicate the run DELIVERED a ТЗ, as opposed to merely quoting
# the standard or consuming somebody else's ТЗ as input.
TZ_PRODUCED = (
    "# техническое задание",
    "# тз ",
    "настоящее техническое задание",
)

# Substrings that indicate a ТЗ arrived on the INPUT side of the run.
TZ_CONSUMED = (
    "тз заказчика",
    "предмет оценки",
    "тендерн",
    "оценка исполнимости",
)

SCALAR = re.compile(r"^([a-z_]+):\s*(.*)$")


def parse_metadata(path: Path) -> dict:
    """Read top-level scalars of a run metadata file.

    A real YAML parser is avoided on purpose: the files are machine-shaped and
    the container must run without third-party dependencies, matching
    exp/ba-requirements-normalization-539/aggregate-runs.py.
    """
    data: dict = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = SCALAR.match(line)
        if match:
            data[match.group(1)] = match.group(2).strip().strip('"')
    return data


def classify(run_dir: Path) -> dict:
    meta = parse_metadata(run_dir / "metadata.yaml")
    outputs_dir = run_dir / "outputs"
    outputs = sorted(p.name for p in outputs_dir.glob("*.md")) if outputs_dir.is_dir() else []
    artifacts = [name for name in outputs if Path(name).stem not in NON_ARTIFACT_STEMS]

    text = ""
    for name in outputs:
        text += (outputs_dir / name).read_text(encoding="utf-8", errors="replace").lower()

    return {
        "run": run_dir.name,
        "process": meta.get("process", ""),
        "run_type": meta.get("run_type", ""),
        "status": meta.get("status", ""),
        "outputs": outputs,
        "artifacts": artifacts,
        "artifact_count": len(artifacts),
        # Fan-out: one analysis rendered for several audiences at once.
        "levelled_renders": [n for n in artifacts if LEVEL_MARKER.match(n)],
        "renders": [n for n in artifacts if Path(n).stem not in COMPANION_STEMS],
        "tz_produced": any(marker in text for marker in TZ_PRODUCED),
        "tz_consumed": any(marker in text for marker in TZ_CONSUMED),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mango-root", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    runs_root = args.mango_root / "runs"
    run_dirs = sorted(p for p in runs_root.glob("*/RUN-*") if (p / "metadata.yaml").is_file())
    rows = [classify(p) for p in run_dirs]

    with_artifact = [r for r in rows if r["artifact_count"] > 0]
    # Fan-out in the strict sense: one core rendered into several DELIVERED
    # documents for different audiences, companions excluded.
    fan_out = [r for r in rows if len(r["renders"]) > 1]

    summary = {
        "mango_commit": subprocess.run(
            ["git", "-C", str(args.mango_root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True,
        ).stdout.strip(),
        "runs_total": len(rows),
        # Routing to completion under the linear ФТ→ТЗ decomposition: the only
        # terminal contract is C-TZ, so a run counts only if it delivered a ТЗ.
        "runs_delivering_tz": sum(1 for r in rows if r["tz_produced"]),
        "runs_consuming_tz_as_input": sum(1 for r in rows if r["tz_consumed"] and not r["tz_produced"]),
        # Routing to completion under the layered decomposition: the terminal
        # contract is C-OUT, satisfied by any delivered document.
        "runs_delivering_any_document": len(with_artifact),
        "runs_with_audience_fan_out": len(fan_out),
        "fan_out_runs": [r["run"] for r in fan_out],
        "runs_with_levelled_renders": sum(1 for r in rows if r["levelled_renders"]),
    }
    summary["share_delivering_tz"] = round(summary["runs_delivering_tz"] / len(rows), 4)
    summary["share_delivering_any_document"] = round(
        summary["runs_delivering_any_document"] / len(rows), 4
    )

    args.out.write_text(
        json.dumps({"summary": summary, "runs": rows}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
