from __future__ import annotations

# Standard library imports
from datetime import date
from logging import Logger, getLogger
from typing import ClassVar, List, Optional, Tuple

# First-party imports
from harness_core.git.git_repository import GitRepository
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.models.fragments.changelog_fragment import ChangelogFragment
from release_notes.models.versions.exceptions import SEInvalidSemanticVersionException
from release_notes.models.versions.semantic_version import SemanticVersion
from release_notes.service.changelog.changelog_document import ChangelogDocument
from release_notes.service.exceptions import SEVersionRefusedError
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.service.versions.version_advisor import VersionAdvisor
from release_notes.storage.files.text_files import TextFiles


class ChangelogBuilder:
    """Builds a version's CHANGELOG.md section from the fragments, then deletes them.

    Attributes:
        BULLETS (Tuple[str, ...]): The list markers a fragment line may start with, removed before the line is listed.
        repository (GitRepository): The repository, read for its tags.
        files (TextFiles): The repository's files.
        reader (FragmentReader): Reads the fragments.
        catalog (ChangelogTypeCatalog): The types, whose order is the subsections' order.
        coordinates (GithubCoordinates): The repository on GitHub, for the issue links.
        logger (Logger): Logger instance.

    Notes:
        - Everything is checked before anything is written: an invalid version, an existing one, an older one, an
          invalid fragment or a changelog without ``[Unreleased]`` leaves every file as it was.
        - The fragments are deleted, not ``git rm``-ed: the caller stages the deletion with the changelog.
    """

    BULLETS: ClassVar[Tuple[str, ...]] = ("- ", "* ")

    def __init__(
        self,
        repository: GitRepository,
        files: TextFiles,
        reader: FragmentReader,
        catalog: ChangelogTypeCatalog,
        coordinates: GithubCoordinates,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what the section is built from.

        Args:
            repository (GitRepository): The repository, read for its tags.
            files (TextFiles): The repository's files.
            reader (FragmentReader): Reads the fragments.
            catalog (ChangelogTypeCatalog): The types, whose order is the subsections' order.
            coordinates (GithubCoordinates): The repository on GitHub, for the issue links.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.files = files
        self.reader = reader
        self.catalog = catalog
        self.coordinates = coordinates
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _refuse(self, message: str) -> SEVersionRefusedError:
        """Log and build the refusal of a version.

        Args:
            message (str): Why the version cannot be released.

        Returns:
            SEVersionRefusedError: The error to raise.
        """
        self.logger.error("The version is refused: %s", message)
        return SEVersionRefusedError(message)

    def _version(self, text: str, document: ChangelogDocument) -> SemanticVersion:
        """Check that a version can be released.

        Args:
            text (str): The version asked for.
            document (ChangelogDocument): The changelog.

        Returns:
            SemanticVersion: The version.

        Raises:
            SEVersionRefusedError: When it is not ``x.y.z``, is already released or tagged, or is not newer than the
                last released one.
        """
        try:
            version = SemanticVersion.parse(text)
        except SEInvalidSemanticVersionException as error:
            raise self._refuse(str(error)) from error
        if document.has(str(version)) or f"{VersionAdvisor.TAG_PREFIX}{version}" in self.repository.tags(
            f"{VersionAdvisor.TAG_PREFIX}{version}"
        ):
            raise self._refuse(f"{version} is already released.")
        released = [SemanticVersion.parse(item) for item in document.versions()]
        latest = max(released, key=lambda item: item.key) if released else None
        if latest is not None and version.key <= latest.key:
            raise self._refuse(f"{version} is not newer than {latest}, the last released version.")
        return version

    def _section(self, version: SemanticVersion, today: date, fragments: List[ChangelogFragment]) -> str:
        """Write the version's section.

        Args:
            version (SemanticVersion): The version.
            today (date): The release date.
            fragments (List[ChangelogFragment]): The fragments.

        Returns:
            str: The section, its heading first.
        """
        parts = [f"## [{version}] - {today.isoformat()}"]
        for kind in self.catalog.types:
            chosen = sorted((item for item in fragments if item.type_name == kind.name), key=lambda item: item.number)
            if not chosen:
                continue
            bullets = []
            for fragment in chosen:
                link = f"([{fragment.ticket}]({self.coordinates.issue_link(fragment.number)}))"
                for line in fragment.lines:
                    text = next((line[len(bullet) :] for bullet in self.BULLETS if line.startswith(bullet)), line)
                    bullets.append(f"- {text.strip()} {link}")
            parts.append(f"### {kind.heading}\n\n" + "\n".join(bullets))
        return "\n\n".join(parts)

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self, version: str, today: date) -> List[str]:
        """Add a version's section to CHANGELOG.md and delete the fragments it used.

        Args:
            version (str): The version, such as ``1.4.0``.
            today (date): The release date written in the heading.

        Returns:
            List[str]: The deleted fragments, relative to the repository root.

        Raises:
            SEVersionRefusedError: When the version cannot be released.
            SEFragmentsRefusedError: When there is no fragment, or one of them is invalid.
            SEChangelogInvalidError: When CHANGELOG.md has no ``[Unreleased]`` section.
        """
        document = ChangelogDocument(self.files.read(ChangelogDocument.PATH), self.logger)
        checked = self._version(version, document)
        fragments = VersionAdvisor(self.repository, self.reader, self.logger).fragments()
        text = document.insert(self._section(checked, today, fragments))
        self.files.write(ChangelogDocument.PATH, text)
        deleted = []
        for fragment in sorted(fragments, key=lambda item: item.file_name):
            path = self.reader.path(fragment.file_name)
            self.files.delete(path)
            deleted.append(path)
        self.logger.info("Built %s from %d fragments.", checked, len(deleted))
        return deleted
