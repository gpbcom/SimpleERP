from __future__ import annotations

# Standard library imports
import time
from datetime import datetime
from logging import Logger, getLogger
from typing import Optional


class Clock:
    """The time, and the waits between two events of a watch.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        Tests use a clock that never waits.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def now(self) -> datetime:
        """Read the time.

        Returns:
            datetime: The local time.
        """
        return datetime.now()

    def sleep(self, seconds: float) -> None:
        """Wait.

        Args:
            seconds (float): How long.
        """
        self.logger.debug("Waiting %.0f s.", seconds)
        time.sleep(seconds)
