---
status: draft
version: 0.1
updated: 2026-09-07
temperature: 0.2
type: research
context: [ba, methodology, inventory, knowledge-map, taxonomy, governance-layers, issue-557]
method: corpus-measurement + artifact-classification + prior-art-evaluation
scope: ecosystem
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557"
based_on:
  - research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md
related_artifacts:
  - "research/ba-requirements/methodology-unification/10-theory.md"
  - "docs/ecosystem-map.md"
  - "docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557"
---

# Таксономии: реестр знаний, карта и слои методологии

> Файл отвечает на ФТ-1 issue #557: инвентаризация, топологическая Карта знаний
> и явная оценка уже существующих артефактов «типа Роадмап». Числовая
> доказательная база вынесена в датированный замер
> [`2026-09-07-ecosystem-knowledge-inventory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md);
> здесь — классификация и интерпретация. Все ссылки абсолютные (НФТ-2).

## 1. Оценка существующих артефактов «типа Роадмап»

Постановка требует: если такой артефакт уже есть, оценить, решает ли он задачу
картографии текущего состояния. Кандидатов в корпусе три.

| Кандидат | Что содержит | Решает ли картографию текущего состояния | Вердикт |
| --- | --- | --- | --- |
| [`docs/ecosystem-map.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/ecosystem-map.md) (`draft` v0.4, 2026-06-12) | Матрица из 5 проектов, граф связей репозиториев, Roadmap экосистемы из трёх этапов | **Нет.** Единица карты — репозиторий, а не знание. Карта отвечает «какие проекты есть и как они подключены», но не «какое знание существует, на что опирается и где разрывы». Roadmap внутри неё — инфраструктурный (Need-to-Know, Smart Sync), а не методологический. Актуальность: карта не обновлялась 3 месяца, `clarify-engine-ai` указан без ссылки на репозиторий. | Не заменяет; **дополняется** настоящим замером на уровень ниже |
| [`docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md) | Целевой конвейер БА `M0`–`M4`, контракты `C-IA`/`C-RK`/`C-CORE`/`C-OUT`/`C-CL`, гейты `HG-0`…`HG-8`, маршрутный лист | **Нет — и не должен.** Это описание **целевого состояния** и плана исследования конвейера. Вопрос «где мы сейчас и что уже написано» в нём не ставится; слово «roadmap» относится к плану модулей исследования, а не к состоянию знаний. | Не заменяет; является **входом** настоящего модуля и остаётся принятой рамкой конвейера |
| [`pr-ops/artifact-map.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/artifact-map.md) (`canonical` v2.9) | Полный навигационный реестр артефактов **Хаба** с типом и назначением | **Частично.** Это лучший существующий реестр, но его периметр — один репозиторий, единица — файл, а связи между артефактами не выражены как граф. Межрепозиторной топологии и оценки зрелости в нём нет по назначению. | Не заменяет; настоящий замер **расширяет** его на три репозитория и добавляет измерение связности |

**Вывод.** Артефакта, отвечающего на вопрос «какое знание по БА существует в
трёх репозиториях, на что оно опирается и где разрывы», в экосистеме нет.
Создание нового артефакта обосновано по принципу Anti-Inflation: ни один из трёх
кандидатов не покрывает предмет, и ни один не расширяется до него без смены
единицы описания.

## 2. Классификация корпуса

Единица реестра — **артефакт знания**: markdown-документ, претендующий на
переносимость (исследование, стандарт, решение, анализ, аудит, отчёт, бэклог).
Операционный контур (`runs/`, `prompts/`, `patterns/`, `kb/`) в реестр не входит:
это исполнение, а не знание, и он замерен отдельно.

Восемь классов и их роль в методологии:

| Класс | Роль | Всего | Свойство корпуса |
| --- | --- | --- | --- |
| Research | Производит переносимое знание | 173 | 94 % в Хабе; спицы знание почти не производят |
| Standard | Нормирует исполнение | 53 | Рассредоточен по трём репозиториям без отношения наследования |
| RFC | Предлагает решение | 39 | 28 в Хабе; поток предложений опережает поток норм |
| ADR | Фиксирует решение | 37 | В спицах ADR больше, чем анализов |
| Analysis | Разбирает конкретный случай | 31 | — |
| Audit | Проверяет соответствие | 21 | — |
| Backlog | Планирует | 7 | Все 7 в Clarify: у него бэклог — класс знания, а не операционный файл |
| Report | Фиксирует результат проверки | 7 | — |

**Три системных наблюдения.**

`O-1. Нормирована форма, а не содержание.` Из 15 центров притяжения графа 13
нормируют оформление знания. BA-релевантен **1 стандарт Хаба из 26**. Экосистема
умеет требовать, чтобы документ был правильно оформлен, и не умеет требовать,
чтобы требование было правильно сформулировано.

`O-2. Предметное ядро БА лежит в спице и не имеет статуса.` Единственный
предметный BA-артефакт среди центров притяжения —
[`standards/ba-ontology.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/ba-ontology.md)
Mango (16 входящих, статус `draft`). Вместе с
[`docs/taxonomy.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/taxonomy.md)
(13 операций, 9 процессов) и
[`standards/bcreq-process-standard.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/bcreq-process-standard.md)
(6 подпроцессов, 3 человеческих гейта) они образуют де-факто методологию БА
экосистемы — с формальным статусом черновика одной команды.

`O-3. Наследование инвертировано.` `mango → hub` 81 ребро, `hub → mango` 31.
Спица наследует от Хаба форму и возвращает ссылки, но норму производит сама.
В терминах [`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/10-theory.md)
это означает: слой `L2` существует, слой `L1` не существует, слой `L0`
присутствует только как реестр ссылок.

## 3. Отнесение существующих артефактов к слоям

Таблица — операционный результат ФТ-2: где сегодня физически лежит каждый слой
и что в нём отсутствует.

| Слой | Что уже есть | Где лежит | Чего нет |
| --- | --- | --- | --- |
| `L0` индустриальная база | Сверенный реестр внешних источников (29148, 25010, ГОСТ 34.602-2020, BABOK, ODA, ISO/IEC Directives) с правилами `И1`–`И6`; маппинг 13 операций на 6 областей знаний BABOK | [`standards/industry-standards-standard.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/industry-standards-standard.md), [`docs/taxonomy.md §4.1`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/taxonomy.md) — **оба в спице** | Слой существует как **список ссылок**, а не как изложенная база: нет ответа «что именно из 29148 мы применяем и в какой редакции». Реестр находится в спице, хотя нужен всей экосистеме |
| `L1` дельта ИТ-Телеком | [TM Forum ODA](https://www.tmforum.org/oda/) присутствует в реестре как «de facto, информативный» источник | — | **Слоя нет.** Ни одного артефакта, излагающего отраслевую дельту: eTOM-декомпозиция, понятия услуги/продуктового предложения/канала, регуляторика связи нигде не нормированы. Это крупнейший структурный разрыв |
| `L2` дельта КК Манго | Онтология БА, таксономия 13 операций / 9 процессов, процесс BCREQ `П1`–`П6` с гейтами `G1`–`G3`, стандарты промпта, прогонов, KB, именования | [`standards/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/standards) и [`docs/adr/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/docs/adr) Mango | Слой богат, но: (а) статус `draft`, (б) якорей `D2` к `L0` почти нет — норма и заимствование не различимы, (в) невозможно отличить, что здесь отраслевое (должно быть в `L1`), а что командное |
| Execution | Класс навыка определён: `ai-rules/skills/<slug>/SKILL.md`, различающий тест «кто инициирует применение» | `P.5` [RFC оси «Среда»](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md) | **Ни одного носителя.** Каталог не создан, навыков нет; ближайший функциональный аналог — промпты Mango, которые не самодостаточны и не объявляют гейт |

## 4. Таксономия объектов методологии

Для сборки навыков нужен общий словарь объектов. Экосистема располагает двумя
частично пересекающимися словарями; они сводятся так.

| Объект | Определение | Носитель сегодня | Соответствие `L0` |
| --- | --- | --- | --- |
| **Процесс БА** | Повторяемый рабочий сценарий (9 штук: формирование ФТ/ТЗ, валидация, тендеры, UC/US, UML/BPMN, помощь ПО/ПМ, статистика, Impact, Risk) | [`docs/taxonomy.md §2`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/taxonomy.md) | Области знаний BABOK (BAPM, EC, RLCM, SA, RADD, SE) |
| **Операция** | Атомарный тип мыслительной работы (13 штук: `ingestion`, `understanding`, `validation`, `modeling`, `solution_design`, `documentation`, `quality`, `research`, `governance`, `impact_analysis`, `reverse_requirements`, `risk_analysis`, `release_readiness`) | [`docs/taxonomy.md §1`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/taxonomy.md) | Techniques BABOK; **кандидат на носителя навыка** |
| **Подпроцесс** | Фаза конвейера формирования одного узла BCREQ (`П1`–`П6`) | [`standards/bcreq-process-standard.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/bcreq-process-standard.md) | Requirements Life Cycle Management |
| **Артефакт** | Продукт операции: BCREQ, ФТ, ТЗ, UC, US, AC, реестр рисков | [`standards/ba-ontology.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/ba-ontology.md) | Requirements и их атрибуты по [29148](https://www.iso.org/standard/72089.html) |
| **Состояние ЖЦ** | `raw` → `draft` → `in-review` → `validated` → `approved` → `baselined` | [`standards/ba-ontology.md §5`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/ba-ontology.md) | Baselining по 29148 |
| **Гейт** | Точка подтверждения; типы `G-self` / `G-mach` / `G-human` | Гейты `G1`–`G3` Mango, `HG-0`…`HG-8` Хаба, типология — [`10-theory.md §5`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/10-theory.md) | Verification & Validation |
| **Навык** | Разрешённый исполнимый артефакт под одну операцию | **отсутствует** | — |

**Правило соответствия `M-1`.** Носителем навыка выбирается **операция**, а не
процесс: процесс задействует несколько операций и потому не атомарен (нарушил бы
`I-5`), а подпроцесс `П1`–`П6` уже определён как композиция операций. Проверка
гипотезы — `H-4`.

## 5. Таксономия сред исполнения

Три среды из постановки, различающиеся не содержанием норм, а поверхностью
обнаружения и режимом гейта. Состав среды `serverless` намеренно не
детализируется — рабочее имя, предмет
[RFC оси «Среда»](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md).

| Среда | Кто исполняет | Как обнаруживает навык | Доступный тип гейта | Статус знания |
| --- | --- | --- | --- | --- |
| **Claude Code** (`local`) | Агент общего назначения и субагенты | Корневой `AGENTS.md` + каталог навыков | Все три: `G-self` в субагенте, `G-mach` через локальные валидаторы и CI, `G-human` через PR-ревью | Проверено практикой экосистемы |
| **GigaCode** (`gigacode`) | Агент среды в контуре компании | Нативный реестр навыков среды; путь — предмет вопроса `Q-2` RFC оси «Среда» | `G-self` предполагается; наличие `G-mach` и формы `G-human` **не подтверждено документацией** | **Допущение.** Проверенного источника у исполнителя нет |
| **VPS/Serverless** (`serverless`) | Бэкенд-процесс, вызываемый извне | Системный промпт собирается роутером из markdown | `G-self` и `G-mach` в конвейере; `G-human` требует внешнего интерфейса и по умолчанию отсутствует | Рабочее имя; композиция отложена |

**Следствие `E-1`.** Различие сред затрагивает **доступность гейтов**, а не
содержание норм. Это делает `H-5` проверяемой: если для GigaCode придётся менять
текст навыка, а не только оболочку, гипотеза ортогональности падает.

**Следствие `E-2`.** Среда без `G-human` (чистый serverless) не может исполнять
навыки, чей объявленный гейт — человеческий. Это не дефект среды, а ограничение
маршрутизации: набор допустимых навыков — функция среды. Формализовано в
[`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/30-decision-framework.md).
