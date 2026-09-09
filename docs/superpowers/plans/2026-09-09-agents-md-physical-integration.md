# AGENTS.md Physical Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Physically integrate the accepted root `AGENTS.md` contract across the Hub, spoke templates, repository structure validation, and the `pr-ops/` to `ops/` migration in one atomic pull request.

**Architecture:** `/AGENTS.md` becomes the sole AI-agent bootstrap entrypoint and delegates detailed routing to `/ai-rules/agent-work-routing.md`; `.hub-profile.json` is the machine-readable SSOT for `archetype` and `environment`. Hub and template validators enforce the profile-specific contract while migration tests protect the `ops/` rename and the absence of named `plans/`/`tasks/` deny rules.

**Tech Stack:** Markdown contracts, JSON profiles and template manifest, Bash validators/tests, Python manifest generator, Git/GitHub Actions.

**Spec:** `docs/rfc/2026-09-03-rfc-agents-md-root-contract.md` and `docs/adr/2026-09-adr-012-agents-md-root-contract.md`

## Global Constraints

- `AGENTS.md` is SSOT #0 and must remain a short dispatcher with mandatory XML sections and absolute Hub URLs.
- `.hub-profile.json` is the SSOT for `archetype` and `environment`; validator/profile disagreement is a failure.
- Remove named `plans/` and `tasks/` prohibitions as a class; do not add an allow rule that compensates for a deny rule.
- Preserve `CONTRIBUTING.md` and `GOVERNANCE.md` for human workflow/governance, but neither may compete with `/AGENTS.md` as the AI bootstrap.
- Rename `pr-ops/` to `ops/` atomically and update active, historical, template, generated-manifest, and validator references so no repository-local reference remains stale.
- Work only on `issue-567-f41623e824fb`, commit atomic green steps, and push only that branch.

---

### Task 1: Executable integration contract

**Files:**
- Create: `tools/test-agents-md-integration.sh`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: RFC P.2, P.6, P.7, P.9 and ADR-012.
- Produces: a black-box regression suite that invokes `tools/validate-repository-structure.sh` in isolated repository copies and verifies Hub/template invariants.

- [ ] **Step 1: Write failing tests**

Create isolated cases that assert: root `AGENTS.md` and `.hub-profile.json` are required; `archetype`/`environment` values must agree; HTOM and Spoke templates include `AGENTS.md` plus profiles; `plans/` and `tasks/` are not rejected by name; `pr-ops/` no longer exists; active paths and validator contracts use `ops/`.

- [ ] **Step 2: Verify RED**

Run: `bash tools/test-agents-md-integration.sh`

Expected: failure because the root/profile/template artifacts and validator checks are absent and `pr-ops/` still exists.

- [ ] **Step 3: Register the test in CI**

Add a named `Test AGENTS.md physical integration` step to `.github/workflows/validate.yml` that runs `bash tools/test-agents-md-integration.sh` before the production structure validator.

- [ ] **Step 4: Commit the red contract**

Run: `git add docs/superpowers/plans/2026-09-09-agents-md-physical-integration.md tools/test-agents-md-integration.sh .github/workflows/validate.yml && git commit -m "test: define AGENTS integration contract"`

### Task 2: Root bootstrap contract and routing cleanup

**Files:**
- Create: `AGENTS.md`
- Create: `.hub-profile.json`
- Create: `ai-rules/agent-work-routing.md`
- Create: `standards/agents-md-bootstrap-standard.md`
- Modify: `templates/agents-md-root-draft.md`
- Modify: `CONTRIBUTING.md`
- Modify: `ai-rules/agent-work-rules.md`
- Modify: `ai-rules/agent-onboarding-protocol.md`
- Modify: `docs/adr/2026-07-adr-007-hub-root-structure.md`
- Modify: `standards/README.md`

**Interfaces:**
- Consumes: `.hub-profile.json` keys `archetype` and `environment`.
- Produces: mandatory `/AGENTS.md` XML sections, absolute Hub routing URLs, canonical detailed routing at `/ai-rules/agent-work-routing.md`, and the reusable bootstrap standard.

- [ ] **Step 1: Add the Hub profile**

Declare the Hub as archetype `A` with environment `local`, following the accepted environment RFC vocabulary.

- [ ] **Step 2: Promote and normalize the root dispatcher**

Build `/AGENTS.md` from the accepted draft; replace implementation notes and `pr-ops/` URLs with final `ops/` URLs, keep hard rules and escalation in the root, and ensure every Hub link is absolute.

- [ ] **Step 3: Extract detailed routing**

Create `/ai-rules/agent-work-routing.md` with task-class routes, command/skill distinction, route purpose, and the accepted priority graph. Make root and existing AI rules point to this canonical document without duplicating it.

- [ ] **Step 4: Remove competing entrypoints**

Replace `CONTRIBUTING.md` AI onboarding prose with a thin `/AGENTS.md` pointer; update local onboarding rules so they begin from `/AGENTS.md`; leave `GOVERNANCE.md` as the human-facing thin governance anchor.

- [ ] **Step 5: Add the cross-archetype standard**

Create `standards/agents-md-bootstrap-standard.md` with required sections, profile agreement, absolute-link invariant, size thresholds, adapter/no-copy rule, and declaration-over-denylist rule. Register it in standards and ADR-007.

- [ ] **Step 6: Run focused contract tests**

Run: `bash tools/test-agents-md-integration.sh`

Expected: root-contract cases advance; template/validator/migration cases remain red.

- [ ] **Step 7: Commit**

Run: `git add AGENTS.md .hub-profile.json ai-rules standards templates/agents-md-root-draft.md CONTRIBUTING.md docs/adr/2026-07-adr-007-hub-root-structure.md && git commit -m "feat: establish root AGENTS bootstrap"`

### Task 3: Template injection and profile-aware validation

**Files:**
- Create: `templates/htom/AGENTS.md`
- Create: `templates/htom/.hub-profile.json`
- Create: `templates/spoke/AGENTS.md`
- Create: `templates/spoke/.hub-profile.json`
- Modify: `templates/htom/AI_QUICK_RULES.md`
- Modify: `templates/htom/AI_SESSION_HANDOVER_PROMPT.md`
- Modify: `templates/htom/CONTRIBUTING.md`
- Modify: `templates/spoke/CONTRIBUTING.md`
- Modify: `templates/htom/init.sh`
- Modify: `templates/htom/tools/validate-repository-structure.sh`
- Modify: `templates/sync-metadata.json`
- Modify: `tools/validate-repository-structure.sh`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: profile `archetype`, optional/defaulted `environment`, and `project_specific_directories[].reason`.
- Produces: generated repositories with a root dispatcher and a validator that selects the applicable structure by environment rather than a single fixed list.

- [ ] **Step 1: Inject dispatchers and profiles**

Add HTOM and Spoke template variants with absolute Hub URLs and explicit archetype/environment declarations; ensure init/sync metadata treats them as CORE bootstrap artifacts.

- [ ] **Step 2: Fix K-3 template routing**

Make HTOM quick rules, session handover, and both template contribution guides begin from local `/AGENTS.md`, not `CONTRIBUTING.md` as the governance bootstrap.

- [ ] **Step 3: Implement profile parsing**

In Hub and HTOM validators, parse JSON with Python from the repository root, default a missing `environment` to `local` where the accepted environment RFC requires backward compatibility, reject unknown values, and compare the effective values with the declarations in `AGENTS.md`.

- [ ] **Step 4: Enforce generic directory declarations**

Validate `project_specific_directories` entries and non-empty `reason` fields generically; do not introduce any named `plans` or `tasks` branch, denylist, or compensating allowlist.

- [ ] **Step 5: Enforce bootstrap gates**

Require root/template `AGENTS.md`, profile, bootstrap standard, routing contract, absolute URLs, and 8K-token maximum; emit a warning above 4K tokens.

- [ ] **Step 6: Verify GREEN for bootstrap/profile tests**

Run: `bash tools/test-agents-md-integration.sh`

Expected: bootstrap and profile cases pass; only `ops/` migration assertions may remain red.

- [ ] **Step 7: Regenerate manifest and commit**

Run: `python3 tools/generate-manifest.py`

Run: `git add templates tools .github/workflows/validate.yml && git commit -m "feat: inject AGENTS into repository templates"`

### Task 4: Atomic `pr-ops/` to `ops/` migration

**Files:**
- Move: `pr-ops/` to `ops/`
- Modify: every tracked text file containing `pr-ops/`, including active contracts, historical artifacts, templates, tests, validators, and generated manifest entries

**Interfaces:**
- Consumes: all repository-local `pr-ops/` path references.
- Produces: one canonical `/ops/` home and zero stale `pr-ops/` path references.

- [ ] **Step 1: Move the directory with history**

Run: `git mv pr-ops ops`

- [ ] **Step 2: Replace repository-local paths globally**

Mechanically rewrite `pr-ops/` to `ops/` in tracked textual files, preserving external prose meaning while making every path resolve after the migration.

- [ ] **Step 3: Audit stale and broken references**

Run: `git grep -n 'pr-ops/'`

Expected: no matches.

Run a Markdown-link path audit for relative links affected by the move and correct changed relative depths where necessary.

- [ ] **Step 4: Update migration-facing contracts**

Update root structure lists, artifact map/backlog statuses, changelog, filename rules, sync prompt, validator allowlists, and test fixtures to name `/ops/`.

- [ ] **Step 5: Regenerate manifest**

Run: `python3 tools/generate-manifest.py`

- [ ] **Step 6: Verify GREEN**

Run: `bash tools/test-agents-md-integration.sh`

Expected: all integration regression cases pass.

- [ ] **Step 7: Commit**

Run: `git add -A && git commit -m "refactor: migrate pr-ops to ops"`

### Task 5: Full verification, review, and PR finalization

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `ops/backlog.md`
- Modify: `ops/artifact-map.md`
- Modify: PR #568 title/body/state

**Interfaces:**
- Consumes: completed implementation and all local validation commands.
- Produces: clean pushed branch, accurate ready-for-review PR, and passing fresh CI.

- [ ] **Step 1: Update lifecycle records**

Mark the Sprint 13 items implemented/review with issue #567 and PR #568 traceability; update artifact map and changelog for the root contract, standard, routing file, templates, and migration.

- [ ] **Step 2: Run every test script**

Run each `tools/test-*.sh`, saving combined output to `/tmp/issue567-test-logs/` and checking every exit status.

- [ ] **Step 3: Run production validators**

Run the contributing-guide checks: agent rule size, file naming, frontmatter, repository structure, RRP links, historical immutability, evidence structure, nonempty diff, and manifest check.

- [ ] **Step 4: Audit repository references and diff**

Run `git grep -n 'pr-ops/'`, verify all changed Markdown links resolve, inspect `git diff upstream/main...HEAD`, and confirm no unrelated feature removal or named `plans`/`tasks` rule was introduced.

- [ ] **Step 5: Request code review**

Review the complete diff against issue #567 and fix all critical/important findings, then rerun focused and full checks.

- [ ] **Step 6: Commit final records**

Run: `git add CHANGELOG.md ops/backlog.md ops/artifact-map.md templates/manifest.json && git commit -m "docs: record AGENTS physical integration"`

- [ ] **Step 7: Verify clean state and synchronize base**

Fetch upstream, merge `upstream/main` if it moved, rerun the full suite, and verify `git status --short` is empty.

- [ ] **Step 8: Push and finalize PR**

Push only `issue-567-f41623e824fb`; update PR #568 title/body with reproduction, test evidence, migration notes, and `Closes #567`; mark it ready.

- [ ] **Step 9: Verify fresh CI**

List recent runs with timestamp/SHA, ensure the run is for the latest pushed commit, download logs for any non-passing run into `ci-logs/`, diagnose/fix the actual errors, and report the final passing run with the PR URL.
