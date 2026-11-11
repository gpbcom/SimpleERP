from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TicketCheck(ABC):
    """One check of a ticket folder against the ticket-docs skill and the rules.

    Attributes:
        logger (Logger): Logger instance.

    Notes:
        A check never raises on what it reads: everything wrong becomes a problem line, so that ``check`` lists
        all of them at once.
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

    @abstractmethod
    def problems(self, folder: TicketFolder) -> List[str]:
        """List what is wrong with a ticket folder.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem, empty when the folder passes.
        """
