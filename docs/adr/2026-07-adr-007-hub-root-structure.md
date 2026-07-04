---
status: accepted
version: 0.2
updated: 2026-07-04
temperature: 0.1
owner: G-Ivan-A
decision-type: methodology
---

# ADR-007: Целевая структура корня Хаба

## Decision Metadata

| Field | Value |
| --- | --- |
| ADR | ADR-007 |
| Backlog item | B-047 |
| Decision type | methodology |
| Status | accepted |
| Decision date | 2026-07-04 |
| Owner | G-Ivan-A |
| Source issue | [#378](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/378) |
| Refinement issue | [#382](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/382) |
| Primary input | [B-034 migration and root structure plan](../analysis/2026-07-04-hub-migration-and-root-structure-plan.md) |
| Upstream decisions | [ADR-001](2026-06-adr-001-ecosystem-infrastructure-methodology.md), [ADR-002](2026-06-adr-002-artifact-document-methodology.md) |
| Impacted artifacts | `governance/backlog.md`, `governance/artifact-map.md`, `governance/repo-model.md`, `tools/validate-repository-structure.sh`, future B-048 migration PR |
| Supersedes | none |
| Superseded by | none |

## Context

B-034 produced an upstream analysis/plan for the current Hub root structure after
Research, Analysis and Audit standardization. That analysis intentionally left
several root-level targets as ambiguous because they needed founder decision.

Issue #378 closes those ambiguities. The decision is already made by the
founder, so this ADR records the accepted target and downstream consequences
instead of proposing an RFC with alternatives. This ADR does not physically move
files, rewrite links or cancel current entry points. Physical migration remains
the scope of B-048 after ADR-007 acceptance.

ADR-001 and ADR-002 remain the source of truth for ecosystem infrastructure and
artifact routing. The Research/Analysis/Audit standards are not a source of root
repository structure. The Hub remains Archetype A; Hub != Portal.

PR #379 merged this ADR as the B-047 decision gate. Issue #382 refines the
record by making the final target tree readable without opening ADR-001 in
parallel; it does not change the accepted architecture and does not perform
physical migration.

## Decision

Полная структура Хаба = ADR-001 (универсальное ядро) + ADR-007 (дельта для архетипа A).
Ниже приведена полная целевая структура (To-Be) с комментариями.

Adopt the following To-Be root decisions for the Hub repository.

### Full To-Be Repository Structure

This tree is the consolidated B-048 target. It lists structural homes and
stable anchors, not every current file. Current paths remain active until the
physical migration PR rewrites links and registries.

```text
hybrid-Intelligence-lab/
├── ai-governance/                 # [NEW] Политики: государство, бизнес-правила, ИБ, внешние ограничения
├── ai-rules/                      # [NEW] Правила поведения агента и быстрая синхронизация внешнего агента
├── pr-ops/                        # [NEW] Управление задачами, PR и review; плоско по правилу 2FA
├── standards/                     # Плоские стандарты; provisional = lifecycle status draft/proposed
├── docs/                          # Документация, решения и outputs по типам артефактов
│   ├── adr/                       # ADR decision records
│   ├── rfc/                       # Proposal-stage RFC; target for migrated governance/rfc/
│   ├── analysis/                  # Analysis-артефакты
│   ├── audit/                     # Audit-отчёты и conformance checks
│   ├── report/                    # General reports and statistics
│   ├── guides/                    # Человеко-ориентированные руководства; target from ADR-007
│   └── concept.md                 # Target for current root CONCEPT.md
├── kb/                            # Операционно применимые знания; вводится по факту боли
│   ├── taxonomy/                  # Operational taxonomies
│   ├── roles/                     # Role definitions used during execution
│   ├── rules/                     # Reusable operational rules that are not AI-agent behavior rules
│   ├── processes/{name}/          # Process-specific operational knowledge
│   └── patterns/                  # Reusable execution patterns
├── runs/                          # Execution records and reproducible run outputs
├── research/                      # Доменный research; базовое расширение archetype A
│   ├── hub/                       # Hub methodology and governance research
│   ├── mango/                     # Mango domain research
│   ├── open-ai-ru/                # Open-ai.ru project research
│   ├── reputation-technologies/   # Reputation Technologies research
│   ├── governance/                # Governance research corpus
│   ├── cicd/                      # CI/CD research corpus
│   └── external-knowledge/        # External source registry and derived insights
├── practices/                     # Внешние практики экосистемы; специфика Хаба в корне
│   ├── agent-work/                # Практики AI-assisted work
│   └── ai-governance/             # External AI governance practices, not the policy bucket
├── projects/                      # Проектные споки/подпроекты
│   ├── education-ba-prompt/       # Education BA Prompt spoke materials
│   └── repo-development/          # Repository-development spoke materials
├── projects-sink/                 # [NEW] Управленческий буфер приёма из проектов; плоский intake
├── frameworks/                    # [Зарезервировано] Future home for frameworks after research -> standard confirmation
├── education/                     # [Зарезервировано] Cross-project education materials
├── templates/                     # Копируемые поверхности for HTOM/spoke reuse
│   ├── htom/                      # HTOM team template surface
│   └── spoke/                     # Spoke repository template surface
├── tools/                         # Валидаторы и maintenance utilities
├── .github/                       # CI workflows and issue templates
├── GOVERNANCE.md                  # Target org-governance anchor aligned with AI_GOVERNANCE.md
├── README.md                      # Repository entry point
├── CHANGELOG.md                   # Date-based governance change log
├── CONTRIBUTING.md                # Contribution workflow and local validation commands
├── LICENSE                        # License placeholder until final license decision
├── .gitignore                     # Git ignore rules
└── .gitattributes                 # Optional git attributes anchor if introduced

# Удалено при миграции: website/, mkdocs.yml, experiments/
```

| Target | Decision |
| --- | --- |
| `projects-sink/` | Create a Hub-specific flat management intake buffer for incoming material from ecosystem projects. Move `AI_PROJECT_CONTEXT-Summary.md` there during physical migration. |
| `ai-governance/` | Use for policies: state constraints, business rules, information security, external compliance and other policy-level obligations. |
| `ai-rules/` | Use for agent behavior rules and fast synchronization of an external agent with project context. |
| `practices/` | Keep at the repository root as a Hub-specific divergence from ADR-001 `docs/practice/`. |
| `docs/guides/` | Use as the unified home for guides. A missing backlog task for guide migration is not a blocker; it can be added or renumbered after migration. |
| `education/` | Use for cross-project education materials. A follow-up standard for archetype D can be added or renumbered after migration. |
| `frameworks/` | Reserve as the future home for frameworks after the research -> standard path confirms framework scope. |
| `docs/concept.md` | Use as the target for current root `CONCEPT.md`. |

Delete or retire the following root artifacts during physical migration:

| Current artifact | Decision |
| --- | --- |
| `website/` | Retire because the Hub web strategy is cancelled. The Hub must not be turned into Portal. |
| `mkdocs.yml` | Retire as a consequence of cancelling the Hub website strategy. |
| `experiments/` | Retire as a root directory. Validator tests move to `tools/`; no other experiment corpus remains there. |

Split the current `governance/` area as follows:

| Current area | To-Be route |
| --- | --- |
| policy, compliance and external constraints | `ai-governance/` |
| PR/task/review operations | `pr-ops/` |
| RFC documents | `docs/rfc/` |
| `governance/rfc/` | `docs/rfc/` |

Use lifecycle status as the provisional-standard mechanism:

- `draft` and `proposed` status mark provisional standards.
- Do not create `standards/provisional/` now.
- Create `standards/provisional/` only if review pain proves that lifecycle
  status is insufficient.

Adopt the following implementation strategy for B-048:

1. Phase 0: accept this ADR as B-047 decision gate.
2. Phase 1: introduce neutral target anchors without changing semantics.
3. Phase 2: move `governance/rfc/` to `docs/rfc/` with link rewrites.
4. Phase 3: split `governance/` into `ai-governance/`, `ai-rules/`, `pr-ops/`
   and `docs/rfc/`.
5. Phase 4: reconcile all previously ambiguous entities as one task/PR, not as
   one PR per catalog. The executor runs validators and cross-reference
   stress-tests inside the PR before review.
6. Phase 5: synchronize validators, artifact-map, repo-model, manifest and
   navigation in the same PR as the structural changes.
7. Phase 6: stabilize aliases and remove transitional compatibility only after
   links and registries are proven stable.

Link rewrite strategy:

- Rewrite links in the same PR as the physical move.
- Keep aliases or compatibility notes until cross-references stabilize.
- Use named anchors, not section numbers.
- Update artifact-map, repo-model, validators and other synchronous registries
  in the same PR as path changes.

## Decision Drivers

- B-034 identified the root-structure source of truth as ADR-001 plus ADR-002,
  not Research/Analysis/Audit standards.
- The founder decision already exists; an RFC would reopen a closed decision and
  add review overhead.
- The Hub must remain an ecosystem infrastructure Hub and must not drift into a
  Web Portal profile.
- `ai-governance/` and `ai-rules/` need a stable semantic boundary before file
  moves, otherwise policy/compliance material and agent behavior rules will
  collapse back into one bucket.
- Provisional standards need a low-inflation mechanism; lifecycle status is
  enough until proven otherwise.
- B-048 needs a single implementation strategy that combines moves, link
  rewrites, aliases and registry synchronization.

## Alternatives Considered

This ADR intentionally does not propose alternatives or trade-offs. B-034
recorded the open options and issue #378 records the founder decision that closes
them. No alternative is under review in this ADR.

## Consequences

| Backlog item | Consequence |
| --- | --- |
| B-048 | Is the physical migration task after ADR-007/B-047 acceptance. It implements this target structure and performs the integrity stress-test before review. |
| B-054 | Remains deferred until after migration and standard-desync repair; the B-048 stress-test is execution evidence, not the future process standard itself. |
| B-055 | Is absorbed by ADR-007/B-047 for the `ai-governance/` vs `ai-rules/` boundary. A separate post-migration ADR is not needed unless this ADR is later superseded. |
| B-056 | Uses this ADR as the policy/rule split source when physically separating current governance material. |
| B-057 | Reserved logical follow-up for `docs/guides/` routing if migration work needs a separate backlog item. |
| B-058 | Reserved logical follow-up for `education/` and archetype D education standardization. |
| B-059 | Reserved logical follow-up for `frameworks/` research -> standard confirmation. |
| B-060 | Reserved logical follow-up for `CONCEPT.md` -> `docs/concept.md`. |
| B-061 | Reserved logical follow-up for `AI_PROJECT_CONTEXT-Summary.md` -> `projects-sink/`. |
| B-062 | Reserved logical follow-up for retiring `website/`, `mkdocs.yml` and root `experiments/`. |

B-057..B-062 are named here as consequence slots, not as created backlog rows.
If current backlog numbering differs at migration time, they may be created or
renumbered without blocking B-048.

Current repository paths remain active until B-048 performs the physical
migration. This ADR changes decision state and registries only.

## Impacted Artifacts

| As-Is | To-Be | Impact |
| --- | --- | --- |
| `governance/backlog.md` | future `pr-ops/` backlog area | Current backlog marks B-047 as the accepted ADR gate and B-048 as the physical migration task. |
| `governance/artifact-map.md` | future registry location governed by B-048 | Current artifact-map registers this ADR and remains the active map until migration. |
| `governance/repo-model.md` | future synchronized repo model | B-048 updates it with accepted target paths. |
| `governance/rfc/` | `docs/rfc/` | RFC path migration happens in B-048. |
| `AI_GOVERNANCE.md` and policy material | `ai-governance/` | Policy/compliance material moves according to the boundary in this ADR. |
| agent behavior and sync material | `ai-rules/` | Agent behavior rules and quick-sync context move according to the boundary in this ADR. |
| `practices/` | `practices/` | Root location remains accepted for Hub-specific practices. |
| guide material | `docs/guides/` | Unified guide home is accepted; backlog task may be added later. |
| education material | `education/` | Cross-project education home is accepted; archetype D standardization remains follow-up. |
| framework material | `frameworks/` | Future framework home is accepted after research -> standard confirmation. |
| `CONCEPT.md` | `docs/concept.md` | Physical move remains B-048 or downstream consequence task. |
| `AI_PROJECT_CONTEXT-Summary.md` | `projects-sink/` | Physical move remains B-048 or downstream consequence task. |
| `website/` | removed | Hub web strategy is cancelled. |
| `mkdocs.yml` | removed | Removed as website cancellation consequence. |
| `experiments/` | removed; validator tests in `tools/` | Root experiments directory is retired. |
| provisional standards | lifecycle status `draft` or `proposed` | `standards/provisional/` is not created unless review pain appears. |

## Compliance and Validation

This ADR complies with `standards/adr-structure-standard.md` by using ADR
frontmatter, required sections, decision metadata, lifecycle and related
artifacts. The `Alternatives Considered` section is intentionally closed because
the founder decision has already been made.

This PR validates the decision record and registry synchronization with:

- `./tools/validate-frontmatter.sh .`
- `./tools/validate-file-naming.sh`
- `./tools/validate-repository-structure.sh`

B-048 must additionally validate moved links, aliases, artifact-map,
repo-model, validators, manifest and navigation in the same PR as the physical
migration.

## Lifecycle

This ADR is `accepted` after PR #379 was merged by the repository owner on
2026-07-04. B-047 is complete, and B-048 is the next physical migration task.
Issue #382 is an accepted-ADR refinement: it adds the consolidated To-Be tree
for readability and AI-agent execution, without reopening the decision. Future
ADRs may supersede this decision only by naming the scope they replace.

## Related Artifacts

- [Issue #378](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/378)
- [Issue #382](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/382)
- [B-034 migration and root structure plan](../analysis/2026-07-04-hub-migration-and-root-structure-plan.md)
- [ADR-001: Ecosystem infrastructure methodology](2026-06-adr-001-ecosystem-infrastructure-methodology.md)
- [ADR-002: Artifact/document methodology](2026-06-adr-002-artifact-document-methodology.md)
- [ADR-003: Research structure](2026-07-adr-003-research-structure.md)
- [ADR-004: Reports structure](2026-07-adr-004-reports-structure.md)
- [ADR-005: Audit structure](2026-07-adr-005-audit-structure.md)
- [ADR-006: Analysis structure](2026-07-adr-006-analysis-structure.md)
- [ADR structure standard](../../standards/adr-structure-standard.md)
- [Backlog](../../governance/backlog.md)
- [Artifact map](../../governance/artifact-map.md)
