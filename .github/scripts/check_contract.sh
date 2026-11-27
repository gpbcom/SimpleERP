#!/usr/bin/env bash
# Check the API contract of one service (REQ-T05-05): the tests of <folder>/tests/contracts, which fail when the committed
# openapi.json is stale and, with a baseline, when a field or an endpoint of the base commit's document was removed.
# A service with no openapi.json says so and passes.
#
# Usage: .github/scripts/check_contract.sh <service folder> [<base commit>]
set -euo pipefail

folder="${1:?usage: check_contract.sh <service folder> [<base commit>]}"
base="${2:-}"

if [ ! -f "$folder/openapi.json" ]; then
  echo "No OpenAPI document in $folder: the contract check is not applicable."
  exit 0
fi

unset ERP_CONTRACT_BASELINE
echo "::group::baseline $folder/openapi.json"
if [ -n "$base" ] && [ "$base" != "0000000000000000000000000000000000000000" ] \
  && git cat-file -e "$base^{commit}" 2>/dev/null && git cat-file -e "$base:$folder/openapi.json" 2>/dev/null; then
  baseline="$(mktemp)"
  trap 'rm -f "$baseline"' EXIT
  git show "$base:$folder/openapi.json" > "$baseline"
  export ERP_CONTRACT_BASELINE="$baseline"
  echo "Baseline: $folder/openapi.json at $base."
else
  echo "No baseline OpenAPI document: only the stale check runs."
fi
echo "::endgroup::"

echo "::group::pytest $folder/tests/contracts"
status=0
uv run --package "${folder##*/}" pytest "$folder/tests/contracts" -n 2 || status=$?
echo "::endgroup::"
exit "$status"
