from __future__ import annotations

from logging import Logger, getLogger
from typing import Callable, Dict

import pytest
from erp_lifecycle.runnables.runnable import Runnable

from backend.shared.lifecycle.tests.runnables.recording_runnable import RecordingRunnable


class TestRunnable:
    """Tests of the ``execute`` contract of ``Runnable``."""

    def test_execute_calls_initialize_run_and_close_in_order(self) -> None:
        """Check the order of the calls."""
        runnable = RecordingRunnable()
        runnable.execute()
        assert runnable.calls == ["initialize", "run", "close"]

    def test_a_failed_initialize_still_closes_and_skips_run(self) -> None:
        """Check close runs and the original error propagates."""
        runnable = RecordingRunnable(fail_initialize=True)
        with pytest.raises(RuntimeError, match="initialize failed on purpose"):
            runnable.execute()
        assert runnable.calls == ["initialize", "close"]

    def test_a_failed_run_still_closes(self) -> None:
        """Check close runs and the original error propagates."""
        runnable = RecordingRunnable(fail_run=True)
        with pytest.raises(RuntimeError, match="run failed on purpose"):
            runnable.execute()
        assert runnable.calls == ["initialize", "run", "close"]

    def test_runnable_itself_cannot_be_instantiated(self) -> None:
        """Check the class is abstract."""
        with pytest.raises(TypeError):
            Runnable()  # type: ignore[abstract]

    @pytest.mark.parametrize("missing", ["initialize", "run", "close"])
    def test_a_subclass_missing_a_method_cannot_be_instantiated(self, missing: str) -> None:
        """Check each of the three methods is abstract."""
        methods: Dict[str, Callable[[object], None]] = {
            name: (lambda self: None) for name in ("initialize", "run", "close") if name != missing
        }
        incomplete = type("Incomplete", (Runnable,), methods)
        with pytest.raises(TypeError):
            incomplete()

    def test_without_a_logger_one_is_created(self) -> None:
        """Check the default logger."""
        assert isinstance(RecordingRunnable().logger, Logger)

    def test_a_given_logger_is_kept(self) -> None:
        """Check the given logger is used."""
        logger = getLogger("given")
        assert RecordingRunnable(logger=logger).logger is logger
