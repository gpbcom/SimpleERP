from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod


class Runnable(ABC):
    """A piece of work with a lifecycle: acquire, work, release.

    Notes:
        - Inputs go to the constructor and results are read from attributes afterwards, so the three steps take no
          arguments.
        - **``close`` must be safe after a failed or partial ``initialize``**, because ``execute`` always calls it.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Set what the work needs."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def initialize(self) -> None:
        """Acquire what the work needs."""

    @abstractmethod
    def run(self) -> None:
        """Do the work."""

    @abstractmethod
    def close(self) -> None:
        """Release everything the work acquired."""

    def execute(self) -> None:
        """Initialise, run, and close whatever happens."""
        try:
            self.initialize()
            self.run()
        finally:
            self.close()
