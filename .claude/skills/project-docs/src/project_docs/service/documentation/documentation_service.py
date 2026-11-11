from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Dict, List, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository
from project_docs.service.checks.document_check import DocumentCheck
from project_docs.service.mapping.chapter_mapper import ChapterMapper
from project_docs.service.tickets.ticket_check import TicketCheck


class DocumentationService:
    """Everything the tool does with the project documentation of one repository.

    Attributes:
        repository (GitRepository): The repository, read for the branch's changes.
        mapper (ChapterMapper): Maps a changed path to its chapters.
        checks (List[DocumentCheck]): The checks of the documentation, in the order their problems are listed.
        ticket_check (TicketCheck): Checks that a ticket handled every chapter its branch concerns.
        logger (Logger): Logger instance.

    Notes:
        The branch's changes are its commits since it left the base (``base...HEAD``) and every uncommitted change,
        untracked files included, so that ``map`` can run before the documentation is committed.
    """

    def __init__(
        self,
        repository: GitRepository,
        mapper: ChapterMapper,
        checks: List[DocumentCheck],
        ticket_check: TicketCheck,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set the repository, the mapper and the checks.

        Args:
            repository (GitRepository): The repository.
            mapper (ChapterMapper): Maps a changed path to its chapters.
            checks (List[DocumentCheck]): The checks of the documentation.
            ticket_check (TicketCheck): Checks that a ticket handled every chapter its branch concerns.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.mapper = mapper
        self.checks = checks
        self.ticket_check = ticket_check
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def changed_paths(self, base: str) -> List[str]:
        """List the paths the branch changed.

        Args:
            base (str): The base branch, such as ``origin/develop``.

        Returns:
            List[str]: The committed and uncommitted paths, sorted and unique.

        Raises:
            SEGitCommandFailedError: When the base is unknown or git fails.
        """
        paths = sorted(set(self.repository.changed_files(base)) | set(self.repository.uncommitted_files()))
        self.logger.debug("The branch changed %d paths since %s.", len(paths), base)
        return paths

    def map(self, base: str) -> Dict[str, List[str]]:
        """Map the branch's changes to the chapters they concern.

        Args:
            base (str): The base branch.

        Returns:
            Dict[str, List[str]]: Each chapter concerned, sorted, with the paths that concern it.

        Raises:
            SEGitCommandFailedError: When the base is unknown or git fails.
        """
        mapping = self.mapper.map(self.changed_paths(base))
        self.logger.info("Mapped the changes since %s to %d chapters.", base, len(mapping))
        return mapping

    def check(self, ticket: Optional[str], base: str) -> List[str]:
        """List every problem of the documentation.

        Args:
            ticket (Optional[str]): The ticket whose branch must have handled every chapter it concerns, if any.
            base (str): The base branch, read only with a ticket.

        Returns:
            List[str]: One line per problem, none when the documentation is complete and current.

        Raises:
            SETicketKeyInvalidError: When the ticket key is not ``GH-<n>``.
            SEGitCommandFailedError: When the base is unknown or git fails.
        """
        problems: List[str] = []
        for check in self.checks:
            problems.extend(check.problems())
        if ticket is not None:
            paths = self.changed_paths(base)
            problems.extend(self.ticket_check.unhandled(ticket, self.mapper.map(paths), paths))
        self.logger.info("The documentation check found %d problems.", len(problems))
        return problems
