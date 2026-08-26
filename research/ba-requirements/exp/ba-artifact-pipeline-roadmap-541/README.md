---
status: draft
version: 0.1
updated: 2026-08-26
temperature: 0.1
type: experiment
---

# exp: ba-artifact-pipeline-roadmap-541

Evidence container для отчёта
[`../../2026-08-26-m0-m2-layering-hypothesis-check.md`](../../2026-08-26-m0-m2-layering-hypothesis-check.md)
и RFC
[`docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-08-25-rfc-ba-artifact-pipeline-rrp-roadmap.md),
issue [#541](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/541).

> **Ссылки.** Issue #541 требует абсолютных ссылок. Относительная ссылка на
> родительский отчёт выше — вынужденное исключение: её форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh)
> (регулярное выражение требует префикса `../../`).

## Что здесь проверяется

Владелец процесса предложил читать модули `M0`–`M2` как слои конвейера
(вход → ядро → выход) и потребовал принять гипотезу только при выигрыше в 80 %
кейсов. Контейнер отвечает на формальный вопрос: **какая доля реальных прогонов
доходит до терминального контракта каждой из двух конкурирующих декомпозиций**.

Терминальный контракт линейной декомпозиции — произведённое ТЗ (`C-TZ`);
слоевой — любой выданный документ (`C-OUT`). Оба признака извлекаются из
прогона механически, поэтому проверка опровержима.

Содержательной оценки декомпозиций здесь нет — она в родительском отчёте.

## Состав

| Файл | Что это |
| --- | --- |
| [`classify-runs.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/classify-runs.py) | классификатор прогонов; все правила разметки — именованные константы в шапке |
| [`runs-routing.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/runs-routing.json) | результат: сводка + построчные факты по каждому прогону |
| [`classify-runs.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/classify-runs.log) | вывод запуска, зафиксировавшего числа отчёта |

Контейнер **не копирует** записи прогонов: [`runs/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/runs)
— операционный журнал спицы, и его дубликат в Хабе устареет молча.

## Воспроизведение

```bash
git clone --depth=1 https://github.com/G-Ivan-A/mango_ba_prompts /tmp/mango
python3 research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/classify-runs.py \
  --mango-root /tmp/mango \
  --out research/ba-requirements/exp/ba-artifact-pipeline-roadmap-541/runs-routing.json
```

Числа отчёта сняты на коммите `7c92766` репозитория `mango_ba_prompts`. Корпус
растёт: при расхождении доверять следует коммиту, записанному в поле
`summary.mango_commit` файла `runs-routing.json`, а не тексту отчёта.

## Границы

Классификация ключевая по подстрокам, а не семантическая. Два следствия названы
явно: прогон, оформивший ТЗ без слов-маркеров, будет пропущен; прогон,
процитировавший ГОСТ, но ТЗ не выдавший, в счёт произведённых ТЗ не попадёт —
для этого разведены списки `TZ_PRODUCED` и `TZ_CONSUMED`. Ручная сверка всех 57
прогонов подтвердила обе границы на текущем корпусе.
