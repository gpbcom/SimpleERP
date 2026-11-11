from __future__ import annotations

# Standard library imports
from logging import Logger
from pathlib import Path
from typing import List, Optional, TextIO

# First-party imports
from harness_core.terminal.human_confirmation import HumanConfirmation
from ticket_docs.api.cli.ticket_docs_cli import TicketDocsCli
from ticket_docs.api.factories.command_factory import CommandFactory


class CliCommandFactory(CommandFactory):
    """Builds the ``ticket-docs`` command line.

    Attributes:
        rules_file (Path): The folder rules catalogue.
        catalog_file (Path): The GitHub catalogue.
        logger (Logger): Logger instance.
    """

    def __init__(self, rules_file: Path, catalog_file: Path, logger: Optional[Logger] = None) -> None:
        """Set the catalogues.

        Args:
            rules_file (Path): The folder rules catalogue.
            catalog_file (Path): The GitHub catalogue.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules_file = rules_file
        self.catalog_file = catalog_file

    ############################
    # Publicly Exposed Methods #
    ############################

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
        self.logger.debug("Building the ticket-docs command line.")
        terminal = confirmation if confirmation is not None else HumanConfirmation(logger=self.logger)
        return TicketDocsCli(
            arguments, self.rules_file, self.catalog_file, stdin, stdout, stderr, caller_cwd, terminal, self.logger
        )
