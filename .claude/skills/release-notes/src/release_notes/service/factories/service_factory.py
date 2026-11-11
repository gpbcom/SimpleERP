from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod

# First-party imports
from release_notes.service.changelog.changelog_builder import ChangelogBuilder
from release_notes.service.checks.branch_check import BranchCheck
from release_notes.service.checks.release_note_check import ReleaseNoteCheck
from release_notes.service.notes.release_body import ReleaseBody
from release_notes.service.versions.version_advisor import VersionAdvisor


class ServiceFactory(ABC):
    """Builds the services the ``release-notes`` commands call."""

    @abstractmethod
    def __init__(self) -> None:
        """Set what the services are built with."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def branch_check(self) -> BranchCheck:
        """Build the check of a branch's changelog and fragments.

        Returns:
            BranchCheck: The check.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """

    @abstractmethod
    def release_note_check(self) -> ReleaseNoteCheck:
        """Build the check of a ticket's release note.

        Returns:
            ReleaseNoteCheck: The check.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """

    @abstractmethod
    def version_advisor(self) -> VersionAdvisor:
        """Build the advisor of the next version.

        Returns:
            VersionAdvisor: The advisor.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
        """

    @abstractmethod
    def changelog_builder(self) -> ChangelogBuilder:
        """Build the builder of a version's CHANGELOG.md section.

        Returns:
            ChangelogBuilder: The builder.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
            SEGithubCoordinatesUnreadable: When the repository's GitHub coordinates cannot be read.
        """

    @abstractmethod
    def release_body(self) -> ReleaseBody:
        """Build the writer of a version's GitHub Release body.

        Returns:
            ReleaseBody: The writer.

        Raises:
            SEGitCommandFailedError: When the caller's folder is not inside a git working tree.
            SEGithubCoordinatesUnreadable: When the repository's GitHub coordinates cannot be read.
            SEGithubApiUnreadable: When the GitHub API configuration cannot be read.
        """
