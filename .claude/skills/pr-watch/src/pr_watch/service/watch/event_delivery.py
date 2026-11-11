from __future__ import annotations

# Standard library imports
from datetime import datetime, timedelta
from logging import Logger, getLogger
from typing import Dict, List, Optional

# First-party imports
from pr_watch.models.configuration.timing_config import TimingConfig
from pr_watch.models.enums import DispatchAction, OperationKind
from pr_watch.models.events.operation import Operation
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.sessions.dispatch_outcome import DispatchOutcome
from pr_watch.models.sessions.live_session import LiveSession
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.sessions.session_dispatcher import SessionDispatcher
from pr_watch.storage.state.watch_store import WatchStore


class EventDelivery:
    """Puts new events in their ticket's inbox and brings them to the ticket's session.

    Attributes:
        store (WatchStore): The watcher's files.
        dispatcher (SessionDispatcher): Brings events to a session.
        timing (TimingConfig): How long before a ticket is reminded.
        logger (Logger): Logger instance.

    Notes:
        - An event enters its inbox once, by identifier, and reaches its session once.
        - **An event is marked as delivered only when the dispatch succeeded**: a failed dispatch is recorded as a
          warning and tried again on the next run.
        - A ticket whose delivered events still wait is reminded once per reminder delay.
    """

    def __init__(
        self, store: WatchStore, dispatcher: SessionDispatcher, timing: TimingConfig, logger: Optional[Logger] = None
    ) -> None:
        """Set what the delivery needs.

        Args:
            store (WatchStore): The watcher's files.
            dispatcher (SessionDispatcher): Brings events to a session.
            timing (TimingConfig): How long before a ticket is reminded.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.dispatcher = dispatcher
        self.timing = timing
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _record(self, watch: TicketWatch, outcome: DispatchOutcome, now: datetime) -> None:
        """Log how a dispatch went.

        Args:
            watch (TicketWatch): The pull request.
            outcome (DispatchOutcome): What was done.
            now (datetime): The time of the run.
        """
        kind = OperationKind.NOTIFIED if outcome.action == DispatchAction.NOTIFIED else OperationKind.REOPENED
        self.store.append_operation(
            Operation(at=now, pr_id=watch.id, kind=kind if outcome.ok else OperationKind.WARNING, detail=outcome.detail)
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def deliver(
        self, registry: Registry, state: WatchState, live: Dict[str, LiveSession], found: List[PrEvent], now: datetime
    ) -> int:
        """File the new events and bring the undelivered ones to their sessions.

        Args:
            registry (Registry): Every watched pull request.
            state (WatchState): The watcher's memory, its delivery log updated in place.
            live (Dict[str, LiveSession]): The sessions running now.
            found (List[PrEvent]): The events found on this run.
            now (datetime): The time of the run.

        Returns:
            int: The events newly filed.
        """
        filed = 0
        pending_keys = {key for key, inbox in self.store.inboxes().items() if inbox.pending}
        for key in sorted({event.key for event in found} | pending_keys):
            inbox = self.store.inbox(key)
            known = {event.id for event in inbox.events}
            new = [event for event in found if event.key == key and event.id not in known]
            if new:
                self.store.save_inbox(key, inbox.model_copy(update={"events": inbox.events + new}))
                filed += len(new)
                for event in new:
                    self.store.append_operation(
                        Operation(
                            at=now,
                            pr_id=event.pr_id,
                            kind=OperationKind.DETECTED,
                            detail=event.detail.title,
                            link=event.detail.link,
                        )
                    )
            waiting = [
                event
                for event in inbox.pending + new
                if event.id not in state.delivery.dispatched and event.pr_id in registry.pull_requests
            ]
            if not waiting:
                continue
            watch = registry.pull_requests[waiting[0].pr_id]
            session_id = watch.session.session_id if watch.session else ""
            outcome = self.dispatcher.dispatch(watch, live.get(session_id), waiting)
            self._record(watch, outcome, now)
            if outcome.ok:
                for event in waiting:
                    state.delivery.dispatched[event.id] = now
                state.delivery.notified[key] = now
        self.logger.info("Filed %d new events.", filed)
        return filed

    def remind(self, registry: Registry, state: WatchState, now: datetime) -> None:
        """Remind the tickets whose delivered events still wait after the reminder delay.

        Args:
            registry (Registry): Every watched pull request.
            state (WatchState): The watcher's memory, its delivery log updated in place.
            now (datetime): The time of the run.
        """
        limit = now - timedelta(minutes=self.timing.renotify_minutes)
        for key, inbox in self.store.inboxes().items():
            waiting = [
                event
                for event in inbox.pending
                if event.id in state.delivery.dispatched and event.pr_id in registry.pull_requests
            ]
            last = state.delivery.notified.get(key)
            if not waiting or (last is not None and last > limit):
                continue
            watch = registry.pull_requests[waiting[0].pr_id]
            outcome = self.dispatcher.remind(watch, waiting)
            self.store.append_operation(
                Operation(
                    at=now,
                    pr_id=watch.id,
                    kind=OperationKind.NOTIFIED if outcome.ok else OperationKind.WARNING,
                    detail=outcome.detail,
                )
            )
            if outcome.ok:
                state.delivery.notified[key] = now
            else:
                self.logger.warning("%s could not be reminded.", key)
