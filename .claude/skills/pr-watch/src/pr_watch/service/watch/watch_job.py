from __future__ import annotations

# Standard library imports
from datetime import datetime
from logging import Logger, getLogger
from typing import List, Optional

# Third-party imports
import httpx

from harness_core.github.exceptions import SEGithubError
from harness_core.github.github_connection import GithubConnection
from harness_core.github.github_token import GithubToken

# First-party imports
from harness_core.lifecycle.async_runnable import AsyncRunnable
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import OperationKind, PullRequestStatus
from pr_watch.models.events.operation import Operation
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.exceptions import SEPrWatchError
from pr_watch.models.pull_requests.pull_request_state import PullRequestState
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.report.summary_renderer import SummaryRenderer
from pr_watch.service.watch.event_delivery import EventDelivery
from pr_watch.service.watch.event_detector import EventDetector
from pr_watch.service.watch.pull_request_inspector import PullRequestInspector
from pr_watch.storage.github.pull_request_reader import PullRequestReader
from pr_watch.storage.sessions.session_directory import SessionDirectory
from pr_watch.storage.state.watch_store import WatchStore


class WatchJob(AsyncRunnable):
    """One run of the watcher: check every open pull request, bring new events to their sessions, write the pages.

    Attributes:
        catalog (WatchCatalog): The watcher's configuration.
        store (WatchStore): The watcher's files.
        token (GithubToken): Finds the GitHub token.
        detector (EventDetector): Turns what was read into events.
        delivery (EventDelivery): Files and delivers the events.
        sessions (SessionDirectory): Finds the running sessions.
        renderer (SummaryRenderer): Writes the summary pages.
        transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
        connection (Optional[GithubConnection]): The HTTP client, open between ``initialize`` and ``close``.
        checked (int): The open pull requests checked by the run.
        found (int): The events the run found.
        logger (Logger): Logger instance.

    Notes:
        - The whole run holds the store's lock, so that a session's ``ack`` or ``log`` waits for it.
        - **A pull request that cannot be read does not stop the run**: its snapshot keeps the reason, and one
          warning is logged while the same reason lasts.
        - A merged or closed pull request leaves the watch list: its waiting events are closed and the merge or
          close is logged.
        - The watcher never pushes, rebases or changes a working tree.
    """

    def __init__(
        self,
        catalog: WatchCatalog,
        store: WatchStore,
        token: GithubToken,
        detector: EventDetector,
        delivery: EventDelivery,
        sessions: SessionDirectory,
        renderer: SummaryRenderer,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Set what the run needs.

        Args:
            catalog (WatchCatalog): The watcher's configuration.
            store (WatchStore): The watcher's files.
            token (GithubToken): Finds the GitHub token.
            detector (EventDetector): Turns what was read into events.
            delivery (EventDelivery): Files and delivers the events.
            sessions (SessionDirectory): Finds the running sessions.
            renderer (SummaryRenderer): Writes the summary pages.
            transport (Optional[httpx.AsyncBaseTransport]): The HTTP transport, a stand-in in tests.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.store = store
        self.token = token
        self.detector = detector
        self.delivery = delivery
        self.sessions = sessions
        self.renderer = renderer
        self.transport = transport
        self.connection: Optional[GithubConnection] = None
        self.checked = 0
        self.found = 0
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _warn_once(self, watch: TicketWatch, state: WatchState, reason: str, now: datetime) -> None:
        """Keep why a pull request could not be checked, and log it once while it lasts.

        Args:
            watch (TicketWatch): The pull request.
            state (WatchState): The watcher's memory, its snapshot updated in place.
            reason (str): Why.
            now (datetime): The time of the run.
        """
        previous = state.snapshots.get(watch.id)
        if previous is None or previous.error != reason:
            self.store.append_operation(
                Operation(at=now, pr_id=watch.id, kind=OperationKind.WARNING, detail=f"could not be checked: {reason}")
            )
        base = previous or PrSnapshot(checked_on=now)
        state.snapshots[watch.id] = base.model_copy(update={"error": reason, "checked_on": now})

    def _close(self, watch: TicketWatch, pull_request: PullRequestState, now: datetime) -> TicketWatch:
        """Move a merged or closed pull request to the history, its waiting events closed.

        Args:
            watch (TicketWatch): The pull request.
            pull_request (PullRequestState): What GitHub says of it now.
            now (datetime): The time of the run.

        Returns:
            TicketWatch: The watch, closed.
        """
        inbox = self.store.inbox(watch.key)
        events = [
            event.model_copy(update={"acked_on": now}) if event.pr_id == watch.id and event.is_pending else event
            for event in inbox.events
        ]
        self.store.save_inbox(watch.key, inbox.model_copy(update={"events": events}))
        merged = pull_request.status == PullRequestStatus.MERGED
        commit = pull_request.timeline.merge_commit
        detail = f"merged as {commit[:8]}" if merged and commit else pull_request.status.value
        kind = OperationKind.MERGED if merged else OperationKind.CLOSED
        self.store.append_operation(
            Operation(at=now, pr_id=watch.id, kind=kind, detail=detail, link=watch.pull_request.url)
        )
        return watch

    async def _check(
        self, inspector: PullRequestInspector, watch: TicketWatch, registry: Registry, state: WatchState, now: datetime
    ) -> List[PrEvent]:
        """Check one open pull request, its watch updated in the registry.

        Args:
            inspector (PullRequestInspector): Reads the pull request.
            watch (TicketWatch): The pull request.
            registry (Registry): The registry, updated in place.
            state (WatchState): The watcher's memory, updated in place.
            now (datetime): The time of the run.

        Returns:
            List[PrEvent]: Its events, none when it is closed or could not be read.
        """
        try:
            pull_request, events = await inspector.inspect(watch, state, now)
        except (SEPrWatchError, SEGithubError) as error:
            self.logger.warning("%s could not be checked: %s.", watch.id, type(error).__name__)
            self._warn_once(watch, state, f"{type(error).__name__}: {error}", now)
            return []
        history = watch.history.model_copy(
            update={
                "status": pull_request.status,
                "opened_on": pull_request.timeline.opened_on,
                "closed_on": pull_request.timeline.closed_on,
            }
        )
        updated = watch.model_copy(update={"history": history})
        if not updated.is_open:
            updated = self._close(updated, pull_request, now)
        registry.pull_requests[watch.id] = updated
        return events

    async def _unwatched(self, connection: GithubConnection, registry: Registry, state: WatchState) -> None:
        """Keep the list of open pull requests of the watched repositories that nobody watches.

        Args:
            connection (GithubConnection): The HTTP client.
            registry (Registry): Every watched pull request.
            state (WatchState): The watcher's memory, its list replaced repository by repository.
        """
        watched = {watch.pull_request.label for watch in registry.pull_requests.values()}
        for repository in sorted({watch.pull_request.repository for watch in registry.pull_requests.values()}):
            try:
                found = await PullRequestReader(connection, repository, self.logger).open_pull_requests()
            except (SEPrWatchError, SEGithubError) as error:
                self.logger.warning(
                    "The open pull requests of %s could not be listed: %s.", repository, type(error).__name__
                )
                continue
            kept = {name: item for name, item in state.unwatched.items() if item.repository != repository}
            kept.update(
                {f"{repository}#{item.number}": item for item in found if f"{repository}#{item.number}" not in watched}
            )
            state.unwatched = kept

    ############################
    # Publicly Exposed Methods #
    ############################

    async def initialize(self) -> None:
        """Read the GitHub token and open the HTTP client.

        Raises:
            SEGithubTokenMissingError: When no GitHub token can be found.
        """
        self.connection = GithubConnection(
            self.catalog.github.api_url, self.catalog.github.api_version, self.token.read(), self.transport, self.logger
        )
        self.logger.debug("The GitHub client is open.")

    async def run(self) -> None:
        """Check, deliver, remind, and write the pages."""
        if self.connection is None:
            return
        inspector = PullRequestInspector(self.connection, self.detector, self.catalog.github, self.logger)
        now = datetime.now().astimezone()
        with self.store.lock():
            registry = self.store.registry()
            state = self.store.state()
            found: List[PrEvent] = []
            open_watches = [watch for watch in registry.pull_requests.values() if watch.is_open]
            for watch in open_watches:
                found += await self._check(inspector, watch, registry, state, now)
            await self._unwatched(self.connection, registry, state)
            live = self.sessions.live()
            self.delivery.deliver(registry, state, live, found, now)
            self.delivery.remind(registry, state, now)
            state.last_checked = now
            self.store.save_registry(registry)
            self.store.save_state(state)
            self.renderer.render(registry, state, live)
        self.checked, self.found = len(open_watches), len(found)
        self.logger.info("Checked %d open pull requests: %d events found.", self.checked, self.found)

    async def close(self) -> None:
        """Close the HTTP client, if it was opened."""
        if self.connection is not None:
            await self.connection.aclose()
            self.connection = None
