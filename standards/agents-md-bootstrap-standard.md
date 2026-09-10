---
status: accepted
version: 2.0
updated: 2026-09-10
temperature: 0.1
owner: G-Ivan-A
scope: ecosystem
---

# AGENTS.md bootstrap standard

## Purpose

Every ecosystem repository (archetypes A, B, C and D) MUST contain `/AGENTS.md` as the single AI-agent bootstrap entrypoint. It is a short dispatcher to canonical rules, not a second copy of them. This standard is the SSOT for the **structure** of that file: the required sections and their purpose, the split between general and project-specific rules, the size-validation mechanism, and the frontmatter contract. `/AGENTS.md` itself MUST NOT restate these meta-rules; it links here.

## Required sections

`/AGENTS.md` MUST contain the following sections, each opened and closed by its tag. Order is recommended as listed and is not validated.

| Section | Purpose |
| --- | --- |
| `<scope>` | What the file is, the `archetype` and `environment` values, and the declaration of which sections are general and which are project-specific. |
| `<hard_rules>` | Absolute, generally applicable obligations. Violation stops the change. |
| `<forbidden>` | Absolute, generally applicable prohibitions. |
| `<guidelines>` | Generally applicable recommendations, applied unless they conflict with `<hard_rules>`, `<forbidden>` or the goal; a deviation is recorded in the pull request. |
| `<hybrid_work>` | Human–AI collaboration contract: appeal, autonomy by operating mode, backlog handling, behaviour at the boundary of the project contract. |
| `<project_specific_rules>` | The only home for rules of this repository. |
| `<routing>` | Minimal table of canonical routes, absolute URLs only. |
| `<artifact_homes>` | Where an artifact class lives, separating agent contracts from process contracts. |
| `<issue_levels>` | The distinct levels of a task statement. |
| `<missing_tags>` | What the agent does when required task metadata is absent. |
| `<context_scope>` | The reading budget: what to load and when to expand. |
| `<validation>` | The validators to run before commit. |
| `<models>` | Native adapters and the ban on rule copies. |
| `<escalation>` | Priority graph of task contract versus governance, and the legal exit. |

`<scope>` MUST declare `archetype` and effective `environment` values equal to `.hub-profile.json`.

## General versus project-specific rules

`<hard_rules>`, `<forbidden>`, `<guidelines>` and `<hybrid_work>` are the **general layer**. They are identical across the ecosystem, are delivered from the Hub template into every repository, and a spoke MUST NOT weaken, rewrite or subtract from them.

`<project_specific_rules>` is the **project layer** and the only additive delta. A repository places every rule that follows from its own concept there — nowhere else in the file. The Hub does not describe spoke rules and a spoke does not describe Hub rules; the shipped template carries the section with an explicit placeholder instructing the receiving project to define its own rules in line with its concept.

There is no class of "soft rules". A norm is either absolute (`<hard_rules>` / `<forbidden>`) or a recommendation (`<guidelines>`); an intermediate label is forbidden, because a rule an agent may silently drop is not a rule.

All links from any `AGENTS.md` to Hub artifacts MUST be absolute `https://github.com/G-Ivan-A/hybrid-Intelligence-lab/...` URLs.

## Frontmatter contract

`/AGENTS.md` frontmatter MUST contain `status: canonical`, a `version`, an `updated` date, `temperature`, and `entrypoint: true`. `entrypoint: true` marks the file as a contract an agent loads without being told; it is not exclusive to `/AGENTS.md`, so the single-entrypoint invariant is carried by the root path and the presence gate, not by this field. Changing a `<hard_rules>`, `<forbidden>`, `<hybrid_work>` or `<project_specific_rules>` item is a major `version` increment.

## Profile and environment

`.hub-profile.json` is the SSOT. `archetype` MUST be one of `A`, `B`, `C`, `D`. `environment` MUST be one of `local`, `gigacode`, `serverless`; when absent it defaults to `local`. `secondary_environments` are additive and MUST use the same closed vocabulary.

A non-canonical top-level directory MAY be declared through `project_specific_directories`; every entry MUST contain a relative `path` and non-empty `reason`. Validators MUST apply this generic declaration mechanism and MUST NOT maintain named directory denylists.

## Size and adapters

Size is normed here and only here, because the threshold is a property of the file format, not a rule of agent behaviour: an entrypoint that restates its own limit spends the budget it is protecting. At more than 4,000 estimated tokens, validation SHOULD warn and the maintainer SHOULD extract a non-critical block into its canonical home, leaving one absolute link. Above 8,000 estimated tokens, validation MUST fail. `<hard_rules>`, `<forbidden>` and `<hybrid_work>` MUST remain in `/AGENTS.md` and are not eligible for extraction (`A-6`, ADR-012).

Native model/environment files MAY exist only as generated adapters that import or point to `/AGENTS.md`. They MUST identify themselves as generated and validation MUST reject manual drift. A copied rule set is forbidden.

## Machine gate

Repository CI MUST verify the presence and profile agreement of `/AGENTS.md`, the presence of every required section, the closed profile vocabulary, non-empty reasons for project-specific directories, the hard size limit, and the template variant appropriate to the declared archetype/environment. The reference implementation is [`tools/validate-agents-bootstrap.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-agents-bootstrap.sh), regression-tested by [`tools/test-agents-md-integration.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/test-agents-md-integration.sh).

Norms of this standard that no validator can decide — whether a rule placed in `<project_specific_rules>` is genuinely project-specific, and whether an appeal was owed — are contractual gates: agent self-check plus human review (`A-8`, ADR-012).

## Sources

- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-03-rfc-agents-md-root-contract.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/adr/2026-09-adr-012-agents-md-root-contract.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-rules.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/analysis/2026-09-10-agents-md-hybrid-work-contract-analysis.md
