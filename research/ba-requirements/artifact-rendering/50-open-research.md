---
status: draft
version: 0.1
updated: 2026-08-26
temperature: 0.5
type: research
context: [ba, requirements, artifact-rendering, open-questions, glossary, m2, issue-545]
method: question-closure + hypothesis-ranking + source-review
scope: repo-wide
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545"
related_artifacts:
  - "research/ba-requirements/artifact-rendering/00-introduction.md"
  - "research/ba-requirements/feedback-and-evolution/00-introduction.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545"
---

# Открытые вопросы `M2`

## 1. Что модуль утверждает и чего не утверждает

**Утверждает.** Документ — производная ядра; рендер имеет пять инвариантов;
дрейф добавления и дрейф потери разрешимы машинно и полностью; навязанная форма
ограничивает поставку, но не обязательства.

**Не утверждает.** Что дрейф искажения обнаружим. Что детерминированный режим
достижим для ТЗ по ГОСТ. Что цена ведения прообразов приемлема.

## 2. Закрытие вопросов `RQ-2.1`…`RQ-2.8`

| Вопрос | Статус | Ответ | Остаток |
| --- | --- | --- | --- |
| `RQ-2.1` рендер и его инварианты | **закрыт** | определение и `RN-1`…`RN-5`, [`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-rendering/10-theory.md) | — |
| `RQ-2.2` классы документов | **закрыт** | `DC-1`…`DC-9`, [`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-rendering/20-taxonomy.md) | `DC-5` в практике не наблюдался |
| `RQ-2.3` режимы рендера | **закрыт** | `RM-1`…`RM-3`, правило `M2-R2` | достижимость `RM-1` для `tz` — `H2.2` |
| `RQ-2.4` проекции без расхождения | **закрыт** | `PJ-1`…`PJ-6`, инвариант `RN-5` | цена сверки веера не измерена |
| `RQ-2.5` машинная проверка недрейфа | **закрыт с объявленным пределом** | процедура `ND`, [`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-rendering/30-decision-framework.md) | дрейф искажения не покрыт |
| `RQ-2.6` версионирование поставки | **закрыт** | `C-OUT.version`, `RN-4`, условие `CO-9`, diff прообразов | — |
| `RQ-2.7` форма беднее ядра | **закрыт** | `M2-R5`: приложение обязательно, молчаливая свёртка запрещена | приемлемость приложения для заказчика не проверена |
| `RQ-2.8` двусторонняя проверка формы | **закрыт** | `M2-R4`: карта строится до сборки | одна эмпирическая форма |

Унаследованный `OQ-7` закрыт в §3 рамки решений: ответственность за формат
поставки при внешнем контуре несёт владелец `HG-5`.

## 3. Ранжирование гипотез

| Ранг | Гипотеза | Готовность | Чем проверять |
| --- | --- | --- | --- |
| 1 | `H2.1` весь наблюдаемый вымысел — дрейф добавления | данные есть | разметка 9 прогонов |
| 2 | `H2.5` веер содержит расхождения | данные есть | попарная сверка 23 прогонов |
| 3 | `H2.4` навязанные формы беднее ядра | частично (`RUN-0057`) | сбор ещё 5 форм |
| 4 | `H2.6` `RN-4` дешевле всех и эффективнее всех | низкая цена пилота | внедрить `Δ2.1` и замерить |
| 5 | `H2.2` `RM-1` недостижим для `tz` | требует попытки построить шаблон | 3–5 дней |
| 6 | `H2.3` гибрид выигрывает по цене/доказуемости | требует контролируемого сравнения | `M3` |

## 4. Открытые вопросы

| № | Вопрос | Кому передан |
| --- | --- | --- |
| `OQ-2.1` | Как формализовать разбиение документа на смысловые фрагменты (шаг 2 `ND`) | собственная разработка, блокирует `CO-4` |
| `OQ-2.2` | Каков словарь модальностей для русского языка требований и его полнота | `M3` (калибровка по наблюдаемым спорам) |
| `OQ-2.3` | Какова накладная стоимость ведения `preimages` | `M3` (`RQ-3.1`) |
| `OQ-2.4` | Обнаруживается ли дрейф искажения хотя бы выборочным контролем | `M3` (`RQ-3.3`) |
| `OQ-2.5` | Кто и как принимает решение при `modality_flags > 0`, если владелец `HG-5` не предметный эксперт | `M4` (`RQ-4.3`, эскалация) |
| `OQ-2.6` | Проходит ли StrictDoc ГОСТ-форму | пилот, сводно в `M4` |
| `OQ-2.7` | Приемлемо ли для заказчика приложение вместо колонки формы | `M3`, контур `external-contract` |
| `OQ-2.8` | Примет ли спица дельты `Δ2.1`…`Δ2.9` | issue в [`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts) |

## 5. Источники

**Индустриальные.** ISO/IEC/IEEE 29148:2018 (StRS/SRS/SyRS);
ISO/IEC/IEEE 15289:2019 (информационные продукты); ГОСТ 34.602-2020;
ГОСТ 34.601-90; ISO/IEC 26514 (документирование для пользователя);
BABOK Guide v3 (RADD, Solution Evaluation); Volere Template;
A. Cockburn «Writing Effective Use Cases»; OASIS DITA 1.3 (single-source
publishing, conditional processing); OMG ReqIF 1.2; OSLC RM 2.0;
StrictDoc, Doorstop, Sphinx-Needs (requirements-as-code).

**Практика (спица).**
[`docs/ba-processes/00-index.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/docs/ba-processes/00-index.md),
[`standards/bcreq-process-standard.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/bcreq-process-standard.md),
[`standards/ba-ontology.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/ba-ontology.md),
[`standards/runs-contract-standard.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/runs-contract-standard.md),
корпус `runs/` (57 прогонов, коммит `ef88a9a`).

**Хаб.**
[RFC дорожной карты](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md),
[модуль `M1`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/solution-modeling),
[отчёт замера корпуса](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md).

## 6. Глоссарий модуля

| Термин | Значение в `M2` |
| --- | --- |
| Рендер | тотальное отображение подмножества ядра в документ заданной формы |
| Прообраз (`preimage`) | элемент ядра, из которого получен фрагмент документа |
| Проекция | подача одного утверждения для конкретной формы и аудитории; собственной истинности не имеет |
| Дрейф добавления / потери / искажения | три различимых класса расхождения документа и ядра |
| Пришпиленность | наличие в документе пары `(core.id, core.version)` |
| След трассируемости (`TR-*`) | глубина машиночитаемой связи документа с ядром |
| Навязанная форма (`CF-*`) | внешняя разметка поставки, не выводимая из ядра |

## 7. Самопроверка по постановке issue #545

| Требование issue | Где выполнено |
| --- | --- |
| Полный RRP-модуль `M2` | каталог `artifact-rendering/` |
| Потребление выхода `M1` | вход `C-CORE`, условия `CC-*` проверяются на шаге 1 алгоритма §5 рамки |
| Оси `A1`–`A6` явно | `30-decision-framework.md`, §3 |
| Human Gate явно | `30-decision-framework.md`, §4 (`HG-5`, `HG-5.1`) |
| Контракты RFC | `C-CORE` на входе, `C-OUT` на выходе, инвариант `K5` — §2 рамки |
| Независимые дома | универсальная модель в `10-theory.md` §4 и `20-taxonomy.md`; практика только в матрице `40-practice-and-cases.md` §5 |
| Матрица соответствия | `40-practice-and-cases.md`, §5 |
| Методология кастомизации | `40-practice-and-cases.md`, §6 |
| Абсолютные ссылки | соблюдено, кроме объявленного исключения P2 |
