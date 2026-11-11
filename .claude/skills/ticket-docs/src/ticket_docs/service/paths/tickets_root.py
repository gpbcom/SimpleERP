from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# First-party imports
from harness_core.git.git_repository import GitRepository


class TicketsRoot:
    """Finds the ``docs/tickets`` folder of a repository.

    Attributes:
        TICKETS (Path): The tickets folder, relative to the repository root.
        logger (Logger): Logger instance.

    Notes:
        ``docs/tickets`` is not versioned, so a linked worktree (an agent's, for instance) does not have it: the main
        checkout's folder is used then, where the evidence lives.
    """

    TICKETS: ClassVar[Path] = Path("docs") / "tickets"

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Set the logger.

        Args:
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def of(self, repository: GitRepository) -> Path:
        """Give a repository's tickets folder.

        Args:
            repository (GitRepository): The repository.

        Returns:
            Path: ``<root>/docs/tickets`` when it exists, else the main checkout's when that one exists, else
            ``<root>/docs/tickets``.
        """
        own = repository.root / self.TICKETS
        if own.is_dir():
            return own
        main = repository.main_root() / self.TICKETS
        if main.is_dir():
            self.logger.debug("The tickets of %s live in the main checkout.", repository.root.name)
            return main
        return own
