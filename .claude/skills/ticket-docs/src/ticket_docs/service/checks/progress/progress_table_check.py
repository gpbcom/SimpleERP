from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from typing import ClassVar, List, Optional, Pattern, Tuple

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class ProgressTableCheck(TicketCheck):
    """Checks PROGRESS.md's Status table: a status icon on every row, the times of each step and the total.

    Attributes:
        PROGRESS (str): The progress file.
        SECTION (str): The Status table's heading.
        STATUS_COLUMN (str): The status column's header.
        TIME_COLUMNS (Tuple[str, str, str]): The started, finished and elapsed columns' headers.
        TIMESTAMP (Pattern[str]): A clock reading, ``YYYY-MM-DD HH:MM``.
        ELAPSED (Pattern[str]): A time spent, ``<h>h<mm>``.
        RUNNING_ELAPSED (Pattern[str]): The time spent so far by a running step.
        UNKNOWN (str): What a cell reads when its time cannot be rebuilt.
        TOTAL_LINE (str): The line that sums the steps.
        DONE (str): The icon of a done step, which has all three times.
        RUNNING (str): The icon of a running step, with its start and time so far.
        PAUSED (str): The icon of a paused step, with its start.
        rules (FolderRules): The status icons.
        tables (MarkdownTables): Reads the table.
        logger (Logger): Logger instance.

    Notes:
        A cell may add a note after its time, such as ``(reconstructed)``.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    SECTION: ClassVar[str] = "## Status"
    STATUS_COLUMN: ClassVar[str] = "Status"
    TIME_COLUMNS: ClassVar[Tuple[str, str, str]] = ("Started", "Finished", "Elapsed")
    TIMESTAMP: ClassVar[Pattern[str]] = re.compile(r"^20\d\d-\d\d-\d\d \d\d:\d\d\b")
    ELAPSED: ClassVar[Pattern[str]] = re.compile(r"^\d+h[0-5]\d\b")
    RUNNING_ELAPSED: ClassVar[Pattern[str]] = re.compile(r"^\d+h[0-5]\d so far\b")
    UNKNOWN: ClassVar[str] = "unknown"
    TOTAL_LINE: ClassVar[str] = "**Total time:**"
    DONE: ClassVar[str] = "✅"
    RUNNING: ClassVar[str] = "🔄"
    PAUSED: ClassVar[str] = "⏸️"

    def __init__(self, rules: FolderRules, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the rules and the table reader.

        Args:
            rules (FolderRules): The status icons.
            tables (MarkdownTables): Reads the table.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules
        self.tables = tables

    ############################
    # Internal Helpers Methods #
    ############################

    def _needed(self, status: str, columns: Tuple[int, int, int]) -> List[Tuple[int, Pattern[str]]]:
        """Give the time cells a step's status needs, and their shape.

        Args:
            status (str): The status cell.
            columns (Tuple[int, int, int]): The started, finished and elapsed columns.

        Returns:
            List[Tuple[int, Pattern[str]]]: Each needed column with the pattern its cell matches.
        """
        started, finished, elapsed = columns
        if status.startswith(self.DONE):
            return [(started, self.TIMESTAMP), (finished, self.TIMESTAMP), (elapsed, self.ELAPSED)]
        if status.startswith(self.RUNNING):
            return [(started, self.TIMESTAMP), (elapsed, self.RUNNING_ELAPSED)]
        if status.startswith(self.PAUSED):
            return [(started, self.TIMESTAMP)]
        return []

    def _row_problems(self, folder: TicketFolder, header: List[str], row: List[str]) -> List[str]:
        """List what a Status row lacks.

        Args:
            folder (TicketFolder): The ticket folder.
            header (List[str]): The table's header.
            row (List[str]): The row.

        Returns:
            List[str]: Its problems.
        """
        label = folder.label(self.PROGRESS)
        status_index = header.index(self.STATUS_COLUMN) if self.STATUS_COLUMN in header else 1
        status = row[status_index] if len(row) > status_index else ""
        if not status.startswith(tuple(self.rules.status_icons)):
            return [f"{label}: Status row '{row[0]}' has no status icon"]
        if not all(column in header for column in self.TIME_COLUMNS):
            return []
        columns = (header.index("Started"), header.index("Finished"), header.index("Elapsed"))
        if len(row) <= max(columns):
            return [f"{label}: Status row '{row[0]}' misses time cells"]
        return [
            f"{label}: Status row '{row[0]}' has no valid {header[index]} time ('{row[index]}')"
            for index, pattern in self._needed(status, columns)
            if not (pattern.match(row[index]) or row[index].startswith(self.UNKNOWN))
        ]

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the Status rows without an icon or their times, and a missing total.

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
        problems: List[str] = []
        for row in self.tables.rows(text, self.SECTION):
            problems += self._row_problems(folder, header, row)
        if header and not all(column in header for column in self.TIME_COLUMNS):
            problems.append(f"{label}: Status table lacks the {' / '.join(self.TIME_COLUMNS)} columns")
        if self.TOTAL_LINE not in text:
            problems.append(f"{label}: '{self.TOTAL_LINE}' line missing under the Status table")
        self.logger.debug("%s's Status table has %d problems.", folder.key, len(problems))
        return problems
