from __future__ import annotations

# Standard library imports
import re
from datetime import date
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from release_notes.models.versions.exceptions import SEInvalidSemanticVersionException
from release_notes.models.versions.semantic_version import SemanticVersion
from release_notes.service.exceptions import SEChangelogInvalidError


class ChangelogDocument:
    """The text of CHANGELOG.md, read as Keep a Changelog sections.

    Attributes:
        PATH (str): The changelog, relative to the repository root.
        TITLE (str): Its first line.
        UNRELEASED (str): The heading of the section that comes first.
        SECTION_PATTERN (re.Pattern[str]): Any ``##`` heading.
        RELEASED_PATTERN (re.Pattern[str]): A released section's heading, ``## [x.y.z] - YYYY-MM-DD``.
        text (str): The changelog's text.
        logger (Logger): Logger instance.

    Notes:
        - The ``[Unreleased]`` section comes first, then the released versions, newest first.
        - **A released section is never edited**: ``insert`` only adds a section right after ``[Unreleased]``'s
          block, and keeps everything else as it is.
    """

    PATH: ClassVar[str] = "CHANGELOG.md"
    TITLE: ClassVar[str] = "# Changelog"
    UNRELEASED: ClassVar[str] = "## [Unreleased]"
    SECTION_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^## ")
    RELEASED_PATTERN: ClassVar[re.Pattern[str]] = re.compile(
        r"^## \[(?P<version>\d+\.\d+\.\d+)\] - (?P<date>\d{4}-\d{2}-\d{2})\s*$"
    )

    def __init__(self, text: str, logger: Optional[Logger] = None) -> None:
        """Set the text.

        Args:
            text (str): The changelog's text, empty when the file is missing.
            logger (Optional[Logger]): Logger instance.
        """
        self.text = text
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _headings(self) -> List[Tuple[int, str]]:
        """List the ``##`` headings.

        Returns:
            List[Tuple[int, str]]: The line number and the heading, stripped of trailing spaces.
        """
        return [
            (number, line.rstrip())
            for number, line in enumerate(self.text.splitlines(), start=1)
            if self.SECTION_PATTERN.match(line)
        ]

    def _released(self, heading: str) -> Optional[SemanticVersion]:
        """Read a released section's heading.

        Args:
            heading (str): The heading.

        Returns:
            Optional[SemanticVersion]: Its version, or ``None`` when it is not ``## [x.y.z] - YYYY-MM-DD`` with a real
            date.
        """
        match = self.RELEASED_PATTERN.match(heading)
        if match is None:
            return None
        try:
            date.fromisoformat(match.group("date"))
            return SemanticVersion.parse(match.group("version"))
        except (ValueError, SEInvalidSemanticVersionException):
            return None

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self) -> List[str]:
        """List what is wrong with the changelog's structure.

        Returns:
            List[str]: One line per problem, none when the structure is valid.
        """
        if not self.text.strip():
            return [f"{self.PATH}: missing."]
        problems: List[str] = []
        if self.text.splitlines()[0].rstrip() != self.TITLE:
            problems.append(f'{self.PATH}: does not start with "{self.TITLE}".')
        headings = self._headings()
        if self.UNRELEASED not in [heading for _, heading in headings]:
            problems.append(f"{self.PATH}: no {self.UNRELEASED} section.")
        elif headings[0][1] != self.UNRELEASED:
            problems.append(f"{self.PATH}:{headings[0][0]}: the first section must be {self.UNRELEASED}.")
        previous: Optional[SemanticVersion] = None
        for number, heading in headings:
            if heading == self.UNRELEASED:
                continue
            version = self._released(heading)
            if version is None:
                problems.append(f'{self.PATH}:{number}: invalid heading "{heading}", expected ## [x.y.z] - YYYY-MM-DD.')
                continue
            if previous is not None and version.key >= previous.key:
                problems.append(
                    f"{self.PATH}:{number}: [{version}] comes after [{previous}], versions must be in descending order."
                )
            previous = version
        self.logger.debug("CHANGELOG.md has %d structure problems.", len(problems))
        return problems

    def versions(self) -> List[str]:
        """List the released versions, in the changelog's order.

        Returns:
            List[str]: The versions of the valid released headings.
        """
        found = [self._released(heading) for _, heading in self._headings()]
        return [str(version) for version in found if version is not None]

    def has(self, version: str) -> bool:
        """Tell whether a version has its released section.

        Args:
            version (str): The version, such as ``1.4.0``.

        Returns:
            bool: ``True`` when ``## [<version>] - YYYY-MM-DD`` is there.
        """
        return version in self.versions()

    def section(self, version: str) -> Optional[str]:
        """Give a released section, heading included.

        Args:
            version (str): The version.

        Returns:
            Optional[str]: The section's lines up to the next ``##`` heading, stripped, or ``None`` when it is not
            there.
        """
        lines = self.text.splitlines()
        headings = self._headings()
        for index, (number, heading) in enumerate(headings):
            found = self._released(heading)
            if found is not None and str(found) == version:
                end = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
                return "\n".join(lines[number - 1 : end]).strip()
        return None

    def insert(self, section: str) -> str:
        """Add a released section right after the ``[Unreleased]`` block.

        Args:
            section (str): The section, its heading first.

        Returns:
            str: The changelog's new text.

        Raises:
            SEChangelogInvalidError: When the changelog has no ``[Unreleased]`` section.
        """
        headings = self._headings()
        position = next((index for index, (_, heading) in enumerate(headings) if heading == self.UNRELEASED), None)
        if position is None:
            self.logger.error("CHANGELOG.md has no [Unreleased] section to add a release after.")
            raise SEChangelogInvalidError(
                f"{self.PATH} has no {self.UNRELEASED} section. "  # noqa: E501
                "Restore it from the release-notes template before building a release."
            )
        lines = self.text.splitlines()
        end = headings[position + 1][0] - 1 if position + 1 < len(headings) else len(lines)
        before = "\n".join(lines[:end]).rstrip()
        after = "\n".join(lines[end:]).strip()
        self.logger.info("Added a section after [Unreleased].")
        return f"{before}\n\n{section.strip()}\n" + (f"\n{after}\n" if after else "")
