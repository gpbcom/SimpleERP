from __future__ import annotations

from logging import Logger
from typing import List, Optional

from erp_lifecycle.runnables.runnable import Runnable


class RecordingRunnable(Runnable):
    """A runnable that records each lifecycle call and can fail on demand."""

    def __init__(
        self,
        fail_initialize: bool = False,
        fail_run: bool = False,
        logger: Optional[Logger] = None,
    ) -> None:
        """Create the runnable.

        Args:
            fail_initialize (bool): Raise from ``initialize`` when true.
            fail_run (bool): Raise from ``run`` when true.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.fail_initialize = fail_initialize
        self.fail_run = fail_run
        self.calls: List[str] = []

    def initialize(self) -> None:
        """Record the call, and fail when asked to."""
        self.calls.append("initialize")
        if self.fail_initialize:
            raise RuntimeError("initialize failed on purpose")

    def run(self) -> None:
        """Record the call, and fail when asked to."""
        self.calls.append("run")
        if self.fail_run:
            raise RuntimeError("run failed on purpose")

    def close(self) -> None:
        """Record the call."""
        self.calls.append("close")
