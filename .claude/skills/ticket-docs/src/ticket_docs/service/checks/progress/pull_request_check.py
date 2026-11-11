from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from typing import ClassVar, List, Optional, Pattern

# First-party imports
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class PullRequestCheck(TicketCheck):
    """Checks PROGRESS.md's Pull request section (GIT-5) and that an open pull request has its PR review section.

    Attributes:
        PROGRESS (str): The progress file.
        SECTION (str): The Pull request section's heading.
        REVIEW_SECTION (Pattern[str]): The PR review section's heading.
        DESCRIPTION (Pattern[str]): A description, in a ``text`` code block.
        SLOT (str): The start of the template's description, a slot still to fill.
        MAX_LINES (int): The longest description allowed, blank lines included.
        catalog (GithubCatalog): The repository, whose pull request links are searched.
        tables (MarkdownTables): Reads the section.
        logger (Logger): Logger instance.
    """

    PROGRESS: ClassVar[str] = "PROGRESS.md"
    SECTION: ClassVar[str] = "## Pull request"
    REVIEW_SECTION: ClassVar[Pattern[str]] = re.compile(r"^## PR review\s*$", re.M)
    DESCRIPTION: ClassVar[Pattern[str]] = re.compile(r"^```text\n(.*?)\n```", re.M | re.S)
    SLOT: ClassVar[str] = "<"
    MAX_LINES: ClassVar[int] = 10

    def __init__(self, catalog: GithubCatalog, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the repository and the section reader.

        Args:
            catalog (GithubCatalog): The repository, whose pull request links are searched.
            tables (MarkdownTables): Reads the section.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.catalog = catalog
        self.tables = tables

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the descriptions over 10 lines or without ``Closes #<n>``, and a missing PR review section.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem, none when PROGRESS.md does not exist.
        """
        text = folder.text(self.PROGRESS)
        section = self.tables.section(text or "", self.SECTION, nested=True)
        if text is None or section is None:
            return []
        label = folder.label(self.PROGRESS)
        closes = f"Closes #{folder.key.split('-', 1)[1]}"
        problems: List[str] = []
        for number, description in enumerate(self.DESCRIPTION.findall(section), start=1):
            if description.startswith(self.SLOT):
                continue
            lines = len(description.split("\n"))
            if lines > self.MAX_LINES:
                problems.append(
                    f"{label}: pull request description #{number} has {lines} lines, {self.MAX_LINES} at most (GIT-5)"
                )
            if not re.search(rf"\b{re.escape(closes)}\b", description):
                problems.append(f"{label}: pull request description #{number} does not contain '{closes}' (GIT-5)")
        link = rf"github\.com/{re.escape(self.catalog.owner)}/{re.escape(self.catalog.repository)}/pull/\d+"
        if re.search(link, section) and not self.REVIEW_SECTION.search(text):
            problems.append(
                f"{label}: the pull request is open but there is no '## PR review' section (pr-review-followup skill)"
            )
        self.logger.debug("%s's Pull request section has %d problems.", folder.key, len(problems))
        return problems
