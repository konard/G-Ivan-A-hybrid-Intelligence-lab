---
status: draft
version: 0.1
updated: 2026-08-25
temperature: 0.1
type: research
context: [ba, requirements, mango, runs, empirical-snapshot, metrics]
method: corpus-measurement + formal-metadata-aggregation
scope: mango-only
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539"
based_on:
  - research/ba-requirements/exp/ba-requirements-normalization-539/runs-aggregate.json
related_artifacts:
  - "research/ba-requirements/normalization/00-introduction.md"
  - "research/ba-requirements/normalization/40-practice-and-cases.md"
  - "research/ba-requirements/exp/ba-requirements-normalization-539/README.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539"
---

# Снимок корпуса прогонов `mango_ba_prompts/runs/` на 2026-08-25

> **Назначение.** Это датированное **измерение**, а не исследование. Все
> интерпретации, таксономии и решения вынесены в модуль
> [`research/ba-requirements/normalization/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/normalization/00-introduction.md).
> Снимок существует отдельно, потому что у модуля нет единой даты (файлы
> обновляются на разных циклах), а у измерения она есть: корпус растёт, и через
> месяц числа будут другими.

## 1. Что измерено

Источник — каталог `runs/` репозитория
[`G-Ivan-A/mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/runs)
на коммите `524a8eb`. Агрегатор:
[`exp/ba-requirements-normalization-539/aggregate-runs.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-requirements-normalization-539/aggregate-runs.py).
Скрипт читает только `metadata.yaml` и текстовые файлы прогона; содержательной
классификации в нём нет — иначе вывод исследования был бы предрешён разметкой.

## 2. Состав корпуса

| Показатель | Значение |
| --- | --- |
| Прогонов | 56 |
| Период | 2026-04-10 … 2026-08-25 |
| `run_type` | `statistics` 47, `execution` 9 |
| `status` | `draft` 29, `works-with-edits` 19, `partial-success` 5, `success` 1, `needs-rework` 1, `experimental` 1 |

Распределение по префиксу процесса (первый сегмент поля `process`):

| Префикс | Прогонов | Что это на входе |
| --- | --- | --- |
| `task-` | 32 | задача с трекера/чата — уже упакованное обращение |
| `fr-` | 9 | работа с функциональными требованиями (анализ, драфт, валидация) |
| `bcreq-` | 4 | бизнес-обращение заказчика (business change request) |
| `prompt-` | 3 | работа над самими промптами, а не над требованием |
| `tz-`, `usecase-`, `user-`, `gap-`, `kb-`, `industry-`, `session-`, `multichannel-` | по 1 | единичные типы |

**Наблюдение.** 32 из 56 прогонов начинаются с `task-`, то есть с артефакта,
который уже прошёл чью-то нормализацию. Исходное обращение в корпусе
представлено слабо (4 `bcreq-`): наблюдаемость **самого раннего** участка входа
— пробел данных, а не свойство процесса.

## 3. Метрики прогонов

Числа даны как `n` (сколько прогонов имеют метрику) / медиана / диапазон, потому
что метрики заполнены неравномерно и среднее по разнородному корпусу вводит в
заблуждение.

| Метрика | n | Сумма | Медиана | Диапазон |
| --- | --- | --- | --- | --- |
| `episodes` | 41 | 1080 | 15 | 1 … 83 |
| `iterations` | 37 | 1052 | 19 | 1 … 83 |
| `turns` | 34 | 2084 | 44 | 2 … 166 |
| `success_rate` | 18 | — | 0.60 | 0.25 … 0.92 |
| `hallucinations` | 11 | 41 | 3 | 2 … 8 |
| `hallucinations_shipped` | 11 | 12 | 1 | 0 … 3 |
| `ba_edits` | 10 | 53 | 6 | 0 … 11 |
| `quality` | 11 | 31 | 3 | 2 … 3 |
| `tokens_dialog_total` | 32 | 61 360 738 | 720 806 | 3 387 … 9 225 333 |
| `duration_wall_clock_s` | 11 | 1 331 029 | 45 675 | 2 762 … 522 867 |

Прогоны, где хотя бы одна галлюцинация дошла до артефакта
(`hallucinations_shipped > 0`): **9** — RUN-0016, RUN-0018, RUN-0021, RUN-0022,
RUN-0024, RUN-0025, RUN-0026, RUN-0027, RUN-0028.

## 4. Покрытие ключевых понятий по корпусу

Подстрочный поиск по всем `.md`/`.yaml` файлам прогонов (регистр не учитывается):

| Понятие | Подстрока | Прогонов из 56 |
| --- | --- | --- |
| Оценка покрытия | `покрыт` | 41 |
| Уточняющие вопросы | `уточнени` | 23 |
| Галлюцинации | `галлюцин` | 20 |
| Домысливание | `домысл` | 11 |
| Кастом-разработка | `кастом` | 10 |
| Тарифная привязка | `тариф` | 7 |
| Права доступа | `прав доступа` | 5 |
| «Уже реализовано» | `уже реализован` | 3 |
| Discoverability | `discoverab` | **0** |
| Устаревание/вывод из эксплуатации | `deprecat`, `вывод из эксплуатации` | **0** |

## 5. Ограничения измерения

1. **Разнородная схема метрик.** Галлюцинации записаны тремя разными ключами:
   `hallucinations` (11 прогонов), `hallucinations_found` (3),
   `hallucinations_prevented` (3). Ранние прогоны (RUN-0017, RUN-0020, RUN-0023)
   держат метрики в блоке `eval:`, поздние — в `metrics:`. Агрегатор объединяет
   оба блока, но **не** склеивает разноимённые ключи: сумма по `hallucinations`
   является нижней границей.
2. **`success_rate` несопоставим между прогонами.** Поле
   `success_rate_basis` в RUN-0023 прямо предупреждает: шкала «принято
   человеком» там неприменима, и «прямое сравнение с `success_rate` прогонов,
   считанных по принятию человеком (например RUN-0020), некорректно».
   Медиана 0.60 описывает корпус, а не качество процесса.
3. **Заполненность метрик — от 10 до 41 прогона из 56.** Отсутствие метрики
   чаще означает «не измеряли», а не «ноль».
4. **Ключевые слова не равны явлениям.** Ноль по `deprecat` означает, что тема
   устаревания контекста в корпусе **не обсуждается**; из этого не следует, что
   явления нет — следует, что его не фиксируют.
5. **Снимок датирован.** На более поздних коммитах `mango_ba_prompts` числа
   изменятся; воспроизводимость обеспечена полем `repo_sha` в
   [`runs-aggregate.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-requirements-normalization-539/runs-aggregate.json).
