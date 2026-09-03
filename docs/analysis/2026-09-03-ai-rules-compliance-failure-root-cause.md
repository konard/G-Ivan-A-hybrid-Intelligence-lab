---
status: draft
version: 0.1
updated: 2026-09-03
temperature: 0.1
type: internal-analysis
analysis-subtype: recommendation
scope: ecosystem
context: [hub, mango, aether-orbis, ai-rules, compliance, agents-md, issue-547]
method: repository-review + issue-corpus-review + industry-practice-comparison
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547"
related_artifacts:
  - "research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md"
  - "templates/agents-md-root-draft.md"
  - "ai-rules/agent-work-rules.md"
  - "ai-rules/agent-onboarding-protocol.md"
  - "pr-ops/repo-model.md"
  - "standards/contract-documentation-standard.md"
  - "standards/issue-workflow.md"
external_artifacts:
  - "https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/docs/contracts"
  - "https://github.com/G-Ivan-A/aether-orbis/issues"
---

# Анализ: коренные причины несоблюдения правил экосистемы ИИ-агентами

## Summary (BLUF)

**Текущая архитектура правил экосистемы провалилась в обеспечении compliance со стороны ИИ.**
Это не единичные ошибки исполнителей и не «плохие модели»: наблюдаемые сбои воспроизводятся
в разных репозиториях, у разных агентов и в разные месяцы, то есть являются системными
и объясняются устройством самой архитектуры доставки правил, а не поведением конкретного агента.

Проверенные коренные причины (в порядке вклада):

1. **Отсутствие корневой точки входа.** Правила лежат в
   [`ai-rules/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/ai-rules) и
   [`standards/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/standards).
   Ни один инструментальный агент (Codex, Claude Code, Copilot, Cursor) не загружает эти каталоги
   автоматически: все они читают файлы фиксированных имён в корне или в `.github/`/`.cursor/`.
   Правила физически не попадают в контекст, если человек не вставил их вручную.
2. **Дырки в самих контрактах, а не только в их доставке.** Класс документов «контракт» описан в
   [`standards/contract-documentation-standard.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/contract-documentation-standard.md)
   по форме (RFC 2119, структура), но **канонический дом для контрактных документов там не задан**.
   Агент в Mango не «нарушил» правило — правила для этого случая не существовало, и он изобрёл
   `docs/contracts/`.
3. **Отсутствие распространения генома в спицы.** Шаблон задачи Хаба никогда не был доставлен в
   Aether-Orbis: каталога `.github/ISSUE_TEMPLATE` в этом репозитории нет. Требовать соблюдения
   шаблона, которого нет в репозитории, невозможно.
4. **Смешение уровней требований в самом шаблоне Хаба.** Действующий шаблон сводит
   User Story / ФТ / НФТ в одну необязательную строку заголовка, из-за чего агенты и люди
   заполняют её как «задачу исполнителю» — то есть шаблон сам провоцирует нарушение
   IEEE 29148 / BABOK.
5. **Раздутие как усилитель, а не как первопричина.** Объём канонических правил велик, но
   даже идеально краткий `ai-rules/` не был бы прочитан: причина №1 первична по отношению к объёму.

Вывод по вопросу контракта задачи «раздутие vs отсутствие явных запретов vs слабая маршрутизация»:
**решающий фактор — слабая (фактически отсутствующая) маршрутизация из корня; вторым по значимости
идёт отсутствие явных запретов; раздутие — третий фактор и работает как усилитель первых двух.**

Отсюда рекомендация: корневой `AGENTS.md`-диспетчер — необходимое, но **недостаточное** условие.
Без принудительной инъекции в спицы и без машинной валидации он повторит судьбу `ai-rules/`.

## Контекст и границы

Анализ выполнен по [issue #547](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547).

В границах: причины несоблюдения правил ИИ-агентами в Хабе и спицах (Mango, Aether-Orbis);
пригодность текущих механизмов доставки контекста; уровневая ошибка в шаблонах задач.

Вне границ: изменение стандартов и ADR (запрещено ограничением процесса №1 issue #547),
размещение `AGENTS.md` в корне (требует легализации — вынесено в бэклог),
исправление структуры самих спиц (вынесено в бэклог).

Метод: проверка каждого утверждения issue против фактического состояния репозиториев
через GitHub API, чтение действующих контрактов Хаба, сопоставление с индустриальными практиками
(вынесено в отдельный research-артефакт
[`research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md)).

## Findings

### F1. Вердикт: архитектура правил провалилась в обеспечении compliance

Формулируется прямо, как требует контракт задачи №1.

Экосистема располагает развитой нормативной базой: канонические
[`ai-rules/agent-work-rules.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-rules.md),
[`ai-rules/agent-onboarding-protocol.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-onboarding-protocol.md)
(помеченный `executable: true`, `entrypoint: true`),
[`pr-ops/repo-model.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/repo-model.md),
корпус стандартов и валидаторы в
[`tools/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/tools).

При этом фактический результат: агенты создают каталоги вне генома, заводят задачи мимо шаблона
и не опираются на КБ. Нормативная полнота не конвертировалась в исполнение. Признак провала —
не наличие ошибок, а то, что **механизм не имеет ни одной точки, в которой правило встречается
с агентом принудительно**: `entrypoint: true` во frontmatter — это метка для человека, а не
загрузчик контекста. Ни один инструмент не читает frontmatter, чтобы найти точку входа.

### F2. Mango: `docs/contracts/` — следствие пробела в стандарте, а не своеволия агента

Проверено: [`docs/contracts/kb-citations.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/contracts/kb-citations.md)
в Mango существует, имеет `type: contract` и `ai-generated: true` во frontmatter, при том что
`ai-generated` во frontmatter Хабом запрещён. Параллельно в Mango существует каталог
[`ai-rules/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/ai-rules) — то есть канонический
дом там был, но агент его не выбрал.

Корневая причина: `standards/contract-documentation-standard.md` задаёт формат контрактного
документа и словарь RFC 2119, но не отвечает на вопрос «где такой документ живёт». В
`pr-ops/repo-model.md` строки для класса «контракт» тоже нет. При отсутствии правила маршрутизации
агент действует по наиболее вероятному индустриальному паттерну — `docs/<class>/` — и получает
`docs/contracts/`. Это ровно тот сбой, который явный запрет плюс явный роутинг («контракты живут в
`ai-rules/`; ЗАПРЕЩЕНО создавать `docs/contracts/`») закрывает одной строкой.

### F3. Aether-Orbis: шаблон задачи не был доставлен в репозиторий

Проверено: в [aether-orbis](https://github.com/G-Ivan-A/aether-orbis) отсутствует каталог
`.github/ISSUE_TEMPLATE` (запрос к API возвращает 404), а также отсутствуют `ai-rules/`,
`pr-ops/`, `standards/`. Issues репозитория используют самодельную структуру
(«Описание / Definition of Done / Зависимости / Контекст») вместо структуры Хаба.

Корневая причина: геном экосистемы распространяется вручную и не проверяется. Формулировка
«агент грубо нарушает шаблон экосистемы» неточна: **шаблона в этом репозитории не было**.
Это меняет приоритет техдолга — сначала инъекция генома, потом требование соблюдения.

### F4. Уровневая ошибка встроена в сам шаблон Хаба

В действующем
[`.github/ISSUE_TEMPLATE/task.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/.github/ISSUE_TEMPLATE/task.md)
User Story, ФТ и НФТ представлены одной необязательной строкой заголовка
(`User Story / ФТ / НФТ (optional): -`), а вся содержательная часть постановки собрана в разделах
«Контракты задачи» и «Готово, когда», где субъектом выступает исполнитель.

Следствие: субъектом «ФТ» и «НФТ» на практике становится исполнитель («агент должен создать
отчёт»), что противоречит IEEE 29148 и BABOK, где субъект функционального и нефункционального
требования — **система**. Пока три разных уровня живут в одной опциональной строке, корректное
заполнение является исключением, а не нормой. Это дефект контракта, а не дисциплины.

### F5. Раздутие правил: усилитель, а не первопричина

Суммарный объём канонических правил Хаба (ai-rules + standards) на порядки превышает
рекомендованные индустрией пределы для инструкционных файлов (Copilot — «около двух страниц»,
Claude Code — ориентир менее 200 строк, Cursor — менее 500 строк на правило; см. research-артефакт).
Но даже сжатый до одной страницы `ai-rules/agent-work-rules.md` остался бы непрочитанным, потому что
не находится ни на одном пути автозагрузки.

Раздутие проявляется вторично: когда правила всё-таки попадают в контекст целиком, ключевые запреты
оказываются в середине длинного контекста, где внимание модели минимально
(эффект «lost in the middle», Liu et al., TACL 2023 —
https://arxiv.org/abs/2307.03172). Поэтому корневой файл обязан быть коротким диспетчером,
а не копией правил.

### F6. Одного `AGENTS.md` недостаточно

Открытый формат `AGENTS.md` читают Codex и ряд агентов, но Claude Code читает `CLAUDE.md`,
GitHub Copilot — `.github/copilot-instructions.md`, Cursor — `.cursor/rules/*.mdc`. Все эти
механизмы доставляют **контекст, а не принудительную конфигурацию**: модель может проигнорировать
инструкцию. Следовательно, корневой `AGENTS.md` закрывает доставку, но не гарантирует исполнение.

Обязательное дополнение к техдолгу (как требует раздел «Не выполнено и вопросы» issue #547):
машинная проверка — расширение `tools/validate-repository-structure.sh` явными запретами
(в том числе `docs/contracts/`), валидация структуры issue по пяти уровням и pre-commit/CI-гейт.
Запрет, проверяемый CI, — единственный механизм из перечисленных, который не зависит от того,
прочитал ли агент файл.

## Рекомендации

| № | Рекомендация | Куда вынесено |
|---|---|---|
| R1 | Ввести корневой `AGENTS.md` как единый диспетчер: жёсткие короткие правила, явные запреты, маршрутизация абсолютными URL | черновик [`templates/agents-md-root-draft.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/templates/agents-md-root-draft.md); размещение в корне — B-110 |
| R2 | Легализовать `AGENTS.md` как обязательный артефакт бутстрапа (ускоренно, через стандарт, без RFC) | бэклог B-110 |
| R3 | Реализовать `tools/inject-agents-md.sh` для принудительной синхронизации во все спицы | бэклог B-111 |
| R4 | Закрыть пробел F2: задать канонический дом для контрактных документов и исправить структуру Mango | бэклог B-112 |
| R5 | Привести Aether-Orbis в соответствие с геномом, начиная с `.github/ISSUE_TEMPLATE` | бэклог B-113 |
| R6 | Инициировать стандарт правил формирования Story/ФТ/НФТ (IEEE 29148 / BABOK) | бэклог B-114 |
| R7 | Разделить пять уровней постановки в шаблонах задач Хаба | выполнено в этом PR + легитимизация B-115 |
| R8 | Добавить машинные гейты (явные запреты в валидаторе структуры, валидация уровней issue, pre-commit/CI) | бэклог B-116 (обязательное дополнение по F6) |

## Ограничения и зафиксированные пробелы постановки

- Issue #547 требует разместить `AGENTS.md` «строго в корне», но ограничение процесса №1 запрещает
  изменения в `standards/` и `docs/adr/`; корневая структура Хаба закреплена ADR-007. Поэтому в
  рамках PR поставляется **черновик** файла, а фактическое размещение в корне и легализация
  вынесены в задачу B-110. Это отклонение зафиксировано в PR и в бэклоге.
- Issue #547 не определяет, к какому классу артефактов относится сам результат; классификация
  выбрана по содержанию: причины сбоев — Analysis, индустриальные практики — Research.

## Связанные артефакты

- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/547
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/templates/agents-md-root-draft.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/backlog.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/contract-documentation-standard.md
- https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/issue-workflow.md
