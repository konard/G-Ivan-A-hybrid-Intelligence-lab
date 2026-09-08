---
status: draft
version: 0.1
updated: 2026-09-08
temperature: 0.1
type: experiment
---

# exp: ba-micro-structure-561

Evidence container для датированного замера
[`../../2026-09-08-artifact-structure-variance-facts.md`](../../2026-09-08-artifact-structure-variance-facts.md)
и модуля
[`research/ba-requirements/artifact-micro-structure/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/artifact-micro-structure),
issue [#561](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/561).

> **Ссылки.** Issue #561 требует абсолютных ссылок. Относительная ссылка на
> родительский отчёт выше — вынужденное исключение: её форму машинно проверяет
> [`tools/validate-evidence-structure.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-evidence-structure.sh).

## Что здесь измеряется

Контракты 2 и 3 issue #561 требуют классификации допустимых структур артефакта
и синтеза Golden Set там, где исторические прогоны не покрывают продуктовые
случаи. Оба вывода зависят от одного факта: **насколько устойчива структура
результирующего документа в корпусе `runs/`**. Написанный руками ответ на этот
вопрос непроверяем, поэтому он вычисляется: скрипт обходит `outputs/` всех
прогонов, отображает подписи разделов в закрытый словарь слотов и считает
расхождение скелетов внутри одной задачи и одного процесса.

Машинно проверяемые утверждения родительского отчёта: размер корпуса,
сегментация `outputs/` на три класса файлов, число результирующих документов и
число различных скелетов среди них, коэффициенты Жаккара по группам,
частота и позиционное распределение слотов, классы формата, продуктовое
покрытие.

Содержательной интерпретации (что означает расхождение, какой должна быть
норма) здесь нет — она в родительском отчёте и в модуле.

## Состав

| Файл | Что это |
| --- | --- |
| [`measure-artifact-structure.py`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-micro-structure-561/measure-artifact-structure.py) | измеритель; словарь слотов, продуктовые правила и правила формата — именованные константы в шапке |
| [`artifact-structure.json`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-micro-structure-561/artifact-structure.json) | результат: сводка + запись на каждый просмотренный артефакт |
| [`measure-artifact-structure.log`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-micro-structure-561/measure-artifact-structure.log) | вывод прогона, фиксирующий опубликованные цифры и коммит корпуса |
| [`2026-09-08-golden-set-contact-center-ivr-settings.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-micro-structure-561/2026-09-08-golden-set-contact-center-ivr-settings.md) | синтетический эталон, продуктовый класс `contact-center` (функция с настройками) |
| [`2026-09-08-golden-set-self-service-lk.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/exp/ba-micro-structure-561/2026-09-08-golden-set-self-service-lk.md) | синтетический эталон, продуктовый класс `self-service-lk` (функция без настроек) |

## Воспроизведение

```bash
git clone https://github.com/G-Ivan-A/mango_ba_prompts.git /tmp/mango
python3 measure-artifact-structure.py --mango /tmp/mango
```

Коммит, на котором получены опубликованные цифры, записан в поле
`corpus.commit` результата: `8cbf82aa73129ec5747af07f790aaf438b0fb6e9`.
На других коммитах цифры будут другими — это ожидаемо, отчёт датирован.

## Статус двух Golden Set

Эталоны в этом каталоге **синтетические**. Они не извлечены из корпуса и не
являются поставленными заказчику документами: замер (§6 родительского отчёта)
показал, что чистых продуктовых выборок в `runs/` нет, поэтому индукция по
истории невозможна. Эталоны собраны как модель ожидаемой структуры по правилам
модуля и подлежат проверке человеком до любого применения в качестве few-shot
образца. До прохождения этой проверки их статус — `draft`, и они не являются
нормой.

## Границы измерения

- Учитываются только заголовки уровня `##`. Документ, у которого структура
  выражена жирным текстом без заголовков, будет измерен как малоструктурный —
  это занижает оценку структурности, а не завышает её.
- Слот присваивается по первому сработавшему правилу; раздел со смешанным
  содержанием получает один слот, поэтому смешение (например, ФТ и UI в одном
  разделе) измерением **занижается**.
- Продуктовая разметка лексическая и множественная. Она пригодна для ответа
  «чистых выборок нет» и непригодна для утверждений о долях.
- Корпус — одна спица. Переносимость выводов на другие предметные области
  здесь не проверяется.
