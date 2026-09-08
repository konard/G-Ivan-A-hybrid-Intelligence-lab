---
status: draft
version: 0.3
updated: 2026-09-07
temperature: 0.1
---

# BA Requirements — конвейер артефактов бизнес-анализа

Направление исследует **полный конвейер** артефактов бизнес-анализа: как
обращение произвольного качества превращается в проверяемое требование (`M0`),
как требования собираются в согласованное ядро (`M1`), как ядро разворачивается
в целевые документы без потери смысла (`M2`), как результат замыкается обратной
связью (`M3`) и как всё это маршрутизируется между людьми и агентами (`M4`).
Декомпозиция задана
[RFC дорожной карты](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md).

Направление намеренно отделено от [`research/mango/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/mango):
там лежат датированные отчёты по конкретным задачам спицы MANGO OFFICE, здесь —
переносимая рамка, у которой Mango является одним (первым) применением.

## Модули

- [`normalization/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/normalization/00-introduction.md)
  — таксономия нормализации требований: терминология входного артефакта,
  универсальная и Mango-специализированная таксономии, матрица корреляции,
  рамка принятия решений, три гипотезы реализации, граничные кейсы.
  Оформлен по [Reference Research Pattern](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-07-17-rfc-reference-research-pattern.md)
  (`00…50`).
- [`solution-modeling/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/00-introduction.md)
  — модуль `M1`: ядро требований. Инварианты `INV-1`…`INV-9`, классы моделей
  `MO-1`…`MO-12`, типы элементов `EL-1`…`EL-8`, контракт `C-CORE` и гейты
  `HG-3`/`HG-4`.
- [`artifact-rendering/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-rendering/00-introduction.md)
  — модуль `M2`: рендер ядра в целевые документы. Инварианты рендера
  `RN-1`…`RN-5`, классы документов `DC-1`…`DC-9`, процедура контроля недрейфа
  `ND`, контракт `C-OUT` и гейты `HG-5`/`HG-5.1`.
- [`feedback-and-evolution/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/feedback-and-evolution/00-introduction.md)
  — модуль `M3`: обратная связь, статистика решений и эволюция требований.
  Инварианты замыкания `CL-1`…`CL-6`, словарь метрик `MK-*`, контракт `C-CL`
  и гейты `HG-6`/`HG-7`.
- [`orchestration/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/orchestration/00-introduction.md)
  — сквозной модуль `M4`: маршрутизация, роли, прерывания и человеческие гейты.
  Инварианты маршрута `RT-1`…`RT-7`, типовые маршруты `RT-A`…`RT-F`, контракт
  `C-RK`, гейты `HG-0` и `HG-8`, сводный build-vs-buy по всему конвейеру.
- [`methodology-unification/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/00-introduction.md)
  — предметная ось методологии БА: двухуровневая рамка «управление ↔ исполнение».
  Управляющий уровень — наследование `L0` (индустрия) → `L1` (ИТ-телеком) →
  `L2` (Манго) с правилами дельты `D1`–`D5`; исполнительный — разрешённый
  навык `SKILL.md` с инвариантами `I-1`…`I-7`, жизненный цикл `S0`–`S7`,
  типология гейтов `G-self`/`G-mach`/`G-human`, реестр разрывов `G-01`…`G-15`
  и роадмап каскада `B-121`…`B-135` (issue
  [#557](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557)).
  Ось ортогональна конвейеру `M0`–`M4`: те модули отвечают на вопрос «как
  устроен артефакт», этот — «откуда берётся норма».

- [`artifact-micro-structure/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/00-introduction.md)
  — микро-уровень той же оси: как индустриальный базис и продуктовые дельты
  сводятся к **одной** структуре результирующего документа. Словарь слотов
  `S-*` с ровно одной канонической подписью, классы формата `F-*`, проекции
  `V-BIZ`/`V-APPROVE`/`V-DEV` одного размеченного ядра, профили продукта
  `P-SETTINGS`/`P-NO-SETTINGS`/`P-DEVICE`/`P-API`, правила сведения `R-1`…`R-6`,
  разделение операции и навыка (`OP-1`, `OP-2`), контракт скомпилированного
  артефакта `CA-1`…`CA-6`, Golden Set как обязательный элемент гейта `G-mach`
  (`GS-1`…`GS-5`), 12 граничных кейсов `E-1`…`E-12` и задачи `B-136`…`B-143`
  (issue [#561](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/561)).
  Модуль `methodology-unification/` намеренно **не переписывается**: поправки
  к нему оформлены как `П-1`…`П-5` и заведены задачей `B-141`.

- [`ba-meta-model/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/ba-meta-model/00-introduction.md)
  — синтез накопленной базы в каноническую мета-модель БА (issue
  [#563](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/563)):
  девять канонических сущностей и закон производства `MM-1`…`MM-4`, четыре
  канонические таксономии (артефакты `A-*`, операции, процессы, продуктовые
  классы) плюс служебная таксономия гейтов и контрактов, депрекация режимов
  запуска `stepwise`/`oneshot`/`legacy` (`DP-1`…`DP-4`, ADR-013), контракт
  скомпилированного `SKILL.md` (`SK-1`…`SK-6`), маршрутный лист (`EP-R1`…`EP-R4`),
  Golden Set (`EP-G1`…`EP-G5`), Mermaid-модель производства BCREQ и план
  вертикального MVP-среза с метриками `M-1`…`M-5`. Модули `M0`–`M4` и осевые
  модули **не переписываются**: расхождения сведены отображениями.

## Датированные снимки

- [`2026-08-26-rrp-full-cycle-corpus-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md)
  — общая доказательная база модулей `M1`–`M4`: замер корпуса `runs/` на
  коммите `ef88a9a` (57 прогонов). Все четыре модуля ссылаются на один замер,
  а не выдвигают независимые утверждения о практике.
- [`2026-08-25-mango-runs-empirical-snapshot.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-25-mango-runs-empirical-snapshot.md)
  — снимок корпуса `runs/` репозитория `mango_ba_prompts` на 2026-08-25.
  Модуль ссылается на снимок, а не наоборот: у модуля нет единой даты, у
  измерения она есть.
- [`2026-09-07-ecosystem-knowledge-inventory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md)
  — инвентаризация и топологическая карта знаний трёх репозиториев экосистемы
  (368 артефактов, коммиты `c259d61` / `8cbf82a` / `96c288f`): реестр по
  классам и статусам, граф связей, перевёрнутое наследование Манго → Хаб и
  отсутствующий канал наследования у `clarify-engine-ai` — при этом §5.3
  содержит сплошную экспертную разметку всех 53 его артефактов, показывающую 8
  механизмов, переносимых в методологию. Доказательная база модуля
  `methodology-unification/`.

- [`2026-09-08-artifact-structure-variance-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-08-artifact-structure-variance-facts.md)
  — замер структуры результирующих артефактов корпуса `runs/` на коммите
  `8cbf82a`: 67 прогонов, 17 результирующих документов и **17 различных
  скелетов** — ни одного совпадения, в том числе внутри одной задачи. Слот
  «сценарии» встретился 14 раз под 14 подписями, «UI-логика» и «критерии
  приёмки» — по одному разу на 17 документов. Доказательная база модуля
  `artifact-micro-structure/` и основание обязательного синтеза Golden Set.

- [`2026-09-08-meta-model-inputs-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-08-meta-model-inputs-facts.md)
  — замер входных данных мета-модели на коммите `8cbf82a`: режим запуска входит
  в идентичность 24 промптов (13 способностей, дублирование 1.85), но варианты
  одного и того же не разделяют скелет (13 пар, средний Жаккар **0.077**, ни
  одной идентичной пары), а маршрутизации по режиму в метаданных прогонов не
  наблюдается (50 из 67 прогонов без ссылки на промпт). Покрыто 6 операций из
  13, из девяти процессов наблюдается один. Доказательная база модуля
  `ba-meta-model/` и решения ADR-013.

## Эксперименты

- [`exp/ba-requirements-normalization-539/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-requirements-normalization-539)
  — воспроизводимый агрегатор корпуса `runs/` (issue
  [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539)).
- [`exp/ba-rrp-full-cycle-545/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-rrp-full-cycle-545)
  — воспроизводимый замер корпуса для модулей `M1`–`M4` (issue
  [#545](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545)).
- [`exp/ba-methodology-unification-557/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-methodology-unification-557)
  — воспроизводимый сканер трёх репозиториев: реестр артефактов, классы,
  статусы и граф ссылок (issue
  [#557](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557)).

- [`exp/ba-micro-structure-561/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-micro-structure-561)
  — воспроизводимый замер структуры результирующих документов и два
  синтетических эталона Golden Set для классов `contact-center` и
  `self-service-lk` (issue
  [#561](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/561)).

- [`exp/ba-meta-model-563/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-meta-model-563)
  — воспроизводимый замер входных данных мета-модели: идентичность промптов,
  расхождение скелетов вариантов режима, наблюдаемость маршрутизации, покрытие
  операций и процессов, продуктовая разметка (issue
  [#563](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/563)).

## Политика ссылок

Все ссылки в направлении — **абсолютные** (полные URL). Требование зафиксировано
в issue [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539).
Единственное исключение — обязательные внутримодульные относительные ссылки в
`40-practice-and-cases.md`, которых требует машинная проверка правила P2
([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh));
исключение объявлено в самом файле.
