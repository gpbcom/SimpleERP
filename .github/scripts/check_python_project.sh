#!/usr/bin/env bash
# Check one Python project of the uv workspace (a service or a shared package): ruff, ruff format, mypy on its src/,
# pytest on its tests/ with a JUnit report in reports/<report>.xml. A step that does not apply says so and passes.
#
# Usage: .github/scripts/check_python_project.sh <project folder> <report name>
set -euo pipefail

folder="${1:?usage: check_python_project.sh <project folder> <report name>}"
report="${2:?usage: check_python_project.sh <project folder> <report name>}"

echo "::group::ruff check $folder"
uv run ruff check "$folder"
echo "::endgroup::"

echo "::group::ruff format --check $folder"
uv run ruff format --check "$folder"
echo "::endgroup::"

echo "::group::mypy $folder/src"
if [ -d "$folder/src" ]; then
  MYPYPATH="$folder/src" uv run mypy "$folder/src"
else
  echo "No src/ in $folder: mypy is not applicable."
fi
echo "::endgroup::"

echo "::group::pytest $folder/tests"
if [ -n "$(find "$folder/tests" -name 'test_*.py' -print -quit 2>/dev/null)" ]; then
  mkdir -p reports
  uv run pytest "$folder/tests" -n 2 --junitxml="reports/$report.xml"
else
  echo "No test in $folder/tests: pytest is not applicable."
fi
echo "::endgroup::"
