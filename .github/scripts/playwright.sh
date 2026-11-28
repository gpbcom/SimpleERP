#!/usr/bin/env bash
# Run the Playwright tests of every front end that has an e2e/ folder (frontend/<app>/e2e, frontend/portals/<portal>/e2e)
# against the stack compose.e2e.yaml already started. Extra arguments go to `playwright test`, such as --grep @smoke.
# A front end whose e2e/ folder holds playwright.config.ts runs it with `--config e2e/playwright.config.ts`, otherwise
# with Playwright's defaults. Each front end writes its own playwright-report/ and test-results/. Every front end runs, even after a failure.
#
# Usage: .github/scripts/playwright.sh [playwright test arguments...]
set -uo pipefail

status=0
found=0
for e2e in frontend/*/e2e frontend/portals/*/e2e; do
  [ -d "$e2e" ] || continue
  found=1
  project="${e2e%/e2e}"
  config=()
  if [ -f "$e2e/playwright.config.ts" ]; then
    config=(--config e2e/playwright.config.ts)
  fi
  echo "::group::Playwright $project $*"
  if ! (cd "$project" && pnpm exec playwright install --with-deps chromium && pnpm exec playwright test "${config[@]}" "$@"); then
    echo "::error::Playwright failed in $project."
    status=1
  fi
  echo "::endgroup::"
done
if [ "$found" = 0 ]; then
  echo "No front end has an e2e/ folder: Playwright is not applicable."
fi
exit "$status"
