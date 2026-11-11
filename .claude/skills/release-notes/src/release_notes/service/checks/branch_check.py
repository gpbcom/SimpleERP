from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from harness_core.models.branches.branch_kind import BranchKind
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from release_notes.service.changelog.changelog_document import ChangelogDocument
from release_notes.service.fragments.fragment_reader import FragmentReader
from release_notes.storage.files.text_files import TextFiles


class BranchCheck:
    """Checks the changelog and the fragments a GitFlow branch must hold (DOC-3, GIT-8).

    Attributes:
        repository (GitRepository): The repository, read for the current branch.
        files (TextFiles): The repository's files.
        reader (FragmentReader): Reads the fragments.
        logger (Logger): Logger instance.

    Notes:
        - Every branch needs a valid CHANGELOG.md structure.
        - A ``feature/`` or ``bugfix/`` branch needs exactly one valid fragment for its ticket. Other tickets'
          fragments, merged from ``develop``, are theirs to check.
        - A ``release/<x.y.z>`` branch needs its built section and no fragment left.
        - A ``hotfix/<x.y.z>-GH-<n>-<slug>`` branch needs its own fragment until it is built, then the same as a
          release.
    """

    def __init__(
        self, repository: GitRepository, files: TextFiles, reader: FragmentReader, logger: Optional[Logger] = None
    ) -> None:
        """Set the repository, the files and the fragment reader.

        Args:
            repository (GitRepository): The repository, read for the current branch.
            files (TextFiles): The repository's files.
            reader (FragmentReader): Reads the fragments.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.files = files
        self.reader = reader
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _ticket_fragment(self, ticket: str) -> List[str]:
        """Check that a ticket has exactly one valid fragment.

        Args:
            ticket (str): The ticket, such as ``GH-12``.

        Returns:
            List[str]: The problems, none when its one fragment is valid.
        """
        own = [name for name in self.reader.names() if name.startswith(f"{ticket}.")]
        if not own:
            return [f"{self.reader.FOLDER}/: no fragment {ticket}.<type>.md for {ticket}."]
        if len(own) > 1:
            return [
                f"{self.reader.FOLDER}/: {len(own)} fragments for {ticket} ({', '.join(own)}), exactly one expected."
            ]
        return self.reader.read(own[0])[1]

    def _released(self, document: ChangelogDocument, version: str) -> List[str]:
        """Check that a version is built: its section is there and no fragment is left.

        Args:
            document (ChangelogDocument): The changelog.
            version (str): The version.

        Returns:
            List[str]: The problems, none when the release is built.
        """
        problems = [] if document.has(version) else [f"{document.PATH}: no section ## [{version}] - YYYY-MM-DD."]
        problems.extend(
            f"{self.reader.path(name)}: left over, release-notes build {version} moves it into {document.PATH}."
            for name in self.reader.names()
        )
        return problems

    ############################
    # Publicly Exposed Methods #
    ############################

    def problems(self, branch: Optional[str]) -> List[str]:
        """List what the branch lacks.

        Args:
            branch (Optional[str]): The branch name, by default the one checked out.

        Returns:
            List[str]: One line per problem, none when DOC-3 holds on the branch.

        Raises:
            SEGitCommandFailedError: When the current branch cannot be read.
        """
        value = branch if branch is not None else self.repository.current_branch()
        try:
            name = BranchName.parse(value)
        except SEInvalidBranchNameException as error:
            self.logger.warning("%s is not a GitFlow branch name.", value)
            return [f"{value}: not a GitFlow branch name. {error}"]
        document = ChangelogDocument(self.files.read(ChangelogDocument.PATH), self.logger)
        problems = document.problems()
        match name.kind:
            case BranchKind.FEATURE | BranchKind.BUGFIX:
                problems.extend(self._ticket_fragment(str(name.ticket)))
            case BranchKind.RELEASE:
                problems.extend(self._released(document, str(name.version)))
            case BranchKind.HOTFIX if document.has(str(name.version)):
                problems.extend(self._released(document, str(name.version)))
            case BranchKind.HOTFIX:
                problems.extend(self._ticket_fragment(str(name.ticket)))
            case _:
                self.logger.debug("%s only needs a valid changelog.", value)
        self.logger.info("%s has %d changelog problems.", value, len(problems))
        return problems
