from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import Optional


class Runnable(ABC):
    """A synchronous unit of work with an ``initialize``, ``run`` and ``close`` lifecycle.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        - Inputs go to the constructor, and results are read from attributes afterwards.
        - **``close()`` must be safe after a failed or partial ``initialize()``**, because ``execute()`` always calls
          it.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the runnable.

        Args:
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        self.logger = logger if logger else getLogger(__name__)

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
        """Release everything, safely after a failed or partial ``initialize()``."""

    def execute(self) -> None:
        """Initialise, run and close, closing whatever happens.

        Raises:
            Exception: Whatever ``initialize()``, ``run()`` or ``close()`` raised, unchanged.
        """
        name = type(self).__name__
        self.logger.debug("Executing %s.", name)
        try:
            self.initialize()
            self.logger.debug("Initialised %s.", name)
            self.run()
            self.logger.info("Ran %s.", name)
        except Exception as error:
            self.logger.error("Failed to execute %s: %s.", name, type(error).__name__)
            raise
        finally:
            self.logger.debug("Closing %s.", name)
            self.close()
