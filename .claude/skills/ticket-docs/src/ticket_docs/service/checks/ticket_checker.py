from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from harness_core.lifecycle.runnable import Runnable
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class TicketChecker(Runnable):
    """Runs every check of a ticket folder and gathers their problems.

    Attributes:
        folder (TicketFolder): The ticket folder.
        checks (List[TicketCheck]): The checks, in the order their problems are listed.
        logger (Logger): Logger instance.
        problems (List[str]): One line per problem, empty when the folder is complete.
    """

    def __init__(self, folder: TicketFolder, checks: List[TicketCheck], logger: Optional[Logger] = None) -> None:
        """Set the folder and its checks.

        Args:
            folder (TicketFolder): The ticket folder.
            checks (List[TicketCheck]): The checks, in the order their problems are listed.
            logger (Optional[Logger]): Logger instance.
        """
        self.folder = folder
        self.checks = checks
        self.logger = logger if logger else getLogger(__name__)
        self.problems: List[str] = []

    ############################
    # Publicly Exposed Methods #
    ############################

    def initialize(self) -> None:
        """Start from no problem."""
        self.problems = []
        self.logger.debug("Checking %s with %d checks.", self.folder.key, len(self.checks))

    def run(self) -> None:
        """Run every check, or name the folder when it does not exist."""
        if not self.folder.path.is_dir():
            self.logger.warning("%s has no folder.", self.folder.key)
            self.problems = [f"{self.folder.path}: no such folder"]
            return
        for check in self.checks:
            self.problems.extend(check.problems(self.folder))
        self.logger.info("%s has %d problems.", self.folder.key, len(self.problems))

    def close(self) -> None:
        """Release nothing: the checks only read."""
        self.logger.debug("The checker of %s is closed.", self.folder.key)
