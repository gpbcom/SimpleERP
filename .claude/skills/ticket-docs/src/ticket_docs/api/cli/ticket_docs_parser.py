from __future__ import annotations

# Standard library imports
import argparse
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from ticket_docs.models.enums import Expectation, RunKind, RunPlace, TicketDocsCommand


class TicketDocsParser:
    """Describes the ``ticket-docs`` command line.

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
    # Internal Helpers Methods #
    ############################

    def _root(self, parser: argparse.ArgumentParser) -> None:
        """Add the ``--root`` option.

        Args:
            parser (argparse.ArgumentParser): A command's parser.
        """
        parser.add_argument(
            "--root", type=Path, help="the docs/tickets folder (default: the one of the current repository)"
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self) -> argparse.ArgumentParser:
        """Build the parser.

        Returns:
            argparse.ArgumentParser: The parser of every command.
        """
        root = argparse.ArgumentParser(prog="ticket-docs", description="Keep a ticket's documentation folder.")
        commands = root.add_subparsers(dest="command", required=True)
        record = commands.add_parser(TicketDocsCommand.RECORD_RUN.value, help="record a run into an evidence folder")
        record.add_argument("--ticket", required=True, help="the ticket, such as GH-12")
        record.add_argument("--kind", required=True, choices=[kind.value for kind in RunKind])
        record.add_argument("--where", required=True, choices=[place.value for place in RunPlace])
        record.add_argument("--check", required=True, help="the check's name, such as tdd-red-storage")
        record.add_argument("--what", required=True, help="what the run proves")
        record.add_argument("--expect", default=Expectation.GREEN.value, choices=[e.value for e in Expectation])
        record.add_argument("--run-id", help="a GitHub Actions run to record instead of a command")
        self._root(record)
        record.add_argument("argv", nargs=argparse.REMAINDER, help="-- then the command")
        check = commands.add_parser(TicketDocsCommand.CHECK.value, help="check a ticket folder")
        check.add_argument("key")
        check.add_argument("--offline", action="store_true", help="leave GitHub out")
        self._root(check)
        index = commands.add_parser(TicketDocsCommand.REPORT_INDEX.value, help="write docs/tickets/README.md")
        index.add_argument("--output", type=Path, help="write the index there instead")
        self._root(index)
        bundle = commands.add_parser(TicketDocsCommand.HISTORY_BUNDLE.value, help="save the branch before a squash")
        bundle.add_argument("key")
        self._root(bundle)
        archive = commands.add_parser(TicketDocsCommand.ARCHIVE.value, help="upload the folder to its pre-release")
        archive.add_argument("key")
        archive.add_argument("--dry-run", action="store_true", help="print the gh commands instead")
        self._root(archive)
        board = commands.add_parser(TicketDocsCommand.BOARD.value, help="set the issue's status on the board")
        board.add_argument("key")
        board.add_argument("status")
        commands.add_parser(TicketDocsCommand.GIT_GATE.value, help="answer the PreToolUse hook on Bash")
        commands.add_parser(TicketDocsCommand.TIME_REMINDER.value, help="answer the PostToolUse hook on Bash")
        squash = commands.add_parser(
            TicketDocsCommand.ALLOW_SQUASH.value, help="let the staged GIT-4 squash be committed once (human only)"
        )
        squash.add_argument("key")
        commands.add_parser(TicketDocsCommand.FILE_GATE.value, help="answer the PreToolUse hook on the file tools")
        self.logger.debug("Built the ticket-docs parser.")
        return root
