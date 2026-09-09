#!/usr/bin/env python3
"""Замер присутствия конструкций мета-модели в историческом корпусе спицы.

Комментарий фаундера к PR #564 требует механизма, защищающего новые контракты
от диктата исторических данных: старые промпты и прогоны не должны задавать
структуру и логику новых процессов. Механизм нельзя объявить — нужно знать,
насколько корпус вообще способен быть базисом для новой нормы.

Скрипт отвечает на два вопроса на корпусе `mango_ba_prompts`:

1. Сколько из 12 нормативных конструкций мета-модели (объявленный вход,
   объявленный продуктовый класс, самопроверка, машинный гейт, человеческий
   гейт, условие отказа, контракт, след, эталон, закрытый словарь, версия во
   frontmatter, объявленный выходной артефакт) присутствует в активных
   промптах и в прогонах — то есть можно ли вывести норму из корпуса.
2. Какая доля активных промптов несёт хотя бы одну из конструкций.

Отрицательный результат здесь так же информативен, как положительный: если
конструкций в корпусе нет, корпус не может быть базисом новых контрактов ни
при каком порядке работы, и правило «свидетельство, а не норма» перестаёт
быть предпочтением. Интерпретация — в датированном отчёте
research/ba-requirements/2026-09-09-legacy-normative-influence-facts.md.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# Двенадцать нормативных конструкций мета-модели. Ключ — идентификатор правила
# или сущности, значение — лексические маркеры (регистронезависимо, RU + EN).
# Маркеры намеренно широкие: цель — не пропустить присутствие конструкции,
# поэтому ошибка смещена в сторону завышения покрытия корпуса.
CONSTRUCTS: dict[str, tuple[str, tuple[str, ...]]] = {
    "MM-1 объявленный входной артефакт": (
        "шаг не начинается без объявленного входа",
        (r"входн\w* артефакт", r"input[_ ]artifact", r"artifact_in"),
    ),
    "MM-4 объявленный продуктовый класс": (
        "продуктовый класс объявлен до начала шага",
        (r"продуктов\w* класс", r"product[_ ]class", r"product_domain"),
    ),
    "G-self самопроверка": (
        "чек-лист самопроверки агента до выдачи результата",
        (r"g-self", r"самопроверк", r"self[- ]check", r"self[- ]review"),
    ),
    "G-mach машинный гейт": (
        "проверка валидатором по схеме",
        (r"g-mach", r"валидатор", r"validator", r"json[- ]schema"),
    ),
    "G-human человеческий гейт": (
        "точка приёмки человеком",
        (r"g-human", r"hg-\d", r"человеческ\w* гейт", r"human[- ]gate"),
    ),
    "SK-4 условие отказа": (
        "условия, при которых навык обязан остановиться",
        (r"fail[- ]closed", r"услови\w* отказа", r"обязан остановиться", r"остановить маршрут"),
    ),
    "Contract объявленный контракт": (
        "контракт как проверяемое обязательство артефакта",
        (r"c-in\b", r"c-out\b", r"c-core\b", r"контракт \w*артефакт", r"контракт вход"),
    ),
    "MM-3 след прогона": (
        "происхождение выхода: вход, актор, гейты",
        (r"trace\b", r"traceabilit", r"прослеживаем", r"след прогона"),
    ),
    "EP-G1 эталон (Golden Set)": (
        "эталон структуры как элемент гейта",
        (r"golden[ _-]?set", r"эталон"),
    ),
    "T-1 закрытый словарь": (
        "значение вне словаря — отказ на входе",
        (r"закрыт\w* словар", r"closed[- ]vocabular", r"значение вне словаря"),
    ),
    "SK-5 версионирование во frontmatter": (
        "версия объявлена в метаданных, а не в имени файла",
        (r"^version:", r"^\s*version:"),
    ),
    "OPS-2 объявленный выходной артефакт": (
        "навык объявляет свои выходные артефакты",
        (r"выходн\w* артефакт", r"output[_ ]artifact", r"artifact_out"),
    ),
}

RUN_MODES = ("stepwise", "oneshot", "legacy")


def corpus_commit(mango: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(mango), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def active_prompts(mango: Path) -> list[Path]:
    """Активные промпты: `prompts/*.md` без архива и без исполняемых файлов."""
    return sorted(
        p for p in (mango / "prompts").glob("*.md")
        if not p.name.endswith(".executable.md") and p.name != "README.md"
    )


def run_documents(mango: Path) -> list[tuple[str, list[Path]]]:
    """Прогоны `runs/RUN-*`: идентификатор и все markdown/yaml файлы внутри."""
    rows: list[tuple[str, list[Path]]] = []
    for run_dir in sorted((mango / "runs").rglob("RUN-*")):
        if not run_dir.is_dir():
            continue
        files = [f for f in run_dir.rglob("*") if f.suffix in (".md", ".yaml", ".yml")]
        rows.append((run_dir.name, files))
    return rows


def constructs_in_text(text: str) -> list[str]:
    low = text.lower()
    return [
        name for name, (_, patterns) in CONSTRUCTS.items()
        if any(re.search(p, low, flags=re.MULTILINE) for p in patterns)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mango", type=Path, required=True, help="каталог клона mango_ba_prompts")
    parser.add_argument("--json", type=Path, default=Path("legacy-normative-influence.json"))
    args = parser.parse_args()

    if not (args.mango / "prompts").is_dir():
        print(f"ERROR: не найден {args.mango}/prompts", file=sys.stderr)
        return 1

    prompts = active_prompts(args.mango)
    prompt_rows = []
    for path in prompts:
        text = path.read_text(encoding="utf-8", errors="replace")
        mode = next((m for m in RUN_MODES if path.stem.endswith(f"-{m}")), None)
        prompt_rows.append({
            "file": path.name,
            "mode": mode,
            "constructs": constructs_in_text(text),
        })

    run_rows = []
    for run_id, files in run_documents(args.mango):
        text = "\n".join(f.read_text(encoding="utf-8", errors="replace") for f in files)
        run_rows.append({"run": run_id, "constructs": constructs_in_text(text)})

    per_construct = {}
    for name in CONSTRUCTS:
        per_construct[name] = {
            "purpose": CONSTRUCTS[name][0],
            "prompts": sum(1 for r in prompt_rows if name in r["constructs"]),
            "runs": sum(1 for r in run_rows if name in r["constructs"]),
        }

    absent_in_prompts = sorted(n for n, v in per_construct.items() if v["prompts"] == 0)
    absent_everywhere = sorted(
        n for n, v in per_construct.items() if v["prompts"] == 0 and v["runs"] == 0
    )

    result = {
        "corpus": {
            "repo": "mango_ba_prompts",
            "commit": corpus_commit(args.mango),
            "prompts": len(prompt_rows),
            "runs": len(run_rows),
        },
        "constructs": {
            "declared": len(CONSTRUCTS),
            "absent_in_prompts": absent_in_prompts,
            "absent_everywhere": absent_everywhere,
            "per_construct": per_construct,
        },
        "coverage": {
            "prompts_without_any_construct": sum(1 for r in prompt_rows if not r["constructs"]),
            "max_constructs_in_one_prompt": max((len(r["constructs"]) for r in prompt_rows), default=0),
            "mean_constructs_per_prompt": round(
                sum(len(r["constructs"]) for r in prompt_rows) / max(1, len(prompt_rows)), 2
            ),
            "runs_without_any_construct": sum(1 for r in run_rows if not r["constructs"]),
        },
        "detail": {"prompt_rows": prompt_rows, "run_rows": run_rows},
    }

    args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    s = result
    print(f"corpus commit: {s['corpus']['commit']}")
    print(f"активных промптов: {s['corpus']['prompts']}, прогонов: {s['corpus']['runs']}")
    print(f"нормативных конструкций мета-модели: {s['constructs']['declared']}")
    print(f"отсутствуют во всех промптах: {len(s['constructs']['absent_in_prompts'])} — "
          f"{s['constructs']['absent_in_prompts']}")
    print(f"отсутствуют и в промптах, и в прогонах: {len(s['constructs']['absent_everywhere'])} — "
          f"{s['constructs']['absent_everywhere']}")
    print(f"среднее число конструкций на промпт: {s['coverage']['mean_constructs_per_prompt']}, "
          f"максимум в одном промпте: {s['coverage']['max_constructs_in_one_prompt']}")
    print(f"промптов без единой конструкции: {s['coverage']['prompts_without_any_construct']}, "
          f"прогонов без единой конструкции: {s['coverage']['runs_without_any_construct']}")
    for name, v in s["constructs"]["per_construct"].items():
        print(f"  {name}: промптов {v['prompts']}/{s['corpus']['prompts']}, "
              f"прогонов {v['runs']}/{s['corpus']['runs']}")
    print(f"результат: {args.json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
