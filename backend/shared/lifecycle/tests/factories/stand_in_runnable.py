"""A runnable that records its calls, for the tests of the factories."""

from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import List, Optional

# First-party imports
from erp_lifecycle.runnables.runnable import Runnable


class StandInRunnable(Runnable):
    """Runnable that only records which lifecycle methods were called.

    Attributes:
        name (str): The name given by the factory that built it.
        calls (List[str]): The lifecycle methods called, in order.
    """

    def __init__(self, name: str, logger: Optional[Logger] = None) -> None:
        """Create the stand-in with its name."""
        super().__init__(logger)
        self.name = name
        self.calls: List[str] = []

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Record the call."""
        self.calls.append("initialize")

    def run(self) -> None:
        """Record the call."""
        self.calls.append("run")

    def close(self) -> None:
        """Record the call."""
        self.calls.append("close")
