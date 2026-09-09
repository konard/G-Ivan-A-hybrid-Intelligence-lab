---
status: canonical
version: 1.0
updated: 2026-09-09
temperature: 0.1
type: agent-rule
context: [agent-work, routing, onboarding, commands, skills, escalation]
scope: ecosystem
---

# Agent work routing

`/AGENTS.md` is SSOT #0. This document is its full task router; it selects context but does not copy the selected contract.

## Priority graph

1. The issue, explicit maintainer request, and latest human comments define goal and scope.
2. `/AGENTS.md`, governance, and standards constrain safe execution and artifact placement.
3. The task class selects the execution contract below.
4. When the task and repository contract conflict, follow neither silently: record the concrete conflict and escalate for a human decision.

Missing tags or fields do not block safe work. Derive them from active contracts when deterministic and record the remaining gap.

## Routes

| Task or need | Read | Purpose |
| --- | --- | --- |
| Any agent task | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-onboarding-protocol.md | Preflight context, authorization, and PR state |
| Execution rules and DoD | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-rules.md | Operating mode, autonomy, verification, escalation |
| Artifact location | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/repo-model.md | Repository model and Anti-Inflation |
| Existing artifact lookup | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/artifact-map.md | Canonical artifact registry |
| Backlog change | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/backlog-instruction.md | Backlog ownership and update rules |
| Knowledge lifecycle | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/knowledge-lifecycle-proposal.md | Artifact lifecycle and transitions |
| Research | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/research-standard.md | Evidence and research artifact contract |
| Analysis | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/analysis-standard.md | Analysis boundary and format |
| Audit | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/audit-standard.md | Normative comparison and evidence |
| Report | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/report-standard.md | Result reporting |
| ADR or RFC | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/adr-structure-standard.md and https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/rfc-structure-standard.md | Decision/proposal boundaries |
| Document metadata | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/frontmatter-standard.md | Required frontmatter and vocabulary |
| Human-invoked procedure | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/ai-rules/commands | Imperative command selected by name |
| Reusable task capability | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/ai-rules/skills | Skill selected by task meaning or explicitly invoked as `/<slug>` |

## Context boundary

Read the routed contract completely, but do not preload unrelated routes. A missing link, contradictory rule, or required artifact home is an escalation trigger; it is not permission to invent a replacement.
