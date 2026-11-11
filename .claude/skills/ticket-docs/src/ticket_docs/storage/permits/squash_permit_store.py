from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from ticket_docs.models.permits.exceptions import SEInvalidSquashPermitException
from ticket_docs.models.permits.squash_permit import SquashPermit
from ticket_docs.storage.permits.exceptions import SESquashPermitStoreError


class SquashPermitStore:
    """Reads and writes the squash permits, one JSON file per ticket, outside every repository.

    Attributes:
        FOLDER (Path): The permits folder, relative to the home folder.
        SUFFIX (str): The extension of a permit file.
        root (Path): The permits folder.
        logger (Logger): Logger instance.

    Notes:
        - The folder is under ``~/.local/state/claude-harness``, next to the harness logs, so that no working tree,
          stash or worktree carries a permit.
        - A permit that cannot be read counts as none: the gate then refuses, on the safe side.
    """

    FOLDER: ClassVar[Path] = Path(".local") / "state" / "claude-harness" / "squash-permits"
    SUFFIX: ClassVar[str] = ".json"

    def __init__(self, root: Path, logger: Optional[Logger] = None) -> None:
        """Set the permits folder.

        Args:
            root (Path): The permits folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.root = root
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def default(cls, home: Path, logger: Optional[Logger] = None) -> SquashPermitStore:
        """Build the store of a home folder.

        Args:
            home (Path): The home folder.
            logger (Optional[Logger]): Logger instance.

        Returns:
            SquashPermitStore: The store of ``<home>/.local/state/claude-harness/squash-permits``.
        """
        return cls(home / cls.FOLDER, logger)

    def path(self, ticket: str) -> Path:
        """Give the file of a ticket's permit.

        Args:
            ticket (str): The ticket.

        Returns:
            Path: ``<root>/<ticket>.json``.
        """
        return self.root / f"{ticket}{self.SUFFIX}"

    def read(self, ticket: str) -> Optional[SquashPermit]:
        """Read a ticket's permit.

        Args:
            ticket (str): The ticket.

        Returns:
            Optional[SquashPermit]: The permit, ``None`` when there is none or it cannot be read.
        """
        path = self.path(ticket)
        if not path.is_file():
            self.logger.debug("%s has no squash permit.", ticket)
            return None
        try:
            return SquashPermit.model_validate_json(path.read_text(encoding="utf-8"))
        except (OSError, ValidationError, SEInvalidSquashPermitException) as error:
            self.logger.warning("The squash permit of %s cannot be read: %s.", ticket, type(error).__name__)
            return None

    def write(self, permit: SquashPermit) -> Path:
        """Write a ticket's permit, replacing an older one.

        Args:
            permit (SquashPermit): The permit.

        Returns:
            Path: Its file.

        Raises:
            SESquashPermitStoreError: When the file cannot be written.
        """
        path = self.path(permit.ticket)
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(permit.model_dump_json(indent=2) + "\n", encoding="utf-8")
        except OSError as error:
            self.logger.error("The squash permit of %s cannot be written: %s.", permit.ticket, type(error).__name__)
            raise SESquashPermitStoreError(
                f"The squash permit of {permit.ticket} cannot be written to {path}. "  # noqa: E501
                f"The system said: {error}."
            ) from error
        self.logger.info("Wrote the squash permit of %s.", permit.ticket)
        return path

    def delete(self, ticket: str) -> None:
        """Delete a ticket's permit, if there is one.

        Args:
            ticket (str): The ticket.
        """
        self.path(ticket).unlink(missing_ok=True)
        self.logger.info("Deleted the squash permit of %s.", ticket)
