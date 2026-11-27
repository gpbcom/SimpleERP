"""Tests of ``AsyncRunnable``."""

from __future__ import annotations

import inspect
from logging import getLogger
from typing import Dict

import pytest
from erp_lifecycle.runnables.async_runnable import AsyncRunnable

from backend.shared.lifecycle.tests.runnables.recording_async_runnable import RecordingAsyncRunnable


class TestAsyncRunnable:
    """The async lifecycle: ``execute`` always awaits ``close``."""

    @pytest.mark.parametrize("name", ["execute", "initialize", "run", "close"])
    def test_every_lifecycle_method_is_a_coroutine_function(self, name: str) -> None:
        """Each lifecycle method is awaited, not called."""
        assert inspect.iscoroutinefunction(getattr(AsyncRunnable, name))

    def test_the_base_class_cannot_be_instantiated(self) -> None:
        """The base class is abstract."""
        with pytest.raises(TypeError):
            AsyncRunnable()  # type: ignore[abstract]

    @pytest.mark.parametrize("missing", ["initialize", "run", "close"])
    def test_a_subclass_missing_a_method_cannot_be_instantiated(self, missing: str) -> None:
        """A subclass must define the three lifecycle methods."""
        methods: Dict[str, object] = {
            name: getattr(RecordingAsyncRunnable, name) for name in ("initialize", "run", "close") if name != missing
        }
        incomplete = type("Incomplete", (AsyncRunnable,), methods)
        with pytest.raises(TypeError):
            incomplete()

    def test_the_logger_defaults_to_a_logger(self) -> None:
        """Without a logger, one is created."""
        assert RecordingAsyncRunnable().logger is not None

    def test_the_given_logger_is_kept(self) -> None:
        """A logger passed in is the one stored."""
        logger = getLogger("given")
        assert RecordingAsyncRunnable(logger=logger).logger is logger

    async def test_execute_runs_initialize_run_and_close_in_order(self) -> None:
        """A clean run awaits the three steps in order."""
        runnable = RecordingAsyncRunnable()
        await runnable.execute()
        assert runnable.calls == ["initialize", "run", "close"]

    async def test_close_is_awaited_and_run_skipped_when_initialize_fails(self) -> None:
        """A failed initialize skips run, still closes and keeps the original error."""
        runnable = RecordingAsyncRunnable(fail_initialize=True)
        with pytest.raises(RuntimeError) as raised:
            await runnable.execute()
        assert str(raised.value) == RecordingAsyncRunnable.INITIALIZE_MESSAGE
        assert runnable.calls == ["initialize", "close"]

    async def test_close_is_awaited_when_run_fails(self) -> None:
        """A failed run still closes and keeps the original error."""
        runnable = RecordingAsyncRunnable(fail_run=True)
        with pytest.raises(RuntimeError) as raised:
            await runnable.execute()
        assert str(raised.value) == RecordingAsyncRunnable.RUN_MESSAGE
        assert runnable.calls == ["initialize", "run", "close"]
