---
status: canonical
version: 1.0
updated: {{date}}
temperature: 0.1
entrypoint: true
---

# AGENTS.md — {{project_name}}

<scope>
This file is the single AI-agent entrypoint for this production spoke. Read it before the first action; detailed ecosystem rules remain in the Hub.

- archetype: `B`
- environment: `local`

The values mirror `.hub-profile.json`. Rules are not copied into model- or environment-specific files.
</scope>

<hard_rules>
1. Read the current issue, latest comments, local README, product contracts, and relevant Hub route before editing.
2. Keep product code in `src/`, tests in `tests/`, and architecture decisions in `docs/adr/`.
3. Use issue → PR → review, preserve human decision rights, and run CI checks before commit.
4. Do not invent facts, paths, decisions, or missing context; record gaps and escalate material conflicts.
</hard_rules>

<forbidden>
- Do not create `docs/contracts/` or copy Hub rules locally.
- Do not use `ai-generated` in frontmatter.
- Do not add named directory denylists. Declare non-canonical project directories in `.hub-profile.json` with `path` and a non-empty `reason`.
- Do not use relative links to Hub rules.
</forbidden>

<routing>
| Need | Canonical route |
| --- | --- |
| Full agent router | {{hub_url}}/blob/main/ai-rules/agent-work-routing.md |
| Agent work rules | {{hub_url}}/blob/main/ai-rules/agent-work-rules.md |
| Repository model | {{hub_url}}/blob/main/ops/repo-model.md |
| Standards | {{hub_url}}/tree/main/standards |
</routing>

<artifact_homes>
Production code lives in `src/`, automated tests in `tests/`, and product analysis/RFC/ADR artifacts in `docs/analysis/`, `docs/rfc/`, and `docs/adr/`.
</artifact_homes>

<issue_levels>
Separate user story, system functional requirements, system non-functional requirements, executor task, and process constraints.
</issue_levels>

<missing_tags>
Missing task metadata does not block safe work; derive deterministic values and record unresolved gaps.
</missing_tags>

<context_scope>
Load the local task and product contracts first, then only the Hub routes relevant to the task class.
</context_scope>

<validation>
Run the repository linters, tests, and documentation validators before commit. A failure stops the change.
</validation>

<models>
Use `/AGENTS.md` directly or through a generated, drift-protected native adapter. Never copy its rules.
</models>

<escalation>
Ask in the issue or PR when the task conflicts with the repository genome, needs an unauthorized decision, or would delete an existing artifact.
</escalation>
