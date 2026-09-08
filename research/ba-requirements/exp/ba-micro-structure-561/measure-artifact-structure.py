#!/usr/bin/env python3
"""Замер микро-структуры результирующих артефактов БА в корпусе прогонов Mango.

Вопрос замера (issue #561, контракты 2 и 3): насколько предсказуема структура
результирующего документа, если задача и продукт совпадают? Ответ должен быть
вычислен, а не заявлен, поэтому скрипт:

1. обходит `runs/<год>/RUN-*/` локального клона `mango_ba_prompts`;
2. отбирает артефакты, несущие требования (ФТ/ТЗ/US/UC), по признакам заголовков
   и лексики, а не по имени файла: имена в корпусе не унифицированы;
3. снимает скелет разделов уровня H2 и нормализует подписи в замкнутый словарь
   слотов `S-*` (ключ -> слот задан таблицей SLOT_RULES ниже);
4. размечает продуктовый класс по словарю, выведенному из
   `standards/product-classification-contract.md` спицы Mango;
5. считает вариативность: сколько различных скелетов приходится на одну задачу
   (BCREQ) и на один процесс, и какова попарная мера Жаккара по слотам.

Границы измерения названы в README контейнера. Скрипт ничего не интерпретирует:
интерпретация — в модуле `research/ba-requirements/artifact-structure-micro/`.

Запуск:
    python3 measure-artifact-structure.py --mango <путь-к-клону> \
        [--json artifact-structure.json]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import asdict, dataclass, field
from itertools import combinations
from pathlib import Path

# --- Словарь слотов -------------------------------------------------------
#
# Слот — это роль раздела в документе, а не его подпись. Две подписи
# («1. Глоссарий» и «1. Термины и определения») означают один слот; именно
# расхождение подписей при совпадении слота и есть измеряемый предмет.
# Порядок правил значим: первое совпадение выигрывает.
SLOT_RULES: list[tuple[str, str]] = [
    ("S-GLOSSARY", r"глоссари|термин|определени|сокращени"),
    ("S-PROBLEM", r"проблем|цель|цели|задач[аи]|обоснован|контекст|предпосыл"),
    ("S-SCOPE", r"границ|scope|периметр|вне рамок"),
    ("S-SOLUTION", r"описание разрабатываемого|решени|архитектур|модель данных|"
                   r"моделирование"),
    ("S-UI", r"\bui\b|интерфейс|экран|макет|верстк"),
    ("S-FR", r"функциональн(ые|ых) требован|^требования|состав требован|"
             r"перечень требован"),
    ("S-SCENARIO", r"сценари|use ?case|user ?stor|пользовательск(ие|их) истори"),
    ("S-AC", r"критери|acceptance|приемк|приёмк"),
    ("S-NFR", r"нефункциональн"),
    ("S-LIMITS", r"ограничен|особенности реализац|допущени|риск"),
    ("S-INTEGRATION", r"интеграц|api|обмен данными"),
    ("S-TRACE", r"трассируем|traceab|источник|ссылк|приложени"),
    ("S-OPEN", r"вопрос|открыт|незакрыт|уточнени|todo"),
    # Слоты журнала прогона. Они не принадлежат результирующему документу, но
    # встречаются в том же каталоге outputs/ и должны опознаваться явно, иначе
    # остаток S-OTHER растёт за счёт чужого класса документов.
    ("S-EPISODE", r"эпизод|что происходило|что подал|что вернула|что ответила|"
                  r"реплик|раскладка|воспроизвед|как воспроизвести"),
    ("S-VERDICT", r"вердикт|оценка|итог|вывод|резюме|сводка|результат"),
    ("S-DEFECT", r"галлюцинац|дефект|ошибк|замечани|что не сработало"),
    ("S-METRIC", r"метрик|статистик|покрытие|a/b|эксперимент"),
    ("S-TEST", r"тест|self-test|чек-лист|проверк"),
    ("S-PURPOSE", r"назначени|о документе|для кого"),
    ("S-PROPOSAL", r"предложени|рекомендац|идеи|шаги"),
    ("S-PROCESS", r"как получен|ход работы|метод|процесс прогона|лог|маршрут|"
                  r"детекция|системный промпт|соответствие промпту"),
]

# Признаки журнала прогона в подписях разделов: если документ описывает, как шёл
# прогон, он не является результирующим артефактом БА.
JOURNAL_SLOTS = {"S-EPISODE", "S-VERDICT", "S-DEFECT", "S-METRIC", "S-PROCESS"}

# Признаки результирующего документа в заголовке H1 или имени файла.
DOCUMENT_TITLE_RE = re.compile(
    r"функциональн\w* требован|техническое задание|\bфт\b|\bтз\b|bcreq|"
    r"требования|user ?stor|use ?case|спецификац|fr\b",
    re.IGNORECASE,
)

# --- Словарь продуктовых классов -----------------------------------------
#
# Выведен из standards/product-classification-contract.md Mango (уровни Domain и
# Capability). Разметка грубая: один артефакт может получить несколько классов,
# в этом случае фиксируются все — комбинация продуктов сама по себе предмет
# гипотезы фаундера.
PRODUCT_RULES: list[tuple[str, str]] = [
    ("contact-center", r"контакт-центр|контакт центр|\bкц\b|оператор|очеред|"
                       r"обзвон|ivr|маршрутизац|супервизор|скрипт разговор"),
    ("self-service-lk", r"личн(ый|ого|ом) кабинет|\bлк\b|самообслуживан|"
                        r"пользовательск(ий|ого) кабинет"),
    ("voice-ucaas", r"виртуальн(ая|ой) атс|\bатс\b|телефони|номер|сип|\bsip\b|"
                    r"звонк|вызов"),
    ("analytics-reporting", r"отчет|отчёт|аналитик|статистик|дашборд|выгрузк|"
                            r"метрик"),
    ("integration", r"интеграц|\bcrm\b|вебхук|webhook|\bapi\b"),
    ("billing-finance", r"тариф|расход|биллинг|счет|счёт|оплат|договор"),
]

REQUIREMENT_MARKERS = re.compile(
    r"функциональн\w* требован|техническое задание|\bбcreq\b|\bbcreq\b|\bфт\b|"
    r"\bтз\b|user ?stor|use ?case|критери\w* приемк|критери\w* приёмк|"
    r"система должна",
    re.IGNORECASE,
)

HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.MULTILINE)
NUMBER_PREFIX_RE = re.compile(r"^\s*(?:\d+(?:\.\d+)*\.?|[IVX]+\.)\s*")
FR_ID_RE = re.compile(r"\b(?:FR|ФТ|НФТ|NFR|US|UC)[\s\-–—]?\d+", re.IGNORECASE)
BCREQ_RE = re.compile(r"BCREQ[\s\-–—]?(\d+)", re.IGNORECASE)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


@dataclass
class Artifact:
    run_id: str
    path: str
    process: str
    date: str
    status: str
    model: str
    bcreq: str | None
    products: list[str]
    headings: list[str]
    slots: list[str]
    slot_set: list[str]
    heading_count: int
    word_count: int
    requirement_ids: int
    doc_kind: str = ""
    format_class: str = ""
    unmapped_headings: list[str] = field(default_factory=list)


def read_metadata(run_dir: Path) -> dict[str, str]:
    """Минимальный разбор metadata.yaml: только скалярные поля верхнего уровня.

    Полный YAML-парсер здесь избыточен и добавил бы зависимость; нужные поля
    (run_id, process, date, status, model) во всём корпусе записаны скалярами.
    """
    meta: dict[str, str] = {}
    path = run_dir / "metadata.yaml"
    if not path.exists():
        return meta
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not match:
            continue
        key, value = match.group(1), match.group(2).strip().strip('"')
        if value:
            meta[key] = value
    return meta


def normalize_heading(raw: str) -> str:
    text = NUMBER_PREFIX_RE.sub("", raw)
    text = re.sub(r"[«»\"'`*_]", "", text)
    return text.strip().lower()


def map_slot(normalized: str) -> str:
    for slot, pattern in SLOT_RULES:
        if re.search(pattern, normalized):
            return slot
    return "S-OTHER"


def detect_products(text: str) -> list[str]:
    lowered = text.lower()
    return [name for name, pattern in PRODUCT_RULES if re.search(pattern, lowered)]


def classify_doc_kind(title: str, filename: str, slots: list[str],
                      requirement_ids: int) -> str:
    """Различает результирующий документ БА и журнал прогона.

    Разделение обязательно: в `outputs/` лежат оба класса, а вопрос issue #561
    про предсказуемость структуры относится только к документу, который ждёт
    пользователь. Смешение классов завышало бы вариативность структуры.
    """
    journal_share = (
        sum(1 for slot in slots if slot in JOURNAL_SLOTS) / len(slots)
        if slots else 0.0
    )
    looks_like_document = bool(
        DOCUMENT_TITLE_RE.search(title) or DOCUMENT_TITLE_RE.search(filename)
    )
    carries_requirement_body = bool(
        {"S-FR", "S-SCENARIO", "S-SOLUTION", "S-AC", "S-NFR"} & set(slots)
    ) or requirement_ids >= 5
    if journal_share >= 0.5:
        return "run-journal"
    if looks_like_document and carries_requirement_body:
        return "requirement-document"
    return "analysis-note"


def classify_format(heading_count: int, word_count: int, requirement_ids: int) -> str:
    """Классы формата по наблюдаемому размеру, а не по декларации автора.

    Пороги подобраны по распределению корпуса и названы в README: граница
    «короткий/классический» проходит по числу разделов H2, потому что именно
    оно определяет, помещается ли документ в один экран согласования.
    """
    if heading_count <= 3 and word_count < 700:
        return "F-SHORT"
    if heading_count >= 5 and requirement_ids >= 3:
        return "F-CLASSIC"
    if requirement_ids == 0:
        return "F-NARRATIVE"
    return "F-MIXED"


def collect(mango_root: Path) -> list[Artifact]:
    artifacts: list[Artifact] = []
    runs_root = mango_root / "runs"
    for run_dir in sorted(p for p in runs_root.glob("*/RUN-*") if p.is_dir()):
        meta = read_metadata(run_dir)
        outputs = run_dir / "outputs"
        if not outputs.is_dir():
            continue
        for md in sorted(outputs.rglob("*.md")):
            if md.name.lower() == "readme.md":
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            body = FRONTMATTER_RE.sub("", text)
            headings = [
                (len(level), title)
                for level, title in HEADING_RE.findall(body)
            ]
            h2 = [title for level, title in headings if level == 2]
            if not REQUIREMENT_MARKERS.search(body) or len(h2) < 2:
                continue
            normalized = [normalize_heading(title) for title in h2]
            slots = [map_slot(title) for title in normalized]
            word_count = len(body.split())
            requirement_ids = len(set(FR_ID_RE.findall(body)))
            bcreq_match = BCREQ_RE.search(body) or BCREQ_RE.search(md.name)
            h1 = next((title for level, title in headings if level == 1), "")
            artifacts.append(
                Artifact(
                    run_id=meta.get("run_id", run_dir.name),
                    path=str(md.relative_to(mango_root)),
                    process=meta.get("process", "not-recorded"),
                    date=meta.get("date", "not-recorded"),
                    status=meta.get("status", "not-recorded"),
                    model=meta.get("model", "not-recorded"),
                    bcreq=bcreq_match.group(1) if bcreq_match else None,
                    products=detect_products(body),
                    headings=h2,
                    slots=slots,
                    slot_set=sorted(set(slots)),
                    heading_count=len(h2),
                    word_count=word_count,
                    requirement_ids=requirement_ids,
                    doc_kind=classify_doc_kind(h1, md.name, slots, requirement_ids),
                    format_class=classify_format(len(h2), word_count, requirement_ids),
                    unmapped_headings=[
                        title
                        for title, slot in zip(h2, slots)
                        if slot == "S-OTHER"
                    ],
                )
            )
    return artifacts


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 1.0


def group_variance(artifacts: list[Artifact], key: str) -> list[dict]:
    groups: dict[str, list[Artifact]] = {}
    for art in artifacts:
        value = getattr(art, key)
        if not value:
            continue
        groups.setdefault(str(value), []).append(art)
    result = []
    for value, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        skeletons = {"|".join(m.slots) for m in members}
        labels = {"|".join(normalize_heading(h) for h in m.headings) for m in members}
        pairs = [
            jaccard(set(a.slot_set), set(b.slot_set))
            for a, b in combinations(members, 2)
        ]
        result.append(
            {
                "key": value,
                "artifacts": len(members),
                "runs": sorted({m.run_id for m in members}),
                "distinct_slot_skeletons": len(skeletons),
                "distinct_label_skeletons": len(labels),
                "mean_slot_jaccard": round(sum(pairs) / len(pairs), 3),
                "min_slot_jaccard": round(min(pairs), 3),
                "format_classes": sorted({m.format_class for m in members}),
            }
        )
    return result


def head_commit(repo: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def build_report(mango_root: Path) -> dict:
    scanned = collect(mango_root)
    kind_freq: dict[str, int] = {}
    for art in scanned:
        kind_freq[art.doc_kind] = kind_freq.get(art.doc_kind, 0) + 1
    # Все производные метрики считаются по результирующим документам: вопрос
    # предсказуемости структуры поставлен именно про них.
    artifacts = [a for a in scanned if a.doc_kind == "requirement-document"]
    slot_freq: dict[str, int] = {}
    label_by_slot: dict[str, dict[str, int]] = {}
    for art in artifacts:
        for heading, slot in zip(art.headings, art.slots):
            slot_freq[slot] = slot_freq.get(slot, 0) + 1
            bucket = label_by_slot.setdefault(slot, {})
            key = normalize_heading(heading)
            bucket[key] = bucket.get(key, 0) + 1

    format_freq: dict[str, int] = {}
    product_freq: dict[str, int] = {}
    for art in artifacts:
        format_freq[art.format_class] = format_freq.get(art.format_class, 0) + 1
        for product in art.products or ["unclassified"]:
            product_freq[product] = product_freq.get(product, 0) + 1

    positional: dict[str, dict[str, int]] = {}
    for art in artifacts:
        for index, slot in enumerate(art.slots[:6], start=1):
            bucket = positional.setdefault(f"pos-{index}", {})
            bucket[slot] = bucket.get(slot, 0) + 1

    return {
        "corpus": {
            "repo": "mango_ba_prompts",
            "commit": head_commit(mango_root),
            "runs_scanned": len(list((mango_root / "runs").glob("*/RUN-*"))),
            "markdown_with_requirement_lexicon": len(scanned),
            "doc_kind_frequency": dict(sorted(kind_freq.items(), key=lambda kv: -kv[1])),
            "requirement_documents": len(artifacts),
        },
        "slot_frequency": dict(sorted(slot_freq.items(), key=lambda kv: -kv[1])),
        "label_variants_per_slot": {
            slot: dict(sorted(labels.items(), key=lambda kv: -kv[1]))
            for slot, labels in sorted(label_by_slot.items())
        },
        "format_frequency": dict(sorted(format_freq.items(), key=lambda kv: -kv[1])),
        "product_frequency": dict(sorted(product_freq.items(), key=lambda kv: -kv[1])),
        "positional_slot_distribution": positional,
        "variance_by_bcreq": group_variance(artifacts, "bcreq"),
        "variance_by_process": group_variance(artifacts, "process"),
        "artifacts": [asdict(a) for a in scanned],
    }


def render_log(report: dict) -> str:
    lines: list[str] = []
    corpus = report["corpus"]
    lines.append("# Замер микро-структуры артефактов БА")
    lines.append(
        f"корпус: {corpus['repo']} @ {corpus['commit']}; "
        f"прогонов просмотрено: {corpus['runs_scanned']}; "
        f"markdown с лексикой требований: {corpus['markdown_with_requirement_lexicon']}; "
        f"из них результирующих документов: {corpus['requirement_documents']}"
    )
    lines.append("")
    lines.append("## Классы документов в outputs/")
    for kind, count in corpus["doc_kind_frequency"].items():
        lines.append(f"{kind:<22} {count}")
    lines.append("")
    lines.append("## Частота слотов")
    for slot, count in report["slot_frequency"].items():
        variants = len(report["label_variants_per_slot"].get(slot, {}))
        lines.append(f"{slot:<16} разделов: {count:>3}   различных подписей: {variants}")
    lines.append("")
    lines.append("## Классы формата")
    for name, count in report["format_frequency"].items():
        lines.append(f"{name:<12} {count}")
    lines.append("")
    lines.append("## Продуктовые классы (множественная разметка)")
    for name, count in report["product_frequency"].items():
        lines.append(f"{name:<22} {count}")
    lines.append("")
    lines.append("## Вариативность внутри одной задачи (BCREQ)")
    for row in report["variance_by_bcreq"]:
        lines.append(
            f"BCREQ-{row['key']}: артефактов {row['artifacts']}, "
            f"скелетов по слотам {row['distinct_slot_skeletons']}, "
            f"скелетов по подписям {row['distinct_label_skeletons']}, "
            f"средний Жаккар {row['mean_slot_jaccard']}, "
            f"минимальный {row['min_slot_jaccard']}, "
            f"прогоны {', '.join(row['runs'])}"
        )
    lines.append("")
    lines.append("## Вариативность внутри одного процесса")
    for row in report["variance_by_process"]:
        lines.append(
            f"{row['key']}: артефактов {row['artifacts']}, "
            f"скелетов по слотам {row['distinct_slot_skeletons']}, "
            f"средний Жаккар {row['mean_slot_jaccard']}"
        )
    lines.append("")
    lines.append("## Позиционное распределение слотов (первые шесть разделов)")
    for position, dist in report["positional_slot_distribution"].items():
        top = ", ".join(
            f"{slot}={count}"
            for slot, count in sorted(dist.items(), key=lambda kv: -kv[1])
        )
        lines.append(f"{position}: {top}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mango", required=True, type=Path,
                        help="путь к локальному клону mango_ba_prompts")
    parser.add_argument("--json", type=Path, default=Path("artifact-structure.json"))
    parser.add_argument("--log", type=Path, default=Path("measure-artifact-structure.log"))
    args = parser.parse_args()

    report = build_report(args.mango)
    args.json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    log = render_log(report)
    args.log.write_text(log, encoding="utf-8")
    print(log)


if __name__ == "__main__":
    main()
