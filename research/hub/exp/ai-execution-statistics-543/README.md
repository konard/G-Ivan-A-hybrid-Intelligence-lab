---
status: draft
version: 0.1
updated: 2026-08-26
temperature: 0.1
type: experiment
---

# exp: ai-execution-statistics-543

Evidence container для отчёта
[`../../../../docs/report/2026-08-26-ai-execution-statistics.md`](../../../../docs/report/2026-08-26-ai-execution-statistics.md),
issue [#543](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/543).

> **Ссылки.** Относительная ссылка на родительский отчёт выше — вынужденная
> форма: её машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh)
> (регулярное выражение требует префикса `../../../../docs/report/`).

## Что здесь измеряется

Отчёт обязан отвечать на два вопроса без права додумывать: **сколько задач
закрыто** и **сколько за них фактически заплачено**. Второй вопрос опасен —
цену легко «оценить» и выдать оценку за факт. Поэтому контейнер сводит вопрос
о стоимости к машинному предикату: *в тексте PR или его комментариев напечатан
один из трёх известных числовых маркеров стоимости — да или нет*.

Три маркера, и только они (приоритет сверху вниз внутри одного лога):

| Приоритет | Маркер | Кто печатает |
| --- | --- | --- |
| 1 | `### 💰 Cost: **$X**` | Claude Code, актуальный формат |
| 2 | `- Calculated by Anthropic: $X USD` | Claude Code, ранний формат (цифра провайдера) |
| 3 | `- Public pricing estimate: $X USD` | Codex; ранний Claude Code (оценка по публичному прайсу) |

Если маркера нет — PR попадает в список «стоимость не указана» и не получает
никакого значения. Расчёт цены по токенам, экстраполяция и перенос цифры с
соседней сессии в скрипте отсутствуют как код, а не как обещание.

## Состав

| Файл | Что это |
| --- | --- |
| [`collect-pr-costs.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/exp/ai-execution-statistics-543/collect-pr-costs.py) | сбор и разбор; все правила распознавания — именованные регулярные выражения в шапке файла |
| [`pr-cost-dataset.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/exp/ai-execution-statistics-543/pr-cost-dataset.json) | результат: агрегаты + построчные факты по каждому закрытому PR и каждой сессии |
| [`collect-pr-costs.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/hub/exp/ai-execution-statistics-543/collect-pr-costs.log) | вывод запуска, зафиксировавшего числа отчёта |

Контейнер **не копирует** тела PR и комментарии: первоисточник — GitHub, и его
дубликат в репозитории устареет молча. Хранятся только извлечённые факты.

## Воспроизведение

```bash
cd research/hub/exp/ai-execution-statistics-543
python3 collect-pr-costs.py --out pr-cost-dataset.json
```

Требуется авторизованный `gh` CLI с доступом на чтение обоих репозиториев.
Сеть используется только на чтение; скрипт ничего не пишет в GitHub.

Репозитории живые, поэтому числа отчёта — срез. Горизонт среза записан в поле
`summary.data_horizon` датасета (`latest_closed_at` = `2026-08-26T09:23:35Z`);
при расхождении с текстом отчёта доверять следует датасету.

## Границы

- Открытые PR не анализируются — контракт issue #543 ограничивает выборку
  закрытыми.
- Удалённый комментарий недоступен через API: отличить «сессии не было» от
  «лог удалён» по данным GitHub нельзя, оба случая дают «стоимость не указана».
- Причины динамики затрат здесь не разбираются — контейнер производит числа,
  интерпретация принадлежит Analysis.
