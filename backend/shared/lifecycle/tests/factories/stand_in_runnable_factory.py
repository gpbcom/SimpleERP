"""A concrete factory, for the tests of the abstract one."""

from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import Optional

from erp_lifecycle.factories.runnable_factory import RunnableFactory

# First-party imports
from backend.shared.lifecycle.tests.factories.stand_in_runnable import StandInRunnable


class StandInRunnableFactory(RunnableFactory[StandInRunnable]):
    """Factory of ``StandInRunnable``, which gets its inputs at its constructor.

    Attributes:
        name (str): The name given to every runnable it builds.
    """

    def __init__(self, name: str, logger: Optional[Logger] = None) -> None:
        """Create the factory with the name of its runnables."""
        super().__init__(logger)
        self.name = name

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self) -> StandInRunnable:
        """Build one new ``StandInRunnable``."""
        return StandInRunnable(self.name, self.logger)
