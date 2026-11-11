from __future__ import annotations

# Standard library imports
from datetime import datetime, timedelta
from logging import Logger, getLogger
from operator import attrgetter
from pathlib import Path
from string import Template
from typing import ClassVar, Dict, List, Optional

# First-party imports
from pr_watch.models.configuration.timing_config import TimingConfig
from pr_watch.models.enums import OperationKind, PullRequestStatus
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.events.operation import Operation
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.report.summary_cells import SummaryCells
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore


class SummaryRenderer:
    """Writes the summary page of the watched pull requests, one per local repository.

    Attributes:
        PAGE (Path): Where the page sits in a repository.
        COUNTED (List[str]): The status icons counted at the top of the page.
        store (WatchStore): The watcher's files.
        files (TextFiles): Writes the page at once.
        cells (SummaryCells): Writes the cells.
        template_file (Path): The page's template.
        timing (TimingConfig): The timer's interval and the operations shown.
        sessions (SessionDirectory): Finds the running sessions, for a page written outside a run.
        logger (Logger): Logger instance.

    Notes:
        - The page is ``docs/tickets/pull-request-summary/README.md`` in the main working tree of each repository a
          pull request was registered from. ``docs/tickets/`` is ignored by git: the page is local and generated,
          never edited by hand.
        - The page shows only the pull requests, operations and unwatched pull requests of its own repository.
    """

    PAGE: ClassVar[Path] = Path("docs") / "tickets" / "pull-request-summary" / "README.md"
    COUNTED: ClassVar[List[str]] = ["🟢", "🔀", "🔧", "🚧", "✍️", "⚠️"]

    def __init__(
        self,
        store: WatchStore,
        files: TextFiles,
        cells: SummaryCells,
        template_file: Path,
        timing: TimingConfig,
        sessions: SessionDirectory,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what the page is made of.

        Args:
            store (WatchStore): The watcher's files.
            files (TextFiles): Writes the page at once.
            cells (SummaryCells): Writes the cells.
            template_file (Path): The page's template.
            timing (TimingConfig): The timer's interval and the operations shown.
            sessions (SessionDirectory): Finds the running sessions, for a page written outside a run.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.files = files
        self.cells = cells
        self.template_file = template_file
        self.timing = timing
        self.sessions = sessions
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _closed_on(self, watch: TicketWatch) -> datetime:
        """Give the sort key of a closed pull request.

        Args:
            watch (TicketWatch): The pull request.

        Returns:
            datetime: When it closed, or when it was registered when unknown.
        """
        return watch.history.closed_on or watch.history.registered_on

    def _closed_rows(self, watches: List[TicketWatch], operations: List[Operation]) -> str:
        """Build the rows of the merged or closed pull requests, the latest first.

        Args:
            watches (List[TicketWatch]): The pull requests.
            operations (List[Operation]): Their operations.

        Returns:
            str: The rows.
        """
        rows = []
        for watch in sorted(watches, key=self._closed_on, reverse=True):
            detected = sum(1 for item in operations if item.pr_id == watch.id and item.kind == OperationKind.DETECTED)
            history = watch.history
            rows.append(
                f"| {self.cells.ticket(watch.key)} | {self.cells.pull_request(watch)} "
                f"| {self.cells.time(history.opened_on)} "
                f"| {self.cells.time(history.closed_on)} | {self.cells.duration(history.opened_on, history.closed_on)} "
                f"| {detected} | {self.cells.cost(watch.key)} |"
            )
        return self.cells.rows(rows, 7)

    def _ongoing_row(
        self,
        watch: TicketWatch,
        state: WatchState,
        inboxes: Dict[str, Inbox],
        last: Optional[Operation],
        live: Dict[str, LiveSession],
    ) -> str:
        """Build the row of an open pull request.

        Args:
            watch (TicketWatch): The pull request.
            state (WatchState): What the last runs saw.
            inboxes (Dict[str, Inbox]): The events of each ticket.
            last (Optional[Operation]): Its last operation.
            live (Dict[str, LiveSession]): The sessions running now.

        Returns:
            str: The row.
        """
        snapshot = state.snapshots.get(watch.id)
        branch = snapshot.branches.head_ref if snapshot is not None and snapshot.branches is not None else "?"
        return (
            f"| {self.cells.status(snapshot)} | {self.cells.ticket(watch.key)} | {self.cells.pull_request(watch)} "
            f"| `{branch}` | {self.cells.checks(snapshot)} | {self.cells.stages(snapshot)} "
            f"| {self.cells.review(snapshot)} "
            f"| {self.cells.handling(inboxes.get(watch.key), snapshot, watch)} | {self.cells.cost(watch.key)} "
            f"| {self.cells.session(watch, live)} | {self.cells.time(watch.history.opened_on)} "
            f"| {self.cells.operation(last)} |"
        )

    def _page(
        self,
        watches: List[TicketWatch],
        state: WatchState,
        inboxes: Dict[str, Inbox],
        operations: List[Operation],
        live: Dict[str, LiveSession],
    ) -> str:
        """Fill the template for the pull requests of one repository.

        Args:
            watches (List[TicketWatch]): The repository's pull requests.
            state (WatchState): What the last runs saw.
            inboxes (Dict[str, Inbox]): The events of each ticket.
            operations (List[Operation]): The operations of these pull requests.
            live (Dict[str, LiveSession]): The sessions running now.

        Returns:
            str: The page.
        """
        open_watches = sorted((watch for watch in watches if watch.is_open), key=attrgetter("id"))
        chronological = sorted(operations, key=attrgetter("at"))
        last = {operation.pr_id: operation for operation in chronological}
        statuses = [self.cells.status(state.snapshots.get(watch.id)) for watch in open_watches]
        counts = " · ".join(f"{icon} {sum(1 for status in statuses if icon in status)}" for icon in self.COUNTED)
        ids = {watch.id for watch in watches}
        waiting = sum(1 for inbox in inboxes.values() for event in inbox.pending if event.pr_id in ids)
        repositories = {watch.pull_request.repository for watch in watches}
        unwatched = [
            f"| [{item.repository}#{item.number}]({item.url}) | {item.ticket or self.cells.EMPTY} "
            f"| {self.cells.text(item.title, 70)} "
            f"| {self.cells.time(item.updated_on)} |"
            for _, item in sorted(state.unwatched.items())
            if item.repository in repositories
        ]
        shown = list(reversed(chronological))[: self.timing.operations_shown]
        operation_rows = [
            f"| {self.cells.time(item.at)} | {self.cells.OPERATION_ICONS[item.kind]} | {item.key} "
            f"| {item.pr_id.split(':', 1)[-1]} | {self.cells.text(item.detail, 140)}"
            f"{f' ([link]({item.link}))' if item.link else ''} |"
            for item in shown
        ]
        next_check = (
            state.last_checked + timedelta(minutes=self.timing.interval_minutes) if state.last_checked else None
        )
        merged = [watch for watch in watches if watch.history.status == PullRequestStatus.MERGED]
        closed = [watch for watch in watches if watch.history.status == PullRequestStatus.CLOSED]
        template = Template(self.files.read(self.template_file) or "")
        return template.substitute(
            last_checked=self.cells.time(state.last_checked),
            next_check=self.cells.time(next_check),
            open_count=len(open_watches),
            merged_count=len(merged),
            closed_count=len(closed),
            status_counts=f"{counts} · ⏳ {waiting} events waiting",
            ongoing_rows=self.cells.rows(
                [self._ongoing_row(watch, state, inboxes, last.get(watch.id), live) for watch in open_watches], 12
            ),
            unwatched_rows=self.cells.rows(unwatched, 4),
            operations_shown=self.timing.operations_shown,
            operation_rows=self.cells.rows(operation_rows, 5),
            merged_rows=self._closed_rows(merged, operations),
            closed_rows=self._closed_rows(closed, operations),
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def render(self, registry: Registry, state: WatchState, live: Dict[str, LiveSession]) -> List[Path]:
        """Write the summary page of every repository with a watched pull request.

        Args:
            registry (Registry): Every watched pull request.
            state (WatchState): What the last runs saw.
            live (Dict[str, LiveSession]): The sessions running now.

        Returns:
            List[Path]: The pages written.
        """
        inboxes = self.store.inboxes()
        operations = self.store.operations()
        written = []
        for root in sorted({watch.pull_request.root for watch in registry.pull_requests.values()}):
            watches = [watch for watch in registry.pull_requests.values() if watch.pull_request.root == root]
            ids = {watch.id for watch in watches}
            page = Path(root) / self.PAGE
            content = self._page(watches, state, inboxes, [item for item in operations if item.pr_id in ids], live)
            self.files.write(page, content)
            written.append(page)
            self.logger.info("Wrote the summary page of %s: %d pull requests.", root, len(watches))
        return written

    def refresh(self) -> List[Path]:
        """Write the pages again from the stored state. The caller holds the store's lock.

        Returns:
            List[Path]: The pages written.
        """
        return self.render(self.store.registry(), self.store.state(), self.sessions.live())
