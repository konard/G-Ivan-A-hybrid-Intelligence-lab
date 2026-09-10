---
status: superseded
version: 2.0
updated: 2026-09-10
temperature: 0.1
level: ecosystem
---

# Шаблон корневого `AGENTS.md` (superseded)

Этот черновик был базой корневого `AGENTS.md` до того, как файл появился в корне
репозитория. С момента физической интеграции у артефакта есть действующие источники,
и черновик их не дублирует, чтобы не расходиться с ними:

- структура и её норма —
  [`standards/agents-md-bootstrap-standard.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/agents-md-bootstrap-standard.md);
- эталон Хаба (архетип A) —
  [`/AGENTS.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/AGENTS.md);
- поставляемые в проекты варианты —
  [`templates/spoke/AGENTS.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/templates/spoke/AGENTS.md)
  (архетип B) и
  [`templates/htom/AGENTS.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/templates/htom/AGENTS.md)
  (архетип D).

Новый репозиторий берёт вариант, соответствующий его архетипу, подставляет значения
`archetype` и `environment` из `.hub-profile.json` и заполняет секцию
`<project_specific_rules>` правилами своей концепции. Историческое содержание черновика
доступно в истории git (версия 1.0, коммит физической интеграции `AGENTS.md`).
