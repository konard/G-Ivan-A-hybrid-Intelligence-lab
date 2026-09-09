---
status: draft
version: 0.1
updated: 2026-09-08
temperature: 0.3
type: research
context: [ba, methodology, micro-level, artifact-structure, slots, golden-set, skills, edge-cases, issue-561]
method: corpus-measurement + projection-modeling + synthetic-reference-modeling + case-modeling
scope: ecosystem
source: "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/561"
based_on:
  - research/ba-requirements/2026-09-08-artifact-structure-variance-facts.md
  - research/ba-requirements/exp/ba-micro-structure-561/artifact-structure.json
  - research/ba-requirements/methodology-unification/10-theory.md
related_artifacts:
  - "research/ba-requirements/methodology-unification/00-introduction.md"
  - "research/ba-requirements/artifact-rendering/00-introduction.md"
  - "ops/backlog.md"
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/561"
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557"
---

# Микро-уровень методологии БА: единая структура артефакта

> **Модуль** оформлен по
> [Reference Research Pattern](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/docs/rfc/2026-07-17-rfc-reference-research-pattern.md):
> `00` — рамка и навигация, `10` — теория проекции слоёв в структуру, `20` —
> таксономии слотов, форматов и продуктов, `30` — рамка принятия решений и
> гейты, `40` — практика, эталоны и граничные кейсы, `50` — открытые вопросы,
> бэклог и незакрытое.
> **Ссылки абсолютные** (требование issue #561). Единственное исключение —
> ссылки внутри модуля в
> [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/40-practice-and-cases.md):
> правило `P2` требует относительной ссылки и проверяется машинно
> ([`tools/validate-rrp-links.sh`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/tools/validate-rrp-links.sh)).

## Отношение к макро-уровню

Модуль
[`methodology-unification/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/methodology-unification/00-introduction.md)
(issue [#557](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/557))
отвечает на вопрос **откуда берётся норма**: наследование слоёв, форма дельты,
контракт навыка, типология гейтов. Он останавливается там, где начинается
вопрос **что именно окажется в документе, который получит заказчик**.

Настоящий модуль продолжает ту же ось вниз, к микро-уровню, и **не переписывает
макро-модуль**: расхождения макро-модуля с решениями фаундера, закрытыми в
issue #561 (переименование слоёв, размещение операций и процессов, формулировка
`S-R2`), вынесены отдельными задачами бэклога, а здесь зафиксированы как
поправки в [`50-open-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/50-open-research.md).

## BLUF: десять утверждений

1. **Структура результирующего документа сегодня не воспроизводится.** 17
   результирующих документов корпуса дали 17 различных скелетов; совпадений нет
   даже после огрубления до множества разделов
   ([замер](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-08-artifact-structure-variance-facts.md), §3).
2. **Расхождение не объясняется различием задач.** На одной задаче BCREQ-1074
   три прогона дали три скелета (средний Жаккар 0.69), внутри одного процесса
   Жаккар падает до 0.167.
3. **Устойчива арность, а не семантика.** Шесть разделов воспроизводятся, но
   раздел с одним и тем же номером в трёх документах несёт три разных предмета.
   Норма, заданная числом разделов, не является нормой.
4. **Слой смысла и слой подписи нужно разделить.** `S-SCENARIO` встретился 14
   раз под 14 разными подписями. Пока подпись — свободный текст, ни один
   машинный гейт по структуре невозможен.
5. **UI и критерии приёмки не выделены.** `S-UI` и `S-AC` встретились по одному
   разу на 17 документов: поведение интерфейса и условия приёмки растворены
   внутри функциональных требований. Это машинное подтверждение постановки
   фаундера о смешении системной логики и поведения интерфейса.
6. **Механизм сведения слоёв — проекция, а не конкатенация.** Индустриальный
   базис и продуктовая дельта не складываются в документ по частям: слои
   объявляют **обязательность и содержание слотов**, а документ собирается из
   одного закрытого скелета применением профиля продукта и класса формата
   ([`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/10-theory.md), §3).
7. **Продуктовая вариативность не имеет права попадать в скелет.** Различие
   «функция с настройками» и «функция без настроек» выражается заполненностью
   объявленного слота, а не перестановкой разделов. Пустой слот с объявленной
   причиной отличает «настроек нет» от «вопрос не рассматривался».
8. **Один артефакт вместо трёх — за счёт проекций, а не за счёт трёх
   документов.** Бизнес-ФТ, документ на согласование и техническая
   спецификация — три **проекции одного** размеченного документа
   ([`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/20-taxonomy.md), §5).
9. **Golden Set обязателен и синтетичен.** Корпус не даёт чистых продуктовых
   выборок, поэтому эталон нельзя получить индукцией: он моделируется и
   становится обязательной частью гейта `G-mach`, а не альтернативой ему.
10. **Навык — атомарный скомпилированный артефакт.** Операция — абстрактный тип
    работы; навык — её единственная исполнимая реализация; процесс — не навык,
    а оркестрация навыков. Навык самодостаточен: активных ссылок на слои, по
    которым агент должен ходить во время исполнения, в нём нет.

## Что закрывают файлы модуля

| Контракт issue #561 | Где закрыт |
| --- | --- |
| 1. Таксономия микро-уровня и сведение слоёв к одной структуре | [`10-theory.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/10-theory.md) §2–§4, [`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/20-taxonomy.md) §2–§6 |
| 2. Классификация формулировок и форматов | [`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/20-taxonomy.md) §3–§4, [`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/30-decision-framework.md) §2 |
| 3. Синтез Golden Set и восполнение пробелов | [`30-decision-framework.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/30-decision-framework.md) §4, [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/40-practice-and-cases.md) §3 |
| 4. Моделирование граничных кейсов | [`40-practice-and-cases.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/40-practice-and-cases.md) §5 |
| 5. Связь с бэклогом | [`50-open-research.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/50-open-research.md) §3, [`ops/backlog.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/ops/backlog.md) |

## Доказательная база

- [`2026-09-08-artifact-structure-variance-facts.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/2026-09-08-artifact-structure-variance-facts.md)
  — датированный замер структуры 17 результирующих документов.
- [`exp/ba-micro-structure-561/`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/tree/main/research/ba-requirements/exp/ba-micro-structure-561)
  — измеритель, сырой результат, лог прогона и два синтетических эталона.
- Корпус [`mango_ba_prompts/runs/`](https://github.com/G-Ivan-A/mango_ba_prompts/tree/main/runs)
  на коммите `8cbf82a`.

## Чего в модуле нет

Модуль **не** задаёт продуктовую онтологию Манго и не подменяет
[`standards/product-classification-contract.md`](https://github.com/G-Ivan-A/mango_ba_prompts/blob/main/standards/product-classification-contract.md)
спицы: из него в Хаб перенесён только **контракт разметки** (§6
[`20-taxonomy.md`](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/blob/main/research/ba-requirements/artifact-micro-structure/20-taxonomy.md)),
поскольку общая методология течёт из Хаба и не может опираться на артефакт со
статусом `draft`, лежащий в спице. Модуль также не является стандартом: он
исследование, и переход в норму идёт задачами бэклога.
