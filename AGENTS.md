---
status: canonical
version: 1.0
updated: 2026-09-09
temperature: 0.1
entrypoint: true
---

# AGENTS.md

<scope>
This file is the single entrypoint for every AI agent working with this repository. Read it completely before the first action. It is a dispatcher; detailed rules remain in their canonical documents.

- archetype: `A`
- environment: `local`

The values mirror `.hub-profile.json`, which is the SSOT. A mismatch is a validation failure. This contract applies to every model; model- or environment-specific files may only be generated pointers, never copies of these rules. Above 4K tokens, extract a non-critical block into a sub-contract; above 8K tokens, validation fails. `<hard_rules>` and `<forbidden>` remain here.
</scope>

<hard_rules>
1. Read this file before changing files, then follow the full router at https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-routing.md.
2. Start from an issue or explicit maintainer request; read its latest comments and current PR feedback before editing.
3. Do not invent repository structure, facts, estimates, or sources. Classify an artifact by content and place it in its canonical home.
4. One artifact exists only for an operational need (Anti-Inflation).
5. Work through a pull request; direct commits to `main` are forbidden.
6. Run applicable validators before committing. A red validator stops the change.
7. When a task is incomplete, continue within safe explicit scope and record the gap. Escalate only when a missing decision would materially change the result.
8. Hub research expands the considered boundary: missing status, existing linkage, or alignment with an accepted concept is not grounds for excluding an artifact or alternative. Exclusion requires a recorded substantive analysis. Spoke execution may narrow scope to its accepted product contract.
</hard_rules>

<forbidden>
- Do not create `docs/contracts/`; agent contracts live in `ai-rules/`.
- Do not copy rules into model- or environment-specific files. Generated, validator-protected pointers are allowed.
- Do not use `ai-generated` in document frontmatter.
- Do not add a top-level directory outside the core, archetype, declared environment, or `project_specific_directories` without the required decision record.
- Do not add named directory denylists. A non-canonical directory is declared in `.hub-profile.json` with `path` and a non-empty `reason`; absence from the canonical set is not a prohibition.
- Do not change `standards/` or `docs/adr/` without explicit task authority.
- Do not delete or overwrite another contributor's artifacts instead of creating the required new version.
- Do not use relative links to Hub rules from a spoke.
</forbidden>

<routing>
| Need | Canonical route |
| --- | --- |
| Full task-class routing and priority graph | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-routing.md |
| Agent execution rules, modes, autonomy and DoD | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-rules.md |
| Preflight onboarding protocol | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-onboarding-protocol.md |
| Repository model and artifact homes | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/repo-model.md |
| Artifact registry | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/artifact-map.md |
| Standards | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/standards |
| Governance | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/GOVERNANCE.md |
</routing>

<artifact_homes>
| Artifact class | Home |
| --- | --- |
| Research | `research/<domain>/YYYY-MM-DD-name.md` |
| Analysis / audit / report | `docs/analysis/`, `docs/audit/`, `docs/report/` |
| Architecture decision | `docs/adr/YYYY-MM-adr-NNN-name.md` |
| Mandatory reusable norm | `standards/<name>.md` |
| Always-loaded agent rule | `ai-rules/<name>.md` |
| Human-invoked command | `ai-rules/commands/<slug>.md` |
| Context-selected skill | `ai-rules/skills/<slug>/SKILL.md` |
| Operational process artifact | `ops/<name>.md` |
</artifact_homes>

<issue_levels>
Keep five levels distinct: user story, system functional requirements, system non-functional requirements, executor task, and process constraints. The system—not the executor—is the subject of functional and non-functional requirements.
</issue_levels>

<missing_tags>
Missing task type, operating mode, or another required field triggers an escalation record but does not stop safe work. Infer only from active contracts; record anything that cannot be derived.
</missing_tags>

<context_scope>
Do not read the whole repository. Start with this file, then load only the issue/PR context, nearest README, and canonical routes needed for the task class. Expand context when evidence identifies another dependency.
</context_scope>

<validation>
Before committing, run the applicable commands from https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/CONTRIBUTING.md, including `tools/test-*.sh`, `./tools/validate-frontmatter.sh .`, `./tools/validate-file-naming.sh`, `./tools/validate-repository-structure.sh`, `./tools/validate-rrp-links.sh`, and `python3 tools/generate-manifest.py --check`.
</validation>

<models>
Codex reads `AGENTS.md` natively. Other tools may use a native adapter that imports or points to `/AGENTS.md`; the adapter must be generated, marked as such, and protected from manual drift. If a tool cannot auto-load it, the operator supplies `/AGENTS.md` in the system prompt.
</models>

<escalation>
The task contract has priority for scope and desired outcome; repository governance has priority for safe execution and artifact placement. Stop and ask when a required decision is absent, the requested path conflicts with the genome, authorization does not cover a standards/ADR change, or deletion would remove an existing artifact. Record the question in the issue or PR. Do not silently violate either branch of this priority graph.
</escalation>
