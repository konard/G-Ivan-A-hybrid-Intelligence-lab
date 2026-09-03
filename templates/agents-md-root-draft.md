---
status: draft
version: 0.1
updated: 2026-09-03
temperature: 0.1
level: ecosystem
---

# Черновик корневого `AGENTS.md`

> Это **черновик** артефакта, предназначенного для размещения по пути `/AGENTS.md` в корне каждого
> репозитория экосистемы (Хаб и все спицы). Размещение в корне и легализация выполняются задачей
> B-110, принудительная инъекция в спицы — задачей B-111
> (https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/backlog.md).
> Обоснование структуры: https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/2026-09-03-ai-agent-onboarding-entrypoint-practices.md
>
> Ниже — содержание файла «как есть», без заголовка этого черновика.

---

# AGENTS.md

<scope>
Этот файл — единственная точка входа для любого ИИ-агента, работающего с этим репозиторием.
Он обязателен к прочтению до первого действия и является диспетчером: правила живут в каноничных
документах, ссылки на них — ниже. Все ссылки абсолютные, потому что агент может работать из спицы.
Файл единый для всех моделей. Модель-специфичные файлы правил (CODEX.md, OPUS.md и подобные) ЗАПРЕЩЕНЫ.
</scope>

<hard_rules>
1. Прочитай этот файл целиком до первого изменения файлов.
2. Не изобретай структуру. Если для артефакта не найден дом — не создавай каталог, задай вопрос
   в issue или зафиксируй пробел в артефакте.
3. Класс артефакта определяется содержанием, а не удобством пути.
4. Один артефакт создаётся только под операционную боль (принцип Anti-Inflation).
5. Каждое изменение проходит через Pull Request. Прямые коммиты в `main` запрещены.
6. Перед коммитом запусти валидаторы репозитория (см. <validation>). Красный валидатор — стоп.
7. Не выдумывай факты, оценки и ссылки. Утверждение без проверяемого источника не публикуется.
8. Если постановка задачи неполна — выполни её без блокирования и явно зафиксируй пробел в артефакте.
</hard_rules>

<forbidden>
- ЗАПРЕЩЕНО создавать каталог `docs/contracts/` в любом репозитории экосистемы.
  Контрактные документы живут в `ai-rules/`.
- ЗАПРЕЩЕНО создавать модель-специфичные файлы правил: CODEX.md, OPUS.md, QWEN.md, DEEPSEEK.md и т. п.
- ЗАПРЕЩЕНО указывать `ai-generated` во frontmatter любого документа.
- ЗАПРЕЩЕНО создавать новые каталоги верхнего уровня без ADR.
- ЗАПРЕЩЕНО заводить issue без пяти уровней постановки (см. <issue_levels>).
- ЗАПРЕЩЕНО менять файлы в `standards/` и `docs/adr/` без задачи, явно разрешающей это.
- ЗАПРЕЩЕНО удалять или перезаписывать чужие артефакты вместо создания новой версии.
- ЗАПРЕЩЕНО использовать относительные ссылки на правила Хаба из спиц.
</forbidden>

<routing>
| Тема | Каноничный документ (абсолютный URL) |
|---|---|
| Правила работы агента (SSOT, режимы, автономия, DoD) | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-work-rules.md |
| Протокол онбординга (выполнить до старта) | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ai-rules/agent-onboarding-protocol.md |
| Все правила агента | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/ai-rules |
| Дома артефактов и структура репозитория | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/repo-model.md |
| Реестр артефактов | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/artifact-map.md |
| Бэклог и правила его ведения | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/backlog-instruction.md |
| Жизненный цикл задачи и статусы | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/issue-workflow.md |
| Шаблон задачи (Markdown) | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/.github/ISSUE_TEMPLATE/task.md |
| Именование файлов | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/file-naming.md |
| Frontmatter документов | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/frontmatter-standard.md |
| Research | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/research-standard.md |
| Analysis | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/analysis-standard.md |
| Audit | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/audit-standard.md |
| Report | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/report-standard.md |
| Контрактные документы (формат, RFC 2119) | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/contract-documentation-standard.md |
| Все стандарты | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/standards |
| Governance | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/GOVERNANCE.md |
| Правила вклада | https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/CONTRIBUTING.md |
</routing>

<artifact_homes>
| Класс артефакта | Дом |
|---|---|
| Исследование (внешнее знание, практики) | `research/<направление>/YYYY-MM-DD-name.md` |
| Анализ (разбор ситуации, варианты, рекомендации) | `docs/analysis/YYYY-MM-DD-name.md` |
| Аудит (проверка соответствия норме) | `docs/audit/YYYY-MM-DD-name.md` |
| Отчёт (фиксация результата) | `docs/report/YYYY-MM-DD-name.md` |
| Решение об архитектуре | `docs/adr/YYYY-MM-adr-NNN-name.md` |
| Норма, обязательная к исполнению | `standards/<name>.md` |
| Правила для ИИ-агента | `ai-rules/<name>.md` |
| Операционные артефакты процесса | `pr-ops/<name>.md` |

Имена файлов: в корне — UPPERCASE, во вложенных каталогах — lowercase-with-hyphens,
хронологические артефакты начинаются с даты `YYYY-MM-DD-`.
</artifact_homes>

<issue_levels>
Любая задача формулируется пятью раздельными уровнями. Смешение уровней — дефект постановки.

1. **User Story** — кто и зачем, от лица пользователя системы.
2. **ФТ к системе** — что СИСТЕМА должна делать для пользователя. Субъект требования — система.
3. **НФТ к системе** — с какими атрибутами качества система это делает. Субъект требования — система.
4. **Задача исполнителю** — какие артефакты создать или изменить. Субъект — исполнитель.
5. **Ограничения процесса** — как работать: запреты, обязательные стандарты, границы PR.

Исполнитель не является субъектом ФТ и НФТ (IEEE 29148, BABOK/CBAP).
</issue_levels>

<validation>
Перед каждым коммитом из корня репозитория:

```bash
./tools/validate-frontmatter.sh .
./tools/validate-file-naming.sh
./tools/validate-repository-structure.sh
```

Валидаторы — источник истины о структуре. Если валидатор запрещает то, что кажется правильным,
меняется не обход валидатора, а задача в бэклоге.
</validation>

<models>
Содержание правил одинаково для всех моделей. Различается только способ, которым инструмент
подхватывает этот файл. Дублировать правила в перечисленные ниже файлы ЗАПРЕЩЕНО — только ссылка.

| Инструмент / модель | Как подхватывается | Что требуется в репозитории |
|---|---|---|
| OpenAI Codex | читает `AGENTS.md` по цепочке global → корень → рабочий каталог | ничего сверх `/AGENTS.md` |
| Claude Code (Claude Opus и др.) | читает `CLAUDE.md` | `CLAUDE.md` с одной строкой импорта `@AGENTS.md` |
| GitHub Copilot | читает `.github/copilot-instructions.md` | файл-указатель со ссылкой на `/AGENTS.md` |
| Cursor | читает `.cursor/rules/*.mdc` и `AGENTS.md` | правило с `alwaysApply: true`, ссылающееся на `/AGENTS.md` |
| Qwen, DeepSeek, YandexGPT, GigaChat и прочие через универсальные обвязки | автозагрузки нет | содержимое `/AGENTS.md` передаётся в системный промпт обвязкой |

Если инструмент не умеет автозагрузку — обязанность оператора передать этот файл в системный промпт.
</models>

<escalation>
Останавливайся и спрашивай, а не догадывайся, если: не найден дом артефакта; требуется изменение
`standards/` или `docs/adr/`, не разрешённое задачей; задача противоречит действующему стандарту;
требуется удаление существующего артефакта. Вопрос задаётся комментарием в issue или PR.

ОСОБЫЙ СЛУЧАЙ — постановка предписывает путь вне генома. Если раздел «Готово, когда» или
«Задача исполнителю» называет конкретный путь файла, СНАЧАЛА сверь его с <artifact_homes> и
<forbidden>. Если путь противоречит геному — НЕ создавай его молча и НЕ игнорируй DoD:
зафиксируй конфликт комментарием в issue, предложи каноничный путь и дождись решения.
Прецедент: путь `docs/contracts/kb-citations.md` был предписан постановкой
https://github.com/G-Ivan-A/mango_ba_prompts/issues/353 и исполнен буквально — так каталог вне
генома попал в репозиторий при зелёных валидаторах.
</escalation>
