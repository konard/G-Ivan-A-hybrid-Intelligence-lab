# Research: structure & governance репозитория

Исследование по структуре и governance самого репозитория
`hybrid-Intelligence-lab`: сравнение предложений трёх команд, независимый 4-й
вариант, итоговое видение для межкомандного согласования и черновик issue на
изменения.

Связанная задача: [issue #13](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/13)

## Документы

| Документ | Назначение |
| --- | --- |
| [comparison.md](comparison.md) | Сравнение подходов команд C / Q / G + независимый Вариант 4. |
| [final-vision.md](final-vision.md) | Итоговое видение репозитория, артефактов и их содержания для подтверждения. |
| [change-proposal.md](change-proposal.md) | Готовый текст follow-up issue на изменения в репозитории. |

## Важно

Это исследование **не меняет** структуру репозитория (требование issue #13).
Сами изменения вынесены в отдельную issue — см.
[change-proposal.md](change-proposal.md). Финальные решения принимает Founder &
PO и назначенные ревьюеры (human-in-control).

## Ключевой вывод

Все три команды сходятся на root-level core governance + лёгком
`/governance/`-layering. Вариант 4 уточняет порядок: **сначала операционный
костяк** (`CHANGELOG`, `CONTRIBUTING`, шаблоны задач, `LICENSE`) и исправление
дефектов (переименование репозитория, путь `experiments/tz-corpus`), а
`/governance/`-дерево — позже по явному триггеру (governance-as-you-grow).
