from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from ticket_docs.models.evidence.run_request import RunRequest
from ticket_docs.service.checks.ticket_checker import TicketChecker
from ticket_docs.service.github.board_mover import BoardMover
from ticket_docs.service.github.evidence_archiver import EvidenceArchiver
from ticket_docs.service.history.history_bundler import HistoryBundler
from ticket_docs.service.hooks.file_gate import FileGate
from ticket_docs.service.hooks.git_gate import GitGate
from ticket_docs.service.hooks.time_reminder import TimeReminder
from ticket_docs.service.index.report_index import ReportIndex
from ticket_docs.service.permits.squash_permits import SquashPermits
from ticket_docs.service.runs.run_recorder import RunRecorder


class ServiceFactory(ABC):
    """Builds the services of ``ticket-docs`` and its runnables, the run recorder and the ticket checker.

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
    def tickets_root(self) -> Path:
        """Give the ``docs/tickets`` folder.

        Returns:
            Path: The tickets folder.
        """

    @abstractmethod
    def run_recorder(self, request: RunRequest) -> RunRecorder:
        """Build the recorder of one run.

        Args:
            request (RunRequest): What to record.

        Returns:
            RunRecorder: The recorder, not run yet.
        """

    @abstractmethod
    def ticket_checker(self, key: str, offline: bool) -> TicketChecker:
        """Build the checker of one ticket folder.

        Args:
            key (str): The ticket.
            offline (bool): Whether to leave GitHub out.

        Returns:
            TicketChecker: The checker, not run yet.
        """

    @abstractmethod
    def report_index(self) -> ReportIndex:
        """Build the evidence index.

        Returns:
            ReportIndex: The index.
        """

    @abstractmethod
    def history_bundler(self) -> HistoryBundler:
        """Build the history bundler.

        Returns:
            HistoryBundler: The bundler.
        """

    @abstractmethod
    def evidence_archiver(self, dry_run: bool) -> EvidenceArchiver:
        """Build the archiver.

        Args:
            dry_run (bool): Whether to list the gh commands instead of running them.

        Returns:
            EvidenceArchiver: The archiver.
        """

    @abstractmethod
    def board_mover(self) -> BoardMover:
        """Build the board mover.

        Returns:
            BoardMover: The mover.
        """

    @abstractmethod
    def git_gate(self) -> GitGate:
        """Build the gate of the ``PreToolUse`` hook.

        Returns:
            GitGate: The gate.
        """

    @abstractmethod
    def time_reminder(self) -> TimeReminder:
        """Build the reminder of the ``PostToolUse`` hook.

        Returns:
            TimeReminder: The reminder.
        """

    @abstractmethod
    def squash_permits(self) -> SquashPermits:
        """Build the squash permits of the person's home folder.

        Returns:
            SquashPermits: The permits.
        """

    @abstractmethod
    def file_gate(self) -> FileGate:
        """Build the gate of the ``PreToolUse`` hook on the file tools.

        Returns:
            FileGate: The gate.
        """
