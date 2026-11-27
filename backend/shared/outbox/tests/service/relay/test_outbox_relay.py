from __future__ import annotations

import logging
import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest
from erp_outbox.models.exceptions import SEOutboxStoreError
from erp_outbox.service.relay.outbox_relay import OutboxRelay
from erp_outbox.storage.publishers.recording_publisher import RecordingPublisher
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore

from backend.shared.outbox.tests.service.relay.helpers import an_envelope, count_customers, write_change
from backend.shared.outbox.tests.service.relay.refusing_publisher import RefusingPublisher
from backend.shared.outbox.tests.service.relay.unmarkable_store import UnmarkableStore


class TestOutboxRelay:
    SCRIPT = Path(__file__).with_name("write_then_stop.py")

    def test_every_written_event_is_published_once_in_write_order(
        self, store: SqliteOutboxStore, publisher: RecordingPublisher, caller: sqlite3.Connection
    ) -> None:
        envelopes = [an_envelope(f"customer.event{number}") for number in range(3)]
        for number, envelope in enumerate(envelopes):
            write_change(caller, store, number, envelope)
        caller.commit()
        relay = OutboxRelay(store, publisher)
        relay.execute()
        assert publisher.published == envelopes
        assert relay.published_count == 3
        assert store.pending(caller) == []

    def test_a_second_execute_publishes_nothing_new(
        self, store: SqliteOutboxStore, publisher: RecordingPublisher, caller: sqlite3.Connection
    ) -> None:
        write_change(caller, store, 1, an_envelope())
        caller.commit()
        OutboxRelay(store, publisher).execute()
        second = OutboxRelay(store, publisher)
        second.execute()
        assert len(publisher.published) == 1
        assert second.published_count == 0

    def test_an_event_written_before_a_stop_is_published_after_the_restart(
        self, database_path: Path, store: SqliteOutboxStore, publisher: RecordingPublisher
    ) -> None:
        result = subprocess.run([sys.executable, str(self.SCRIPT), str(database_path)], check=False)
        assert result.returncode == 0
        OutboxRelay(store, publisher).execute()
        assert [envelope.event_type for envelope in publisher.published] == ["customer.created"]

    def test_a_rolled_back_change_publishes_nothing(
        self, store: SqliteOutboxStore, publisher: RecordingPublisher, caller: sqlite3.Connection
    ) -> None:
        write_change(caller, store, 1, an_envelope())
        caller.rollback()
        relay = OutboxRelay(store, publisher)
        relay.execute()
        assert publisher.published == []
        assert relay.published_count == 0
        assert count_customers(caller) == 0

    def test_a_refused_publish_leaves_the_event_pending_and_the_next_run_publishes_it(
        self, store: SqliteOutboxStore, caller: sqlite3.Connection, caplog: pytest.LogCaptureFixture
    ) -> None:
        envelopes = [an_envelope("customer.first"), an_envelope("customer.second")]
        for number, envelope in enumerate(envelopes):
            write_change(caller, store, number, envelope)
        caller.commit()
        publisher = RefusingPublisher(refusals=1)
        with caplog.at_level(logging.WARNING):
            first = OutboxRelay(store, publisher)
            first.execute()
        assert first.published_count == 0
        assert any(record.levelno == logging.WARNING for record in caplog.records)
        assert store.pending(caller) == envelopes
        caller.commit()
        second = OutboxRelay(store, publisher)
        second.execute()
        assert publisher.published == envelopes
        assert store.pending(caller) == []

    def test_a_stop_between_publish_and_mark_publishes_the_event_again_later(
        self, database_path: Path, store: SqliteOutboxStore, publisher: RecordingPublisher, caller: sqlite3.Connection
    ) -> None:
        envelope = an_envelope()
        write_change(caller, store, 1, envelope)
        caller.commit()
        with pytest.raises(SEOutboxStoreError):
            OutboxRelay(UnmarkableStore(database_path), publisher).execute()
        assert publisher.published == [envelope]
        OutboxRelay(store, publisher).execute()
        assert publisher.published == [envelope, envelope]

    def test_an_unreachable_database_raises_and_closes_safely(
        self, tmp_path: Path, publisher: RecordingPublisher
    ) -> None:
        relay = OutboxRelay(SqliteOutboxStore(tmp_path / "missing" / "service.db"), publisher)
        with pytest.raises(SEOutboxStoreError):
            relay.execute()
        relay.close()
        assert publisher.published == []
