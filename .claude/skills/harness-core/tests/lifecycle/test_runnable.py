from __future__ import annotations

from typing import List

import pytest

from harness_core.lifecycle.runnable import Runnable


class RecordingRunnable(Runnable):
    """Records the order of its lifecycle calls."""

    def __init__(self, fail_on: str = "") -> None:
        self.calls: List[str] = []
        self.fail_on = fail_on

    def initialize(self) -> None:
        self.calls.append("initialize")
        if self.fail_on == "initialize":
            raise RuntimeError("initialize failed.")

    def run(self) -> None:
        self.calls.append("run")
        if self.fail_on == "run":
            raise RuntimeError("run failed.")

    def close(self) -> None:
        self.calls.append("close")


class TestRunnable:
    def test_execute_runs_the_three_steps_in_order(self) -> None:
        runnable = RecordingRunnable()
        runnable.execute()
        assert runnable.calls == ["initialize", "run", "close"]

    @pytest.mark.parametrize("step", ["initialize", "run"])
    def test_execute_closes_even_when_a_step_fails(self, step: str) -> None:
        runnable = RecordingRunnable(fail_on=step)
        with pytest.raises(RuntimeError):
            runnable.execute()
        assert runnable.calls[-1] == "close"

    def test_a_runnable_without_its_steps_cannot_be_built(self) -> None:
        with pytest.raises(TypeError):
            Runnable()  # type: ignore[abstract]
