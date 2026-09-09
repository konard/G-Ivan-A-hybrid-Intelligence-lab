---
status: canonical
version: 1.0
updated: {{date}}
temperature: 0.1
entrypoint: true
---

# AGENTS.md — {{project_name}}

<scope>
This file is the single AI-agent entrypoint for this HTOM team. Read it before the first action; detailed ecosystem rules remain in the Hub.

- archetype: `D`
- environment: `local`

The values mirror `.hub-profile.json`. Rules are not copied into model- or environment-specific files.
</scope>

<hard_rules>
1. Read the current issue, latest comments, local README, and relevant Hub route before editing.
2. Keep fundamental research in the Hub and link to it; keep this repository focused on team operations and artifacts.
3. Use issue → PR → review. Preserve human decision rights and run local validation before commit.
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
Team decisions live in `docs/adr/`; audits live in `docs/audit/`; local governance stays in the existing governance contract. Fundamental research remains in `research/` of the Hub.
</artifact_homes>

<issue_levels>
Separate user story, system functional requirements, system non-functional requirements, executor task, and process constraints.
</issue_levels>

<missing_tags>
Missing task metadata does not block safe work; derive deterministic values and record unresolved gaps.
</missing_tags>

<context_scope>
Load the local task and nearest documentation first, then only the Hub routes relevant to the task class.
</context_scope>

<validation>
Run `./tools/validate-repository-structure.sh` before commit. A failure stops the change.
</validation>

<models>
Use `/AGENTS.md` directly or through a generated, drift-protected native adapter. Never copy its rules.
</models>

<escalation>
Ask in the issue or PR when the task conflicts with the repository genome, needs an unauthorized decision, or would delete an existing artifact.
</escalation>
