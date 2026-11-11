from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from pathlib import Path
from typing import List, Optional, TextIO

# First-party imports
from harness_core.terminal.human_confirmation import HumanConfirmation
from ticket_docs.api.cli.ticket_docs_cli import TicketDocsCli


class CommandFactory(ABC):
    """Builds the entry points of ``ticket-docs``.

    Attributes:
        logger (Logger): Logger instance.
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
    def cli(
        self,
        arguments: List[str],
        stdin: TextIO,
        stdout: TextIO,
        stderr: TextIO,
        caller_cwd: Path,
        confirmation: Optional[HumanConfirmation] = None,
    ) -> TicketDocsCli:
        """Build the command line.

        Args:
            arguments (List[str]): The command line, without the program name.
            stdin (TextIO): Where a hook's input is read.
            stdout (TextIO): Where results go.
            stderr (TextIO): Where errors go.
            caller_cwd (Path): The folder ``ticket-docs`` was called from.
            confirmation (Optional[HumanConfirmation]): The person's terminal, ``/dev/tty`` when ``None``.

        Returns:
            TicketDocsCli: The command line, not run yet.
        """
