from __future__ import annotations

# Standard library imports
import fcntl
from contextlib import contextmanager
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, Iterator, List, Optional

# Third-party imports
from pydantic import ValidationError

# First-party imports
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.events.operation import Operation
from pr_watch.models.exceptions import SEPrWatchError
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.exceptions import SEWatchStoreUnreadableError


class WatchStore:
    """The watcher's files under its state folder: registry, memory, inboxes and operations.

    Attributes:
        state_dir (Path): The state folder.
        files (TextFiles): Reads and writes the files at once.
        logger (Logger): Logger instance.

    Notes:
        - The timer run and the commands a session sends (``ack``, ``log``) share the files: every change is made
          under ``lock``, and every JSON file is replaced at once.
        - ``operations.jsonl`` is append-only, one operation per line.
    """

    def __init__(self, state_dir: Path, files: TextFiles, logger: Optional[Logger] = None) -> None:
        """Set the state folder.

        Args:
            state_dir (Path): The state folder.
            files (TextFiles): Reads and writes the files at once.
            logger (Optional[Logger]): Logger instance.
        """
        self.state_dir = state_dir
        self.files = files
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _unreadable(self, path: Path, error: Exception) -> SEWatchStoreUnreadableError:
        """Log and build the error of a state file that cannot be read back.

        Args:
            path (Path): The file.
            error (Exception): Why it cannot be read.

        Returns:
            SEWatchStoreUnreadableError: The error to raise.
        """
        self.logger.error("%s cannot be read back: %s.", path, type(error).__name__)
        return SEWatchStoreUnreadableError(
            f"The state file {path} cannot be read back. "  # noqa: E501
            f"The error was {type(error).__name__}."
        )

    def _inbox_path(self, key: str) -> Path:
        """Give the file of a ticket's inbox.

        Args:
            key (str): The ticket.

        Returns:
            Path: ``inbox/<KEY>.json`` under the state folder.
        """
        return self.state_dir / "inbox" / f"{key}.json"

    ############################
    # Publicly Exposed Methods #
    ############################

    @contextmanager
    def lock(self) -> Iterator[None]:
        """Hold the state folder's lock.

        Yields:
            None: While the lock is held.
        """
        self.state_dir.mkdir(parents=True, exist_ok=True)
        with (self.state_dir / ".lock").open("w", encoding="utf-8") as handle:
            fcntl.flock(handle, fcntl.LOCK_EX)
            self.logger.debug("Holding the lock of %s.", self.state_dir)
            try:
                yield
            finally:
                fcntl.flock(handle, fcntl.LOCK_UN)

    def registry(self) -> Registry:
        """Read the registry.

        Returns:
            Registry: Every watched pull request, an empty registry before the first one.

        Raises:
            SEWatchStoreUnreadableError: When the file cannot be read back.
        """
        path = self.state_dir / "registry.json"
        content = self.files.read(path)
        try:
            return Registry.model_validate_json(content) if content else Registry()
        except (ValidationError, SEPrWatchError) as error:
            raise self._unreadable(path, error) from error

    def save_registry(self, registry: Registry) -> None:
        """Write the registry.

        Args:
            registry (Registry): Every watched pull request.
        """
        self.files.write(self.state_dir / "registry.json", registry.model_dump_json(indent=2))

    def state(self) -> WatchState:
        """Read the watcher's memory.

        Returns:
            WatchState: What the last runs saw and did, an empty memory before the first run.

        Raises:
            SEWatchStoreUnreadableError: When the file cannot be read back.
        """
        path = self.state_dir / "state.json"
        content = self.files.read(path)
        try:
            return WatchState.model_validate_json(content) if content else WatchState()
        except (ValidationError, SEPrWatchError) as error:
            raise self._unreadable(path, error) from error

    def save_state(self, state: WatchState) -> None:
        """Write the watcher's memory.

        Args:
            state (WatchState): What the runs saw and did.
        """
        self.files.write(self.state_dir / "state.json", state.model_dump_json(indent=2))

    def inbox(self, key: str) -> Inbox:
        """Read the inbox of a ticket.

        Args:
            key (str): The ticket.

        Returns:
            Inbox: Its events, an empty inbox when it has none yet.

        Raises:
            SEWatchStoreUnreadableError: When the file cannot be read back.
        """
        path = self._inbox_path(key)
        content = self.files.read(path)
        try:
            return Inbox.model_validate_json(content) if content else Inbox()
        except (ValidationError, SEPrWatchError) as error:
            raise self._unreadable(path, error) from error

    def save_inbox(self, key: str, inbox: Inbox) -> None:
        """Write the inbox of a ticket.

        Args:
            key (str): The ticket.
            inbox (Inbox): Its events.
        """
        self.files.write(self._inbox_path(key), inbox.model_dump_json(indent=2))

    def inboxes(self) -> Dict[str, Inbox]:
        """Read every inbox.

        Returns:
            Dict[str, Inbox]: The events of each ticket, by ticket.
        """
        folder = self.state_dir / "inbox"
        keys = sorted(path.stem for path in folder.glob("*.json")) if folder.exists() else []
        return {key: self.inbox(key) for key in keys}

    def append_operation(self, operation: Operation) -> None:
        """Add an operation to the log.

        Args:
            operation (Operation): The operation.
        """
        self.files.append_line(self.state_dir / "operations.jsonl", operation.model_dump_json())
        self.logger.info("%s %s: %s.", operation.pr_id, operation.kind.value, operation.detail)

    def operations(self) -> List[Operation]:
        """Read the log of operations.

        Returns:
            List[Operation]: Every operation, oldest first.

        Raises:
            SEWatchStoreUnreadableError: When a line cannot be read back.
        """
        path = self.state_dir / "operations.jsonl"
        content = self.files.read(path) or ""
        try:
            return [Operation.model_validate_json(line) for line in content.splitlines() if line.strip()]
        except (ValidationError, SEPrWatchError) as error:
            raise self._unreadable(path, error) from error
