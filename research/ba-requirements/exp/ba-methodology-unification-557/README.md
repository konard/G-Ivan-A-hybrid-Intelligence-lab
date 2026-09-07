---
status: draft
version: 0.1
updated: 2026-09-07
temperature: 0.1
type: experiment
---

# exp: ba-methodology-unification-557

Evidence container для датированного замера
[`../../2026-09-07-ecosystem-knowledge-inventory.md`](../../2026-09-07-ecosystem-knowledge-inventory.md)
и модуля
[`research/ba-requirements/methodology-unification/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/methodology-unification),
issue [#557](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557).

> **Ссылки.** Issue #557 требует абсолютных ссылок на артефакты и источники.
> Относительная ссылка на родительский отчёт выше — вынужденное исключение:
> её форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh)
> (регулярное выражение требует префикса `../../` и датированного имени).

## Что здесь измеряется

ФТ-1 issue #557 требует инвентаризации и топологической Карты знаний по трём
репозиториям. Реестр, написанный руками, невоспроизводим и устаревает в момент
публикации, поэтому реестр здесь **вычисляется**: скрипт обходит три локальных
клона, классифицирует markdown-артефакты знания, читает frontmatter и строит
граф ссылок между ними.

Проверяемые машинно утверждения родительского отчёта: размер корпуса, разбивка
по репозиториям, классам и статусам, доля артефактов без frontmatter, слой
BA-релевантных документов, число рёбер графа и кросс-репозиторных ссылок,
изолированные узлы и топ входящих степеней.

Содержательной интерпретации (что означает перекос статусов, где разрывы
методологии) здесь нет — она в родительском отчёте и в модуле.

## Состав

| Файл | Что это |
| --- | --- |
| [`inventory-knowledge.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-methodology-unification-557/inventory-knowledge.py) | сканер корпуса; все правила классификации — именованные константы в шапке |
| [`knowledge-inventory.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-methodology-unification-557/knowledge-inventory.json) | результат: сводка + построчная запись на каждый артефакт с рёбрами |
| [`inventory-knowledge.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-methodology-unification-557/inventory-knowledge.log) | вывод прогона, фиксирующий цифры отчёта и коммиты трёх репозиториев |

## Воспроизведение

```bash
mkdir -p /tmp/eco && cd /tmp/eco
git clone https://github.com/G-Ivan-A/hybrid-Intelligence-lab.git
git clone https://github.com/G-Ivan-A/mango_ba_prompts.git
git clone https://github.com/G-Ivan-A/clarify-engine-ai.git
python3 inventory-knowledge.py --root /tmp/eco --out knowledge-inventory.json
```

Коммиты, на которых получены опубликованные цифры, записаны в поле `heads`
результата: `hub` `c259d61`, `mango` `8cbf82a`, `clarify` `96c288f`.
На других коммитах цифры будут другими — это ожидаемо, отчёт датирован.

## Границы измерения

- Учитываются только markdown-файлы в каталогах классов знания
  (`research/`, `docs/analysis/`, `docs/audit/`, `docs/rfc/`, `docs/adr/`,
  `standards/` и их варианты). Операционный контур `runs/`, `prompts/`,
  `patterns/`, `kb/` в корпус **не входит** — это другой класс артефактов,
  он замерен отдельно в
  [`2026-08-26-rrp-full-cycle-corpus-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-08-26-rrp-full-cycle-corpus-facts.md).
- Ребро графа — markdown-ссылка (относительная либо `github.com/G-Ivan-A/...`),
  цель которой существует в корпусе. Ссылки на внешние источники и на файлы вне
  корпуса отброшены, поэтому число рёбер — нижняя оценка связности.
- «BA-релевантность» определяется словарём ключевых слов по пути и заголовку.
  Это грубый фильтр с обеими ошибками: он не заменяет экспертную разметку и
  используется только для оценки порядка величины слоя.
