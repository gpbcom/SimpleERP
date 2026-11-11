from __future__ import annotations

# Standard library imports
import fcntl
import os
import tempfile
from contextlib import contextmanager
from logging import Logger, getLogger
from pathlib import Path
from typing import Iterator, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from ai_cost.models.ledger.exceptions import (
    SEInvalidCostRunException,
    SEInvalidLedgerException,
    SEInvalidModelUsageException,
)
from ai_cost.models.ledger.ledger import Ledger
from ai_cost.storage.ledgers.exceptions import SELedgerTicketRefusedError, SELedgerUnreadableError
from harness_core.models.branches.branch_name import BranchName


class LedgerRepository:
    """Reads and writes the ledger of each ticket, one JSON file per ticket.

    Attributes:
        state_dir (Path): The folder of the ledgers.
        logger (Logger): Logger instance.

    Notes:
        - Each ticket has its own lock file (``<KEY>.lock``), held with ``fcntl`` while a ledger is read and
          written again, so that two runs of the same ticket never lose each other's records.
        - A ledger is written to a temporary file then renamed, so that a reader never sees half a file.
    """

    def __init__(self, state_dir: Path, logger: Optional[Logger] = None) -> None:
        """Set the folder of the ledgers.

        Args:
            state_dir (Path): The folder of the ledgers.
            logger (Optional[Logger]): Logger instance.
        """
        self.state_dir = state_dir
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _path(self, ticket: str, suffix: str) -> Path:
        """Give the file of a ticket, its folder created.

        Args:
            ticket (str): The ticket.
            suffix (str): The file's extension, such as ``.json``.

        Returns:
            Path: The file.

        Raises:
            SELedgerTicketRefusedError: When the key is not a ticket, so that it cannot name a file elsewhere.
        """
        if not BranchName.TICKET_PATTERN.match(ticket):
            self.logger.error("Refused the ledger key %r.", ticket)
            raise SELedgerTicketRefusedError(
                f"{ticket!r} is not a ticket key. "  # noqa: E501
                "A ledger is named after a ticket such as GH-12."
            )
        self.state_dir.mkdir(parents=True, exist_ok=True)
        return self.state_dir / f"{ticket}{suffix}"

    ############################
    # Publicly Exposed Methods #
    ############################

    @contextmanager
    def lock(self, ticket: str) -> Iterator[None]:
        """Hold the lock of a ticket's ledger.

        Args:
            ticket (str): The ticket.

        Yields:
            None: While the lock is held.
        """
        with open(self._path(ticket, ".lock"), "w", encoding="utf-8") as handle:
            self.logger.debug("Waiting for the lock of %s.", ticket)
            fcntl.flock(handle, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)

    def exists(self, ticket: str) -> bool:
        """Tell whether a ticket has a ledger.

        Args:
            ticket (str): The ticket.

        Returns:
            bool: ``True`` once a paid run was tried or charged for it.
        """
        return self._path(ticket, ".json").exists()

    def read(self, ticket: str) -> Optional[Ledger]:
        """Read a ticket's ledger.

        Args:
            ticket (str): The ticket.

        Returns:
            Optional[Ledger]: The ledger, ``None`` when the ticket has none yet.

        Raises:
            SELedgerUnreadableError: When the file cannot be read or is not a valid ledger.
        """
        path = self._path(ticket, ".json")
        if not path.exists():
            self.logger.debug("%s has no ledger yet.", ticket)
            return None
        try:
            ledger = Ledger.model_validate_json(path.read_text(encoding="utf-8"))
        except (
            OSError,
            ValidationError,
            SEInvalidLedgerException,
            SEInvalidCostRunException,
            SEInvalidModelUsageException,
        ) as error:
            self.logger.error("The ledger of %s cannot be read: %s.", ticket, type(error).__name__)
            raise SELedgerUnreadableError(
                f"The ledger {path} cannot be read. "  # noqa: E501
                f"The error was {type(error).__name__}: {error}"
            ) from error
        self.logger.debug("Read the ledger of %s: %d runs.", ticket, len(ledger.runs))
        return ledger

    def save(self, ledger: Ledger) -> Path:
        """Write a ticket's ledger at once. The caller holds the ticket's lock.

        Args:
            ledger (Ledger): The ledger.

        Returns:
            Path: The file written.
        """
        path = self._path(ledger.ticket, ".json")
        descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(ledger.model_dump_json(indent=2))
        os.replace(temporary, path)
        self.logger.info("Saved the ledger of %s: %d runs.", ledger.ticket, len(ledger.runs))
        return path
