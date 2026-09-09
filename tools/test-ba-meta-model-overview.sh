#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCUMENT="$ROOT_DIR/docs/ba-meta-model-overview.md"

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

[[ -f "$DOCUMENT" ]] || fail "missing stakeholder overview: docs/ba-meta-model-overview.md"

required_sections=(
  "Executive Summary"
  "Почему набора промптов недостаточно"
  "Концептуальная модель"
  "Четыре таксономии"
  "Artifact Production Model"
  "Orchestration Model"
  "AI Execution Model"
  "GigaCode Mapping"
  "Evidence Map"
  "Итог исследования"
  "Что ещё не доказано"
  "Первый MVP"
)

for section in "${required_sections[@]}"; do
  grep -Fq "$section" "$DOCUMENT" || fail "missing section: $section"
done

[[ "$(grep -c '^```mermaid$' "$DOCUMENT")" -ge 3 ]] ||
  fail "expected at least three Mermaid visualizations"

for token in "Product" "Artifact" "Process" "Operation" "Gate" "Result" \
             "Actor" "Contract" "Traceability" "Route" "Governance" \
             "Skills" "Subagents" "Rules" "AI Workflows" \
             "FACT" "OBSERVATION" "HYPOTHESIS" "DESIGN DECISION"; do
  grep -Fq "$token" "$DOCUMENT" || fail "missing required concept: $token"
done

if grep -Po '\]\(\K[^)#]+' "$DOCUMENT" | grep -Evq '^https://'; then
  fail "all Markdown links must use absolute HTTPS URLs"
fi

echo "BA meta-model stakeholder overview contract test passed."
