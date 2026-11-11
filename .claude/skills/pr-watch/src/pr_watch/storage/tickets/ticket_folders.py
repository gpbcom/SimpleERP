from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional


class TicketFolders:
    """Reads the local ticket folders, ``docs/tickets/GH-<n>/``.

    Attributes:
        KEY_PATTERN (re.Pattern[str]): The name of a ticket folder.
        HEADING_PATTERN (re.Pattern[str]): A Markdown heading, its level in the first group.
        SECTION_TITLE (re.Pattern[str]): The title of the section that holds the pull request link.
        LINK_PATTERN (re.Pattern[str]): A GitHub pull request link.
        tickets_dir (Path): The folder of the ticket folders.
        logger (Logger): Logger instance.

    Notes:
        Only the "Pull request" section of ``PROGRESS.md`` is read, so that a link to another ticket's pull request
        written elsewhere in the file is never watched for this one.
    """

    KEY_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^GH-(\d+)$")
    HEADING_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")
    SECTION_TITLE: ClassVar[re.Pattern[str]] = re.compile(r"^pull request\b", re.IGNORECASE)
    LINK_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"https://github\.com/[\w.-]+/[\w.-]+/pull/\d+")

    def __init__(self, tickets_dir: Path, logger: Optional[Logger] = None) -> None:
        """Set the folder of the ticket folders.

        Args:
            tickets_dir (Path): The folder, ``<repository>/docs/tickets``.
            logger (Optional[Logger]): Logger instance.
        """
        self.tickets_dir = tickets_dir
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _section(self, text: str) -> str:
        """Cut the "Pull request" section out of a ``PROGRESS.md``.

        Args:
            text (str): The file.

        Returns:
            str: The section's lines, up to the next heading of the same level or higher, empty when there is none.
        """
        level: Optional[int] = None
        lines: List[str] = []
        for line in text.splitlines():
            heading = self.HEADING_PATTERN.match(line)
            if heading and level is not None and len(heading.group(1)) <= level:
                break
            if heading and level is None and self.SECTION_TITLE.match(heading.group(2)):
                level = len(heading.group(1))
                continue
            if level is not None:
                lines.append(line)
        return "\n".join(lines)

    ############################
    # Publicly Exposed Methods #
    ############################

    def progress_file(self, key: str) -> Path:
        """Give the ``PROGRESS.md`` of a ticket.

        Args:
            key (str): The ticket.

        Returns:
            Path: The file, which may not exist.
        """
        return self.tickets_dir / key / "PROGRESS.md"

    def pull_request_links(self, key: str) -> List[str]:
        """Read the pull request links of a ticket's ``PROGRESS.md``.

        Args:
            key (str): The ticket.

        Returns:
            List[str]: Each distinct link of its "Pull request" section, in order, none when there is no file.
        """
        path = self.progress_file(key)
        if not path.exists():
            self.logger.debug("%s has no PROGRESS.md.", key)
            return []
        links = list(dict.fromkeys(self.LINK_PATTERN.findall(self._section(path.read_text(encoding="utf-8")))))
        self.logger.debug("%s lists %d pull request links.", key, len(links))
        return links

    def ticket_keys(self) -> List[str]:
        """List the tickets that have a folder.

        Returns:
            List[str]: The keys, ``GH-<n>``, by issue number.
        """
        if not self.tickets_dir.exists():
            return []
        found = [
            path.name for path in self.tickets_dir.iterdir() if path.is_dir() and self.KEY_PATTERN.match(path.name)
        ]
        return sorted(found, key=lambda name: int(name.split("-")[1]))
