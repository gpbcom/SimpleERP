#!/usr/bin/env bash
# Print, as GitHub Actions outputs, the services and front ends that have a Dockerfile, and those a change touches.
#   detect-components.sh [<base ref>]
# Without a base, every component counts as changed. A change in packages/, uv.lock or pyproject.toml changes all.
set -euo pipefail
base="${1:-}"
all_services=$(find services -mindepth 2 -maxdepth 2 -name Dockerfile -printf '%h\n' 2>/dev/null | xargs -r -n1 basename | sort || true)
all_frontends=$(find frontends -mindepth 2 -maxdepth 2 -name Dockerfile -printf '%h\n' 2>/dev/null | xargs -r -n1 basename | sort || true)
if [ -z "$base" ]; then
  changed_files="__all__"
else
  changed_files=$(git diff --name-only "$base"...HEAD)
fi
everything=false
if [ "$changed_files" = "__all__" ] || grep -qE '^(packages/|uv\.lock$|pyproject\.toml$|compose\.e2e\.yaml$)' <<<"$changed_files"; then
  everything=true
fi
pick() {
  local kind="$1" names="$2" out=()
  for name in $names; do
    if $everything || grep -q "^$kind/$name/" <<<"$changed_files"; then out+=("\"$name\""); fi
  done
  local IFS=,; echo "[${out[*]}]"
}
services=$(pick services "$all_services")
frontends=$(pick frontends "$all_frontends")
{
  echo "services=$services"
  echo "frontends=$frontends"
  echo "any=$([ "$services$frontends" = "[][]" ] && echo false || echo true)"
  echo "compose=$([ -f compose.e2e.yaml ] && echo true || echo false)"
} | tee -a "${GITHUB_OUTPUT:-/dev/null}"
