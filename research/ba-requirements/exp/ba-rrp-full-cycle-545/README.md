---
status: draft
version: 0.1
updated: 2026-08-26
temperature: 0.1
type: experiment
---

# exp: ba-rrp-full-cycle-545

Evidence container для отчёта
[`../../2026-08-26-rrp-full-cycle-corpus-facts.md`](../../2026-08-26-rrp-full-cycle-corpus-facts.md)
и четырёх RRP-модулей конвейера артефактов БА (`M1`–`M4`), открытых по
issue [#545](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/545)
после принятия
[RFC дорожной карты](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md).

> **Ссылки.** Issue #545 требует абсолютных ссылок. Относительная ссылка на
> родительский отчёт выше — вынужденное исключение: её форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh)
> (регулярное выражение требует префикса `../../`).

## Что здесь проверяется

Модули `M1`–`M4` формулируют утверждения о том, чего в практике **нет**:
единой схемы записи о закрытии (`C-CL`), объявленного маршрутного листа
(`C-RK`), отделённого ядра требований (`C-CORE`) и наблюдаемой стоимости
прогона. Такие утверждения дёшево постулировать и дорого проверять, поэтому
контейнер отвечает на них механически: измеряет корпус прогонов
[`mango_ba_prompts`](https://github.com/G-Ivan-A/mango_ba_prompts) и выдаёт
факты, которые можно опровергнуть повторным запуском.

Проверяемые вопросы:

1. **`M1`.** Сколько прогонов формируют ядро требований и сколько — модели
   сценариев (US/UC), то есть насколько ядро отделено от рендера в практике.
2. **`M2`.** Какая доля прогонов выдаёт более одного документа из одного
   основания и в скольких прогонах есть уровневый веер по аудиториям.
3. **`M3`.** Сколько прогонов имеют вердикт, `success_rate`, `eval`,
   объявленную достоверность (`measured`) и связь с другими прогонами.
4. **`M4`.** Сколько различных ключей метрик встречается в корпусе — прямая
   мера отсутствия схемы, из которой мог бы работать маршрутизатор.

Содержательной интерпретации здесь нет: она в родительском отчёте и в разделах
`40-practice-and-cases.md` каждого модуля.

## Состав

| Файл | Что это |
| --- | --- |
| [`measure-pipeline.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-rrp-full-cycle-545/measure-pipeline.py) | замерщик корпуса; все правила разметки — именованные константы в шапке |
| [`pipeline-facts.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-rrp-full-cycle-545/pipeline-facts.json) | результат: сводка `summary` + построчные факты по каждому прогону |
| [`measure-pipeline.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-rrp-full-cycle-545/measure-pipeline.log) | вывод запуска, зафиксировавшего числа отчёта |

Контейнер **не копирует** записи прогонов:
[`runs/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/runs) —
операционный журнал спицы, и его дубликат в Хабе устареет молча.

## Воспроизведение

```bash
git clone --depth=1 https://github.com/G-Ivan-A/mango_ba_prompts /tmp/mango
python3 research/ba-requirements/exp/ba-rrp-full-cycle-545/measure-pipeline.py \
  --mango-root /tmp/mango \
  --commit "$(git -C /tmp/mango rev-parse --short HEAD)" \
  --out research/ba-requirements/exp/ba-rrp-full-cycle-545/pipeline-facts.json
```

Числа сняты на коммите `ef88a9a` репозитория `mango_ba_prompts` (57 прогонов).
Корпус растёт: при расхождении доверять следует полю `summary.mango_commit`
файла `pipeline-facts.json`, а не тексту отчёта.

## Границы

1. **Разметка ключевая, а не семантическая.** Принадлежность прогона к
   моделированию (`MODELING_MARKERS`) и к ядру (`CORE_MARKERS`) определяется по
   подстрокам в имени процесса. Следствие названо явно: прогон, смоделировавший
   сценарии внутри процесса с другим именем, в счёт `m1_modeling_runs` не
   попадёт — поэтому цифра 2 из 57 читается как «моделирование почти никогда не
   является самостоятельным процессом», а не как «сценарии не строятся».
2. **Документом считается `.md`-файл в `outputs/`, кроме `README`.** Документ,
   выданный вложением или ссылкой, не виден замеру.
3. **`metrics` парсится как плоский блок скаляров.** Вложенные структуры внутри
   `metrics` были бы пропущены; на текущем корпусе таких нет — проверено ручной
   сверкой ключей `m4_metric_key_frequency` с исходными файлами.
4. **Корпус — предпроектный и оценочный контур.** Ни один прогон не доставил
   договорное ТЗ до baseline (замер issue #541), поэтому все выводы о `M2` и
   `M3` относятся к контуру до договора, а не после него.
