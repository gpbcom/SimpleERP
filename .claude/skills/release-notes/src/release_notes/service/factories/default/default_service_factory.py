from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# Third-party imports
import httpx

# First-party imports
from harness_core.git.git_repository import GitRepository
from harness_core.github.github_token import GithubToken
from release_notes.models.catalogs.changelog_type_catalog import ChangelogTypeCatalog
from release_notes.models.catalogs.github_api import GithubApi
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.models.settings.release_notes_settings import ReleaseNotesSettings
from release_notes.service.changelog.changelog_builder import ChangelogBuilder
from release_notes.service.checks.branch_check import BranchCheck
from release_notes.service.checks.release_note_check import ReleaseNoteCheck
from release_notes.service.factories.service_factory import ServiceFactory
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.service.notes.release_body import ReleaseBody
from release_notes.service.versions.version_advisor import VersionAdvisor
from release_notes.storage.files.text_files import TextFiles


class DefaultServiceFactory(ServiceFactory):
    """Builds the real services, on the repository that holds the caller's folder.

    Attributes:
        settings (ReleaseNotesSettings): Where the tool reads.
        catalog (ChangelogTypeCatalog): The fragment types.
        transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport to GitHub, a stand-in in tests.
        logger (Logger): Logger instance.
    """

    def __init__(
        self,
        settings: ReleaseNotesSettings,
        catalog: ChangelogTypeCatalog,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the settings and the fragment types.

        Args:
            settings (ReleaseNotesSettings): Where the tool reads.
            catalog (ChangelogTypeCatalog): The fragment types.
            transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport to GitHub, by default the network.
            logger (Optional[Logger]): Logger instance.
        """
        self.settings = settings
        self.catalog = catalog
        self.transport = transport
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _repository(self) -> GitRepository:
        """Find the caller's repository.

        Returns:
            GitRepository: The repository at the working tree's top level.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
        repository = GitRepository.discover(self.settings.caller_cwd, self.logger)
        self.logger.debug("The repository is %s.", repository.root)
        return repository

    def _template(self) -> str:
        """Read the release note template.

        Returns:
            str: The template, empty when it cannot be read.
        """
        return TextFiles(self.settings.skill_dir, self.logger).read(
            self.settings.release_note_template.relative_to(self.settings.skill_dir).as_posix()
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def branch_check(self) -> BranchCheck:
        """Build the check of a branch's changelog and fragments.

        Returns:
            BranchCheck: The check.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
        repository = self._repository()
        files = TextFiles(repository.root, self.logger)
        return BranchCheck(repository, files, FragmentReader(files, self.catalog, self.logger), self.logger)

    def release_note_check(self) -> ReleaseNoteCheck:
        """Build the check of a ticket's release note.

        Returns:
            ReleaseNoteCheck: The check.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
        return ReleaseNoteCheck(TextFiles(self._repository().root, self.logger), self._template(), self.logger)

    def version_advisor(self) -> VersionAdvisor:
        """Build the advisor of the next version.

        Returns:
            VersionAdvisor: The advisor.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """
        repository = self._repository()
        files = TextFiles(repository.root, self.logger)
        return VersionAdvisor(repository, FragmentReader(files, self.catalog, self.logger), self.logger)

    def changelog_builder(self) -> ChangelogBuilder:
        """Build the builder of a version's CHANGELOG.md section.

        Returns:
            ChangelogBuilder: The builder.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
            SEGithubCoordinatesUnreadable: When the repository's GitHub coordinates cannot be read.
        """
        repository = self._repository()
        files = TextFiles(repository.root, self.logger)
        return ChangelogBuilder(
            repository,
            files,
            FragmentReader(files, self.catalog, self.logger),
            self.catalog,
            GithubCoordinates.load(self.settings.github_file),
            self.logger,
        )

    def release_body(self) -> ReleaseBody:
        """Build the writer of a version's GitHub Release body.

        Returns:
            ReleaseBody: The writer.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
            SEGithubCoordinatesUnreadable: When the repository's GitHub coordinates cannot be read.
            SEGithubApiUnreadable: When the GitHub API configuration cannot be read.
        """
        marker = ReleaseNoteCheck(TextFiles(self.settings.skill_dir, self.logger), self._template(), self.logger).marker
        return ReleaseBody(
            TextFiles(self._repository().root, self.logger),
            GithubCoordinates.load(self.settings.github_file),
            GithubApi.load(self.settings.github_api_file),
            GithubToken(self.logger),
            marker,
            self.transport,
            self.logger,
        )
