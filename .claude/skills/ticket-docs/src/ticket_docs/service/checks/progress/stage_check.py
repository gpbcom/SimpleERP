from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import ClassVar, List, Optional

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class StageCheck(TicketCheck):
    """Checks PROGRESS.md's Stage validation table: a 💻, a 🟦 and a 🟪 row, each with its status icon.

    Attributes:
        PROGRESS (str): The progress file.
        SECTION (str): The table's heading.
        STATUS_COLUMN (str): The status column's header.
        rules (FolderRules): The stage and status icons.
        tables (MarkdownTables): Reads the table.
        logger (Logger): Logger instance.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    SECTION: ClassVar[str] = "## Stage validation"
    STATUS_COLUMN: ClassVar[str] = "Status"

    def __init__(self, rules: FolderRules, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the rules and the table reader.

        Args:
            rules (FolderRules): The stage and status icons.
            tables (MarkdownTables): Reads the table.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules
        self.tables = tables

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the missing stage rows and the rows without a status icon.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem, none when PROGRESS.md does not exist.
        """
        text = folder.text(self.PROGRESS)
        if text is None:
            return []
        label = folder.label(self.PROGRESS)
        header = self.tables.header(text, self.SECTION)
        rows = self.tables.rows(text, self.SECTION)
        status = header.index(self.STATUS_COLUMN) if self.STATUS_COLUMN in header else 1
        problems = [
            f"{label}: Stage validation has no {icon} row"
            for icon in self.rules.stage_icons
            if not any(row[0].startswith(icon) for row in rows)
        ]
        problems += [
            f"{label}: Stage validation row '{row[0]}' has no status icon"
            for row in rows
            if len(row) <= status or not row[status].startswith(tuple(self.rules.status_icons))
        ]
        self.logger.debug("%s's Stage validation has %d problems.", folder.key, len(problems))
        return problems
