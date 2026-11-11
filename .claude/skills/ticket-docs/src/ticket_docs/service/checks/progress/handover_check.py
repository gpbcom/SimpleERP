from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import ClassVar, List, Optional

# First-party imports
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class HandoverCheck(TicketCheck):
    """Checks that a handed-over ticket has its documentation (DOC-2) and its release note (DOC-3) done.

    Attributes:
        PROGRESS (str): The progress file.
        DOCUMENTATION (str): The Documentation section's heading.
        RELEASE_NOTE (str): The Release note section's heading.
        DONE (str): The icon of a done row.
        WAIVED (str): What a chapter row says when the ticket leaves it unchanged.
        AFTER_PUSH (str): The release-note row done after the push, so after the hand-over.
        tables (MarkdownTables): Reads the sections' tables.
        logger (Logger): Logger instance.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    DOCUMENTATION: ClassVar[str] = "## Documentation"
    RELEASE_NOTE: ClassVar[str] = "## Release note"
    DONE: ClassVar[str] = "✅"
    WAIVED: ClassVar[str] = "no doc impact:"
    AFTER_PUSH: ClassVar[str] = "issue comment"

    def __init__(self, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the table reader.

        Args:
            tables (MarkdownTables): Reads the sections' tables.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.tables = tables

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the Documentation and Release note rows not done at the hand-over.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per row not done, none before the hand-over.
        """
        text = folder.text(self.PROGRESS)
        if text is None or not folder.handed_over():
            return []
        label = folder.label(self.PROGRESS)
        problems = [
            f"{label}: handed over but Documentation row '{row[0]}' is not ✅ (DOC-2)"
            for row in self.tables.rows(text, self.DOCUMENTATION)
            if not (len(row) > 1 and row[1].startswith(self.DONE)) and self.WAIVED not in " ".join(row)
        ]
        problems += [
            f"{label}: handed over but Release note row '{row[0]}' is not ✅ (DOC-3)"
            for row in self.tables.rows(text, self.RELEASE_NOTE)
            if not (len(row) > 1 and row[1].startswith(self.DONE)) and self.AFTER_PUSH not in row[0].lower()
        ]
        self.logger.debug("%s has %d hand-over rows not done.", folder.key, len(problems))
        return problems
