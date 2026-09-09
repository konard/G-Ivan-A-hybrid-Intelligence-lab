---
status: accepted
version: 1.0
updated: 2026-09-09
temperature: 0.1
owner: G-Ivan-A
scope: ecosystem
---

# AGENTS.md bootstrap standard

## Purpose

Every ecosystem repository (archetypes A, B, C and D) MUST contain `/AGENTS.md` as the single AI-agent bootstrap entrypoint. It is a short dispatcher to canonical rules, not a second copy of them.

## Required contract

`/AGENTS.md` MUST contain `<scope>`, `<hard_rules>`, `<forbidden>`, `<routing>`, `<artifact_homes>`, `<issue_levels>`, `<missing_tags>`, `<context_scope>`, `<validation>`, `<models>`, and `<escalation>` sections. `<scope>` MUST declare `archetype` and effective `environment` values equal to `.hub-profile.json`.

All links from any `AGENTS.md` to Hub artifacts MUST be absolute `https://github.com/G-Ivan-A/hybrid-Intelligence-lab/...` URLs. Spoke-specific rules are an additive delta; they MUST NOT copy or weaken the Hub base contract.

## Profile and environment

`.hub-profile.json` is the SSOT. `archetype` MUST be one of `A`, `B`, `C`, `D`. `environment` MUST be one of `local`, `gigacode`, `serverless`; when absent it defaults to `local`. `secondary_environments` are additive and MUST use the same closed vocabulary.

A non-canonical top-level directory MAY be declared through `project_specific_directories`; every entry MUST contain a relative `path` and non-empty `reason`. Validators MUST apply this generic declaration mechanism and MUST NOT maintain named directory denylists or compensating allow rules.

## Size and adapters

At more than 4,000 estimated tokens, validation SHOULD warn and the maintainer SHOULD extract a non-critical block into its canonical home, leaving one absolute link. Above 8,000 estimated tokens, validation MUST fail. `<hard_rules>` and `<forbidden>` MUST remain in `/AGENTS.md`.

Native model/environment files MAY exist only as generated adapters that import or point to `/AGENTS.md`. They MUST identify themselves as generated and validation MUST reject manual drift. A copied rule set is forbidden.

## Machine gate

Repository CI MUST verify the presence and profile agreement of `/AGENTS.md`, validate the closed profile vocabulary, require non-empty reasons for project-specific directories, enforce the hard size limit, and validate the template variant appropriate to the declared archetype/environment.

## Sources

- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-03-rfc-agents-md-root-contract.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/adr/2026-09-adr-012-agents-md-root-contract.md
