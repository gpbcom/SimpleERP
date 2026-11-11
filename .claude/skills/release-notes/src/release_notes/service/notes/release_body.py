from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# Third-party imports
import httpx

# First-party imports
from harness_core.github.exceptions import SEGithubError
from harness_core.github.github_connection import GithubConnection
from harness_core.github.github_token import GithubToken
from harness_core.markdown.markdown_text import MarkdownText
from release_notes.models.catalogs.github_api import GithubApi
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.service.changelog.changelog_document import ChangelogDocument
from release_notes.service.exceptions import SEVersionNotFoundError
from release_notes.storage.files.text_files import TextFiles
from release_notes.storage.github.issue_comments import IssueComments


class ReleaseBody:
    """Writes the GitHub Release body of a version: its changelog, its issues' release notes, their upgrade notes.

    Attributes:
        NOTES_HEADING (str): The heading of the release notes part.
        UPGRADE_HEADING (str): The heading of the upgrade notes part, and of a note's own section.
        NOTHING_TO_DO (str): What a note says when an upgrade needs nothing.
        files (TextFiles): The repository's files.
        coordinates (GithubCoordinates): The repository on GitHub.
        api (GithubApi): How GitHub's REST API is read.
        token (GithubToken): Finds the GitHub token.
        marker (str): The first line of a release note comment.
        transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
        logger (Logger): Logger instance.

    Notes:
        - The issues are the ones the version's section links, in the order they first appear.
        - An issue's note is its last comment that starts with the marker, the latest edit of the note.
        - **A note that is missing or cannot be read becomes a line saying so**, never a failure: the Release is
          published with what is known, and the line shows what to add.
    """

    NOTES_HEADING: ClassVar[str] = "## Release notes"
    UPGRADE_HEADING: ClassVar[str] = "Upgrade notes"
    NOTHING_TO_DO: ClassVar[str] = "Nothing to do."

    def __init__(
        self,
        files: TextFiles,
        coordinates: GithubCoordinates,
        api: GithubApi,
        token: GithubToken,
        marker: str,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set where the changelog and the notes are read.

        Args:
            files (TextFiles): The repository's files.
            coordinates (GithubCoordinates): The repository on GitHub.
            api (GithubApi): How GitHub's REST API is read.
            token (GithubToken): Finds the GitHub token.
            marker (str): The first line of a release note comment.
            transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
            logger (Optional[Logger]): Logger instance.
        """
        self.files = files
        self.coordinates = coordinates
        self.api = api
        self.token = token
        self.marker = marker
        self.transport = transport
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _issues(self, section: str) -> List[int]:
        """List the issues a section links.

        Args:
            section (str): The version's section.

        Returns:
            List[int]: The issue numbers, in the order they first appear.
        """
        link = re.escape(
            self.coordinates.ISSUE_LINK.format(
                owner=self.coordinates.owner, repository=self.coordinates.repository, number=""
            )
        )
        numbers = [int(found) for found in re.findall(rf"{link}(\d+)", section)]
        return list(dict.fromkeys(numbers))

    async def _notes(self, numbers: List[int]) -> Dict[int, str]:
        """Read each issue's release note, or the line that replaces it.

        Args:
            numbers (List[int]): The issue numbers.

        Returns:
            Dict[int, str]: Each issue's note without its marker line, or the line saying why there is none.
        """
        try:
            token = self.token.read()
        except SEGithubError as error:
            self.logger.warning("No GitHub token: the release notes are not read.")
            return {number: self._unread(number, error) for number in numbers}
        notes: Dict[int, str] = {}
        connection = GithubConnection(self.api.api_url, self.api.api_version, token, self.transport, self.logger)
        try:
            comments = IssueComments(connection, self.coordinates, self.logger)
            for number in numbers:
                try:
                    bodies = await comments.bodies(number)
                except SEGithubError as error:
                    self.logger.warning("The comments of issue #%d could not be read.", number)
                    notes[number] = self._unread(number, error)
                    continue
                found = [body for body in bodies if body.lstrip().startswith(self.marker)]
                notes[number] = (
                    found[-1].lstrip().removeprefix(self.marker).strip()
                    if found
                    else f"No release note was found on issue #{number}."
                )
        finally:
            await connection.aclose()
        return notes

    def _unread(self, number: int, error: Exception) -> str:
        """Write the line of a note that could not be read.

        Args:
            number (int): The issue number.
            error (Exception): Why it could not be read.

        Returns:
            str: The line, naming the error's type only.
        """
        return f"The release note of issue #{number} could not be read ({type(error).__name__})."

    def _upgrade(self, note: str) -> Optional[str]:
        """Give what a note asks of an upgrade.

        Args:
            note (str): The note.

        Returns:
            Optional[str]: Its upgrade notes, or ``None`` when it has none or they say there is nothing to do.
        """
        section = (MarkdownText.section(note, self.UPGRADE_HEADING) or "").strip()
        if not section or section.rstrip(".").lower() == self.NOTHING_TO_DO.rstrip(".").lower():
            return None
        return section

    ############################
    # Publicly Exposed Methods #
    ############################

    async def text(self, version: str) -> str:
        """Write the Release body of a version.

        Args:
            version (str): The version, such as ``1.4.0``.

        Returns:
            str: The body: the CHANGELOG section, the release notes, then the upgrade notes.

        Raises:
            SEVersionNotFoundError: When CHANGELOG.md has no section for the version.
        """
        section = ChangelogDocument(self.files.read(ChangelogDocument.PATH), self.logger).section(version)
        if section is None:
            self.logger.error("CHANGELOG.md has no section for %s.", version)
            raise SEVersionNotFoundError(
                f"CHANGELOG.md has no section for {version}. "  # noqa: E501
                f"Run release-notes build {version} on the release branch first."
            )
        numbers = self._issues(section)
        notes = await self._notes(numbers)
        upgrades = [(number, self._upgrade(notes[number])) for number in numbers]
        upgrade_parts = [f"### GH-{number}\n\n{text}" for number, text in upgrades if text is not None]
        parts = [
            section,
            self.NOTES_HEADING,
            *[notes[number] for number in numbers],
            f"## {self.UPGRADE_HEADING}",
            *(upgrade_parts or [self.NOTHING_TO_DO]),
        ]
        self.logger.info("Wrote the Release body of %s with %d issues.", version, len(numbers))
        return "\n\n".join(parts) + "\n"
