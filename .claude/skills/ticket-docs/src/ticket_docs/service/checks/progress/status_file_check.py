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


class StatusFileCheck(TicketCheck):
    """Checks STATUS.md: an icon on every entry, and a complete entry for every rebase conflict.

    Attributes:
        PROGRESS (str): The progress file.
        STATUS (str): The status file.
        ENTRY (Pattern[str]): A dated entry's heading.
        REBASE_MENTION (Pattern[str]): A rebase conflict named in PROGRESS.md.
        REBASE_ENTRY (Pattern[str]): A rebase-conflict entry's heading.
        FAILED (str): The icon of an open rebase-conflict entry, which needs every part.
        ENTRY_SECTIONS (Tuple[str, ...]): The parts of an open rebase-conflict entry.
        rules (FolderRules): The status icons.
        tables (MarkdownTables): Blanks code and comments.
        logger (Logger): Logger instance.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    STATUS: ClassVar[str] = "STATUS.md"
    ENTRY: ClassVar[Pattern[str]] = re.compile(r"^## (.+)$", re.M)
    REBASE_MENTION: ClassVar[Pattern[str]] = re.compile(
        r"rebase conflict|need manual rebase|CONFLICT \(content\)", re.I
    )
    REBASE_ENTRY: ClassVar[Pattern[str]] = re.compile(r"rebase conflict", re.I)
    FAILED: ClassVar[str] = "❌"
    ENTRY_SECTIONS: ClassVar[Tuple[str, ...]] = (
        "In short",
        "Conflict",
        "Resolution",
        "Verification",
        "State left behind",
        "How to resume",
    )

    def __init__(self, rules: FolderRules, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the rules and the text reader.

        Args:
            rules (FolderRules): The status icons.
            tables (MarkdownTables): Blanks code and comments.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules
        self.tables = tables

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the entries without an icon, a rebase conflict with no entry, and the entries missing a part.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem.
        """
        label = folder.label(self.STATUS)
        status = self.tables.without_blocks(folder.text(self.STATUS) or "")
        problems = [
            f"{label}: entry '{heading}' does not start with a status icon"
            for heading in self.ENTRY.findall(status)
            if not heading.startswith(tuple(self.rules.status_icons))
        ]
        entries = re.split(r"^## ", status, flags=re.M)[1:]
        conflicts = [entry for entry in entries if self.REBASE_ENTRY.search(entry.splitlines()[0])]
        if self.REBASE_MENTION.search(self.tables.prose(folder.text(self.PROGRESS) or "")) and not conflicts:
            problems.append(f"{label}: PROGRESS.md mentions a rebase conflict, STATUS.md has no rebase-conflict entry")
        for entry in conflicts:
            heading = entry.splitlines()[0].strip()
            if heading.startswith(self.FAILED):
                problems += [
                    f"{label}: entry '{heading}' misses '### {section}'"
                    for section in self.ENTRY_SECTIONS
                    if not re.search(rf"^### {re.escape(section)}\b", entry, re.M)
                ]
        self.logger.debug("%s's STATUS.md has %d problems.", folder.key, len(problems))
        return problems
