---
status: draft
version: 0.2
updated: 2026-08-26
temperature: 0.1
---

# BA Requirements — конвейер артефактов бизнес-анализа

Направление исследует **полный конвейер** артефактов бизнес-анализа: как
обращение произвольного качества превращается в проверяемое требование (`M0`),
как требования собираются в согласованное ядро (`M1`), как ядро разворачивается
в целевые документы без потери смысла (`M2`), как результат замыкается обратной
связью (`M3`) и как всё это маршрутизируется между людьми и агентами (`M4`).
Декомпозиция задана
[RFC дорожной карты](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md).

Направление намеренно отделено от [`research/mango/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/mango):
там лежат датированные отчёты по конкретным задачам спицы MANGO OFFICE, здесь —
переносимая рамка, у которой Mango является одним (первым) применением.

## Модули

- [`normalization/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/normalization/00-introduction.md)
  — таксономия нормализации требований: терминология входного артефакта,
  универсальная и Mango-специализированная таксономии, матрица корреляции,
  рамка принятия решений, три гипотезы реализации, граничные кейсы.
  Оформлен по [Reference Research Pattern](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-07-17-rfc-reference-research-pattern.md)
  (`00…50`).
- [`solution-modeling/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/solution-modeling/00-introduction.md)
  — модуль `M1`: ядро требований. Инварианты `INV-1`…`INV-9`, классы моделей
  `MO-1`…`MO-12`, типы элементов `EL-1`…`EL-8`, контракт `C-CORE` и гейты
  `HG-3`/`HG-4`.
- [`artifact-rendering/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-rendering/00-introduction.md)
  — модуль `M2`: рендер ядра в целевые документы. Инварианты рендера
  `RN-1`…`RN-5`, классы документов `DC-1`…`DC-9`, процедура контроля недрейфа
  `ND`, контракт `C-OUT` и гейты `HG-5`/`HG-5.1`.
- [`feedback-and-evolution/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/feedback-and-evolution/00-introduction.md)
  — модуль `M3`: обратная связь, статистика решений и эволюция требований.
  Инварианты замыкания `CL-1`…`CL-6`, словарь метрик `MK-*`, контракт `C-CL`
  и гейты `HG-6`/`HG-7`.
- [`orchestration/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/orchestration/00-introduction.md)
  — сквозной модуль `M4`: маршрутизация, роли, прерывания и человеческие гейты.
  Инварианты маршрута `RT-1`…`RT-7`, типовые маршруты `RT-A`…`RT-F`, контракт
  `C-RK`, гейты `HG-0` и `HG-8`, сводный build-vs-buy по всему конвейеру.

## Датированные снимки

- [`2026-08-26-rrp-full-cycle-corpus-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md)
  — общая доказательная база модулей `M1`–`M4`: замер корпуса `runs/` на
  коммите `ef88a9a` (57 прогонов). Все четыре модуля ссылаются на один замер,
  а не выдвигают независимые утверждения о практике.
- [`2026-08-25-mango-runs-empirical-snapshot.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-25-mango-runs-empirical-snapshot.md)
  — снимок корпуса `runs/` репозитория `mango_ba_prompts` на 2026-08-25.
  Модуль ссылается на снимок, а не наоборот: у модуля нет единой даты, у
  измерения она есть.

## Эксперименты

- [`exp/ba-requirements-normalization-539/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-requirements-normalization-539)
  — воспроизводимый агрегатор корпуса `runs/` (issue
  [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539)).
- [`exp/ba-rrp-full-cycle-545/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-rrp-full-cycle-545)
  — воспроизводимый замер корпуса для модулей `M1`–`M4` (issue
  [#545](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545)).

## Политика ссылок

Все ссылки в направлении — **абсолютные** (полные URL). Требование зафиксировано
в issue [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539).
Единственное исключение — обязательные внутримодульные относительные ссылки в
`40-practice-and-cases.md`, которых требует машинная проверка правила P2
([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh));
исключение объявлено в самом файле.
