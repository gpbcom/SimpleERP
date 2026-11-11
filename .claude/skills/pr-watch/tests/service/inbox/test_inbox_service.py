from __future__ import annotations

from pathlib import Path

import pytest

from pr_watch.models.enums import OperationKind, PullRequestStatus
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.exceptions import SEWatchNotFoundError
from pr_watch.service.inbox.inbox_service import InboxService
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import NOW, SESSION_ID, a_watch, an_event


class TestInboxService:
    @pytest.fixture
    def store(self, tmp_path: Path) -> WatchStore:
        return WatchStore(tmp_path / "state", TextFiles())

    @pytest.fixture
    def watch(self, store: WatchStore, tmp_path: Path) -> TicketWatch:
        watch = a_watch(tmp_path)
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        store.save_inbox(watch.key, Inbox(events=[an_event(watch, "a"), an_event(watch, "b")]))
        return watch

    def test_the_hook_hands_the_owner_its_waiting_events_and_nobody_else(
        self, store: WatchStore, watch: TicketWatch
    ) -> None:
        context = InboxService(store).hook_context(SESSION_ID)
        assert context is not None
        assert "Run /pr-watch GH-12" in context
        assert "2 checks failed on 668501e0" in context
        assert "excerpt:\n    - unit: failure" in context
        assert InboxService(store).hook_context("another-session") is None

    def test_taken_events_stop_being_handed_over(self, store: WatchStore, watch: TicketWatch) -> None:
        service = InboxService(store)
        taken = service.ack(watch.key, [f"{watch.id}|a"], NOW)
        assert [event.id for event in taken] == [f"{watch.id}|a"]
        assert [event.id for event in service.pending(watch.key)] == [f"{watch.id}|b"]
        service.ack(watch.key, [], NOW)
        assert service.hook_context(SESSION_ID) is None
        assert [operation.kind for operation in store.operations()] == [OperationKind.ACKED] * 2

    def test_a_closed_pull_request_hands_nothing(self, store: WatchStore, watch: TicketWatch) -> None:
        closed = watch.model_copy(
            update={"history": watch.history.model_copy(update={"status": PullRequestStatus.MERGED})}
        )
        store.save_registry(Registry(pull_requests={watch.id: closed}))
        assert InboxService(store).hook_context(SESSION_ID) is None

    def test_an_operation_is_logged_on_the_tickets_pull_request(self, store: WatchStore, watch: TicketWatch) -> None:
        operation = InboxService(store).log("GH-12", OperationKind.FIXED, "unit test fixed", "https://x/c/1", None, NOW)
        assert (operation.pr_id, store.operations()[-1].detail) == (watch.id, "unit test fixed")

    def test_a_ticket_with_several_pull_requests_needs_a_choice(
        self, store: WatchStore, watch: TicketWatch, tmp_path: Path
    ) -> None:
        other = a_watch(tmp_path, number=8)
        store.save_registry(Registry(pull_requests={watch.id: watch, other.id: other}))
        service = InboxService(store)
        with pytest.raises(SEWatchNotFoundError, match="--pr"):
            service.watch_of("GH-12", None)
        assert service.watch_of("GH-12", "gpbcom/simple-erp#8") == other
        with pytest.raises(SEWatchNotFoundError, match="pr-watch register GH-99"):
            service.watch_of("GH-99", None)

    def test_the_status_lists_every_watch(self, store: WatchStore, watch: TicketWatch) -> None:
        assert InboxService(store).status() == [f"{watch.id} open session={SESSION_ID} waiting=2"]
        assert InboxService(store).describe(an_event(watch)).startswith("- [checks_failed] 2 checks failed")
