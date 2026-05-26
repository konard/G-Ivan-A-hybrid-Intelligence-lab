# Итоговое видение репозитория и артефактов (для межкомандного согласования)

Версия: 1

Дата среза: 25 мая 2026 г.

Связанная задача: [issue #13](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/13)

Статус: proposal (ожидает подтверждения Founder & PO и команд C / Q / G)

## Назначение документа

Зафиксировать единое видение по:

1. структуре репозитория `hybrid-Intelligence-lab`;
2. набору артефактов и их размещению;
3. содержанию (минимальной структуре) артефактов;

— для межкомандного согласования и подтверждения. Документ синтезирует
предложения команд C, Q, G и
[Вариант 4](comparison.md#вариант-4--независимый-синтез-operational-backbone-before-taxonomy).

Документ **не** меняет репозиторий. Изменения вносятся отдельной issue:
[change-proposal.md](change-proposal.md).

## Принятые решения (для подтверждения)

| № | Решение | Источник | Статус |
| --- | --- | --- | --- |
| 1 | Сохранить root-level core governance; не строить глубокую `/meta`-иерархию как основной слой. | C, Q, G | На подтверждение |
| 2 | `/governance/`-layering вводить по триггеру (≥3 политик области), а не сразу. | Вариант 4 | На подтверждение |
| 3 | Сначала закрыть операционный костяк: `CHANGELOG`, `CONTRIBUTING`, `.github/` шаблоны, `LICENSE`. | Вариант 4 | На подтверждение |
| 4 | `AI_GOVERNANCE.md` оставить как операционный контракт; переименование в `GOVERNANCE.md` — позже, вместе с `/governance/`. | Вариант 4 | На подтверждение |
| 5 | Ввести статусы зрелости `draft` / `reviewed` / `published` / `superseded` как frontmatter `status:`. | Q, G, Вариант 4 | На подтверждение |
| 6 | Привести имя `hybrid-Intelligence-lab` и URL во всех документах. | Вариант 4 | На подтверждение |
| 7 | Перенести `experiments/tz-corpus` в контекст проекта Mango. | issue #13, Вариант 4 | На подтверждение |
| 8 | Синхронизировать шаблоны задач с опытом `open-ai.ru`. | issue #13 | На подтверждение |

## Целевая структура репозитория

Текущая структура сохраняется; добавляется операционный костяк. `/governance/`
показан как **будущий** слой (вводится по триггеру, не сейчас).

```text
hybrid-Intelligence-lab/
├── README.md                     # точка входа, навигация
├── PRODUCT_VISION.md             # продуктовое видение (Product Vision Board)
├── AI_GOVERNANCE.md              # операционный контракт human + AI
├── CONTRIBUTING.md               # ← добавить: как вносить вклад (GitHub-native)
├── CHANGELOG.md                  # ← добавить: журнал изменений
├── LICENSE                       # ← добавить: лицензия (по решению Founder & PO)
│
├── .github/                      # ← добавить
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml
│   │   ├── ai_implementation_task.yml   # синхр. с open-ai.ru
│   │   ├── research_task.md
│   │   └── governance_change.md
│   └── pull_request_template.md
│
├── docs/
│   ├── concept/                  # repository-structure, vision-standard
│   └── governance/               # hybrid-team-collaboration
│
├── research/
│   ├── mango/                    # доменное исследование Mango
│   └── repository-governance/    # это исследование (issue #13)
│
├── frameworks/
├── education/
│   └── ba-prompt-engineering/
├── projects/
├── standards/                    # шаблоны артефактов (research / framework / ...)
├── meta/                         # служебная навигация; artifact-map по триггеру
├── experiments/
│   └── mango/tz-corpus/          # ← перенести сюда из experiments/tz-corpus
├── tests/
│   └── validate-repository-structure.sh
│
└── governance/                   # БУДУЩИЙ слой (по триггеру, не сейчас)
    ├── ai/
    ├── research/
    └── frameworks/
```

### Роли каталогов (подтверждение единого vocabulary)

| Каталог | Роль | Не должен содержать |
| --- | --- | --- |
| root `*.md` | Публичный core governance и точки входа. | Доменные исследования, длинные политики. |
| `docs/concept` | Обоснование решений (RFC-lite + ADR). | Ежедневные операционные правила. |
| `docs/governance` | Правила взаимодействия людей и AI. | Доменные артефакты. |
| `research/<domain>` | Независимые исследования по домену. | Production-секреты, скрипты экспериментов. |
| `experiments/<project>/<slug>` | Воспроизводимые эксперименты, привязанные к проекту/домену. | Финальный исследовательский текст. |
| `frameworks` | Методологии (только после сравнения с существующими). | Фреймворки «ради уникальности». |
| `education` | Open education. | Коммерческое обучение под клиента (→ `projects/` или spoke). |
| `projects` | Проектные рабочие области. | Production-код с собственным lifecycle (→ spoke). |
| `standards` | Шаблоны и стандарты оформления. | Сами артефакты. |
| `meta` | Служебная навигация репозитория. | Публичный governance. |
| `governance` (будущий) | Специализированные политики, когда их станет много. | — |

> Разные направления могут иметь разные внутренние структуры; едиными остаются
> terminology, governance lifecycle, contribution rules, review model и
> publication rules (согласие всех трёх команд).

## Артефактная карта (где что хранить)

| Тип артефакта | Где хранить | Минимальная структура | Критерий готовности |
| --- | --- | --- | --- |
| Framework proposal | `frameworks/<slug>/` | Проблема, существующие фреймворки, gap, решение, примеры, ограничения. | Есть сравнительная таблица; ясно, почему внешний фреймворк недостаточен. |
| Education program | `education/<course-slug>/` | ЦА, цели, модули, материалы, сценарий, результаты. | По материалам можно провести занятие. |
| Research report | `research/<domain>/<topic>.<lang>.md` | Вопрос, метод, источники, анализ, вывод, ограничения, next steps. | Вывод подтверждён источниками/экспериментом или помечен как допущение. |
| Project knowledge base | `projects/<project-slug>/` | Цель, роли, контекст, промпты/процессы, связи с framework/research. | Используется как контекст AI-агента без монолитного промпта. |
| Standard / template | `standards/<slug>.md` или `docs/concept/` | Область применения, формат, обязательные поля, пример. | Понятно, какие документы обязаны следовать стандарту. |
| Experiment | `experiments/<project>/<slug>/` | README, скрипты, входы/выходы, команда воспроизведения. | Другой участник может повторить проверку. |
| Governance / policy | root или (по триггеру) `governance/<area>/` | Роли, правила, workflow, критерии готовности, эскалация. | Однозначно, кто и как применяет правило. |
| Operational contract | `standards/contracts/<slug>.md` | Lifecycle, review, citation, bilingual, AI-disclosure, уровни согласования. | Lightweight (1–2 страницы), применим без enterprise-нагрузки. |

## Содержание артефактов: статусы зрелости

Вводится единый набор статусов и способ их фиксации.

| Статус | Значение | Где фиксируется |
| --- | --- | --- |
| `draft` | Черновик, не для публикации. | Frontmatter `status: draft`. |
| `reviewed` | Проверен ревьюером, готов для внутреннего использования. | Frontmatter + строка в `meta/artifact-map.md` (по триггеру). |
| `published` | Публичная версия, при необходимости bilingual ru/en. | Frontmatter + README каталога. |
| `superseded` | Заменён новой версией. | Frontmatter + ссылка на актуальный артефакт. |

Рекомендуемый frontmatter (machine-checkable):

```yaml
---
status: reviewed        # draft | reviewed | published | superseded
version: 1
updated: 2026-05-25
issue: 13
supersedes: null        # путь к предыдущему артефакту, если есть
---
```

Проверку наличия и допустимости `status:` добавляет
`tests/validate-repository-structure.sh` после согласования формата (это
отличает данный подход от чисто декларативной таблицы статусов у других команд).

## Языковая политика (без изменений)

Сохраняется правило из `docs/concept/repository-structure.md`: соседние файлы
`topic.ru.md` / `topic.en.md`; публичные research/framework для международной
аудитории получают ru/en пару или явно зафиксированное исключение. Это
исследование ведётся на русском, потому что issue #13 поставлена на русском.

## Синхронизация с `open-ai.ru`

| Практика `open-ai.ru` | Перенос в `hybrid-Intelligence-lab` |
| --- | --- |
| `CHANGELOG.md` (date-based, Added/Removed/TODO, секция Unreleased) | Завести в том же формате. |
| `.github/ISSUE_TEMPLATE/ai_implementation_task.yml` (Operating Mode, Context, Functional Requirements, Allowed/Forbidden) | Адаптировать под research/edu hub. |
| Шаблоны `feature.md`, `foundation.md` | Адаптировать как `research_task.md`, `governance_change.md`. |
| `.github/workflows/validate-structure.yml` | Рассмотреть как следующий шаг после стабилизации валидатора. |
| Governance-first и AI-native подход | Уже совпадает (`AI_GOVERNANCE.md`). |

## Что НЕ делаем (границы видения)

- Не строим `/governance/{ai,research,frameworks,contracts}/` под ещё не
  существующие политики (избегаем governance overgrowth).
- Не переименовываем `AI_GOVERNANCE.md` сейчас (минимум churn).
- Не превращаем репозиторий в production-codebase.
- Не вводим тяжёлые enterprise-контракты.

## Следующий шаг

Подтвердить решения 1–8 и реализовать их отдельной issue —
[change-proposal.md](change-proposal.md).
