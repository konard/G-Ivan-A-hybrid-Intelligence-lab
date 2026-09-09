#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

failures=0

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  failures=$((failures + 1))
}

assert_file() {
  local path="$1"
  [[ -f "$ROOT_DIR/$path" ]] || fail "required integration artifact is missing: $path"
}

assert_deprecated_pointer_only() {
  local path="$1"
  local entries
  [[ -d "$ROOT_DIR/$path" ]] || {
    fail "deprecated compatibility directory is missing: $path"
    return
  }
  entries="$(find "$ROOT_DIR/$path" -mindepth 1 -maxdepth 1 -printf '%f\n' | sort)"
  [[ "$entries" == "README.md" ]] || fail "$path must contain only README.md during the compatibility cycle"
}

expect_validator_failure() {
  local name="$1"
  local repo="$2"
  local expected="$3"
  local output="$TMP_DIR/${name}.log"
  if "$ROOT_DIR/tools/validate-agents-bootstrap.sh" "$repo" >"$output" 2>&1; then
    fail "$name: validator unexpectedly passed"
    return
  fi
  if ! grep -Fq -- "$expected" "$output"; then
    fail "$name: validator failed for the wrong reason (expected: $expected)"
  fi
}

assert_file "AGENTS.md"
assert_file ".hub-profile.json"
assert_file "ai-rules/agent-work-routing.md"
assert_file "standards/agents-md-bootstrap-standard.md"
assert_file "templates/htom/AGENTS.md"
assert_file "templates/htom/.hub-profile.json"
assert_file "templates/spoke/AGENTS.md"
assert_file "templates/spoke/.hub-profile.json"
assert_deprecated_pointer_only "pr-ops"

if ! "$ROOT_DIR/tools/validate-repository-structure.sh" \
  >"$TMP_DIR/repository-structure.log" 2>&1; then
  fail "repository structure validator rejects the integrated bootstrap or path migration"
fi

if [[ -f "$ROOT_DIR/AGENTS.md" && -f "$ROOT_DIR/.hub-profile.json" ]]; then
  missing_agents="$TMP_DIR/missing-agents"
  mkdir -p "$missing_agents"
  cp "$ROOT_DIR/.hub-profile.json" "$missing_agents/.hub-profile.json"
  expect_validator_failure "missing-agents" "$missing_agents" "missing file: AGENTS.md"

  missing_profile="$TMP_DIR/missing-profile"
  mkdir -p "$missing_profile"
  cp "$ROOT_DIR/AGENTS.md" "$missing_profile/AGENTS.md"
  expect_validator_failure "missing-profile" "$missing_profile" "missing file: .hub-profile.json"

  environment_mismatch="$TMP_DIR/environment-mismatch"
  mkdir -p "$environment_mismatch"
  cp "$ROOT_DIR/AGENTS.md" "$environment_mismatch/AGENTS.md"
  cp "$ROOT_DIR/.hub-profile.json" "$environment_mismatch/.hub-profile.json"
  python3 - "$environment_mismatch/.hub-profile.json" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as source:
    profile = json.load(source)
profile["environment"] = "gigacode"
with open(path, "w", encoding="utf-8") as target:
    json.dump(profile, target, ensure_ascii=False, indent=2)
    target.write("\n")
PY
  expect_validator_failure \
    "environment-mismatch" \
    "$environment_mismatch" \
    "AGENTS.md environment must match .hub-profile.json"

  declared_directories="$TMP_DIR/declared-directories"
  mkdir -p "$declared_directories"
  cp "$ROOT_DIR/AGENTS.md" "$declared_directories/AGENTS.md"
  cp "$ROOT_DIR/.hub-profile.json" "$declared_directories/.hub-profile.json"
  mkdir "$declared_directories/plans" "$declared_directories/tasks"
  python3 - "$declared_directories/.hub-profile.json" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, encoding="utf-8") as source:
    profile = json.load(source)
profile["project_specific_directories"] = [
    {"path": "plans", "reason": "Project-local planning artifacts"},
    {"path": "tasks", "reason": "Project-local task artifacts"},
]
with open(path, "w", encoding="utf-8") as target:
    json.dump(profile, target, ensure_ascii=False, indent=2)
    target.write("\n")
PY
  if ! "$ROOT_DIR/tools/validate-agents-bootstrap.sh" "$declared_directories" \
    >"$TMP_DIR/declared-directories.log" 2>&1; then
    fail "generic directory declarations rejected plans/ or tasks/"
  fi
fi

if [[ -d "$ROOT_DIR/ops" ]]; then
  if git -C "$ROOT_DIR" grep -n 'pr-ops/' -- . \
    ':(exclude)CHANGELOG.md' \
    ':(exclude)pr-ops/README.md' \
    ':(exclude)docs/superpowers/plans/2026-09-09-agents-md-physical-integration.md' \
    ':(exclude)docs/adr/2026-06-adr-001-ecosystem-infrastructure-methodology.md' \
    ':(exclude)docs/rfc/2026-09-03-rfc-agents-md-root-contract.md' \
    ':(exclude).hub-profile.json' \
    ':(exclude)tools/test-agents-md-integration.sh' \
    ':(exclude)tools/test-historical-immutable.sh' \
    ':(exclude)tools/test-post-migration-validator.sh' \
    ':(exclude)tools/validate-repository-structure.sh' \
    ':(exclude)ops/backlog.md' \
    ':(exclude)ops/artifact-map.md' \
    >"$TMP_DIR/stale-pr-ops.log"; then
    fail "active tracked files still contain stale pr-ops/ references"
  fi
fi

if ((failures > 0)); then
  printf '\nAGENTS.md integration regression tests failed with %d issue(s).\n' "$failures" >&2
  exit 1
fi

printf 'AGENTS.md integration regression tests passed.\n'
