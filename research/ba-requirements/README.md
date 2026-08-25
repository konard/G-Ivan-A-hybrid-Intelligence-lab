---
status: draft
version: 0.1
updated: 2026-08-25
temperature: 0.1
---

# BA Requirements — нормализация входящих обращений

Направление исследует **вход** процессов бизнес-анализа: как обращение
произвольного качества превращается в проверяемое требование, кто участвует в
этом превращении и по каким правилам принимается решение «продукт или кастом».

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

## Датированные снимки

- [`2026-08-25-mango-runs-empirical-snapshot.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-25-mango-runs-empirical-snapshot.md)
  — снимок корпуса `runs/` репозитория `mango_ba_prompts` на 2026-08-25.
  Модуль ссылается на снимок, а не наоборот: у модуля нет единой даты, у
  измерения она есть.

## Эксперименты

- [`exp/ba-requirements-normalization-539/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-requirements-normalization-539)
  — воспроизводимый агрегатор корпуса `runs/` (issue
  [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539)).

## Политика ссылок

Все ссылки в направлении — **абсолютные** (полные URL). Требование зафиксировано
в issue [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539).
Единственное исключение — обязательные внутримодульные относительные ссылки в
`40-practice-and-cases.md`, которых требует машинная проверка правила P2
([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh));
исключение объявлено в самом файле.
