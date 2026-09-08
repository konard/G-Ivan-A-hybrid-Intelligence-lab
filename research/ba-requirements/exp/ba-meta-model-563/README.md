---
status: draft
version: 0.1
updated: 2026-09-08
temperature: 0.1
type: experiment
---

# exp: ba-meta-model-563

Evidence container для датированного замера
[`../../2026-09-08-meta-model-inputs-facts.md`](../../2026-09-08-meta-model-inputs-facts.md)
и модуля
[`research/ba-requirements/ba-meta-model/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/ba-meta-model),
issue [#563](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/563).

> **Ссылки.** Issue #563 требует абсолютных ссылок. Относительная ссылка на
> родительский отчёт выше — вынужденное исключение: её форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh).

## Что здесь измеряется

Issue #563 требует двух решений, которые нельзя принять на основании текста:
перевести режимы запуска `stepwise`, `oneshot`, `legacy` в статус
`deprecated` и синтезировать четыре канонические таксономии (артефакты,
операции, процессы, продукты). Оба решения зависят от одного вопроса: **что в
корпусе спицы действительно является идентичностью артефакта, а что —
исторической формой доставки**.

Машинно проверяемые утверждения родительского отчёта: число активных промптов и
их распределение по режимам, кратность дублирования способности по режимам,
расхождение скелетов режимных вариантов одной способности, доля промптов, ни
разу не упомянутых прогонами, покрытие словаря операций промптами, доля меток
`process:` вне словаря процессов, доля прогонов с объявленным продуктом.

Содержательной интерпретации здесь нет — она в родительском отчёте, в модуле и
в [ADR-013](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/adr/2026-09-adr-013-run-modes-deprecation.md).

## Состав

| Файл | Что это |
| --- | --- |
| [`measure-meta-model-inputs.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-meta-model-563/measure-meta-model-inputs.py) | измеритель; словари режимов, операций, процессов и доменов — именованные константы в шапке |
| [`meta-model-inputs.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-meta-model-563/meta-model-inputs.json) | результат: сводка + запись на каждую способность и каждый прогон |
| [`measure-meta-model-inputs.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-meta-model-563/measure-meta-model-inputs.log) | вывод прогона, фиксирующий опубликованные цифры и коммит корпуса |

## Воспроизведение

```bash
git clone https://github.com/G-Ivan-A/mango_ba_prompts.git /tmp/mango
python3 measure-meta-model-inputs.py --mango /tmp/mango --json meta-model-inputs.json
```

Коммит, на котором получены опубликованные цифры, записан в поле
`corpus.commit` результата: `8cbf82aa73129ec5747af07f790aaf438b0fb6e9`.
На других коммитах цифры будут другими — это ожидаемо, отчёт датирован.

## Границы измерения

- Режим определяется **суффиксом имени файла**, а не содержанием промпта.
- Скелет промпта строится только по нумерованным строкам; промпт, размеченный
  маркированным списком, измеряется как малоструктурный, что **занижает**
  совпадение вариантов.
- Ссылка прогона на промпт берётся из `related_artifacts` и является
  объявлением, а не фактом исполнения: замер доказывает отсутствие
  прослеживаемости, а не отсутствие применения.
- Лексические маркеры продуктовых доменов неразделяющие (66 прогонов из 67
  попадают более чем в один домен) и пригодны ровно для вывода «по тексту
  продукт не определяется».
