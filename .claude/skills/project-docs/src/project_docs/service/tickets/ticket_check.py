from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# First-party imports
from harness_core.markdown.markdown_text import MarkdownText
from harness_core.models.branches.branch_name import BranchName
from project_docs.service.exceptions import SETicketKeyInvalidError
from project_docs.storage.files.document_files import DocumentFiles


class TicketCheck:
    """Checks that a ticket handled every chapter its branch concerns: changed, or waived in its PROGRESS.md.

    Attributes:
        PROGRESS (str): The ticket's PROGRESS.md, with ``{key}`` for the ticket.
        SECTION (str): The PROGRESS.md section that lists the chapters.
        WAIVER (str): The words that waive a chapter left as it is.
        SHOWN_PATHS (int): The most paths named in one problem.
        files (DocumentFiles): The repository's files.
        logger (Logger): Logger instance.

    Notes:
        - A chapter is waived by a table row of the ``Documentation`` section that names it and holds
          ``no doc impact:``, such as ``| docs/technical/api.md | ✅ | no doc impact: internal refactoring |``.
        - **The chapter must be named as a whole path**: a row naming ``docs/technical/README.md`` does not waive
          ``README.md``.
    """

    PROGRESS: ClassVar[str] = "docs/tickets/{key}/PROGRESS.md"
    SECTION: ClassVar[str] = "Documentation"
    WAIVER: ClassVar[str] = "no doc impact:"
    SHOWN_PATHS: ClassVar[int] = 5

    def __init__(self, files: DocumentFiles, logger: Optional[Logger] = None) -> None:
        """Set the files.

        Args:
            files (DocumentFiles): The repository's files.
            logger (Optional[Logger]): Logger instance.
        """
        self.files = files
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _waived(self, rows: List[str], chapter: str) -> bool:
        """Tell whether a row of the Documentation section waives a chapter.

        Args:
            rows (List[str]): The section's table rows that hold the waiver words.
            chapter (str): The chapter.

        Returns:
            bool: ``True`` when a row names the chapter as a whole path.
        """
        pattern = re.compile(rf"(?<![\w/.-]){re.escape(chapter)}(?![\w/.-])")
        return any(pattern.search(row) for row in rows)

    def _paths(self, paths: List[str]) -> str:
        """Name the paths that concern a chapter, the first few only.

        Args:
            paths (List[str]): The paths.

        Returns:
            str: The paths, joined, and how many more there are.
        """
        shown = ", ".join(paths[: self.SHOWN_PATHS])
        hidden = len(paths) - self.SHOWN_PATHS
        return f"{shown} and {hidden} more" if hidden > 0 else shown

    ############################
    # Publicly Exposed Methods #
    ############################

    def unhandled(self, key: str, mapping: Dict[str, List[str]], changed: List[str]) -> List[str]:
        """List the chapters the branch concerns that were neither changed nor waived.

        Args:
            key (str): The ticket, such as ``GH-12``.
            mapping (Dict[str, List[str]]): Each chapter the branch concerns, with the paths that concern it.
            changed (List[str]): The paths the branch changed.

        Returns:
            List[str]: One line per chapter left unhandled.

        Raises:
            SETicketKeyInvalidError: When the key is not ``GH-<n>``.
        """
        if not BranchName.TICKET_PATTERN.match(key):
            self.logger.error("The ticket key %r is not GH-<n>.", key)
            raise SETicketKeyInvalidError(
                f"Invalid ticket: {key!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        progress = self.PROGRESS.format(key=key)
        section = MarkdownText.section(self.files.read(progress), self.SECTION) or ""
        rows = [row for row in section.splitlines() if row.lstrip().startswith("|") and self.WAIVER in row]
        problems = []
        for chapter, paths in mapping.items():
            if chapter not in changed and not self._waived(rows, chapter):
                problems.append(
                    f"{chapter}: concerned by {self._paths(paths)} but neither changed in the branch nor waived"
                    f' with "{self.WAIVER}" in {progress}.'
                )
        self.logger.info("%s leaves %d of %d chapters unhandled.", key, len(problems), len(mapping))
        return problems
