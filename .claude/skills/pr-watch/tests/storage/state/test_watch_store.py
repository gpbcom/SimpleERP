from __future__ import annotations

import threading
from datetime import UTC, datetime
from pathlib import Path
from typing import List

import pytest

from pr_watch.models.enums import EventKind, OperationKind
from pr_watch.models.events.inbox import Inbox
from pr_watch.models.events.operation import Operation
from pr_watch.models.events.pr_event import PrEvent
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.exceptions import SEWatchStoreUnreadableError
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import REPOSITORY


class TestWatchStore:
    @pytest.fixture
    def store(self, tmp_path: Path) -> WatchStore:
        return WatchStore(tmp_path / "state", TextFiles())

    def test_an_empty_folder_reads_as_empty_state(self, store: WatchStore) -> None:
        assert store.registry() == Registry()
        assert store.state() == WatchState()
        assert store.inbox("GH-12") == Inbox()
        assert store.inboxes() == {}
        assert store.operations() == []

    def test_what_is_saved_is_read_back(self, store: WatchStore) -> None:
        moment = datetime(2026, 11, 10, 9, 0, tzinfo=UTC)
        watch = TicketWatch(
            key="GH-12",
            pull_request={"repository": REPOSITORY, "number": 7, "root": "/r"},
            history={"registered_on": moment},
        )
        event = PrEvent(id=f"{watch.id}|x", kind=EventKind.QA_WAITING, detail={"title": "t"}, detected_on=moment)
        store.save_registry(Registry(pull_requests={watch.id: watch}))
        store.save_state(WatchState(last_checked=moment))
        store.save_inbox("GH-12", Inbox(events=[event]))
        store.append_operation(Operation(at=moment, pr_id=watch.id, kind=OperationKind.NOTE, detail="one"))
        store.append_operation(Operation(at=moment, pr_id=watch.id, kind=OperationKind.FIXED, detail="two"))
        assert store.registry().pull_requests[watch.id] == watch
        assert store.state().last_checked == moment
        assert store.inboxes() == {"GH-12": Inbox(events=[event])}
        assert [operation.detail for operation in store.operations()] == ["one", "two"]

    def test_a_damaged_file_is_reported(self, store: WatchStore) -> None:
        store.state_dir.mkdir(parents=True)
        (store.state_dir / "registry.json").write_text('{"pull_requests": []}', encoding="utf-8")
        with pytest.raises(SEWatchStoreUnreadableError):
            store.registry()

    def test_the_lock_is_exclusive(self, store: WatchStore) -> None:
        order: List[str] = []
        with store.lock():
            other = threading.Thread(target=self.take_lock, args=(store, order))
            other.start()
            other.join(0.3)
            order.append("first released")
        other.join(5)
        assert order == ["first released", "second held"]

    def take_lock(self, store: WatchStore, order: List[str]) -> None:
        with WatchStore(store.state_dir, TextFiles()).lock():
            order.append("second held")
