from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, List, Optional, Tuple


class MarkdownText:
    """Reads the parts of a Markdown document the harness tools check: links, code blocks, headings and sections.

    Attributes:
        FENCE_PATTERN (re.Pattern[str]): The opening or closing line of a fenced code block, and its language.
        INLINE_CODE_PATTERN (re.Pattern[str]): An inline code span.
        LINK_PATTERN (re.Pattern[str]): An inline link or image, and its target.
        HEADING_PATTERN (re.Pattern[str]): An ATX heading, its level and its title.

    Notes:
        - **Code is never read as Markdown**: a link, a heading or a placeholder written inside a fenced block or an
          inline code span is an example, not part of the document.
        - Line numbers start at 1 and count every line of the document, so a message can point at the line.
        - It only reads text: the callers read and write the files.
    """

    FENCE_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^ {0,3}(?P<fence>`{3,}|~{3,})\s*(?P<language>[\w+-]*)")
    INLINE_CODE_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"(`+)(?:.+?)\1")
    LINK_PATTERN: ClassVar[re.Pattern[str]] = re.compile(
        r"!?\[(?:[^\]\\]|\\.)*\]\(\s*(?:<(?P<angled>[^>\n]*)>|(?P<plain>[^)\s]+))(?:\s+(?:\"[^\"]*\"|'[^']*'))?\s*\)"
    )
    HEADING_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*#*\s*$")

    def __init__(self) -> None:
        """Declare the constructor of a class that only holds class methods."""

    ############################
    # Internal Helpers Methods #
    ############################

    @classmethod
    def _blocks(cls, text: str) -> List[Tuple[int, int, str, str]]:
        """Find the fenced code blocks of a document.

        Args:
            text (str): The document.

        Returns:
            List[Tuple[int, int, str, str]]: The line of each opening fence, the line of its closing fence (the last
            line when the block is never closed), its language in lower case, and its content.
        """
        lines = text.splitlines()
        blocks: List[Tuple[int, int, str, str]] = []
        fence = ""
        start = 0
        language = ""
        body: List[str] = []
        for number, line in enumerate(lines, start=1):
            match = cls.FENCE_PATTERN.match(line)
            if not fence:
                if match:
                    fence, start, language, body = match.group("fence"), number, match.group("language").lower(), []
                continue
            closing = match is not None and not match.group("language") and match.group("fence").startswith(fence)
            if closing:
                blocks.append((start, number, language, "".join(f"{item}\n" for item in body)))
                fence = ""
            else:
                body.append(line)
        if fence:
            blocks.append((start, len(lines), language, "".join(f"{item}\n" for item in body)))
        return blocks

    @classmethod
    def _text_lines(cls, text: str) -> List[Tuple[int, str]]:
        """List the lines that are not inside a fenced code block.

        Args:
            text (str): The document.

        Returns:
            List[Tuple[int, str]]: The line number and the line.
        """
        code = {number for start, end, _, _ in cls._blocks(text) for number in range(start, end + 1)}
        return [(number, line) for number, line in enumerate(text.splitlines(), start=1) if number not in code]

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def prose(cls, text: str) -> str:
        """Give the document with its code blanked out.

        Args:
            text (str): The document.

        Returns:
            str: The same number of lines, each ended by a line feed, fenced blocks emptied and inline code spans
            removed.
        """
        kept = dict(cls._text_lines(text))
        return "".join(
            f"{cls.INLINE_CODE_PATTERN.sub('', kept[number]) if number in kept else ''}\n"
            for number in range(1, len(text.splitlines()) + 1)
        )

    @classmethod
    def links(cls, text: str) -> List[Tuple[int, str]]:
        """List the inline links and images outside code.

        Args:
            text (str): The document.

        Returns:
            List[Tuple[int, str]]: The line number and the target of each link, in reading order.
        """
        found: List[Tuple[int, str]] = []
        for number, line in enumerate(cls.prose(text).splitlines(), start=1):
            for match in cls.LINK_PATTERN.finditer(line):
                found.append((number, match.group("angled") if match.group("angled") is not None else match["plain"]))
        return found

    @classmethod
    def fenced_blocks(cls, text: str, language: str) -> List[Tuple[int, str]]:
        """List the fenced code blocks of one language.

        Args:
            text (str): The document.
            language (str): The language written after the opening fence, such as ``mermaid``.

        Returns:
            List[Tuple[int, str]]: The line number of each opening fence and the block's content, fences left out.
        """
        return [(start, body) for start, _, found, body in cls._blocks(text) if found == language.lower()]

    @classmethod
    def headings(cls, text: str, level: int) -> List[str]:
        """List the titles of the headings of one level, outside code.

        Args:
            text (str): The document.
            level (int): The heading level, 1 for ``#``.

        Returns:
            List[str]: The titles, in reading order.
        """
        titles: List[str] = []
        for _, line in cls._text_lines(text):
            match = cls.HEADING_PATTERN.match(line)
            if match and len(match.group("marks")) == level:
                titles.append(match.group("title"))
        return titles

    @classmethod
    def section(cls, text: str, heading: str) -> Optional[str]:
        """Give the content under a heading, up to the next heading of the same or a higher level.

        Args:
            text (str): The document.
            heading (str): The heading's title, compared without case.

        Returns:
            Optional[str]: The lines under the heading, or ``None`` when the document has no such heading.
        """
        wanted = heading.strip().lower()
        level = 0
        code = {number for start, end, _, _ in cls._blocks(text) for number in range(start, end + 1)}
        body: List[str] = []
        for number, line in enumerate(text.splitlines(), start=1):
            match = None if number in code else cls.HEADING_PATTERN.match(line)
            if level and match and len(match.group("marks")) <= level:
                break
            if level:
                body.append(line)
            elif match and match.group("title").strip().lower() == wanted:
                level = len(match.group("marks"))
        if not level:
            return None
        return "".join(f"{line}\n" for line in body)
