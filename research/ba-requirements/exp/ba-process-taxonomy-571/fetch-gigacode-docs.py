#!/usr/bin/env python3
"""Снимок документации среды GigaCode / GitVerse (issue #571, SSOT п.4).

Скрипт загружает страницы документации, перечисленные в постановке задачи,
извлекает читаемый текст и фиксирует проверяемые признаки: HTTP-код, sha256
исходного HTML, заголовки разделов и наличие ключевых утверждений, на которые
опирается модуль ba-meta-model (форма SKILL.md, каталоги размещения, поля
объявления агента, права на инструменты).

Сеть обязательна: воспроизводимость обеспечивается сравнением sha256 и
контрольных утверждений, а не хранением копии чужой документации в Хабе.

Использование:
    python3 fetch-gigacode-docs.py [--out gigacode-docs.json] [--text-dir DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

BASE = "https://gitverse.ru/docs/ai/"

PAGES = [
    "ai-development",
    "ai-development/quick-start",
    "ai-development/repository-setup",
    "ai-development/workflow",
    "ai-development/context",
    "ai-development/tools",
    "ai-development/skills",
    "ai-development/agents",
    "gigacode-on-gitverse",
    "mcp",
    "mcp/gitverse-mcp-tools",
]

# Контрольные утверждения: подстрока -> идентификатор факта модуля.
# Совпадение подтверждает, что утверждение Хаба всё ещё опирается на источник.
CLAIMS = {
    "ai-development/skills": {
        "GC-1": "папка с файлом SKILL.md",
        "GC-2": "Оба поля обязательны",
        "GC-3": ".agents/skills",
        "GC-4": "должно быть уникальным",
        "GC-5": "Рядом с SKILL.md можно положить вспомогательные файлы",
        "GC-6": "Сначала он видит только имена и описания",
        # GC-25..GC-28 добавлены по комментарию фаундера к PR #572:
        # проверяют, чем среда ограничивает объём навыка сверху и снизу.
        "GC-25": "инструкция для повторяющейся работы",
        "GC-26": "Короткое правило или команда",
        "GC-27": "Содержит пошаговую процедуру",
        "GC-28": "отдельный набор прав и изолированный контекст",
    },
    "ai-development/agents": {
        "GC-7": ".opencode/agent",
        "GC-8": "mode",
        "GC-9": "permission",
        "GC-10": "steps",
    },
    "ai-development/tools": {
        "GC-11": "выполнение команд оболочки: сборка, тесты, линтеры",
        "GC-12": "чтение файлов с секретами",
        "GC-13": "Model Context Protocol",
    },
    "ai-development/workflow": {
        "GC-14": "проверка выполнена и показана, а не заявлена словами",
        "GC-15": "каждое утверждение подтверждено файлом и строкой",
    },
    "ai-development/context": {
        "GC-16": "диалог сжимается автоматически",
        "GC-17": "агент помнит выводы, но не дословную переписку",
    },
    "ai-development/repository-setup": {
        "GC-18": "AGENTS.md в корне репозитория",
    },
    "ai-development": {
        "GC-19": "результат — проверить машинно",
        "GC-20": "он додумает",
    },
    "gigacode-on-gitverse": {
        "GC-21": "AI-исполнитель задач",
    },
    "mcp/gitverse-mcp-tools": {
        "GC-22": "issue_read",
        "GC-23": "add_issue_comment",
        "GC-24": "get_job_logs",
    },
}


def to_text(raw: str) -> str:
    """Грубое извлечение читаемого текста: разметка не сохраняется."""
    match = re.search(r"<main.*?</main>", raw, re.S) or re.search(
        r"<article.*?</article>", raw, re.S
    )
    body = match.group(0) if match else raw
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
    body = re.sub(r"<(h[1-6])[^>]*>", "\n\n### ", body)
    body = re.sub(r"</(p|li|div|h[1-6]|tr)>", "\n", body)
    body = re.sub(r"<li[^>]*>", "- ", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def fetch(url: str, timeout: int = 30) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "hub-research/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.status, response.read().decode("utf-8", "replace")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="gigacode-docs.json")
    parser.add_argument("--text-dir", default=None, help="куда сложить извлечённый текст")
    args = parser.parse_args()

    result = {
        "measured_at": date.today().isoformat(),
        "source_issue": "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/571",
        "base": BASE,
        "pages": [],
        "claims": {},
        "errors": [],
    }

    text_dir = Path(args.text_dir) if args.text_dir else None
    if text_dir:
        text_dir.mkdir(parents=True, exist_ok=True)

    for page in PAGES:
        url = BASE + page
        try:
            status, raw = fetch(url)
        except Exception as error:  # сеть недоступна или страница переехала
            result["errors"].append({"url": url, "error": str(error)})
            print(f"ОШИБКА {url}: {error}", file=sys.stderr)
            continue

        text = to_text(raw)
        headings = [line[4:].strip() for line in text.splitlines() if line.startswith("### ")]
        result["pages"].append(
            {
                "url": url,
                "http_status": status,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
                "headings": headings,
                "text_chars": len(text),
            }
        )
        if text_dir:
            (text_dir / (page.replace("/", "_") + ".txt")).write_text(text, encoding="utf-8")

        for claim_id, needle in CLAIMS.get(page, {}).items():
            result["claims"][claim_id] = {
                "url": url,
                "needle": needle,
                "found": needle in text,
            }
        print(f"{url}: HTTP {status}, {len(raw)} байт, разделов {len(headings)}")

    missing = [cid for cid, claim in result["claims"].items() if not claim["found"]]
    result["claims_total"] = len(result["claims"])
    result["claims_missing"] = missing

    Path(args.out).write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"страниц: {len(result['pages'])} из {len(PAGES)}")
    print(f"контрольных утверждений: {len(result['claims'])}, не найдено: {len(missing)}")
    if missing:
        print("не найдены: " + ", ".join(sorted(missing)))
    if result["errors"]:
        return 2
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
