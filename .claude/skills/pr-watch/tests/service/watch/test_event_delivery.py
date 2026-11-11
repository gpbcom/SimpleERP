from __future__ import annotations

from datetime import timedelta
from pathlib import Path

import pytest

from pr_watch.models.configuration.commands_config import CommandsConfig
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import OperationKind
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.registry import Registry
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.sessions.session_dispatcher import SessionDispatcher
from pr_watch.service.watch.event_delivery import EventDelivery
from pr_watch.storage.desktop.command_runner import CommandRunner
from pr_watch.storage.files.text_files import TextFiles
from pr_watch.storage.state.watch_store import WatchStore
from tests.stand_ins.helpers import NOW, a_watch, an_event, recorded_calls, write_program


class TestEventDelivery:
    @pytest.fixture
    def store(self, tmp_path: Path) -> WatchStore:
        return WatchStore(tmp_path / "state", TextFiles())

    @pytest.fixture
    def watch(self, tmp_path: Path) -> TicketWatch:
        return a_watch(tmp_path)

    def delivery(self, store: WatchStore, commands: CommandsConfig, catalog: WatchCatalog) -> EventDelivery:
        return EventDelivery(store, SessionDispatcher(commands, CommandRunner()), catalog.timing)

    def test_a_new_event_is_filed_once_and_delivered_once(
        self, store: WatchStore, commands: CommandsConfig, catalog: WatchCatalog, watch: TicketWatch, calls_log: Path
    ) -> None:
        registry, state = Registry(pull_requests={watch.id: watch}), WatchState()
        delivery = self.delivery(store, commands, catalog)
        assert delivery.deliver(registry, state, {}, [an_event(watch)], NOW) == 1
        assert delivery.deliver(registry, state, {}, [an_event(watch)], NOW) == 0
        assert len(store.inbox(watch.key).events) == 1
        assert list(state.delivery.dispatched) == [an_event(watch).id]
        assert [call[0] for call in recorded_calls(calls_log)] == ["code", "xdg-open", "notify-send"]
        kinds = [operation.kind for operation in store.operations()]
        assert kinds == [OperationKind.DETECTED, OperationKind.REOPENED]

    def test_a_failed_dispatch_is_not_marked_and_is_tried_again(
        self, store: WatchStore, commands: CommandsConfig, catalog: WatchCatalog, watch: TicketWatch, tmp_path: Path
    ) -> None:
        broken = commands.model_copy(update={"notifier": str(write_program(tmp_path / "bin", "broken", "exit 1"))})
        registry, state = Registry(pull_requests={watch.id: watch}), WatchState()
        self.delivery(store, broken, catalog).deliver(registry, state, {}, [an_event(watch)], NOW)
        assert state.delivery.dispatched == {}
        assert store.operations()[-1].kind == OperationKind.WARNING
        self.delivery(store, commands, catalog).deliver(registry, state, {}, [], NOW)
        assert list(state.delivery.dispatched) == [an_event(watch).id]

    def test_waiting_events_are_reminded_after_the_delay_only(
        self, store: WatchStore, commands: CommandsConfig, catalog: WatchCatalog, watch: TicketWatch, calls_log: Path
    ) -> None:
        registry, state = Registry(pull_requests={watch.id: watch}), WatchState()
        delivery = self.delivery(store, commands, catalog)
        delivery.deliver(registry, state, {}, [an_event(watch)], NOW)
        delivery.remind(registry, state, NOW + timedelta(minutes=10))
        assert len(recorded_calls(calls_log)) == 3
        delivery.remind(registry, state, NOW + timedelta(minutes=61))
        assert recorded_calls(calls_log)[-1][0] == "notify-send"
        assert state.delivery.notified[watch.key] == NOW + timedelta(minutes=61)
