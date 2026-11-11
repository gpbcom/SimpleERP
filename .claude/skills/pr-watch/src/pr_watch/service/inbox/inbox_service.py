from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from operator import attrgetter
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from pr_watch.models.enums import OperationKind
from pr_watch.models.events.operation import Operation
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.exceptions import SEWatchNotFoundError
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore


class InboxService:
    """What a ticket's session does with its events: read them, take them, and log what it did.

    Attributes:
        SESSION_OPERATIONS (List[OperationKind]): The operations a session may log.
        EXCERPT_LINES (int): The lines of an excerpt handed to the session.
        store (WatchStore): The watcher's files.
        logger (Logger): Logger instance.

    Notes:
        - ``hook_context`` runs on every prompt of every session: it reads the registry and the inboxes only, and
          returns nothing for a session that owns no waiting event.
        - The commands that change the files (``ack``, ``log``) run under the store's lock, held by the caller.
    """

    SESSION_OPERATIONS: ClassVar[List[OperationKind]] = [
        OperationKind.REBASED,
        OperationKind.FIXED,
        OperationKind.WAITING_PUSH,
        OperationKind.PUSHED,
        OperationKind.QA_STARTED,
        OperationKind.NOTE,
    ]
    EXCERPT_LINES: ClassVar[int] = 40

    def __init__(self, store: WatchStore, logger: Optional[Logger] = None) -> None:
        """Set the files.

        Args:
            store (WatchStore): The watcher's files.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def at(cls, state_dir: Path, logger: Optional[Logger] = None) -> InboxService:
        """Build the service on a state folder, for the prompt hook's light entry point.

        Args:
            state_dir (Path): The watcher's state folder.
            logger (Optional[Logger]): Logger instance.

        Returns:
            InboxService: The service.
        """
        return cls(WatchStore(state_dir, TextFiles(logger), logger), logger)

    def describe(self, event: PrEvent) -> str:
        """Write an event for the session.

        Args:
            event (PrEvent): The event.

        Returns:
            str: Its kind, title, identifier, time, link and excerpt.
        """
        seen = event.detected_on.astimezone().strftime("%Y-%m-%d %H:%M")
        lines = [f"- [{event.kind.value}] {event.detail.title} (id `{event.id}`, seen {seen})"]
        if event.detail.link:
            lines.append(f"  link: {event.detail.link}")
        if event.detail.excerpt:
            excerpt = event.detail.excerpt.splitlines()[: self.EXCERPT_LINES]
            lines.append("  excerpt:\n" + "\n".join(f"    {line}" for line in excerpt))
        return "\n".join(lines)

    def pending(self, key: str) -> List[PrEvent]:
        """List the events of a ticket its session has not taken yet.

        Args:
            key (str): The ticket.

        Returns:
            List[PrEvent]: The events, oldest first.
        """
        return self.store.inbox(key).pending

    def ack(self, key: str, event_ids: List[str], now: datetime) -> List[PrEvent]:
        """Mark a ticket's events as taken by its session. The caller holds the store's lock.

        Args:
            key (str): The ticket.
            event_ids (List[str]): The events, every waiting one when empty.
            now (datetime): The time recorded.

        Returns:
            List[PrEvent]: The events taken.
        """
        inbox = self.store.inbox(key)
        taken = [event for event in inbox.pending if not event_ids or event.id in event_ids]
        taken_ids = {event.id for event in taken}
        events = [
            event.model_copy(update={"acked_on": now}) if event.id in taken_ids else event for event in inbox.events
        ]
        self.store.save_inbox(key, inbox.model_copy(update={"events": events}))
        for event in taken:
            self.store.append_operation(
                Operation(
                    at=now,
                    pr_id=event.pr_id,
                    kind=OperationKind.ACKED,
                    detail=f"taken by the session: {event.detail.title}",
                    link=event.detail.link,
                )
            )
        self.logger.info("%s: %d events taken.", key, len(taken))
        return taken

    def watch_of(self, key: str, pull_request: Optional[str]) -> TicketWatch:
        """Find the watched pull request of a ticket.

        Args:
            key (str): The ticket.
            pull_request (Optional[str]): ``<owner>/<name>#<number>`` when the ticket has several.

        Returns:
            TicketWatch: The pull request, an open one first.

        Raises:
            SEWatchNotFoundError: When the ticket has no such pull request, or several and none was chosen.
        """
        watches = [
            watch
            for watch in self.store.registry().pull_requests.values()
            if watch.key == key and (pull_request is None or watch.pull_request.label == pull_request)
        ]
        if not watches:
            self.logger.error("%s has no watched pull request.", key)
            raise SEWatchNotFoundError(
                f"{key} has no watched pull request{f' {pull_request}' if pull_request else ''}. "  # noqa: E501
                f"Run pr-watch register {key} in its session."
            )
        candidates = [watch for watch in watches if watch.is_open] or watches
        if len(candidates) > 1:
            self.logger.error("%s has %d pull requests and none was chosen.", key, len(candidates))
            raise SEWatchNotFoundError(
                f"{key} has several pull requests. "  # noqa: E501
                f"Choose one with --pr: {', '.join(watch.pull_request.label for watch in candidates)}."
            )
        return candidates[0]

    def log(
        self,
        key: str,
        kind: OperationKind,
        detail: str,
        link: Optional[str],
        pull_request: Optional[str],
        now: datetime,
    ) -> Operation:
        """Log an operation done in a ticket's session. The caller holds the store's lock.

        Args:
            key (str): The ticket.
            kind (OperationKind): What was done.
            detail (str): One line saying it.
            link (Optional[str]): The commit, run or comment it refers to.
            pull_request (Optional[str]): ``<owner>/<name>#<number>`` when the ticket has several.
            now (datetime): The time recorded.

        Returns:
            Operation: The operation logged.

        Raises:
            SEWatchNotFoundError: When the ticket has no such pull request.
        """
        watch = self.watch_of(key, pull_request)
        operation = Operation(at=now, pr_id=watch.id, kind=kind, detail=detail, link=link)
        self.store.append_operation(operation)
        return operation

    def hook_context(self, session_id: str) -> Optional[str]:
        """Write what the prompt hook hands a session: the waiting events of the tickets it owns.

        Args:
            session_id (str): The session that is about to read a prompt.

        Returns:
            Optional[str]: The context, ``None`` when the session owns no waiting event.
        """
        keys = sorted(
            {
                watch.key
                for watch in self.store.registry().pull_requests.values()
                if watch.session is not None and watch.session.session_id == session_id and watch.is_open
            }
        )
        pending = [event for key in keys for event in self.store.inbox(key).pending]
        if not pending:
            return None
        return (
            "PR watcher: the pull request of this session's ticket needs attention. "
            f"Run /pr-watch {' '.join(keys)} to handle it (the skill loads the ticket documentation and the rules).\n"
            + "\n".join(self.describe(event) for event in pending)
        )

    def status(self) -> List[str]:
        """List every watched pull request with its owner and its waiting events.

        Returns:
            List[str]: One line per pull request.
        """
        lines = []
        for watch in sorted(self.store.registry().pull_requests.values(), key=attrgetter("id")):
            waiting = [event for event in self.store.inbox(watch.key).pending if event.pr_id == watch.id]
            owner = watch.session.session_id if watch.session else "-"
            lines.append(f"{watch.id} {watch.history.status.value} session={owner} waiting={len(waiting)}")
        return lines
