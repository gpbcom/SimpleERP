from __future__ import annotations

import os

import pytest


def pytest_runtest_setup(item: pytest.Item) -> None:
    """Refuse a test that calls a paid AI model unless the cost guard started it (rule TEST-5).

    ``ai-cost run`` exports ``AI_COST_RUN_ID`` to the command it guards, so a test marked ``llm`` that runs without it
    was started outside the guard: its cost would be neither capped nor recorded.
    """
    if item.get_closest_marker("llm") is not None and not os.environ.get("AI_COST_RUN_ID"):
        raise pytest.UsageError(
            "This test calls a paid AI model. "  # noqa: E501
            "Run it through ai-cost run --ticket <KEY> --estimate-usd <n> -- <command> (rule TEST-5)."
        )
