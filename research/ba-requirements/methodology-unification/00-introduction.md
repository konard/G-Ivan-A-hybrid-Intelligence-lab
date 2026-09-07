---
status: draft
version: 0.1
updated: 2026-09-07
temperature: 0.3
type: research
context: [ba, methodology, governance, execution, skills, gates, knowledge-map, roadmap, issue-557]
method: corpus-measurement + inheritance-modeling + gap-analysis + case-modeling
scope: ecosystem
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557"
based_on:
  - research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md
  - research/ba-requirements/exp/ba-methodology-unification-557/knowledge-inventory.json
related_artifacts:
  - "docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md"
  - "docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md"
  - "docs/rfc/2026-07-17-rfc-reference-research-pattern.md"
  - "pr-ops/backlog.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557"
---

# Единая методология БА под ИИ-агентов: аудит, картография, рамка, роадмап

> **Модуль** оформлен по
> [Reference Research Pattern](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-07-17-rfc-reference-research-pattern.md):
> `00` — рамка и навигация, `10` — теория (двухуровневая модель), `20` —
> таксономии и картография, `30` — рамка принятия решений и разрывы, `40` —
> практика и кейсы, `50` — открытые вопросы и роадмап.
> **Ссылки абсолютные** (НФТ-2 issue #557). Единственное исключение — ссылки на
> файлы этого же модуля в
> [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/40-practice-and-cases.md):
> правило `P2` требует относительной ссылки внутри модуля и проверяется машинно
> ([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh)).

## BLUF: десять утверждений

1. **Единой методологии БА в экосистеме сегодня нет** — есть 368 артефактов
   знания, из которых нормативный статус имеют 13 %, а предметное ядро БА
   (онтология, таксономия операций, процесс BCREQ) целиком лежит в спице
   [`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts) со
   статусом `draft`. Замер:
   [`2026-09-07-ecosystem-knowledge-inventory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md).
2. **Форма знания нормирована, содержание — нет.** 13 из 15 центров притяжения
   графа нормируют оформление (глоссарий, именование, frontmatter, структура
   ADR). BA-релевантен 1 стандарт Хаба из 26.
3. **Наследование методологии сегодня направлено вверх, а не вниз.** Mango
   ссылается на Хаб 81 раз, Хаб на Mango — 31. Спица наследует *форму* от Хаба,
   но *предметную норму* производит сама, и Хаб её не переиспользует.
4. **`clarify-engine-ai` выпал из методологического контура полностью:** 1
   входящее ребро, 0 исходящих, 53 артефакта без frontmatter.
5. **Артефакта, решающего задачу картографии текущего состояния, в экосистеме
   нет.** Ближайший кандидат —
   [RFC конвейера артефактов БА](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md)
   — описывает целевой конвейер `M0`–`M4`, но не описывает **где мы сейчас**;
   разбор — в [`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/20-taxonomy.md), §1.
6. **Предлагается двухуровневая рамка.** Governance-уровень хранит методологию
   как **наследование дельт**: индустриальный стандарт → дельта отрасли
   ИТ-Телеком → дельта команды КК Манго. Execution-уровень хранит **разрешённый**
   (скомпилированный) артефакт — `SKILL.md`, в котором дельты уже сведены.
7. **Агент никогда не вычисляет дельту в рантайме.** Разрешение дельт — шаг
   сборки с человеческим гейтом, а не шаг рассуждения. Обоснование и инварианты —
   [`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/10-theory.md).
8. **Ответ на вопрос фаундера о гейтах: ни то, ни другое в чистом виде.**
   Субагент исполняет навык с ИИ-self-check, но self-check закрывает только
   класс формальных дефектов; необратимые решения остаются за человеком.
   Эмпирика Mango: из 67 прогонов безоговорочный `success` — 2; в прогоне
   RUN-0018 восемь шагов самопроверки не удержали один фактологический дефект,
   дошедший до финального документа. Решение — в
   [`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/30-decision-framework.md).
9. **Ось «Среда» и ось «Методология» ортогональны и обе нужны.**
   [RFC оси «Среда»](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md)
   отвечает «кто исполняет репозиторий», настоящее исследование — «какое
   предметное знание исполняется». Формула композиции расширяется четвёртым
   слагаемым, а не переписывается.
10. **Роадмап каскада — 13 задач `B-121`…`B-133`** в трёх этапах с двумя
    человеческими гейтами; зарегистрированы в
    [`pr-ops/backlog.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/pr-ops/backlog.md),
    обоснование — в
    [`50-open-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/50-open-research.md).
    **Мерж PR по issue #557 = утверждение роадмапа** (условие фаундера).

## Формат исследования и его обоснование

Issue #557 требует «предложить формат исследования (например, RRP)». Выбор
сделан явно, с отклонёнными альтернативами.

| Формат | Что даёт | Почему отклонён / принят |
| --- | --- | --- |
| `M1` — датированный отчёт | Простота, одна дата | Отклонён как основной: задача ставит четыре разнородных ФТ (реестр, рамка, моделирование, роадмап), которые живут разными скоростями. Один файл потребовал бы полной перезаписи при устаревании любой части. |
| `M3` — discussion paper | Свобода изложения | Отклонён: результат обязан стать основанием для 13 каскадных задач, а discussion paper не имеет контракта разделов и не проверяется машинно. |
| **`M2` — Reference Research Pattern** | Шесть файлов с разделением «теория / таксономия / решения / практика / открытое» | **Принят.** Совпадение с ФТ буквальное: ФТ-2 → `10`, ФТ-1 → `20`, гейты и разрывы → `30`, ФТ-3 → `40`, ФТ-4 → `50`. Пять модулей `research/ba-requirements/` уже в этом формате — новый модуль встаёт в ряд, а не рядом. |
| `M2` + датированный снимок | Отделение измеряемого от рассуждаемого | **Принят дополнительно.** У корпуса есть коммит и дата, у рамки — нет. Замер вынесен в [отдельный датированный отчёт](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-07-ecosystem-knowledge-inventory.md), как это уже сделано для модулей `M1`–`M4`. |

Дом артефакта — `research/`, а не `docs/analysis/`: работа производит
**переносимую рамку** (методология БА, не привязанная к одной задаче), а не
разбор конкретного случая. Маршрут задан
[ADR-003](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/adr/2026-07-adr-003-research-structure.md)
и [`standards/research-standard.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/standards/research-standard.md).

## Как читать модуль

| Роль | Минимальный маршрут |
| --- | --- |
| Фаундер (решения) | `00` BLUF → [`30`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/30-decision-framework.md) матрица покрытия и решение по гейтам → [`50`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/50-open-research.md) роадмап и вопросы |
| БА-практик | [`40`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/40-practice-and-cases.md) кейсы и жизненный цикл навыка → [`20`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/20-taxonomy.md) таксономии |
| Архитектор методологии | [`10`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/10-theory.md) целиком → `30` |
| Исполнитель каскадной задачи | `50` (карточка задачи) → `30` (разрыв, который она закрывает) |

## Периметр

**В периметре.** Три репозитория из постановки; методология БА как предметная
дисциплина; governance- и execution-уровни; модель навыков и гейтов; каскад
задач.

**Вне периметра.** (1) Состав среды «VPS/Serverless» — рабочее имя, композиция
отнесена к
[RFC оси «Среда»](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-09-04-rfc-bootstrap-environment-and-structure.md)
(Трек Б, PR [#556](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/pull/556)),
здесь среда используется только как одна из трёх точек исполнения.
(2) Переписывание принятых `M0`–`M4`: модуль их **позиционирует**, а не
заменяет. (3) Написание самих `SKILL.md` — это задачи каскада, не этой работы.
(4) Репозитории вне трёх названных.

## Статус и опровержимость

Статус `draft`. Модуль содержит шесть гипотез `H-1`…`H-6`
([`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/10-theory.md), §6),
у каждой назван критерий опровержения и задача каскада, которая его проверяет.
Утверждения о корпусе воспроизводимы скриптом; утверждения о среде GigaCode
помечены как допущения — проверенной документации у исполнителя нет
(см. [`50-open-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/50-open-research.md),
раздел «Не выполнено и вопросы»).
