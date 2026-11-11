from __future__ import annotations

from pathlib import Path

import pytest

ROOT_CONFTEST = Path(__file__).resolve().parents[1] / "conftest.py"
PAID_TEST = """
import pytest


@pytest.mark.llm
def test_calls_a_paid_model() -> None:
    assert True
"""


class TestLlmMarkerGuard:
    def test_a_paid_test_outside_the_cost_guard_is_an_error(
        self, pytester: pytest.Pytester, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.delenv("AI_COST_RUN_ID", raising=False)
        pytester.makeconftest(ROOT_CONFTEST.read_text(encoding="utf-8"))
        pytester.makepyfile(test_paid=PAID_TEST)
        result = pytester.runpytest("-p", "no:cacheprovider")
        result.assert_outcomes(errors=1)
        result.stdout.fnmatch_lines(["*ai-cost run*"])

    def test_a_paid_test_inside_the_cost_guard_runs(
        self, pytester: pytest.Pytester, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setenv("AI_COST_RUN_ID", "run-1")
        pytester.makeconftest(ROOT_CONFTEST.read_text(encoding="utf-8"))
        pytester.makepyfile(test_paid=PAID_TEST)
        pytester.runpytest("-p", "no:cacheprovider").assert_outcomes(passed=1)

    def test_free_tests_are_not_concerned(self, pytester: pytest.Pytester, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AI_COST_RUN_ID", raising=False)
        pytester.makeconftest(ROOT_CONFTEST.read_text(encoding="utf-8"))
        pytester.makepyfile(test_free="def test_free() -> None:\n    assert True\n")
        pytester.runpytest("-p", "no:cacheprovider").assert_outcomes(passed=1)
