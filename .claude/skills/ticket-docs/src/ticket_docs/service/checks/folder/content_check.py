from __future__ import annotations

# Standard library imports
import re
from logging import Logger
from pathlib import Path
from typing import ClassVar, List, Optional, Pattern, Tuple

# First-party imports
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.service.checks.markdown_tables import MarkdownTables
from ticket_docs.service.checks.ticket_check import TicketCheck
from ticket_docs.service.checks.ticket_folder import TicketFolder


class ContentCheck(TicketCheck):
    """Checks every Markdown file of the folder for placeholders, slots, secrets and broken links.

    Attributes:
        SECRET (Pattern[str]): What a token, a signed URL or a password looks like.
        LINK (Pattern[str]): A Markdown link.
        EXTERNAL (Tuple[str, ...]): The link prefixes that are not files of the folder.
        TEMPLATE_SLOT (Pattern[str]): A ``<…>`` slot of a template, HTML tags excepted.
        rules (FolderRules): The placeholders and the files finished at hand-over.
        tables (MarkdownTables): Blanks code and comments.
        logger (Logger): Logger instance.

    Notes:
        - Links inside code blocks and HTML comments are examples and are not followed.
        - A link to a hand-over file, such as RELEASE-NOTE.md, may point at nothing until the hand-over.
    """

    SECRET: ClassVar[Pattern[str]] = re.compile(
        r"eyJ[A-Za-z0-9_-]{20,}|X-Amz-Security-Token|X-Amz-Signature|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_\w{20,}"
        r"|(?i:password)\s*[:=]\s*[^\s$<]\S*"
    )
    LINK: ClassVar[Pattern[str]] = re.compile(r"\]\(([^)\s]+)\)")
    EXTERNAL: ClassVar[Tuple[str, ...]] = ("http://", "https://", "mailto:")
    TEMPLATE_SLOT: ClassVar[Pattern[str]] = re.compile(
        r"<(?!/?(?:sub|sup|br|details|summary|img|a|b|i|kbd|p|span|div)\b)[^<>\n]{2,120}>"
    )

    def __init__(self, rules: FolderRules, tables: MarkdownTables, logger: Optional[Logger] = None) -> None:
        """Set the rules.

        Args:
            rules (FolderRules): The placeholders and the files finished at hand-over.
            tables (MarkdownTables): Blanks code and comments.
            logger (Optional[Logger]): Logger instance.
        """
        super().__init__(logger)
        self.rules = rules
        self.tables = tables

    ############################
    # Internal Helpers Methods #
    ############################

    def _links(self, path: Path, prose: str, handed_over: bool) -> List[str]:
        """List the relative links of a file that point at nothing.

        Args:
            path (Path): The file.
            prose (str): Its text without code and comments.
            handed_over (bool): Whether the hand-over files must exist.

        Returns:
            List[str]: The broken links.
        """
        broken = []
        for link in self.LINK.findall(prose):
            target = link.split("#", 1)[0]
            if not target or target.startswith(self.EXTERNAL) or (path.parent / target).exists():
                continue
            if not handed_over and Path(target).name in self.rules.handover_files:
                continue
            broken.append(link)
        return broken

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, folder: TicketFolder) -> List[str]:
        """List the placeholders, slots, secrets and broken links of the folder's Markdown files.

        Args:
            folder (TicketFolder): The ticket folder.

        Returns:
            List[str]: One line per problem.
        """
        handed_over = folder.handed_over()
        problems: List[str] = []
        for path in folder.tickets.markdown(folder.key):
            relative = str(path.relative_to(folder.path))
            label = folder.label(relative)
            text = path.read_text(encoding="utf-8")
            prose = self.tables.prose(text)
            problems += [
                f"{label}: template placeholder {name} left" for name in self.rules.placeholders if name in text
            ]
            if self.SECRET.search(text):
                problems.append(f"{label}: looks like a secret")
            problems += [f"{label}: broken link {link}" for link in self._links(path, prose, handed_over)]
            slots = sorted(set(self.TEMPLATE_SLOT.findall(prose)))
            if handed_over and relative in self.rules.finished_files and slots:
                problems.append(f"{label}: template slots left: {', '.join(slots[:5])}")
        self.logger.debug("%s has %d content problems.", folder.key, len(problems))
        return problems
