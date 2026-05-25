# Сравнение подходов к структуре и governance репозитория

Версия: 1

Дата среза: 25 мая 2026 г.

Связанная задача: [issue #13](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/13)

## Цель

Сравнить три независимых предложения по структуре и governance репозитория
(Команда C, Команда Q, Команда G), добавить независимый 4-й вариант и
подготовить основу для итогового видения и межкомандного согласования.

Исследование не меняет структуру репозитория. Это аналитический артефакт:
сами изменения выносятся в отдельную issue (см.
[change-proposal.md](change-proposal.md)).

## Контекст: фактическое состояние репозитория на дату среза

Перед сравнением зафиксирован реальный снимок репозитория, потому что
предложения команд частично опираются на устаревшие факты (старое имя
`research-and-edu-ai-lab`, иной набор файлов).

| Параметр | Фактическое значение |
| --- | --- |
| Имя репозитория | `hybrid-Intelligence-lab` (переименован из `research-and-edu-ai-lab`). |
| Корневые файлы | `README.md`, `PRODUCT_VISION.md`, `AI_GOVERNANCE.md`. |
| Каталоги | `docs/` (`concept/`, `governance/`), `education/`, `experiments/`, `frameworks/`, `meta/`, `projects/`, `research/`, `standards/`, `tests/`. |
| Governance-документы | `AI_GOVERNANCE.md` (роли, режимы, цикл, Definition of Done) + `docs/governance/hybrid-team-collaboration.md`. |
| Концепция | `docs/concept/repository-structure.md`, `docs/concept/vision-standard.md`. |
| Проверка структуры | `tests/validate-repository-structure.sh`. |
| `CHANGELOG`, `CONTRIBUTING`, `LICENSE`, `CODE_OF_CONDUCT` | Отсутствуют. |
| Шаблоны issue / PR (`.github/`) | Отсутствуют. |
| Каталог `/governance/` | Отсутствует (специализированные политики пока не выделены). |
| Известный дефект пути | `experiments/tz-corpus/` относится исключительно к проекту Mango и стоит вне доменного контекста. |
| Несогласованность имени | В `README.md`, `PRODUCT_VISION.md`, `AI_GOVERNANCE.md`, `docs/concept/*` остаётся старое имя и старые URL `research-and-edu-ai-lab`. |

> Важно: все три команды предполагали отсутствие `CONTRIBUTING`/`LICENSE`/`CODE_OF_CONDUCT` (верно), но ни одна не учла переименование репозитория, отсутствие `CHANGELOG` и отсутствие шаблонов задач. Эти факты добавлены в 4-й вариант.

## Краткое содержание предложений команд

### Команда C

- Для early-stage репозитория root-level governance **правильнее** глубокой
  `/meta`-иерархии: discoverability, GitHub-native UX, проще ingest для LLM.
- Главный риск — **governance fragmentation** (`AI_GOVERNANCE.md`, `AI_RULES.md`,
  `AI_QUICK_REF.md` начинают пересекаться). Главный вопрос не «root vs /meta», а
  **governance consistency**.
- Рекомендует **governance layering**: Уровень 1 (core в root: `README`,
  `CONTRIBUTING`, `GOVERNANCE`, `ROADMAP`, `PRODUCT_VISION`, `LICENSE`,
  `CODE_OF_CONDUCT`) и Уровень 2 (специализированные политики в
  `/governance/ai/`, `/governance/research/`, `/governance/frameworks/`).
- Объединить `AI_GOVERNANCE.md` + `AI_RULES.md` → `GOVERNANCE.md` с разделами:
  Repository Governance, AI Contribution Rules, Research Standards, Human Review
  Policy, Publication Workflow. `AI_QUICK_REF.md` оставить как cheat-sheet.
- Добавить **lightweight operational contracts** (например,
  `/governance/research/RESEARCH_CONTRACT.md`).
- Главные тезисы: **operational consistency > structural perfection**,
  **Governance Minimalism**; разные направления могут иметь разные структуры при
  едином vocabulary и lifecycle. Сильнейший дифференциатор —
  formalized hybrid human + AI collaboration governance.

### Команда Q

- Соглашается с Командой C: root-level governance + явный layering.
- Фиксирует **риски**: дублирование `/meta` и `/docs/governance`; рост
  `AI_GOVERNANCE.md` в монолит; конфликт discoverability и глубины.
- Ключевая рекомендация: `GOVERNANCE.md` в root — это **оглавление + entry
  point** со ссылками, а не хранилище всех правил.
- Структура: `/governance/{ai,research,frameworks}/`, `docs/governance/` только
  под уникальные документы, `meta/` только под служебную навигацию
  (`artifact-map.md`, `maturity-model.md`).
- Добавить operational contracts (1–2 страницы) и явные **статусы зрелости
  артефактов**: `draft` / `reviewed` / `published` / `superseded`, с указанием,
  где статус фиксируется.

### Команда G

- Синтез C + Q + best practices. Вердикт: **root-level core + лёгкий layering в
  `/governance/`** — оптимум для early/mid-stage.
- Финальная структура: в root `README`, `PRODUCT_VISION`, `GOVERNANCE.md`
  (переименован из `AI_GOVERNANCE.md`), `CONTRIBUTING`, `CODE_OF_CONDUCT`,
  `LICENSE`; `/governance/{ai,research,frameworks,contracts}/`; `/meta/`
  (`artifact-map.md`, `maturity-model.md`, `repository-structure.md`); далее
  `docs/`, `research/`, `frameworks/`, `education/`, `projects/`, `standards/`,
  `experiments/`, `tests/`.
- Действия сейчас: переименовать `AI_GOVERNANCE.md` → `GOVERNANCE.md`, создать
  `/governance/`, добавить раздел «Governance Layering», зафиксировать статусы
  артефактов, сохранять Governance Minimalism.
- Root vs `/meta`: root — для **публичного** governance, `/meta` — для
  **внутренней** мета-навигации.

## Сравнение по ключевым осям

| Ось | Команда C | Команда Q | Команда G | Вариант 4 (этот документ) |
| --- | --- | --- | --- | --- |
| Root vs deep hierarchy | Root для core | Root для core | Root для core | Root для core |
| `/governance/` layering | Ввести сразу | Ввести сразу | Ввести сразу | Ввести **по триггеру**, не сразу |
| Судьба `AI_GOVERNANCE.md` | Слить в `GOVERNANCE.md` | Сделать оглавлением | Переименовать в `GOVERNANCE.md` | Оставить как есть, не плодить churn |
| Точка входа для контрибьютора | `CONTRIBUTING.md` (упомянут) | `README` + `artifact-map` | `CONTRIBUTING.md` | `CONTRIBUTING.md` + `.github/` шаблоны |
| Статусы зрелости | Через контракты | Таблица статусов | Зафиксировать статусы | **Frontmatter `status:`**, проверяемый валидатором |
| Operational contracts | Да | Да | Да (+ templates) | Да, но как `standards/` шаблоны |
| Учёт переименования репозитория | Нет | Нет | Нет | **Да** |
| `CHANGELOG` | Не упомянут | Не упомянут | Не упомянут | **Да, добавить сейчас** |
| Шаблоны issue/PR | Не упомянуты | Не упомянуты | Не упомянуты | **Да, синхронизировать с `open-ai.ru`** |
| Дефект `experiments/tz-corpus` | Не упомянут | Не упомянут | Не упомянут | **Да, перенести в контекст Mango** |

## Зоны согласия трёх команд

1. Root-level core governance — правильный выбор для текущего этапа.
2. Глубокая `/meta`-иерархия как основной слой — преждевременна (artificial
   complexity).
3. Нужен явный governance layering, чтобы корень не разрастался.
4. Нужны lightweight operational contracts, а не enterprise-документы.
5. Нужны статусы зрелости артефактов (`draft` / `reviewed` / `published` /
   `superseded`).
6. Главная ценность репозитория — formalized hybrid human + AI collaboration
   governance, а не идеальная папочная структура.
7. Разные направления (research / education / projects) могут жить по разным
   правилам при едином vocabulary и lifecycle.

## Зоны расхождения

| Вопрос | Команда C | Команда Q | Команда G |
| --- | --- | --- | --- |
| Имя единого документа | `GOVERNANCE.md` (слияние) | `GOVERNANCE.md` (оглавление) | `GOVERNANCE.md` (переименование) |
| Роль `/meta` | Не акцентирует | Только служебная навигация | Внутренняя мета-навигация |
| `docs/governance` vs `/governance` | Не разводит явно | Видит риск дублирования | `/governance` для политик, `meta` для карт |
| Когда вводить layering | Сейчас | Сейчас | Сейчас |

Расхождения тактические, а не принципиальные: спор идёт о **скорости** и
**именовании**, а не о направлении.

## Вариант 4 — независимый синтез: «Operational backbone before taxonomy»

### Тезис

Все три команды оптимизируют **дерево governance-документов**, но репозиторий
сейчас содержит всего два governance-артефакта (`AI_GOVERNANCE.md` и
`docs/governance/hybrid-team-collaboration.md`). Создавать
`/governance/{ai,research,frameworks,contracts}/` под ещё не существующие
политики — это и есть та самая `governance overgrowth` / `artificial
complexity`, от которой предостерегают сами команды. Сначала нужно закрыть
**операционный костяк**, который даёт ценность немедленно, и только потом
строить таксономию политик.

### Принципы

1. **Operational backbone before document taxonomy.** Сначала то, что нужно
   каждый день: логирование изменений (`CHANGELOG`), точка входа контрибьютора
   (`CONTRIBUTING.md`), шаблоны постановки задач (`.github/ISSUE_TEMPLATE/`),
   лицензия (`LICENSE`). `/governance/`-дерево — позже.
2. **Минимум churn в governance.** `AI_GOVERNANCE.md` уже выполняет роль
   операционного контракта (роли, режимы, цикл, Definition of Done). Не
   переименовывать его в `GOVERNANCE.md` сейчас: это ломает ссылки и валидатор
   без новой ценности. `CONTRIBUTING.md` становится GitHub-native точкой входа и
   ссылается на `AI_GOVERNANCE.md`.
3. **Governance-as-you-grow (триггеры вместо «сразу»).** Каждый слой вводится по
   явному триггеру, а не «на вырост».
4. **Статусы зрелости — машиночитаемые.** `draft` / `reviewed` / `published` /
   `superseded` фиксируются как YAML-frontmatter `status:` в начале артефакта,
   чтобы `tests/validate-repository-structure.sh` мог проверять их
   автоматически. Это операционализирует идею статусов, которую остальные
   команды оставили на уровне таблицы.
5. **Сначала чинить дефекты, потом строить новое.** Переименование, `tz-corpus`,
   отсутствие `CHANGELOG`/шаблонов — это долг, а не развитие.

### Триггеры governance-as-you-grow

| Слой / артефакт | Триггер ввода |
| --- | --- |
| `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`, `.github/` шаблоны | **Сейчас** (операционный костяк отсутствует). |
| Исправление имени `hybrid-Intelligence-lab` во всех файлах | **Сейчас** (несогласованность уже в репозитории). |
| Перенос `experiments/tz-corpus` в контекст Mango | **Сейчас** (известный дефект пути). |
| `/governance/<area>/` подкаталоги | Когда появится **≥3** специализированных политик одной области ИЛИ `AI_GOVERNANCE.md` станет нечитаемо большим. |
| `meta/artifact-map.md` + frontmatter `status:` | Когда число артефактов превысит порог удобной ручной навигации (ориентир: >15 содержательных документов). |
| `CODE_OF_CONDUCT.md`, `ROADMAP.md` | При появлении внешних контрибьюторов / публичного roadmap. |
| Переименование `AI_GOVERNANCE.md` → `GOVERNANCE.md` | Только вместе с вводом `/governance/`-дерева, чтобы делать churn один раз. |

### Что Вариант 4 берёт у команд

- У Команды C — **Governance Minimalism** и «operational consistency >
  structural perfection» (доводит до предела: не строить пустые папки).
- У Команды Q — `CONTRIBUTING`/`README` как точку входа и явные статусы зрелости.
- У Команды G — синтез и принцип «root для core, `/meta` для внутренней
  навигации», а также готовый целевой контур для будущего ввода `/governance/`.

### Чем Вариант 4 отличается

| Отличие | Почему важно |
| --- | --- |
| Приоритет операционного костяка над таксономией | Даёт ценность в день 1; не плодит пустые папки. |
| Триггеры вместо «ввести сразу» | Прямая реализация Governance Minimalism, которую команды декларируют, но нарушают, предлагая `/governance/` под ещё не существующие политики. |
| `status:` во frontmatter + проверка валидатором | Статус становится исполняемым правилом, а не строкой в таблице. |
| Учтены переименование, `CHANGELOG`, шаблоны, `tz-corpus` | Закрывает реальный долг, который команды не увидели из-за устаревшего снимка. |
| Минимум churn (`AI_GOVERNANCE.md` не трогаем сейчас) | Не ломаем ссылки и валидатор без необходимости. |

## Рекомендация исследования

Принять **Вариант 4** как порядок действий, сохранив целевой контур Команды G
как ориентир «куда расти». Тактически:

1. Сейчас закрыть операционный костяк и дефекты (отдельная issue).
2. Целевой `/governance/`-layering и переименование в `GOVERNANCE.md` ввести
   позже по триггеру, одним согласованным изменением.

Итоговое видение для межкомандного согласования: [final-vision.md](final-vision.md).
Черновик issue на изменения: [change-proposal.md](change-proposal.md).

## Ограничения

- Сравнение опирается на текстовые предложения трёх команд из issue #13 и на
  снимок репозитория на дату среза; более поздние коммиты могли изменить факты.
- Пороговые значения триггеров (≥3 политик, >15 документов) — ориентиры для
  обсуждения, а не жёсткие константы.
- Вариант 4 — предложение AI-агента; финальное решение принимает Founder & PO и
  ревьюеры (human-in-control).
