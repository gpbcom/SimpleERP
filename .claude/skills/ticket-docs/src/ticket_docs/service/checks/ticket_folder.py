from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Dict, List, Optional, Pattern

# First-party imports
from ticket_docs.models.evidence.evidence_run import EvidenceRun
from ticket_docs.models.evidence.exceptions import SEInvalidEvidenceRunException
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository
from ticket_docs.storage.evidence.exceptions import SEEvidenceStoreError
from ticket_docs.storage.tickets.ticket_repository import TicketRepository


class TicketFolder:
    """One ticket folder as the checks read it: its files, its evidence and its hand-over state.

    Attributes:
        PROGRESS (str): The progress file.
        STATUS_SECTION (str): The heading of PROGRESS.md's Status table.
        HANDOVER_STEP (Pattern[str]): The name of the hand-over step.
        DONE_ICON (str): The icon of a step that is done.
        key (str): The ticket.
        tickets (TicketRepository): The ticket folders.
        evidence (EvidenceRepository): The evidence folders.
        tables (MarkdownTables): Reads PROGRESS.md's tables.
        logger (Logger): Logger instance.

    Notes:
        Nothing is cached: a check reads the files as they are when it runs.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    STATUS_SECTION: ClassVar[str] = "## Status"
    HANDOVER_STEP: ClassVar[Pattern[str]] = re.compile(r"hand-?over", re.I)
    DONE_ICON: ClassVar[str] = "✅"

    def __init__(
        self,
        key: str,
        tickets: TicketRepository,
        evidence: EvidenceRepository,
        tables: MarkdownTables,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the ticket and where its folder is read.

        Args:
            key (str): The ticket.
            tickets (TicketRepository): The ticket folders.
            evidence (EvidenceRepository): The evidence folders.
            tables (MarkdownTables): Reads PROGRESS.md's tables.
            logger (Optional[Logger]): Logger instance.
        """
        self.key = key
        self.tickets = tickets
        self.evidence = evidence
        self.tables = tables
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def path(self) -> Path:
        """The ticket folder."""
        return self.tickets.folder(self.key)

    def label(self, relative: str) -> str:
        """Name a file of the folder in a problem line.

        Args:
            relative (str): The file's path inside the folder.

        Returns:
            str: ``<KEY>/<relative>``.
        """
        return f"{self.key}/{relative}"

    def text(self, relative: str) -> Optional[str]:
        """Read a file of the folder.

        Args:
            relative (str): The file's path inside the folder.

        Returns:
            Optional[str]: Its text, ``None`` when it does not exist.
        """
        return self.tickets.read(self.key, relative)

    def handed_over(self) -> bool:
        """Tell whether the ticket is handed over: PROGRESS.md's hand-over row is done.

        Returns:
            bool: ``True`` once the hand-over row starts with ✅.
        """
        rows = self.tables.rows(self.text(self.PROGRESS) or "", self.STATUS_SECTION)
        return any(
            len(row) > 1 and self.HANDOVER_STEP.search(row[0]) and row[1].startswith(self.DONE_ICON) for row in rows
        )

    def run_folder(self, name: str) -> Path:
        """Give a run folder's path.

        Args:
            name (str): The run folder's name.

        Returns:
            Path: The folder, which may not exist.
        """
        return self.evidence.evidence_dir(self.key) / name

    def runs(self) -> List[EvidenceRun]:
        """Read every run folder whose README can be read.

        Returns:
            List[EvidenceRun]: The runs, by folder name.
        """
        runs: List[EvidenceRun] = []
        for folder in self.evidence.folders(self.key):
            try:
                runs.append(self.evidence.read(folder))
            except (SEEvidenceStoreError, SEInvalidEvidenceRunException):
                continue
        return runs

    def unreadable(self) -> Dict[str, str]:
        """Give the run folders whose README cannot be read, with the reason.

        Returns:
            Dict[str, str]: The reason by folder name.
        """
        reasons: Dict[str, str] = {}
        for folder in self.evidence.folders(self.key):
            try:
                self.evidence.read(folder)
            except (SEEvidenceStoreError, SEInvalidEvidenceRunException) as error:
                self.logger.warning("The README of %s cannot be read: %s.", folder.name, type(error).__name__)
                reasons[folder.name] = str(error)
        return reasons
