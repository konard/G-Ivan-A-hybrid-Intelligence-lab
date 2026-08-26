---
status: draft
version: 0.1
updated: 2026-08-26
temperature: 0.7
type: research
context: [ba, requirements, solution-modeling, core, m1, introduction, reading-map, mango, issue-545]
method: literature-survey + standards-analysis + taxonomy-building + corpus-measurement + contract-design
scope: repo-wide
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545"
based_on:
  - research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md
  - research/ba-requirements/2026-08-25-mango-runs-empirical-snapshot.md
  - research/ba-requirements/normalization/30-decision-framework.md
related_artifacts:
  - "research/ba-requirements/solution-modeling/10-theory.md"
  - "research/ba-requirements/solution-modeling/20-taxonomy.md"
  - "research/ba-requirements/solution-modeling/30-decision-framework.md"
  - "research/ba-requirements/solution-modeling/40-practice-and-cases.md"
  - "research/ba-requirements/solution-modeling/50-open-research.md"
  - "docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/541"
---

# Моделирование решений и ядро требований (`M1`): введение и карта чтения

> **Модуль.** Это файл `00-introduction.md` модуля
> [`research/ba-requirements/solution-modeling/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/solution-modeling),
> оформленного по **Reference Research Pattern** (статус паттерна: Experimental,
> см. [RFC: Reference Research Pattern](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-07-17-rfc-reference-research-pattern.md)
> и [`standards/research-standard.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/research-standard.md)).
> Модуль открыт решением по
> [issue #545](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545)
> после перевода
> [RFC дорожной карты](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md)
> в статус `accepted`.
>
> **Принцип независимых домов.** Индустриальная практика (BABOK, IREB CPRE,
> ISO/IEC/IEEE 29148, ГОСТ 34.602-2020) моделируется здесь **как универсальная
> база с максимальной полнотой** и не подрезается под текущие возможности
> [`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts). Практика
> Mango используется **только** для матрицы соответствия
> ([§5 файла 40-practice-and-cases.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/40-practice-and-cases.md#5-матрица-соответствия-mango--индустрия))
> и для вывода методологии кастомизации.
>
> **Политика ссылок.** Все ссылки модуля — абсолютные (требование issue #545).
> Единственное исключение объявлено в
> [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/40-practice-and-cases.md):
> там относительные внутримодульные ссылки обязательны по машинной проверке
> правила P2
> ([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh)).
>
> **Статус.** `draft`. Модуль ничего не отменяет и ни один действующий стандарт
> — ни Хаба, ни спицы — не переписывает (правило `P.8` RFC).

## BLUF

1. **Ядро требований — это объект, а не стадия.** `M1` производит контракт
   `C-CORE`: согласованное, версионированное, адресуемое множество утверждений
   о решении, из которого затем **порождаются** любые целевые документы.
   Определение объекта и его инварианты —
   [§2 файла 10-theory.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/10-theory.md#2-ядро-требований-как-объект).
2. **В практике такого объекта нет.** Замер 57 прогонов: процесс-маркер
   моделирования встречается в 2 прогонах из 57, при этом 40 % прогонов выдают
   более одного документа — то есть веер выходов уже строится, но **из
   контекста диалога, а не из зафиксированного ядра**
   ([отчёт замера, §3](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md#3-факты-под-m1-ядро-и-моделирование)).
   Это и есть корневая причина недрейфа, который `M2` потом вынужден ловить
   постфактум.
3. **Моделирование решений ≠ документирование решений.** Индустрия разводит
   пространство проблемы и пространство решения (BABOK Strategy Analysis vs
   RADD; ISO/IEC/IEEE 29148 StRS vs SyRS/SRS). Разбор —
   [§1 файла 10-theory.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/10-theory.md#1-conceptual-framing-что-такое-моделирование-решения).
4. **Приоритет `M1` — читаемость ядра разными типами акторов**, а не строгость
   формы: строгость — параметр `M2`. Из этого следует таксономия аудиторий
   ядра и правило «одно утверждение — много проекций»
   ([§4 файла 20-taxonomy.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/20-taxonomy.md#4-таксономия-d--аудитории-ядра)).
5. **Двенадцать классов моделей, а не «UML или BPMN»**. Таксономия моделей
   строится от вопроса, на который модель отвечает (цель, процесс, сценарий,
   данные, состояние, правило, интерфейс, ограничение, риск, вариант, объём,
   трассировка), а не от нотации —
   [§1 файла 20-taxonomy.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/20-taxonomy.md#1-таксономия-a--классы-моделей-решения-mo-1mo-12).
6. **Владелец `HG-4` определяется осью `A6`** (ответ на `Q-4` RFC, вариант
   «в»): `internal` — БА, `external-contract`/`regulated` — руководитель
   направления. Обоснование через необратимость —
   [§3 файла 30-decision-framework.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/30-decision-framework.md#3-гейты-m1-hg-0-hg-2-hg-3-hg-4).
7. **Build-vs-buy: ядро не пишется с нуля.** Скрининг показывает, что
   requirements-as-code инструменты (StrictDoc, Doorstop, Sphinx-Needs) уже
   реализуют адресуемость, версионирование и трассировку `C-CORE`, а обмен —
   ReqIF; собственной разработке остаются только связь с моделями и
   мультиаудиторные проекции
   ([§6 файла 30-decision-framework.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/30-decision-framework.md#6-build-vs-buy-screening)).
8. **Mango покрывает 6 из 12 классов моделей и 4 из 9 инвариантов ядра.**
   Матрица соответствия и дельты кастомизации —
   [§5](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/40-practice-and-cases.md#5-матрица-соответствия-mango--индустрия)
   и [§6 файла 40-practice-and-cases.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/40-practice-and-cases.md#6-методология-кастомизации-дельты-для-спицы).

## Карта чтения

| Файл | Что внутри | Кому в первую очередь |
| --- | --- | --- |
| [`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/10-theory.md) | что такое моделирование решения; ядро как объект и девять его инвариантов; индустриальные основания; терминологическое решение `T2`; гипотезы `H1.1`–`H1.9` | методологу, автору стандартов |
| [`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/20-taxonomy.md) | 12 классов моделей; 8 типов элементов ядра; уровни строгости ядра; аудитории ядра; таксономия неопределённости | аналитику, проектирующему процесс |
| [`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/30-decision-framework.md) | схема контракта `C-CORE`; применение осей `A1`–`A6`; гейты `HG-0`…`HG-4`; правила выбора моделей; build-vs-buy | владельцу процесса, принимающему решения |
| [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/40-practice-and-cases.md) | корпус, пять граничных кейсов, матрица соответствия Mango ↔ индустрия, дельты кастомизации | БА и разработчику промптов |
| [`50-open-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/50-open-research.md) | источники, закрытие `RQ-1.1`–`RQ-1.7`, открытые вопросы, глоссарий, самопроверка против контракта issue #545 | ревьюеру |

## 1. Проблема

Конвейер артефактов БА в текущей практике устроен так, что **документ является
и результатом, и носителем смысла одновременно**. Требование существует только
внутри ФТ или ТЗ; вне документа его нет. Из этого следуют три наблюдаемых
эффекта.

**Эффект 1 — дрейф между документами.** Если один и тот же смысл нужно выдать
в двух формах (например, ФТ для команды и раздел ТЗ для договора), он пишется
дважды. Второй экземпляр расходится с первым не по злому умыслу, а потому что
у них нет общего источника. Замер показал: 23 прогона из 57 (40,4 %) выдают
более одного документа, и ни в одном из них нет объявленного общего основания.

**Эффект 2 — согласование не имеет предмета.** Заказчик согласует документ
целиком, потому что согласовать «утверждение №14» невозможно — у утверждения
нет идентификатора. Отсюда согласование становится бинарным и необратимым:
любое возражение откатывает документ целиком.

**Эффект 3 — модель сценария теряется.** User Story и Use Case строятся, дают
эффект (находят граничные случаи) и исчезают, потому что их некуда положить:
они не документ-результат и не часть ФТ. Правило `F2` RFC называет US/UC
инструментом стресс-теста, но инструмент без места хранения не даёт
накопления.

`M1` отвечает на вопрос: **какой объект должен появиться между нормализованным
входом (`C-IA`) и порождением документов (`C-OUT`), чтобы эти три эффекта
исчезли по построению, а не по дисциплине исполнителя.**

## 2. Границы исследования

**В границах.**

- Модель объекта «ядро требований» (`C-CORE`): состав, инварианты, схема,
  жизненный цикл, правила версионирования и адресации.
- Классы моделей решения и правила выбора модели по типу неопределённости.
- Применение осей `A1`–`A6` к слою `M1` и правила совместимости, влияющие на
  состав ядра.
- Гейты `HG-0`, `HG-2`, `HG-3`, `HG-4` с машинно-проверяемыми предусловиями.
- Скрининг готовых решений индустрии под задачи `M1`.
- Матрица соответствия «процессы Mango → индустриальные процессы» в части
  моделирования и формирования ядра.

**Вне границ.**

- Порождение документов из ядра, форматы, строгость, проверка недрейфа — это
  [`artifact-rendering/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/artifact-rendering)
  (`M2`).
- Статистика решений, калибровка гейтов, эволюция — это
  [`feedback-and-evolution/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/feedback-and-evolution)
  (`M3`).
- Маршрутизация, режим исполнения, оркестратор — это
  [`orchestration/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/orchestration)
  (`M4`).
- Нормализация входа — выполненный модуль
  [`normalization/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/normalization)
  (`M0`).
- Правка стандартов спицы: `M1` формулирует предложение, но не редактирует
  [`standards/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/standards)
  Mango (правило `P.8` RFC).

## 3. Вопросы исследования

Модуль обязан закрыть семь вопросов, поставленных RFC (`P.1.2`). Ответы
собраны в
[§2 файла 50-open-research.md](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/50-open-research.md#2-закрытие-вопросов-rq-11rq-17).

| № | Вопрос |
| --- | --- |
| `RQ-1.1` | Что такое ядро требований как объект: минимальный состав, гранулярность, идентификация, версионирование? |
| `RQ-1.2` | Какие классы моделей решения существуют и как выбирается класс под тип неопределённости? |
| `RQ-1.3` | Как обеспечивается читаемость одного и того же ядра разными типами акторов без дублирования смысла? |
| `RQ-1.4` | Где проходит граница между «требование зафиксировано» и «решение спроектировано»? |
| `RQ-1.5` | Как устроено согласование ядра, чтобы возражение к одному утверждению не откатывало всё? |
| `RQ-1.6` | Какие предусловия гейтов `HG-2`, `HG-3`, `HG-4` проверяемы машиной? |
| `RQ-1.7` | Какие готовые решения индустрии закрывают задачи `M1` и что остаётся собственной разработке? |

Дополнительно модуль наследует из `M0` открытые вопросы `OQ-1` (гранулярность
инициирующего артефакта) и `OQ-4` (сцепка `domain → capability → feature →
function`) — таблица `P.1.7` RFC.

## 4. Метод

1. **Анализ стандартов.** Первичные рамки — BABOK v3 (Strategy Analysis,
   Requirements Analysis and Design Definition, Requirements Life Cycle
   Management), IREB CPRE Foundation/Advanced (Requirements Modelling),
   ISO/IEC/IEEE 29148:2018 (StRS/SyRS/SRS, характеристики требований),
   ГОСТ 34.602-2020 (структура ТЗ на АС), ISO/IEC 25010 (модель качества).
   Полнота модели задаётся стандартами, а не наличием реализации.
2. **Построение таксономий от вопроса, а не от нотации.** Класс модели
   определяется вопросом, на который модель отвечает; нотация — атрибут.
3. **Замер корпуса.** Утверждения о практике проверяются на 57 прогонах
   контейнером
   [`exp/ba-rrp-full-cycle-545/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-rrp-full-cycle-545).
4. **Контракт-первый дизайн.** Схема `C-CORE` формулируется так, чтобы её
   можно было проверить машиной, а не глазами.
5. **Матрица соответствия, а не подрезка.** Практика Mango сравнивается с
   универсальной моделью **после** её построения; расхождения фиксируются как
   дельты кастомизации, а не как основание сузить модель.

## 5. Ограничения и честные пробелы

1. **Ни один инвариант ядра не проверен на потоке задач.** Девять инвариантов
   `INV-1`…`INV-9` выведены из стандартов и корпуса, но не испытаны на живом
   процессе. Это `OQ-1.3`.
2. **Корпус — одна компания и предпроектный контур.** Ни один прогон не довёл
   документ до договорного baseline, поэтому утверждения о поведении ядра
   после подписания договора — экстраполяция.
3. **Скрининг инструментов выполнен по документации, а не по эксплуатации.**
   Ни StrictDoc, ни Doorstop, ни Sphinx-Needs не разворачивались; выводы
   `§6` файла `30-*.md` — screening, а не выбор.
4. **Стоимость не измерена.** Сколько стоит поддержание ядра отдельно от
   документов — открытый вопрос, переданный в `M3` (`RQ-3.4`).
5. **Аудитории ядра выведены аналитически.** Пять типов акторов не
   валидированы интервью; единственное эмпирическое подтверждение — уровневый
   веер `L0`–`L4` в двух прогонах из 57.
