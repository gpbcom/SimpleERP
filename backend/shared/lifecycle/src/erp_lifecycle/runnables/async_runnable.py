"""The asynchronous lifecycle base class."""

from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import Optional


class AsyncRunnable(ABC):
    """A unit of asynchronous work with an ``initialize``, ``run`` and ``close`` lifecycle.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - ``execute`` awaits the three steps and awaits ``close`` whatever happens.
        - Inputs go to the constructor, and results are read from attributes afterwards.
        - **``close`` must be safe after a failed or partial ``initialize``.**
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Store the logger.

        Args:
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when omitted.
        """
        self.logger = logger if logger else getLogger(__name__)

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
        """Release everything, even after a failed or partial ``initialize``."""

    async def execute(self) -> None:
        """Initialise, run, then close, whatever happens.

        Raises:
            Exception: The error raised by ``initialize`` or ``run``, unchanged.
        """
        try:
            self.logger.debug("Initialising %s.", type(self).__name__)
            await self.initialize()
            self.logger.debug("Running %s.", type(self).__name__)
            await self.run()
        except Exception as error:
            self.logger.error("Failed %s with %s.", type(self).__name__, type(error).__name__)
            raise
        finally:
            self.logger.debug("Closing %s.", type(self).__name__)
            await self.close()
