from __future__ import annotations

import asyncio
from typing import List

import pytest

from harness_core.lifecycle.async_runnable import AsyncRunnable


class RecordingAsyncRunnable(AsyncRunnable):
    """Records the order of its lifecycle calls."""

    def __init__(self, fail_on: str = "") -> None:
        self.calls: List[str] = []
        self.fail_on = fail_on

    async def initialize(self) -> None:
        self.calls.append("initialize")

    async def run(self) -> None:
        self.calls.append("run")
        if self.fail_on == "run":
            raise RuntimeError("run failed.")

    async def close(self) -> None:
        self.calls.append("close")


class TestAsyncRunnable:
    def test_execute_runs_the_three_steps_in_order(self) -> None:
        runnable = RecordingAsyncRunnable()
        asyncio.run(runnable.execute())
        assert runnable.calls == ["initialize", "run", "close"]

    def test_execute_closes_even_when_run_fails(self) -> None:
        runnable = RecordingAsyncRunnable(fail_on="run")
        with pytest.raises(RuntimeError):
            asyncio.run(runnable.execute())
        assert runnable.calls == ["initialize", "run", "close"]
