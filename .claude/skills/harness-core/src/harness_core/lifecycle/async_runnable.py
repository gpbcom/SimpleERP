from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod


class AsyncRunnable(ABC):
    """An asynchronous piece of work with a lifecycle: acquire, work, release.

    Notes:
        - The asynchronous twin of ``Runnable``: the same three steps, awaited.
        - **``close`` must be safe after a failed or partial ``initialize``**, because ``execute`` always calls it.
    """

    @abstractmethod
    def __init__(self) -> None:
        """Set what the work needs."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    async def initialize(self) -> None:
        """Acquire what the work needs."""

    @abstractmethod
    async def run(self) -> None:
        """Do the work."""

    @abstractmethod
    async def close(self) -> None:
        """Release everything the work acquired."""

    async def execute(self) -> None:
        """Initialise, run, and close whatever happens."""
        try:
            await self.initialize()
            await self.run()
        finally:
            await self.close()
