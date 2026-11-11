from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, Pattern


class MarkdownTables:
    """Reads the sections and tables of the ticket folder's Markdown files.

    Attributes:
        FENCE (Pattern[str]): A fenced code block.
        COMMENT (Pattern[str]): An HTML comment, on one line or several.
        INLINE_CODE (Pattern[str]): Inline code.
        CELL_SPLIT (Pattern[str]): A pipe that separates two cells, an escaped one excepted.
        logger (Logger): Logger instance.

    Notes:
        ``prose`` blanks code and comments but keeps every new line, so that line numbers still match the file.
    """

    FENCE: ClassVar[Pattern[str]] = re.compile(r"^```.*?^```[^\n]*$", re.M | re.S)
    COMMENT: ClassVar[Pattern[str]] = re.compile(r"<!--.*?-->", re.S)
    INLINE_CODE: ClassVar[Pattern[str]] = re.compile(r"`[^`\n]*`")
    CELL_SPLIT: ClassVar[Pattern[str]] = re.compile(r"(?<!\\)\|")

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _blank(self, match: re.Match[str]) -> str:
        """Blank a match but keep its new lines.

        Args:
            match (re.Match[str]): The code or comment.

        Returns:
            str: Its new lines only.
        """
        return "\n" * match.group(0).count("\n")

    def _table_lines(self, text: str, heading: str) -> List[str]:
        """Give the table lines of a section, its sub-sections left out.

        Args:
            text (str): The Markdown text.
            heading (str): The section heading.

        Returns:
            List[str]: The lines that start with a pipe, stripped.
        """
        section = self.section(text, heading) or ""
        return [line.strip() for line in section.splitlines() if line.strip().startswith("|")]

    ############################
    # Publicly Exposed Methods #
    ############################

    def section(self, text: str, heading: str, nested: bool = False) -> Optional[str]:
        """Give the text of a section.

        Args:
            text (str): The Markdown text.
            heading (str): The section heading, such as ``## Status``.
            nested (bool): Whether its sub-sections belong to it.

        Returns:
            Optional[str]: The text under the heading, ``None`` when there is no such heading.
        """
        level = len(heading) - len(heading.lstrip("#"))
        stop = rf"^#{{1,{level}}} " if nested and level else r"^#"
        match = re.search(rf"^{re.escape(heading)}\s*$(.*?)(?={stop}|\Z)", text, re.M | re.S)
        return match.group(1) if match else None

    def cells(self, line: str) -> List[str]:
        """Split a table line into its cells.

        Args:
            line (str): The line.

        Returns:
            List[str]: The cells, stripped, escaped pipes kept.
        """
        return [cell.strip() for cell in self.CELL_SPLIT.split(line.strip().strip("|"))]

    def header(self, text: str, heading: str) -> List[str]:
        """Give the header cells of a section's table.

        Args:
            text (str): The Markdown text.
            heading (str): The section heading.

        Returns:
            List[str]: The header cells, empty when the section has no table.
        """
        lines = self._table_lines(text, heading)
        return self.cells(lines[0]) if lines else []

    def rows(self, text: str, heading: str) -> List[List[str]]:
        """Give the rows of a section's table, its header and separator left out.

        Args:
            text (str): The Markdown text.
            heading (str): The section heading.

        Returns:
            List[List[str]]: The cells of each row.
        """
        return [self.cells(line) for line in self._table_lines(text, heading)[2:]]

    def without_blocks(self, text: str) -> str:
        """Blank the code blocks and HTML comments of a text, inline code kept.

        Args:
            text (str): The Markdown text.

        Returns:
            str: The text without them, with as many lines.
        """
        return self.COMMENT.sub(self._blank, self.FENCE.sub(self._blank, text))

    def prose(self, text: str) -> str:
        """Blank the code blocks, HTML comments and inline code of a text.

        Args:
            text (str): The Markdown text.

        Returns:
            str: The text without them, with as many lines.
        """
        return self.INLINE_CODE.sub("", self.without_blocks(text))
