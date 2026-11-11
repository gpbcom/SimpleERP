from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, FrozenSet, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from harness_core.models.branches.branch_kind import BranchKind
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from ticket_docs.models.github.github_catalog import GithubCatalog


class TargetBranch:
    """Finds the remote branch the current branch starts from and merges into (GIT-8).

    Attributes:
        REMOTE (str): The remote whose branches are the targets.
        HEAD (str): What git calls the commit checked out.
        FROM_PRODUCTION (FrozenSet[BranchKind]): The branches that start from the production branch.
        catalog (GithubCatalog): The integration and production branches.
        logger (Logger): Logger instance.

    Notes:
        A branch name that does not follow GitFlow is taken as starting from the integration branch.
    """

    REMOTE: ClassVar[str] = "origin"
    HEAD: ClassVar[str] = "HEAD"
    FROM_PRODUCTION: ClassVar[FrozenSet[BranchKind]] = frozenset({BranchKind.HOTFIX, BranchKind.RELEASE})

    def __init__(self, catalog: GithubCatalog, logger: Optional[Logger] = None) -> None:
        """Set the branches.

        Args:
            catalog (GithubCatalog): The integration and production branches.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def of(self, repository: GitRepository) -> str:
        """Give the remote branch the current branch of a repository starts from.

        Args:
            repository (GitRepository): The repository.

        Returns:
            str: ``origin/<production>`` for a hotfix or release branch, ``origin/<integration>`` otherwise.
        """
        try:
            kind = BranchName.parse(repository.current_branch() or self.HEAD).kind
        except SEInvalidBranchNameException:
            self.logger.warning("The branch name does not follow GitFlow: develop is taken as the base.")
            kind = BranchKind.OTHER
        branch = self.catalog.production_branch if kind in self.FROM_PRODUCTION else self.catalog.default_branch
        self.logger.debug("The branch starts from %s/%s.", self.REMOTE, branch)
        return f"{self.REMOTE}/{branch}"
