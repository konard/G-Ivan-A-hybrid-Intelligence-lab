---
status: canonical
version: 1.55
updated: 2026-09-04
temperature: 0.1
type: backlog
context: [governance, backlog, active-sprints, pr-ops, synchronization]
method: creative-analysis + dependency-mapping
scope: repo-wide
related_artifacts:
  - "pr-ops/backlog-instruction.md"
  - "pr-ops/artifact-map.md"
  - "pr-ops/repo-model.md"
  - "standards/glossary.md"
  - "standards/audit-standard.md"
  - "docs/analysis/2026-06-30-backlog-and-artifact-change-policy-analysis.md"
  - "docs/analysis/2026-07-04-kb-runs-hub-applicability-analysis.md"
  - "docs/adr/2026-07-adr-007-hub-root-structure.md"
  - "docs/adr/2026-07-adr-008-standard-meta-structure.md"
  - "standards/standard-meta-structure.md"
  - "docs/audit/2026-07-04-cross-standard-stress-tests.md"
  - "research/hub/2026-07-04-hub-as-agent-system-global-analysis.md"
  - "docs/rfc/2026-08-06-rfc-task-statement-architecture.md"
  - "docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md"
  - "research/ba-requirements/2026-08-26-m0-m2-layering-hypothesis-check.md"
  - "research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/README.md"
  - "research/ba-requirements/normalization/00-introduction.md"
  - "research/hub/2026-07-31-ops-task-strategy-validation.md"
  - "tools/test-post-migration-validator.sh"
  - "LICENSE"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/396"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/392"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/297"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/294"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/296"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/328"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/370"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/374"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/376"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/380"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/386"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/390"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/394"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/398"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/400"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/402"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/411"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/413"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/419"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/417"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/427"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/434"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/423"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/436"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/437"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/449"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/475"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/511"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/515"
---

# BACKLOG - активные спринты Хаба

Этот файл показывает только незавершённые задачи и их логический порядок.
Правила ведения бэклога вынесены в
[backlog-instruction.md](backlog-instruction.md).

Завершённые задачи удаляются из активного бэклога после архивации спринта.
История остаётся в GitHub Issues/PR, `CHANGELOG.md` и самих артефактах; отдельный
архивный файл бэклога не создаётся.

Если факта нет в исходных issue, PR, артефакте или текущем бэклоге, значение
указывается как `null`. Спринты ниже сгруппированы по логическим цепочкам, а не
по приоритетам.

---

## Спринт 3: Ремонт структуры стандартов

**Story.**
Кросс-стресс-тест issue #370 обнаружил рассинхрон между Research, Analysis,
Audit и Report standards. Stress-test artifact уже маршрутизирован в Audit;
теперь нужно выбрать общий инвариант и только после этого править стандарты.

Этот спринт сохраняет цепочку Analysis -> ADR -> Standard -> Implementation.
Так он не смешивает аудит, выбор решения, нормирование и массовое обновление
существующих стандартов в один PR.

**Цель.**
Принять и применить единый skeleton для стандартов, чтобы future standards не
расходились по section order, profile/model policy и boundary delegation.

**Критерий закрытия.**
B-050/B-051 приняли решение, B-052 создал meta-standard, B-053 выровнял четыре
стандарта, а B-054 остался отложенным или выполнен после B-053.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-050** | Варианты решения структурного рассинхрона стандартов R/A/A/Report | **P1** | B-049 | review | [#407](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/407), [#415](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/415) | Issue #374; findings issue #370; [analysis B-050](../docs/analysis/2026-07-10-r-a-a-report-structural-desync-options.md) | Review amendment устранил circular scoring и вынес в B-051 явный выбор: baseline E либо skeleton F8/F10/F12; `Type Model` = `model`/`N/A`, specific tail связан с Purpose/Scope, routing owner = ADR-002, миграция разделена на mechanical/semantic. Стандарты и валидаторы не менялись. | Hybrid |
| **B-051** | Принять мета-структуру стандартов | **P1** | B-050 | DONE | [#417](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/417), [#434](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/434) | Issue #374; [analysis B-050](../docs/analysis/2026-07-10-r-a-a-report-structural-desync-options.md); [ADR-008](../docs/adr/2026-07-adr-008-standard-meta-structure.md) | Founder decision принят: F10 explicit с точным порядком 10 секций, `N/A + rationale` для всех пустых invariant sections, `Type Model` = `model`/`N/A`, Purpose/Scope cross-reference для specific tail и ADR-002 как canonical routing owner. Issue #434 расширил gate на все стандарты экосистемы и закрыл цикл. | Hybrid |
| **B-052** | Создать мета-стандарт структуры стандартов | **P1** | B-051 | DONE | [#423](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/423) / [PR #435](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/435) / [PR #448](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/448) | Issue #374; [ADR-008](../docs/adr/2026-07-adr-008-standard-meta-structure.md); [Standard Meta-Structure Standard](../standards/standard-meta-structure.md) | F10 explicit нормативно зафиксирован для всех стандартов экосистемы: десять уникальных секций в строгом порядке, `N/A + rationale`, `Type Model` = `model`/`N/A`, specific-tail cross-reference и ADR-002 как canonical boundary owner. PR #448 синхронизировал мета-стандарт, навигацию и validator после расширения scope. | Structured |
| **B-053** | Привести Research/Analysis/Audit/Report standards к мета-стандарту | **P1** | B-052 | DONE | [#451](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/451) / [PR #452](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/452) | Issue #374; [Standard Meta-Structure Standard](../standards/standard-meta-structure.md) | Четыре стандарта приведены к F10 двумя reviewable слоями: mechanical block moves (десять инвариантных секций в строгом порядке, `Type Model` = `model`/`N/A`) и обоснованные semantic deltas (specific-tail cross-reference на `Purpose`/`Scope`, ADR-002 как canonical boundary owner). Дополнительно закрыт вопрос Q5 Evals Contract по смягчённому specific-tail правилу (ADR-008 v0.2). Реализация смержена в PR #452. | Structured |
| **B-054** | Стандарт процесса стресс-тестирования связанных документов | **P3** | B-048, B-053 | TODO | - (deferred) | Issue #374; issue #370 | Отложенная process-задача: описать триггеры, метод, severity/output route и критерии acceptance для повторяемых cross-document stress tests. Не делать до B-053. | Structured |

---

## Спринт 4: Post-migration границы корня Хаба

**Story.**
ADR-007 и PR #388 физически перестроили корень Хаба, но часть follow-up решений
остаётся на уровне активной синхронизации. Здесь собраны задачи, которые
уточняют границы `ai-governance/`, `ai-rules/`, `practices/`, retired website
strategy и будущих root catalogs.

Спринт отделяет уже поглощённые ADR-007 решения от ещё не начатых
trigger-based исследований. Это важно после миграции: новые каталоги не должны
заполняться на вырост, а follow-up должен возникать из реальной боли.

**Цель.**
Довести post-migration границы до исполнимого состояния без расширения
репозитория пустыми правилами и speculative artifacts.

**Критерий закрытия.**
Boundary work по `ai-governance/`/`ai-rules/` выполнен или явно закрыт;
absorbed ADR-007 задачи закрыты; B-059..B-062 стартуют только по своим триггерам.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-056** | Физически разделить remaining policy/rule material между `ai-governance/` и `ai-rules/` | **P1** | B-048, B-047 | DONE | [#425](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/425) / [PR #430](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/430) | Issue #376; issue #378; B-034 Phase 3; ADR-007/B-047 | Root `AI_GOVERNANCE.md` разделён на policy-контракт `ai-governance/ai-governance.md` и agent rules `ai-rules/agent-work-rules.md`; `GOVERNANCE.md` оставлен thin root-anchor по ADR-007. Ссылки, validator и artifact map синхронизированы; остаточные ссылки на root `AI_GOVERNANCE.md` в `pr-ops/artifact-map.md` и в `standards/` дочищены по находкам G-08/G-11 аудита #529 ([issue #533](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/533)). | Hybrid |
| **B-057** | Зафиксировать специфичность Хаба: root `practices/` vs `docs/practice/` | **P1** | B-047 | DONE (absorbed by ADR-007/B-047) | [#378](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/378) | Issue #380; B-034 document-plan; ADR-007 | ADR-007 оставляет root `practices/` как Hub-specific Archetype A extension; отдельный ADR не требуется. | Structured |
| **B-058** | Отменить или подтвердить веб-стратегию Хаба (`website/`, `mkdocs.yml`) | **P1** | B-047 | DONE (absorbed by ADR-007/B-047) | [#378](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/378) | Issue #380; B-034 document-plan; ADR-007; former `mkdocs.yml`; merged PR #388 | ADR-007 retired `website/` and `mkdocs.yml`; PR #388 физически удалил их. | Structured |
| **B-059** | Проверить целесообразность `docs/guides/` как единого дома руководств | **P3** | B-048 | TODO | - (deferred) | Issue #380; B-034; ADR-007; current `guides/` | Triggered research for guide routing when `guides/` vs `docs/guides/` creates review pain or a reconcile task needs a decision. | Creative |
| **B-060** | Структура и правила наполнения `projects-sink/` | **P3** | B-048 | TODO | - (deferred) | Issue #380; B-034 Phase 4; ADR-007; `projects/` intake pain | Triggered research for managed intake from ecosystem projects. Rules should follow real intake ambiguity, not placeholder taxonomy. | Creative |
| **B-061** | Learning Profile архетипа D для `education/` | **P3** | B-048 | TODO | - (deferred) | Issue #380; B-034; ADR-007; `standards/education-profile.md` | Defer until founder starts an actual course or learning product; then standardize education/Learning Profile boundaries from practice. | Creative |
| **B-062** | Стандарт фреймворков (архетип A/B) для `frameworks/` | **P3** | B-048 | TODO | - (deferred) | Issue #380; B-034; ADR-007; current `frameworks/` placeholder | Defer until the first reusable framework emerges and the repo must decide whether it belongs to Hub capability or spoke/product material. | Creative |

---

## Спринт 6: V2 — тонкий вертикальный срез «Валидация ФТ/ТЗ»

**Story.**
До-исследование §15 (issue #400) показало: прежний анализ закрыл структурную
готовность к миграции репо→агент, но не операционно-измеримую. Рекомендация для
RFC — **V2**, тонкий вертикальный срез на процессе «Валидация ФТ/ТЗ» с двумя
параллельными треками (библиотека промптов по статистике ∥ первый Агент). §15.8
выделяет три входа, замыкающих разрывы готовности ПГ-4: контракт evals (RFC-A),
правило изменения библиотеки по run-статистике (RFC-B) и план инфраструктуры
первого Агента (RFC-C). Четвёртый вход — наблюдаемость (RFC-G): нужен ли Хабу
эпизодический слой прогонов, без которого run-статистика RFC-B не на чем считать.

Этот спринт собран как причинная цепочка одной способности — сделать работу
агента измеримой: сначала контракт качества (evals), затем правило улучшения по
статистике и план первого агента, с открытым вопросом наблюдаемости в основании.
Он отделён от несущих правок (Спринт 5), потому что строит новую операционную
способность, а не чинит текущую модель.

**Цель.**
Подготовить входы для RFC, превращающие структурную готовность Mango в
операционно-измеримый срез V2, без принятия решений за человека (Rule 4).

**Критерий закрытия.**
Каждый вход (B-067..B-070) либо эскалирован в собственный RFC/ADR, либо явно
отложен под свой триггер. Наблюдаемость (B-070) координируется с анализом kb/runs
(`docs/analysis/2026-07-04-kb-runs-hub-applicability-analysis.md`) и ADR-007.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-067** | Контракт `evals`/golden-sets для спока | **P1** | - | DONE | [#426](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/426), [#434](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/434) | Global analysis v0.4 §15.8.2/RFC-A; §15.1.6; ПГ4.3; §11-D1/R6; [ADR-008](../docs/adr/2026-07-adr-008-standard-meta-structure.md) | Контракт [`standards/evals-contract-standard.md`](../standards/evals-contract-standard.md) принят; issue #434 включил Evals Contract в универсальную область F10 ADR-008 и закрыл цикл. Значения порогов и минимальное N не назначены (Rule 4) — остаются за B-068; post-merge исправления вынесены в отдельный трек. | Hybrid |
| **B-068** | Правило «изменение библиотеки промптов по run-статистике» + порог N | **P1** | B-067, B-070 | TODO | - (planned) | Global analysis v0.4 §15.8.2/RFC-B; §15.6.1; ПГ-5; §11-A2/R4 | Governance-правило: когда run-статистика (при минимальном N + человеческое ревью) даёт основание менять библиотеку промптов. Требует контракта evals (B-067) и эпизодического слоя прогонов (B-070). | `null` |
| **B-069** | План инфраструктуры первого Агента (V2, «Валидация ФТ/ТЗ») | **P1** | B-067 | TODO | - (planned) | Global analysis v0.4 §15.8.2/RFC-C; §15.6.2; ПГ-6 | Проектный план тонкого вертикального среза: инфраструктура первого Агента на процессе «Валидация ФТ/ТЗ» с human gate на статус (RO2). Опирается на контракт evals (B-067). | `null` |
| **B-070** | Наблюдаемость: нужен ли Хабу эпизодический слой (`runs/`) (закрывает R4) | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §15.8.2/RFC-G; §15.1.7; Q1; §11-A2/R4; ADR-007 | Открытый вопрос AgentOps: нужен ли Хабу журнал прогонов/трасс как эпизодическая память. Поглощает R4 (тот же пробел A2). Текущее решение по kb/runs (анализ 2026-07-04 + ADR-007) — не вводить до боли; строка держит вопрос трассируемым. | `null` |

---

## Спринт 7: Триггерные входы RFC/ADR из анализа v0.4

**Story.**
Оставшиеся входы §8/§11/§15.8 — второго порядка: они не чинят несущий дефект и не
входят в срез V2, а ждут собственного операционного триггера. Мета-рекомендация
§8 прямо запрещает внедрять их пакетом: каждый проходит собственный цикл
observation→RFC→ADR под свою боль, иначе массовое «улучшение» само нарушает
anti-inflation (H7, «start simplest»).

Внутри спринт держит несколько причинных пар: роутер и разум (доспецификация
роутера R5 и критерий вызова Deep Think R9 — оба про интерпретацию входа §9.1);
семантическая целостность (guardrails заземления цитат R6 и машиночитаемый тег
`layer` RFC-E, закрывающий single-source-of-truth R7); петля обучения (обратный
поток Hub↔project R8, без которого метрика петли R11 неизмерима). Отдельно —
watch-item внешних норм (R10) и учебный актив (RFC-F). Все строки — трассируемые
входы для человеческого RFC/ADR, не решения (Rule 4).

**Цель.**
Сохранить трассируемость P2/P3-входов v0.4, чтобы отсутствие строки не читалось
как упущение, но не запускать их до появления реальной боли.

**Критерий закрытия.**
Каждая строка стартует только по своему триггеру: либо эскалируется в RFC/ADR при
появлении боли, либо остаётся отложенной. Спринт не закрывается «пакетом».

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-071** | Доспецифицировать роутер для verb-less / unknown-type входа | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §8/R5; §11-A1; H1/H2 | Роутер недоспецифицирован на входе без глагола / без объекта / неизвестного типа — нет явного правила дефолта и эскалации к человеку. Малая правка research-модели роутера; ценность растёт с числом нетипичных задач. | `null` |
| **B-072** | Семантические guardrails: заземление цитат и проверка ссылок | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §8/R6; §11-D1; H12/H13/H20 | CI проверяет только форму; онбординг покрывает вход, но не середину исполнения. Добавить семантическую проверку (grounding цитат, валидность ссылок) с оценкой стоимости/ложных срабатываний на пилоте. | `null` |
| **B-073** | Машиночитаемый тег `layer` (проект/продукт) (закрывает R7) | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §15.8.2/RFC-E; §15.3.2; ПГ3.5; H11; §11-G4/R7 | Контракт формы против расползания слоёв проект/продукт (RO4) и дрейфа корпуса норм. Поглощает R7 (тот же пробел G4): enforced-граница как single source of truth. | `null` |
| **B-074** | Материализовать обратный поток Hub↔project (трасса синка, арбитраж) | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §8/R8; §9.2; §11-F1; H22 | Синхронизация Hub↔project недоматериализована (наименее зрелая область, 5 ⚠️): нет обратного потока практика→норма, арбитража конфликтов человеком и единой трассы синка. Требует продуктового решения о механике петли. | `null` |
| **B-075** | Критерий «когда вызывать Deep Think» + единое fail-состояние | **P3** | - | TODO | - (deferred) | Global analysis v0.4 §8/R9; §11-D2; H4/H8/H16 | Deep Think сейчас редкий метод; нужен критерий вызова, защита от само-галлюцинации панели и единое fail-состояние. Вводить только когда Deep Think станет частым. | `null` |
| **B-076** | Отслеживание версий внешних норм (EU AI Act, OWASP, NIST) | **P3** | - | TODO | - (deferred) | Global analysis v0.4 §8/R10; §11-G3; H24 | Внешние нормы эволюционируют — риск устаревания проекций. Watch-item; вводить после стабилизации корпуса, иначе обслуживание ради обслуживания. | `null` |
| **B-077** | Метрика эффективности петли обучения (practice-exchange) | **P3** | B-074 | TODO | - (deferred) | Global analysis v0.4 §8/R11; §11-F2; H23 | Нельзя измерить, «прижилась» ли практика. Требует сперва материализованной петли обучения (B-074/R8), поэтому зависит от неё. | `null` |
| **B-078** | Разместить учебный курс в `education/` Хаба | **P2** | - | TODO | - (deferred) | Global analysis v0.4 §15.8.2/RFC-F; §15.2.4; Vision | Международно-заземлённый курс рискует застрять в споке (RO6). Разместить учебный актив в `education/` Хаба как образовательный актив архетипа A. Наполнение — глоссарий §15.9. | `null` |

---

## Спринт 8: Разделение Mango на два репозитория

**Story.**
Текущий репозиторий `mango_ba_prompts` совмещает две роли: операционку (боевые
промпты с приватными данными, прогоны, golden-sets) и публичную методологию
(переиспользуемые паттерны, стандарты, примеры). Это создаёт проблемы:
приватные данные не могут быть публичными, публичный репо не может быть
витриной, разные темпы изменений требуют разных ревью-процессов. Фаундер
принял решение (обсуждение 2026-07-10) разделить Mango на публичный репо
`ai-ba-playbooks` (продукт-методология, архетип B, без привязки к бренду
Mango), а существующий `mango_ba_prompts` перевести в режим Private, оставив
его операционкой Mango (уточнение issue #511: новый приватный репозиторий не
создаётся).

Спринт собран как причинная цепочка: сначала ADR фиксирует решение в Хабе
(принцип «сначала Хаб, потом Mango»), затем план миграции определяет, что
куда переносится, затем создаётся публичный репозиторий и переводится в Private приватный, затем выполняется
физическая миграция артефактов, и в конце настраивается и тестируется
односторонняя синхронизация приватный → публичный.

**Цель.**
Получить два репозитория с разными жизненными циклами и аудиториями —
новый публичный `ai-ba-playbooks` и переведённый в Private
`mango_ba_prompts`, — распределить между ними артефакты и настроить
одностороннюю синхронизацию приватный → публичный.

**Критерий закрытия.**
Спринт закрывается, когда ADR B-079 принят, план миграции B-080 составлен,
публичный репозиторий создан (B-081), `mango_ba_prompts` переведён в Private
(B-082), артефакты мигрированы (B-083), а синхронизация настроена и
протестирована (B-084).

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-079** | ADR о разделении Mango на два репозитория | **P1** | - | DONE | [#424](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/424) / [PR #429](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/429) | Обсуждение 2026-07-10 (решение фаундера); issues #411, #413 | Решение фаундера о разделении Mango на публичный (`ai-ba-playbooks`) и приватный (`mango_ba_prompts` в режиме Private) репозитории зафиксировано в ADR-009; уточнение модели двух репозиториев внесено по issue #511. | Hybrid |
| **B-080** | План миграции Mango | **P2** | B-079 | DONE | [#436](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/436) / [PR #442](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/442) / [PR #447](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/447) | ADR-009 (B-079); issues #411, #413, #446; снимок `mango_ba_prompts@295b65d` | Детальный план миграции построен на фактическом снимке: правила классификации и обезличивания, таблица маршрутизации, фазы и риски. PR #447 зафиксировал решение Q2: всё дерево `kb/` переносится в приватный репозиторий; до B-083 остаётся закрыть Q1 о фактической публичности исходного репозитория. | Hybrid |
| **B-081** | Создание публичного репо `ai-ba-playbooks` | **P2** | B-079, B-080 | ЧАСТИЧНО | - (planned) | ADR B-079; план миграции B-080; issues #411, #413 | Создать публичный репозиторий `ai-ba-playbooks` с базовой структурой архетипа B (`prompt-library/`, `patterns/`, `standards/`, `examples/`, `docs/`, `templates/`) и настроить GitHub Pages для презентационного слоя. | Structured |
| **B-082** | Перевод `mango_ba_prompts` в режим Private | **P2** | B-079, B-080 | TODO | - (planned) | ADR B-079; план миграции B-080; issues #411, #413, #446, #511 | Перевести существующий репозиторий `mango_ba_prompts` в режим Private с сохранением имени, привести структуру операционки к ADR-009 (`prompts/`, полное дерево `kb/`, `runs/`, `evals/`, `internal-rfc/`, `internal-docs/`) и настроить проверки без GitHub-hosted runners: локальные валидаторы либо self-hosted runner в Docker. | Structured |
| **B-083** | Физическая миграция артефактов из `mango_ba_prompts` | **P2** | B-081, B-082 | TODO | - (planned) | План миграции B-080; issues #411, #413 | Перенести артефакты из `mango_ba_prompts` в новые репозитории согласно плану миграции B-080, обновить ссылки и реестры, прогнать валидаторы. | Structured |
| **B-084** | Синхронизация и тестирование | **P2** | B-083 | TODO | - (planned) | ADR B-079; issues #411, #413 | Настроить одностороннюю синхронизацию приватный → публичный (ручной отбор на старте), протестировать workflow и задокументировать lessons learned. | Structured |

## Спринт 9: Теоретическая основа образовательного модуля

**Story.**
Глобальный анализ v0.4 (§15.2) фиксирует структуру обучения и выносит RFC-F
(«Размещение учебного курса в `education/` Хаба») как вход для решения
фаундера. Но RFC-F нечем наполнить: решение о курсе по retrieval-стратегиям
принималось бы на основании блогов и вкусовых предпочтений, а не на основании
того, что известно предметной области. Спринт закрывает этот разрыв: сначала
исследование даёт source-backed теорию, затем RFC-F принимает решение о
продукте.

**Цель.**
Дать фаундеру проверяемый вход для RFC-F: что известно про retrieval-стратегии,
откуда это известно, какие утверждения не выдерживают проверки и какие
конструкции (матрица, уровни готовности) переиспользуемы за пределами курса.

**Критерий закрытия.**
Спринт закрывается, когда исследование B-085 принято фаундером и RFC-F получил
вход. Решение о самом курсе — предмет отдельной задачи (Rule 4).

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-085** | Исследование retrieval-стратегий для AI-агентов | **P2** | - | review | [#418](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/418) | Issue #418 (постановка фаундера, гипотезы H1–H7); глобальный анализ v0.4 §15.1.4, §15.1.6, §15.2.5 (RFC-F) | Научно-теоретическое исследование retrieval-стратегий реализовано как модуль [`research/ai-education/retrieval/`](../research/ai-education/retrieval/) из шести файлов и [RFC Reference Research Pattern](../docs/rfc/2026-07-17-rfc-reference-research-pattern.md) со статусом паттерна `Experimental`. Модуль включает research questions, Conceptual Framing и формальную сигнатуру `S = Decision(KB, Query, Constraints)`, объектную модель, граф зависимостей, 9 точек решений, 20 гипотез с ранжированием; таксономии БЗ/запросов/стратегий, матрицу «БЗ × Запрос → Стратегия», chunking/embeddings/reranking/evaluation, уровни готовности БЗ L0–L5; индустриальные кейсы, тренды 2024–2026, связь с памятью агента и вход для RFC-F. Исходный монолит помечен `superseded` и результатом B-085 больше не является. | Creative |
| **B-086** | Валидация шкалы готовности БЗ L0–L5 на реальных корпусах | **P3** | B-085 | TODO | - (planned) | Исследование B-085, §26.2 (признанная слабость: пороги не измерены) | Проверить шкалу L0–L5 на ≥3 реальных корпусах: воспроизводимы ли шесть признаков без построения индекса, различают ли пороги (95%/80%) уровни на практике, предсказывает ли уровень применимость стратегий. Условие перевода B-085 в `reviewed`. | Structured |
| **B-087** | Исследование самоотравления памяти агента | **P3** | B-085 | TODO | - (planned) | Исследование B-085, §19.2 (открытый вопрос О5) | Когда агент пишет в тот же корпус, из которого читает, возникает класс дефекта, не ловимый ни одной метрикой оценки RAG: faithfulness к самозаписанному контексту высока. Исследовать механизмы разделения пространств «знание человека» / «знание агента» и их различения при извлечении. | Creative |

---

## Спринт 10: Эволюция методологии инженерных исследований

**Story.**
Глубокое ревью исследования Retrieval выявило, что создаваемая структура выходит
за рамки шаблона для AI-доменов. Формируется гипотеза о минимальной архитектуре
инженерного знания, применимой к любым сложным дисциплинам. Чтобы избежать
преждевременной стандартизации, необходимо явно зафиксировать модель зрелости
артефактов, разделить методологию исследования и предметной области, а также
спланировать проверку универсальности паттерна.

**Цель.**
Зафиксировать модель зрелости исследовательских артефактов (Reference Pattern),
внедрить терминологию «Conceptual Framing» и определить дорожную карту валидации
этой методологии за пределами AI.

**Критерий закрытия.**
Модель зрелости задокументирована, разделение методологий явно прописано в
governance-нормах, а план валидации на не-AI доменах добавлен в бэклог как
triggered-задача.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-089** | Зафиксировать модель зрелости Reference Pattern | **P1** | B-085 | DONE | [#437](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/437) / [PR #443](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/443) | Ревью Retrieval и методологическое обсуждение 2026-07-16 | Градация `Discussion Paper → Reference Pattern (Experimental) → Experimental RFC → RFC → Standard` зафиксирована в RFC Reference Research Pattern. Статус паттерна — `Experimental`; критерий продвижения — проверка минимум в трёх независимых доменах. Монолит B-085 реорганизован в модульный retrieval-корпус без потери содержания. | Hybrid |
| **B-090** | Разделить Research Method и Domain Methodology | **P1** | B-089 | DONE | [PR #464](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/464) | Ревью Retrieval и методологическое обсуждение 2026-07-16 | Явно разделить в документации Хаба Research Method — как исследуем (`Theory → Taxonomy → Decision Framework → Practice`) — и Domain Methodology — как устроен объект (`Conceptual Framing → Object Model → Decision Space`). Заменить термин `Mental Model` на `Conceptual Framing`. | Structured |
| **B-092** | Исследование промышленных практик агентного исполнения задач | **P1** | B-089 | review | [#457](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/457) | Issue #457 (постановка фаундера, гипотеза о мандате) | Вторая валидация Reference Research Pattern — на домене agentic task execution. Модуль [`research/ai-education/task-processing/`](../research/ai-education/task-processing/00-introduction.md) из шести файлов: сигнатура `A = Policy(M, S, T, C)`, объектная модель E1–E12, точки решений D1–D10, гипотезы H1–H16; таксономии мандатов M0–M5, подходов к планированию P0–P7 и механизмов контроля G1–G7; матрица «мандат × цена ошибки», правило размещения guardrail по обратимости, шкала автономии A0–A5; индустриальная практика (LangChain, OpenAI Agents SDK, MCP, CrewAI, AutoGen, OTel GenAI, MAST) и описательный разбор прецедентов #454/#456. Без внедрения правил и без RFC — по ограничениям постановки. | Creative |
| **B-098** | Синхронизация методологических определений глоссария | **P1** | B-090, B-103 | DONE | [#517](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/517) | Issue [#517](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/517); корректирующие контракты фаундера в [PR #518](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/518); онтология [ADR-011](../docs/adr/2026-08-adr-011-research-models.md) | [standards/glossary.md](../standards/glossary.md) v2.1 → v2.2 приведён в строгое соответствие с ADR-011: `Analysis` переопределён как отдельный тип артефакта (инвентаризация фактов без новых гипотез) со своим ADR-006, стандартом `analysis-standard.md` и домом `docs/analysis/`, а не как модель research; добавлена связь `Analysis ≠ модель research`. Зонтичный термин `Модель исследования (Research Model)` и `Discussion Paper / Survey` в глоссарий не вводятся до перевода ADR-011 в `accepted` (B-104). Остаются `Research Method`, `Domain Methodology`, `Conceptual Framing`, `Reference Research Pattern (RRP)` с cross-reference на RFC как SSOT. `research-standard.md` не менялся. Тест `tools/test-reference-research-terminology.sh` переведён на проверку разрешённых терминов и запрет запрещённых. | Structured |
| **B-093** | RFC по архитектуре постановки задач для AI-агентов | **P2** | B-092 | review | [PR #470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/470) | Issue #457 (явное вынесение RFC в отдельную задачу) | На фактической базе B-092 подготовлен [RFC об архитектуре постановки задач для AI-агентов](../docs/rfc/2026-08-06-rfc-task-statement-architecture.md). Следствия RFC остаются в статусе `experimental` до проспективного замера эффекта (B-095). | Creative |
| **B-103** | ADR: модели research-артефакта (базовый отчёт, RRP, Discussion Paper / Survey) | **P1** | B-089, B-090 | DONE | [#515](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/515) / [PR #516](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/516) | Issue #515 (пробел маршрутизации: исследования ранней стадии не попадают ни в базовый стандарт, ни в RRP) + корректирующие контракты фаундера в PR #516 | Подготовлен [ADR-011](../docs/adr/2026-08-adr-011-research-models.md) (`proposed`) на базе ADR-003: фиксирует без изменений две существующие модели (базовый датированный отчёт + опц. `exp/`; Reference Research Pattern из шести файлов, SSOT — RFC от 2026-07-17) и предлагает третью — `Discussion Paper / Survey` для ранней стадии, с критериями, выведенными из индустриальных практик (IETF Internet-Draft, W3C Working Draft, ACM Computing Surveys, position paper, публичные обзоры практик построения AI-агентов). Analysis из ряда моделей research исключён как отдельный тип артефакта (ADR-006). `standards/research-standard.md` этим PR не изменяется — правка вынесена в B-104. В [glossary.md](../standards/glossary.md) добавлены `Research Method`, `Domain Methodology`, `Reference Research Pattern (RRP)` с cross-reference на RFC как SSOT структуры RRP. | Creative |
| **B-104** | Внести модели research в `standards/research-standard.md` + статус RRP `Validated` | **P2** | B-103 | DONE | [#523](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/523) / [PR #524](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/524) | ADR-011, решение D5; амендмент D6 по issue #523 | [ADR-011](../docs/adr/2026-08-adr-011-research-models.md) переведён в `accepted` (human decision gate — issue #523) и дополнен амендментом **D6**: статус паттерна RRP повышен `Experimental` → `Validated` по критерию самого RFC (≥ 3 независимых домена), доказательная база — 8 завершённых модулей `research/ai-education/`, выполненных разными исполнителями (3 Codex / 5 Claude по [перекрёстной проверке](../research/hub/2026-08-13-rrp-cross-validation-codex.md)) при 8/8 соблюдении формы по [инвентаризации корпуса](../docs/analysis/2026-08-11-research-methodology-validation.md). В [research-standard.md](../standards/research-standard.md) (v0.2 → v0.3) раздел `Type Model` переведён из `N/A` в модель зрелости M1–M3 и добавлены разделы «Три модели research-артефакта» и «Gate выбора модели исследования» с Decision Tree и правилом: если `research_model` в Контракте дома реализации (или в шаблоне задачи при отсутствии Контракта) не заполнен, исполнитель выбирает модель сам и обосновывает выбор в описании PR. В [glossary.md](../standards/glossary.md) (v2.2 → v2.3) RRP получил статус `Validated` и введён термин `Discussion Paper / Survey`. `Validation status` RFC синхронизирован с D6. Ratchet перенесён в `tools/test-reference-research-terminology.sh` и `tools/validate-repository-structure.sh`. Новых governance-файлов не создано (Anti-Inflation). | Creative |

## Спринт 13: Принудительный онбординг ИИ-агентов — корневой AGENTS.md и уровни постановки

**Story.**
Экосистема располагает каноничными правилами в `ai-rules/` и `standards/`, но ни один
инструментальный агент их не загружает: Codex читает `AGENTS.md`, Claude Code — `CLAUDE.md`,
Copilot — `.github/copilot-instructions.md`, Cursor — `.cursor/rules/`. В результате правила
физически не попадают в контекст, и сбои воспроизводятся системно: Mango создал
[`docs/contracts/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/docs/contracts) вместо
каноничного дома, Aether-Orbis ведёт [issues](https://github.com/G-Ivan-A/aether-orbis/issues) без
шаблона экосистемы (каталога `.github/ISSUE_TEMPLATE` в репозитории нет).

**Цель.**
Ввести корневой `AGENTS.md` как единый диспетчер правил для всех моделей, принудительно
распространить его на спицы, закрыть пробелы, породившие сбои, и подкрепить контекст машинными
гейтами, потому что инструкционный файл доставляет контекст, но не принуждает к исполнению.

**Критерий закрытия.**
`AGENTS.md` легализован и лежит в корне Хаба и каждой спицы; структура Mango и Aether-Orbis
приведена к геному; уровни постановки задачи зафиксированы стандартом; запрет на `docs/contracts/`
и проверка уровней issue выполняются CI, а не доверием к агенту.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-110** | Легализация `AGENTS.md` как обязательного артефакта бутстрапа | **P1** | — | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | [Анализ коренных причин](../docs/analysis/2026-09-03-ai-rules-compliance-failure-root-cause.md); [исследование практик](../research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md); [RFC корневого контракта AGENTS.md](../docs/rfc/2026-09-03-rfc-agents-md-root-contract.md) (issue #551) | Узаконить корневой `AGENTS.md`: обновить [ADR-007 о корневой структуре Хаба](../docs/adr/2026-07-adr-007-hub-root-structure.md) или принять стандарт бутстрапа, включить `AGENTS.md` в обязательные корневые файлы, добавить его в allowlist и `required_files` [`tools/validate-repository-structure.sh`](../tools/validate-repository-structure.sh), разместить в корне содержимое черновика [`templates/agents-md-root-draft.md`](../templates/agents-md-root-draft.md), завести тонкие указатели `CLAUDE.md` (импорт `@AGENTS.md`), `.github/copilot-instructions.md` и `.cursor/rules/` без дублирования правил. Допускается ускоренная легализация через стандарт без предварительного RFC: единый корневой инструкционный файл — наблюдаемая индустриальная практика, а не новация экосистемы. Дублирование правил в модель-специфичные файлы запрещено. | Structured |
| **B-111** | Скрипт `tools/inject-agents-md.sh` для принудительной инъекции в спицы | **P1** | B-110 | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | Вывод В6 [исследования практик](../research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md): Copilot и Cursor читают только файлы внутри самого репозитория | Реализовать идемпотентный скрипт, который раскладывает канонический `AGENTS.md` Хаба и тонкие указатели во все спицы экосистемы (`mango_ba_prompts`, `aether-orbis` и последующие), помечая файл как сгенерированный из Хаба и запрещая ручное расхождение. Требования: dry-run по умолчанию, отчёт о дельте, отказ при локальных правках без флага, вызов из CI/по расписанию, запись в `CHANGELOG` спицы. Обязателен парный check-режим, падающий, если в спице `AGENTS.md` отсутствует или расходится с эталоном. | Structured |
| **B-112** | Mango: устранить `docs/contracts/` и задать канонический дом контрактных документов | **P1** | B-110 | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | Находка F2 [анализа](../docs/analysis/2026-09-03-ai-rules-compliance-failure-root-cause.md): [`docs/contracts/kb-citations.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/contracts/kb-citations.md) | Двухчастная задача. В Хабе: дополнить [`standards/contract-documentation-standard.md`](../standards/contract-documentation-standard.md) и [`pr-ops/repo-model.md`](repo-model.md) явным домом для документов класса «контракт» — текущий стандарт описывает форму, но не отвечает на вопрос «где он живёт», что и породило сбой. В Mango: перенести содержимое `docs/contracts/` в каноничный дом (`ai-rules/`), удалить каталог, убрать запрещённое поле `ai-generated` из frontmatter, обновить ссылки. Задача не считается закрытой, пока запрет на `docs/contracts/` не проверяется машинно (см. B-116). **Уточнение по находке F7:** путь `docs/contracts/kb-citations.md` был предписан дословно в разделе «Готово, когда» задачи [mango#353](https://github.com/G-Ivan-A/mango_ba_prompts/issues/353), а не выбран агентом, — поэтому одного запрета недостаточно: при переносе обязательно закрыть и канал постановки (B-116, пункт 2), иначе исполнитель получит конфликт «правило против DoD». | Structured |
| **B-113** | Aether-Orbis: приведение репозитория в соответствие с геномом | **P1** | B-110, B-111 | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | Находка F3 [анализа](../docs/analysis/2026-09-03-ai-rules-compliance-failure-root-cause.md): в репозитории отсутствует `.github/ISSUE_TEMPLATE` | Разложить в [aether-orbis](https://github.com/G-Ivan-A/aether-orbis) базовый геном: `.github/ISSUE_TEMPLATE/task.md` и `task.yml` из Хаба, `AGENTS.md`, `CONTRIBUTING.md`, минимальный набор валидаторов из [`templates/spoke/`](../templates/spoke/README.md). Провести ревизию существующих issues и зафиксировать, какие из них требуют переоформления по пяти уровням постановки, а какие закрываются как есть. Требование соблюдать шаблон вступает в силу только после его фактической доставки в репозиторий. **Дополнительно (находка F8, ревью PR [#548](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/548)): провести аудит корневых файлов `aether-orbis`. Выявить и устранить дубликаты или запрещённые файлы (например, [`PRODUCT_VISION.md`](https://github.com/G-Ivan-A/aether-orbis/blob/main/PRODUCT_VISION.md), [`GOVERNANCE.md`](https://github.com/G-Ivan-A/aether-orbis/blob/main/GOVERNANCE.md)). Перенести их содержимое в каноничные дома (`docs/vision.md`, `ai-governance/`) и удалить из корня. Обновить все абсолютные ссылки.** Дублирование SSOT подтверждено фактически: [`docs/vision.md`](https://github.com/G-Ivan-A/aether-orbis/blob/main/docs/vision.md) уже существует одновременно с корневым `PRODUCT_VISION.md`. Перенос выполнять с журналированием каждого перемещения (`path_migrations` в `.hub-profile.json`) и с явным указателем на старом месте там, где на файл есть внешние ссылки, — по образцу Mango (F7.5); молчаливое удаление запрещено. | Structured |
| **B-114** | Стандарт правил формирования Story / ФТ / НФТ | **P2** | — | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | Находка F4 [анализа](../docs/analysis/2026-09-03-ai-rules-compliance-failure-root-cause.md); IEEE 29148, BABOK/CBAP | Инициировать стандарт, фиксирующий правила формулирования пяти уровней постановки: субъект ФТ и НФТ — система, субъект задачи исполнителю — исполнитель; критерии проверяемости и измеримости НФТ; типовые антипаттерны смешения уровней. Перед созданием нового документа проверить принцип Anti-Inflation: если правил хватает на раздел внутри [`standards/issue-workflow.md`](../standards/issue-workflow.md), отдельный стандарт не заводится. Задача является легитимизацией правил, применённых в шаблонах в рамках PR по issue #547. | Creative |
| **B-115** | Легитимизация исправленных шаблонов задач Хаба | **P2** | B-114 | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | PR по [issue #547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547): шаблоны переведены на пять уровней постановки | Шаблоны [`task.md`](../.github/ISSUE_TEMPLATE/task.md) и [`task.yml`](../.github/ISSUE_TEMPLATE/task.yml) исправлены в рамках issue #547 (v3.0), раздел «Пять уровней постановки задачи» добавлен в [`standards/issue-workflow.md`](../standards/issue-workflow.md) v1.4. Задача закрывает остаточный контур: синхронизировать [`docs/rfc/2026-08-06-rfc-task-statement-architecture.md`](../docs/rfc/2026-08-06-rfc-task-statement-architecture.md) как источник шаблона, обновить шаблон-донор [`templates/htom/.github/ISSUE_TEMPLATE/task.md`](../templates/htom/.github/ISSUE_TEMPLATE/task.md) и распространить изменение на спицы через B-111. | Structured |
| **B-116** | Машинные гейты соблюдения правил: явные запреты и валидация уровней постановки | **P1** | B-110 | todo | [#547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547) | Находка F6 [анализа](../docs/analysis/2026-09-03-ai-rules-compliance-failure-root-cause.md); вывод В5 [исследования практик](../research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md) | Обязательное дополнение техдолга: инструкционный файл доставляет контекст, но не принуждает к исполнению — индустрия закрывает это hooks и CI. Расширить [`tools/validate-repository-structure.sh`](../tools/validate-repository-structure.sh) явными запретами (`docs/contracts/`, модель-специфичные файлы правил, `ai-generated` во frontmatter), добавить валидацию структуры issue по пяти уровням и pre-commit/CI-гейт в Хабе и спицах. Без этой задачи `AGENTS.md` остаётся рекомендацией, и сбои воспроизводятся. **Расширение по находке F7 (ретроспективный аудит постановок):** (1) снять ограничение `find . -maxdepth 1` в валидаторе структуры — правило «недекларированный каталог = FAIL» из RFC [#532](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/538) нормирует только корень, из-за чего `docs/contracts/` прошёл 42 зелёных валидатора в [mango PR #354](https://github.com/G-Ivan-A/mango_ba_prompts/pull/354); (2) добавить гейт уровня постановки — проверку путей, названных в разделах «Готово, когда» и «Задача исполнителю», против каноничных домов **до** передачи задачи агенту. Без пункта (2) запреты остаются односторонними: постановка задачи является привилегированным каналом записи в структуру репозитория и обходит любой запрет, адресованный исполнителю. | Structured |
| **B-117** | Стандарт бутстрапа: ось «Среда» и контракт классов `ai-rules/` | **P1** | — | todo | [#553](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/553) | [RFC оси «Среда» и рефакторинга базовых структур](../docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md) (issue #553) | Создать `standards/bootstrap-environment-standard.md` по разделам `P.1`–`P.5` RFC: словарь сред (`local`, `gigacode`, `serverless`), формула композиции `ядро ⊕ Δархетип ⊕ Δсреда ⊕ Δпродукт`, правила `R1`–`R7` (аддитивность, разделение предметов, приоритет при конфликте, адаптер вместо второго SSOT, одна первичная среда, дефолт `local`, закрытый словарь), поля `archetype`/`environment`/`secondary_environments` в `.hub-profile.json`, контракт трёх классов `ai-rules/` (правило — плоско, команда — `commands/<slug>.md`, навык — `skills/<slug>/SKILL.md`) с различающим тестом «кто инициирует применение». Подкаталоги `commands/`/`skills/` объявляются разрешёнными, но физически в Хабе не создаются до появления не менее двух артефактов класса. Требует предварительного решения фаундера по `Q-1`, `Q-2`, `Q-3` RFC. Синхронизировать решения новыми ADR к ADR-001 и ADR-007 (шаг `M2` плана миграции), не переписывая принятые ADR. | Structured |
| **B-118** | Исключение path-миграции в гейте исторической иммутабельности | **P1** | B-117 | todo | [#553](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/553) | [RFC оси «Среда» и рефакторинга базовых структур](../docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md) (issue #553), раздел `P.6`, Условие 1 | Расширить [`tools/validate-historical-immutable.sh`](../tools/validate-historical-immutable.sh) третьим исключением: изменение файла в `docs/rfc/`/`docs/adr/` допускается, если дифф сводится к объявленной path-миграции — обратная подстановка к HEAD-версии обязана дать побайтовое совпадение с base-версией. Список подстановок читается из журнала `path_migrations` в `.hub-profile.json` (тот же механизм, что предписан B-113). Добавить парные сценарии в [`tools/test-historical-immutable.sh`](../tools/test-historical-immutable.sh), включая негативный: смысловая правка под видом миграции обязана падать. **Блокирует B-119:** без этой задачи переименование `pr-ops/` не имеет корректного исполнения — измерено 247 вхождений `pr-ops` в 35 иммутабельных документах, из них 74 markdown-ссылки. | Structured |
| **B-119** | Переименование `pr-ops/` → `ops/` одним PR | **P2** | B-118 | todo | [#553](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/553) | [RFC оси «Среда» и рефакторинга базовых структур](../docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md) (issue #553), раздел `P.6` | Единый reviewable PR (дробление гарантирует промежуточное красное состояние): перенос файлов, переписывание ссылок в 140 markdown-файлах, 224 строки [`tools/validate-repository-structure.sh`](../tools/validate-repository-structure.sh) вместе с `require_text`-проверками и version-pin, `templates/htom/`, `templates/spoke/`, `templates/manifest.json`, регенерация манифеста, запись в журнал `path_migrations`. Оставить `pr-ops/README.md` как заглушку `status: deprecated` со ссылкой на `ops/README.md` на один цикл синхронизации — это единственное покрытие внешних входящих ссылок; любой другой файл в `pr-ops/` запрещается валидатором. `CHANGELOG.md` (158 вхождений) намеренно не переписывается: append-only летопись верна для своей даты. Внешние permalink-ссылки на `blob/main/pr-ops/` ломаются при любом сценарии — принятая неустранимая цена. Требует решения фаундера по `Q-4` RFC. | Structured |
| **B-120** | Валидаторы и `AGENTS.md`, чувствительные к объявленной среде | **P1** | B-117 | todo | [#553](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/553) | [RFC оси «Среда» и рефакторинга базовых структур](../docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md) (issue #553), разделы `P.7`, `M5`, `M6` | Двухчастная задача. Валидаторы: [`tools/validate-repository-structure.sh`](../tools/validate-repository-structure.sh) и геном [`templates/htom/tools/validate-repository-structure.sh`](../templates/htom/tools/validate-repository-structure.sh) читают `environment` из `.hub-profile.json` **до** проверки требуемого набора; каталог, канонический для объявленной среды, проходит без записи в `project_specific_directories`; значение вне словаря и вычитающая дельта дают `FAIL`; [`tools/sync-from-hub.sh`](../tools/sync-from-hub.sh) учитывает среду при раскладке, а ручная правка сгенерированного адаптера падает в check-режиме. `AGENTS.md`: правки `A-1`–`A-5` в [RFC корневого контракта](../docs/rfc/2026-09-03-rfc-agents-md-root-contract.md) и в [`templates/agents-md-root-draft.md`](../templates/agents-md-root-draft.md). **Приоритет P1 из-за `A-1`:** действующая формулировка `<forbidden>` «модель-специфичные файлы правил запрещены» буквально запрещает нативную поверхность среды GigaCode и тем самым блокирует Трек А; запрет должен быть сужен до копии правил с разрешением сгенерированного указателя. B-111 дополняется требованием чувствительности скрипта инъекции к среде. | Structured |

## Отложенные задачи с триггером

Задачи этого блока не запускаются по факту регистрации. Они переходят в работу
только после появления указанной операционной боли, чтобы соблюдать принцип
Anti-Inflation.

| ID | Название | Приоритет | Зависимости | Статус | Issue | Источник | Краткое содержание | Режим запуска |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **B-088** | Зафиксировать многоуровневую иерархию SSOT (ADR vs Стандарт) | **P3** | - | deferred (triggered) | - (tech debt) | Обсуждение 2026-07-16; B-050 v0.2 §2; [issue #427](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/427) | Текущая формулировка «ADR имеет приоритет» слишком общая. Необходимо чётко разграничить компетенции: ADR = SSOT для решений, Стандарт = SSOT для исполнения. Задача стартует **только** при появлении боли: повторяющиеся конфликты между свежим ADR и устоявшейся практикой в стандарте. | Creative |
| **B-091** | Проверить Reference Pattern на не-AI доменах | **P2** | B-089, B-090 | deferred (triggered) | - (deferred) | Ревью Retrieval и методологическое обсуждение 2026-07-16 | Проверить гипотезу Reference Pattern за пределами AI на Business Analysis, Requirements Engineering и Prompt Engineering. Запускать только после успешной валидации на Memory и Agents. | Creative |
| **B-094** | Knowledge Integrity Auditor — агент периодического аудита целостности знаний | **P2** | - | deferred (regular) | [#475](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/475) | Согласование ОПС с фаундером (RFC [#470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/470)) | Регулярная задача вне спринтов: автономный агент по расписанию сканирует исторические документы (RFC, ADR) на упоминания дефектов и проверяет, устранены ли они в замерженных PR; добавляет блок `Status Update` со ссылкой на закрывающий PR. Триггер автоматизации — явная боль от ручного аудита; до неё задача не автоматизируется. | Structured |
| **B-095** | Проспективный замер эффекта RFC #470 | **P2** | B-093 | deferred (regular) | [#475](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/475) | RFC [#470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/470); [валидация стратегии постановки задач](../research/hub/2026-07-31-ops-task-strategy-validation.md); PR [#462](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/462) | Регулярная задача вне спринтов, запуск через 3 месяца после внедрения RFC #470: повторный прогон скриптов из `research/hub/exp/ops-task-strategy-461/` для измерения доли непродуктивных PR, `contract_score` и доли PR-с-вопросами. Основание для перевода следствий RFC в canonical или их корректировки. | Structured |
| **B-096** | Создание инструкции по меткам GitHub | **P3** | - | deferred (triggered) | [#475](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/475) | Согласование ОПС с фаундером; PR [#467](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/467) | Документировать допустимые метки (`no-diff-expected`, `needs-human-decision`, `incomplete-dod` и другие) как часть общей инструкции по Хабу, чтобы пользователи не забывали, какие метки можно использовать. Триггер — повторяющиеся ошибки в разметке issues/PR. | Structured |
| **B-097** | Автоматизация переноса неактивных PR-с-вопросами в `pr-ops/backlog.md` | **P3** | B-096 | deferred (triggered) | [#475](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/475) | Согласование ОПС с фаундером; RFC [#470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/470) | Скрипт, который по расписанию или триггеру находит PR с меткой `needs-human-decision` старше N дней, переносит описание вопроса в `backlog.md` и закрывает PR с комментарием. Запуск по запросу; не автоматизировать до явной боли от ручного разбора зависших PR. | Structured |


---

## Источники активного порядка

| Источник | Что даёт бэклогу |
| --- | --- |
| [backlog-instruction.md](backlog-instruction.md) | Правила ведения, статусы, sprint format, archiving policy and `null` rule. |
| [docs/analysis/2026-06-30-backlog-and-artifact-change-policy-analysis.md](../docs/analysis/2026-06-30-backlog-and-artifact-change-policy-analysis.md) | Источник проблем перегрузки бэклога and amendment policy B-036. |
| [docs/analysis/2026-07-04-kb-runs-hub-applicability-analysis.md](../docs/analysis/2026-07-04-kb-runs-hub-applicability-analysis.md) | Trigger-based decision source for not adding root `kb/` and `runs/` to the Hub now. |
| [docs/adr/2026-07-adr-007-hub-root-structure.md](../docs/adr/2026-07-adr-007-hub-root-structure.md) | Decision source for post-migration root boundaries and B-056..B-063. |
| [docs/audit/2026-07-04-cross-standard-stress-tests.md](../docs/audit/2026-07-04-cross-standard-stress-tests.md) | Source findings for the standard-structure repair chain B-049..B-054 after B-049 routing to Audit. |
| [research/hub/2026-07-04-hub-as-agent-system-global-analysis.md](../research/hub/2026-07-04-hub-as-agent-system-global-analysis.md) | Global analysis v0.4 (issues #394/#398/#400): §8 рекомендации, §11 реестр пробелов, §15.8 входы RFC/ADR — источник задач B-064..B-078 (Спринты 5–7). |
| Issue [#411](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/411) / [#413](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/413) (обсуждение 2026-07-10, решение фаундера) | Источник задач B-079..B-084 (Спринт 8): разделение Mango на публичный `ai-ba-playbooks` и приватный `mango_ba_prompts` (существующий репозиторий переводится в режим Private по уточнению issue [#511](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/511)). |
| Issue [#418](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/418) (постановка фаундера) | Источник задач B-085..B-087 (Спринт 9): научно-теоретическое исследование retrieval-стратегий как вход для RFC-F и теоретическая основа образовательного модуля. |
| Issue [#427](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/427) (обсуждение 2026-07-16; B-050 v0.2 §2) | Источник triggered-задачи B-088: разграничение ADR как SSOT для решений и Стандарта как SSOT для исполнения только после появления повторяющейся операционной боли. |
| Issue [#437](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/437) и методологическое обсуждение 2026-07-16 | Источник задач B-089..B-091 (Спринт 10): модель зрелости Reference Pattern, разделение Research Method и Domain Methodology, валидация на не-AI доменах. |
| Issue [#457](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/457) (постановка фаундера) | Источник задач B-092..B-093: исследование промышленных практик агентного исполнения задач как вторая валидация Reference Research Pattern и фактическая база для будущего RFC по архитектуре постановки задач. |
| [docs/rfc/2026-08-06-rfc-task-statement-architecture.md](../docs/rfc/2026-08-06-rfc-task-statement-architecture.md) (RFC [#470](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/470)) | Источник задач ОПС B-094..B-097 и статуса B-093: архитектура постановки задач для AI-агентов, следствия которой требуют проспективного замера эффекта. |
| Issue [#466](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/466) и PR [#467](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/467) | Источник обновления правил работы агентов (`ai-rules/`) и практики разметки артефактов ОПС: вход для B-096 (инструкция по меткам GitHub). |
| GitHub Issues/PR | История выполненных задач, review discussion and implementation evidence. |
