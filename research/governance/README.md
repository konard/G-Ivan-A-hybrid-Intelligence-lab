---
status: draft
version: 0.1
updated: 2026-06-06
ai-generated: true
type: navigation
scope: repo-wide
related_issues:
  - "https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/165"
---

# Research: Governance (форматы и эволюция Хаба)

Направление исследований по **governance-форматам** Хаба: как оформлять
исследования, исполнимые контракты и прочие контракты так, чтобы человек и
ИИ-агент **сразу** видели причину, выводы и команду к действию — а не искали их
в массе описательного текста.

Это направление (`scope: repo-wide`) производит **знание для стандартов**: каждое
исследование завершается рекомендацией, которая фиксируется в соответствующем
стандарте `standards/`. Исследование здесь — *вход* для стандарта, а не
дублирующий его текст (Anti-Inflation).

Задача-источник: [issue #165](https://github.com/G-Ivan-A/hybrid-Intelligence-lab/issues/165)
(режим `creative`, полная автономия исполнителя). Мнения команды Q — **входные
данные, не догма**: каждое решение трассируется к best practices.

## Документы

| Документ | Назначение |
| --- | --- |
| [research-documentation-format-2026-06.md](research-documentation-format-2026-06.md) | Исследование формата исследований: сравнение ≥6 практик (IMRaD, BLUF, Inverted Pyramid, Minto, IETF RFC Abstract, ADR, Diátaxis) по 6 критериям; выбор схемы **Введение → Результаты → Детализация**. Источник стандарта `RESEARCH_DOCUMENTATION_STANDARD.md`. |
| [executable-contract-format-2026-06.md](executable-contract-format-2026-06.md) | Исследование формата исполнимых контрактов: системные промпты, runbooks, императивный UX, action-first. Структура **EXECUTION → EXPLANATION**. Источник стандарта `EXECUTABLE_CONTRACT_STANDARD.md`. |
| [contract-documentation-format-2026-06.md](contract-documentation-format-2026-06.md) | Исследование формата прочих контрактов: OpenAPI, RFC 2119/BCP 14, SLA/SLO, ADR, Pact. Структура «контракт сверху, обоснование под катом». Источник стандарта `CONTRACT_DOCUMENTATION_STANDARD.md`. |
| [governance-folder-structure-decisions-2026-06.md](governance-folder-structure-decisions-2026-06.md) | Решения по спорным вопросам Q1 (`proposals/` → `rfc/`), Q2 (размещение концепции портала) и Q3 (папка `rfc/` в проектах) с обоснованием и учётом мнения команды Q. |

## Связанные стандарты

- [standards/RESEARCH_DOCUMENTATION_STANDARD.md](../../standards/RESEARCH_DOCUMENTATION_STANDARD.md) — формат исследований.
- [standards/EXECUTABLE_CONTRACT_STANDARD.md](../../standards/EXECUTABLE_CONTRACT_STANDARD.md) — формат исполнимых контрактов.
- [standards/CONTRACT_DOCUMENTATION_STANDARD.md](../../standards/CONTRACT_DOCUMENTATION_STANDARD.md) — формат прочих контрактов.

## Политики направления

| Политика | Значение |
| --- | --- |
| Язык результата | Русский (как в Хабе), технические термины — в оригинале. |
| Независимость | Варианты команды Q — **входные данные, не догма**. Каждый вывод трассируется к источнику или best practice. |
| Anti-Inflation | Исследование создаётся под конкретный стандарт; не дублирует его, а обосновывает. |
| Решение за человеком | Перевод в `reviewed`/`canonical` и принятие стандарта как обязательного — за фаундером ([AI_GOVERNANCE.md](../../AI_GOVERNANCE.md), правило 4). |

## Связанные артефакты

- [standards/RESEARCH_PROFILE.md](../../standards/RESEARCH_PROFILE.md) — правила frontmatter, источников и воспроизводимости исследований.
- [governance/ARTIFACT_MAP.md](../../governance/ARTIFACT_MAP.md) — карта артефактов и связей.
- [research/README.md](../README.md) — навигация по исследовательским направлениям.
