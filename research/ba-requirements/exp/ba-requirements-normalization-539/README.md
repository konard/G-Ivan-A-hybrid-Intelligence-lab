---
status: draft
version: 0.1
updated: 2026-08-25
temperature: 0.1
type: experiment
---

# exp: ba-requirements-normalization-539

Evidence container для датированного снимка
[`../../2026-08-25-mango-runs-empirical-snapshot.md`](../../2026-08-25-mango-runs-empirical-snapshot.md)
и модуля
[`research/ba-requirements/normalization/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/normalization/00-introduction.md),
issue [#539](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/539).

> **Ссылки.** Issue #539 требует абсолютных ссылок. Две относительные ссылки на
> родительский отчёт выше — вынужденное исключение: их форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh)
> (регулярное выражение требует префикса `../../`).

## Что здесь проверяется

Утверждения модуля о практике опираются на корпус прогонов
[`mango_ba_prompts/runs/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/runs).
Контейнер отвечает на формальный вопрос «что в корпусе действительно записано»:
сколько прогонов, каких типов, с какими метриками и какие понятия в них
встречаются. Содержательной оценки прогонов здесь нет — она в модуле.

Контейнер **не копирует** записи прогонов: `runs/` — операционный журнал спицы,
его SSOT остаётся в `mango_ba_prompts`. Здесь хранится только агрегат.

## Метод

`aggregate-runs.py` обходит `runs/<year>/RUN-*/metadata.yaml` и:

- читает плоский YAML (только скаляры верхнего уровня и блоки `metrics:` /
  `eval:` — в ранних прогонах метрики лежат в `eval:`); внешних зависимостей у
  скрипта нет намеренно;
- считает распределения по `run_type`, `status` и префиксу поля `process`;
- считает `n`/сумму/медиану/диапазон по десяти метрикам — медиану, а не
  среднее, потому что корпус разнороден и заполнен неравномерно;
- ищет подстроки, соответствующие граничным кейсам нормализации (`покрыт`,
  `уточнени`, `галлюцин`, `тариф`, `прав доступа`, `discoverab`, `deprecat`
  и др.) по всем `.md`/`.yaml`/`.yml` файлам прогона, а не только по метаданным;
- фиксирует `repo_sha` источника, чтобы снимок был воспроизводим.

Классификатор намеренно формальный: если бы он относил прогон к типу входа «по
смыслу», таксономия модуля доказывалась бы собственной разметкой.

## Результаты

Снимок на `mango_ba_prompts@524a8eb`: 56 прогонов, 2026-04-10 … 2026-08-25.
Полный вывод — [`runs-aggregate.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-requirements-normalization-539/runs-aggregate.json),
лог прогона — [`aggregate-runs.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-requirements-normalization-539/aggregate-runs.log).
Таблицы и ограничения замера — в датированном снимке.

Два результата, определяющие выводы модуля:

1. `hallucinations_shipped > 0` в **9** прогонах — человеческий контроль
   пропускает вымысел в артефакт, то есть гейт нельзя считать надёжным по
   умолчанию;
2. **0 прогонов** упоминают устаревание контекста (`deprecat`, «вывод из
   эксплуатации») — граничный кейс «устаревший контекст» эмпирически **не
   подтверждён** и заявлен в модуле как гипотеза, а не как наблюдение.

## Воспроизведение

```bash
git clone https://github.com/G-Ivan-A/mango_ba_prompts /tmp/mango
python3 research/ba-requirements/exp/ba-requirements-normalization-539/aggregate-runs.py \
  --mango-root /tmp/mango \
  --out research/ba-requirements/exp/ba-requirements-normalization-539/runs-aggregate.json
```

Сети скрипт не требует (кроме клонирования источника). На более поздних
коммитах `mango_ba_prompts` числа изменятся вместе с корпусом — это ожидаемо,
снимок датирован полем `repo_sha` внутри JSON.
