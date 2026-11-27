"""A stand-in async runnable that records its calls."""

from __future__ import annotations

from logging import Logger
from typing import List, Optional

from erp_lifecycle.runnables.async_runnable import AsyncRunnable


class RecordingAsyncRunnable(AsyncRunnable):
    """An ``AsyncRunnable`` that records each lifecycle call and fails on request."""

    INITIALIZE_MESSAGE = "recording runnable: initialize failed on purpose"
    RUN_MESSAGE = "recording runnable: run failed on purpose"

    def __init__(self, fail_initialize: bool = False, fail_run: bool = False, logger: Optional[Logger] = None) -> None:
        """Create the runnable, saying which step must fail."""
        super().__init__(logger)
        self.fail_initialize = fail_initialize
        self.fail_run = fail_run
        self.calls: List[str] = []

    async def initialize(self) -> None:
        """Record the call, then fail if asked to."""
        self.calls.append("initialize")
        if self.fail_initialize:
            raise RuntimeError(self.INITIALIZE_MESSAGE)

    async def run(self) -> None:
        """Record the call, then fail if asked to."""
        self.calls.append("run")
        if self.fail_run:
            raise RuntimeError(self.RUN_MESSAGE)

    async def close(self) -> None:
        """Record the call."""
        self.calls.append("close")
