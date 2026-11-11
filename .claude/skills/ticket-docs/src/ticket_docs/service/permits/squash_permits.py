from __future__ import annotations

# Standard library imports
from datetime import UTC, datetime, timedelta
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# First-party imports
from harness_core.git.exceptions import SEGitError
from harness_core.git.git_repository import GitRepository
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from ticket_docs.models.checks.folder_rules import FolderRules
from ticket_docs.models.permits.squash_permit import SquashPermit
from ticket_docs.storage.permits.squash_permit_store import SquashPermitStore


class SquashPermits:
    """Grants and redeems the one-shot permits that let a GIT-4 squash add tests and code in one commit.

    Attributes:
        HEAD (str): What git calls the commit checked out.
        store (SquashPermitStore): Where the permits are kept.
        rules (FolderRules): How long a permit counts.
        logger (Logger): Logger instance.

    Notes:
        - **Only the human grants a permit**, with ``ticket-docs allow-squash <KEY>`` in their own terminal, after
          ``git reset --soft <base>``. The permit records the branch, ``HEAD`` and the staged tree.
        - ``git-gate`` redeems it for the one commit that records exactly that tree on that ``HEAD`` and branch,
          before it expires, and deletes it then. Anything that cannot be read redeems nothing.
    """

    HEAD: ClassVar[str] = "HEAD"

    def __init__(self, store: SquashPermitStore, rules: FolderRules, logger: Optional[Logger] = None) -> None:
        """Set the store and the lifetime.

        Args:
            store (SquashPermitStore): Where the permits are kept.
            rules (FolderRules): How long a permit counts.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.rules = rules
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _carries(self, ticket: str, branch: str) -> bool:
        """Tell whether code for a ticket is written on a branch.

        Args:
            ticket (str): The ticket.
            branch (str): The branch name.

        Returns:
            bool: ``True`` for a feature, bugfix or hotfix branch of that ticket.
        """
        try:
            name = BranchName.parse(branch or self.HEAD)
        except SEInvalidBranchNameException:
            return False
        return name.carries_ticket_work and name.ticket == ticket

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def default(cls, rules: FolderRules, logger: Optional[Logger] = None) -> SquashPermits:
        """Build the permits of the person's home folder.

        Args:
            rules (FolderRules): How long a permit counts.
            logger (Optional[Logger]): Logger instance.

        Returns:
            SquashPermits: The permits kept under ``~/.local/state/claude-harness/squash-permits``.
        """
        return cls(SquashPermitStore.default(Path.home(), logger), rules, logger)

    def grant(self, ticket: str, repository: GitRepository) -> Optional[SquashPermit]:
        """Write a permit for the squash staged now on the ticket's branch.

        Args:
            ticket (str): The ticket.
            repository (GitRepository): The repository, with the squash staged.

        Returns:
            Optional[SquashPermit]: The permit, ``None`` when the current branch does not carry the ticket.

        Raises:
            SESquashPermitStoreError: When the permit cannot be written.
        """
        branch = repository.current_branch()
        if not self._carries(ticket, branch):
            self.logger.warning("%s is not a branch of %s: no squash permit.", branch or "HEAD", ticket)
            return None
        permit = SquashPermit(
            ticket=ticket,
            branch=branch,
            head=repository.head(),
            tree=repository.index_tree(),
            expires_at=datetime.now(UTC) + timedelta(minutes=self.rules.squash_permit_minutes),
        )
        self.store.write(permit)
        self.logger.info("Granted a squash permit to %s for %d minutes.", ticket, self.rules.squash_permit_minutes)
        return permit

    def redeem(self, ticket: str, repository: GitRepository) -> bool:
        """Use the ticket's permit for the commit about to be made, once.

        Args:
            ticket (str): The ticket.
            repository (GitRepository): The repository, with the squash staged.

        Returns:
            bool: ``True`` when an unexpired permit matches the branch, ``HEAD`` and the staged tree exactly. The
            permit is deleted then.
        """
        permit = self.store.read(ticket)
        if permit is None:
            return False
        try:
            found = (permit.ticket, permit.branch, permit.head, permit.tree)
            here = (ticket, repository.current_branch(), repository.head(), repository.index_tree())
        except SEGitError as error:
            self.logger.warning("The squash permit of %s cannot be checked: %s.", ticket, type(error).__name__)
            return False
        if found != here or permit.expires_at <= datetime.now(UTC):
            self.logger.warning("The squash permit of %s does not match this commit or has expired.", ticket)
            return False
        self.store.delete(ticket)
        self.logger.info("Redeemed the squash permit of %s.", ticket)
        return True
