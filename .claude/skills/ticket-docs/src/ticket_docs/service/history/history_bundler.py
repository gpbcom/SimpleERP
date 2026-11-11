from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from ticket_docs.models.github.github_catalog import GithubCatalog
from ticket_docs.service.history.target_branch import TargetBranch
from ticket_docs.storage.evidence.evidence_repository import EvidenceRepository


class HistoryBundler:
    """Saves a branch's commits before they are squashed, so that TEST-7 stays provable (GIT-4).

    Attributes:
        HISTORY (str): The folder of the bundles, in the ticket's evidence.
        PREFIX (str): The start of a bundle's name.
        LIST_SUFFIX (str): The suffix of the file that lists a bundle's commits.
        BASE_SUFFIX (str): The suffix of the file that records the commit a bundle's history starts after.
        repository (GitRepository): The repository whose branch is saved.
        evidence (EvidenceRepository): The evidence folders.
        catalog (GithubCatalog): The integration and production branches.
        target (TargetBranch): Finds the branch the current one starts from.
        logger (Logger): Logger instance.

    Notes:
        - The base is ``origin/develop``, or ``origin/master`` for a hotfix or release branch (GIT-8).
        - Next to each bundle, a ``.txt`` lists its commits (``<hash> <subject>``), readable without git, and a
          ``.base`` records the merge base the history starts after, kept as evidence of the squash.
        - A bundle is never replaced: a second one in the same minute gets ``-2``.
    """

    HISTORY: ClassVar[str] = "history"
    PREFIX: ClassVar[str] = "pre-squash-"
    LIST_SUFFIX: ClassVar[str] = ".txt"
    BASE_SUFFIX: ClassVar[str] = ".base"

    def __init__(
        self,
        repository: GitRepository,
        evidence: EvidenceRepository,
        catalog: GithubCatalog,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the repository and where the bundles go.

        Args:
            repository (GitRepository): The repository whose branch is saved.
            evidence (EvidenceRepository): The evidence folders.
            catalog (GithubCatalog): The integration and production branches.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.evidence = evidence
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)
        self.target = TargetBranch(catalog, self.logger)

    ############################
    # Internal Helpers Methods #
    ############################

    def _free_path(self, ticket: str) -> Path:
        """Give a bundle path that does not exist yet.

        Args:
            ticket (str): The ticket.

        Returns:
            Path: ``history/pre-squash-<YYYYMMDD-HHMM>.bundle``, with ``-2`` and on when taken.
        """
        folder = self.evidence.evidence_dir(ticket) / self.HISTORY
        name = f"{self.PREFIX}{datetime.now():%Y%m%d-%H%M}"
        path = folder / f"{name}.bundle"
        suffix = 2
        while path.exists():
            path = folder / f"{name}-{suffix}.bundle"
            suffix += 1
        return path

    ############################
    # Publicly Exposed Methods #
    ############################

    def bundle(self, ticket: str) -> Path:
        """Save the branch's commits since its base, with their list and the base.

        Args:
            ticket (str): The ticket.

        Returns:
            Path: The bundle.

        Raises:
            SEGitCommandFailedError: When the branch has no commit of its own, or git cannot write the bundle.
        """
        base = self.target.of(self.repository)
        path = self._free_path(ticket)
        self.repository.create_bundle(path, base, "HEAD")
        commits = self.repository.commit_subjects(base, "HEAD")
        path.with_suffix(self.LIST_SUFFIX).write_text("".join(f"{line}\n" for line in commits), encoding="utf-8")
        merge_base = self.repository.merge_base(base, "HEAD")
        path.with_suffix(self.BASE_SUFFIX).write_text(f"{merge_base}\n", encoding="utf-8")
        self.logger.info("Saved %d commits of %s in %s.", len(commits), ticket, path.name)
        return path
