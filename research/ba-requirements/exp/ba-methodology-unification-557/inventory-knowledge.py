#!/usr/bin/env python3
"""Inventory the knowledge artifacts of three ecosystem repositories.

Context: issue #557 asks for a registry and a topological knowledge map over
`research/` and `analysis/` (and their analogues) in three repositories:

    hybrid-Intelligence-lab   — the Hub (methodology owner)
    mango_ba_prompts          — the Mango spoke (prompt library, runs corpus)
    clarify-engine-ai         — the Clarify Engine spoke (RAG runtime)

A registry hand-written from memory rots the day it is written and cannot be
disagreed with. This script derives it mechanically instead, so that every
number in the parent report is reproducible and every classification rule is
visible as a named constant rather than as a verdict.

What it extracts per artifact:

  * class      — Research / Analysis / Audit / RFC / ADR / Report / Standard,
                 taken from the CONTAINING DIRECTORY, not from the title;
  * status     — the `status` field of the YAML frontmatter, or `null` when the
                 file has no frontmatter (a fact worth counting on its own);
  * ba_relevance — whether the artifact feeds the BA methodology layer, decided
                 by keyword match over path + title + frontmatter `context`;
  * edges      — outgoing markdown links to other artifacts of the corpus,
                 both relative and absolute GitHub URLs. These edges are the
                 topology of the knowledge map: "what leans on what".

The script decides nothing about quality or about coverage gaps: those belong
to the report, where a human can argue with them.

Usage:
    python3 inventory-knowledge.py --root /tmp/eco --out knowledge-inventory.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

REPOS = {
    "hub": "hybrid-Intelligence-lab",
    "mango": "mango_ba_prompts",
    "clarify": "clarify-engine-ai",
}

# Knowledge classes are read from the directory that owns the artifact. The Hub
# research standard is explicit that the type is the artifact's substantive role
# and not its folder — but the folder is the only mechanically available proxy,
# so mis-routed artifacts are reported as such rather than silently reclassified.
CLASS_BY_DIR = [
    ("research", "Research"),
    ("docs/research", "Research"),
    ("docs/analysis", "Analysis"),
    ("analysis", "Analysis"),
    ("docs/audit", "Audit"),
    ("docs/reviews", "Audit"),
    ("docs/rfc", "RFC"),
    ("docs/adr", "ADR"),
    ("docs/ADR", "ADR"),
    ("docs/report", "Report"),
    ("docs/backlog", "Backlog"),
    ("standards", "Standard"),
    ("docs/standards", "Standard"),
]

# Directories excluded from the corpus: archives, generated pages, assets.
EXCLUDED_PARTS = {".archive", ".git", "node_modules", "screenshots", "html", "data", "evidence"}

# An artifact feeds the BA methodology layer when it speaks about the BA object
# domain (requirements, artifacts, processes, taxonomies) or about the machinery
# that produces them (skills, gates, prompts, agents, pipeline). The list is
# deliberately visible: a reader who disagrees edits the constant, not a verdict.
BA_KEYWORDS = [
    "ba-", "-ba", "requirement", "требован", "taxonom", "таксоном", "artifact",
    "артефакт", "bcreq", "ontolog", "онтолог", "process", "процесс", "prompt",
    "промпт", "operation", "операц", "normaliz", "нормализ", "tz", "ft",
    "specification", "спецификац", "skill", "gate", "гейт", "pipeline",
    "конвейер", "methodolog", "методолог", "runs", "kb", "rag", "retrieval",
    "orchestrat", "оркестр", "clarify", "user-story", "use-case",
]

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
STATUS_RE = re.compile(r"^status:\s*['\"]?([A-Za-z\-]+)['\"]?\s*$", re.MULTILINE)
CONTEXT_RE = re.compile(r"^context:\s*\[(.*?)\]", re.MULTILINE | re.DOTALL)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
MD_LINK_RE = re.compile(r"\]\(([^)\s]+?)(?:#[^)]*)?\)")
GH_BLOB_RE = re.compile(r"https://github\.com/G-Ivan-A/([A-Za-z_\-]+)/(?:blob|tree)/[^/]+/(.+)")


def classify(rel_path: str) -> str | None:
    for prefix, cls in CLASS_BY_DIR:
        if rel_path.startswith(prefix + "/"):
            return cls
    return None


def is_ba_relevant(rel_path: str, title: str, context: str) -> bool:
    haystack = f"{rel_path} {title} {context}".lower()
    return any(kw in haystack for kw in BA_KEYWORDS)


def head_sha(repo_dir: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()


def scan_repo(key: str, repo_dir: Path) -> list[dict]:
    records = []
    for path in sorted(repo_dir.rglob("*.md")):
        rel = path.relative_to(repo_dir).as_posix()
        if set(rel.split("/")) & EXCLUDED_PARTS:
            continue
        cls = classify(rel)
        if cls is None or path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm = FRONTMATTER_RE.match(text)
        fm_body = fm.group(1) if fm else ""
        status_m = STATUS_RE.search(fm_body)
        context_m = CONTEXT_RE.search(fm_body)
        title_m = TITLE_RE.search(text[fm.end():] if fm else text)
        title = title_m.group(1) if title_m else ""
        context = context_m.group(1).replace("\n", " ") if context_m else ""
        edges = []
        for target in MD_LINK_RE.findall(text):
            gh = GH_BLOB_RE.match(target)
            if gh:
                edges.append({"repo": gh.group(1), "path": gh.group(2)})
            elif not target.startswith(("http", "mailto:", "#")):
                resolved = (path.parent / target).resolve()
                try:
                    edges.append({"repo": repo_dir.name,
                                  "path": resolved.relative_to(repo_dir.resolve()).as_posix()})
                except ValueError:
                    continue
        records.append({
            "repo": key,
            "path": rel,
            "class": cls,
            "status": status_m.group(1) if status_m else None,
            "has_frontmatter": bool(fm),
            "title": title,
            "ba_relevant": is_ba_relevant(rel, title, context),
            "edges": [e for e in edges if e["path"].endswith(".md")],
        })
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, help="directory holding the three clones")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    root = Path(args.root)
    records: list[dict] = []
    heads = {}
    for key, name in REPOS.items():
        repo_dir = root / name
        if not repo_dir.is_dir():
            raise SystemExit(f"missing clone: {repo_dir}")
        heads[key] = head_sha(repo_dir)
        records.extend(scan_repo(key, repo_dir))

    known = {(r["repo"], r["path"]) for r in records}
    by_name = {REPOS[k]: k for k in REPOS}
    internal_edges = 0
    cross_repo_edges = 0
    for rec in records:
        kept = []
        for edge in rec["edges"]:
            repo_key = by_name.get(edge["repo"], edge["repo"] if edge["repo"] in REPOS else None)
            if repo_key and (repo_key, edge["path"]) in known:
                kept.append({"repo": repo_key, "path": edge["path"]})
                if repo_key == rec["repo"]:
                    internal_edges += 1
                else:
                    cross_repo_edges += 1
        rec["edges"] = sorted({(e["repo"], e["path"]) for e in kept})
        rec["edges"] = [{"repo": r, "path": p} for r, p in rec["edges"]]

    indegree: Counter = Counter()
    for rec in records:
        for edge in rec["edges"]:
            indegree[(edge["repo"], edge["path"])] += 1

    summary = {
        "heads": heads,
        "total": len(records),
        "by_repo": dict(Counter(r["repo"] for r in records)),
        "by_class": dict(Counter(r["class"] for r in records)),
        "by_repo_class": {f'{r}/{c}': n for (r, c), n in
                          sorted(Counter((r["repo"], r["class"]) for r in records).items())},
        "by_status": dict(Counter(str(r["status"]) for r in records)),
        "without_frontmatter": sum(1 for r in records if not r["has_frontmatter"]),
        "ba_relevant": sum(1 for r in records if r["ba_relevant"]),
        "ba_relevant_by_repo": dict(Counter(r["repo"] for r in records if r["ba_relevant"])),
        "edges_internal": internal_edges,
        "edges_cross_repo": cross_repo_edges,
        "isolated_nodes": sum(1 for r in records
                              if not r["edges"] and indegree[(r["repo"], r["path"])] == 0),
        "top_referenced": [
            {"repo": k[0], "path": k[1], "indegree": n}
            for k, n in indegree.most_common(15)
        ],
    }

    Path(args.out).write_text(
        json.dumps({"summary": summary, "artifacts": records}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
