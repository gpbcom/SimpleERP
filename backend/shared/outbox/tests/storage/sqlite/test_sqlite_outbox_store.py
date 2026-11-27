from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest
from erp_outbox.models.exceptions import SEOutboxStoreError
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore

from backend.shared.outbox.tests.storage.sqlite.helpers import (
    an_envelope,
    customer_names,
    insert_customer,
)


class TestSqliteOutboxStore:
    def test_a_change_and_its_event_committed_together_leave_the_event_pending(
        self, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        envelope = an_envelope()
        insert_customer(connection, 1, "Acme")
        store.add(connection, envelope)
        connection.commit()
        assert customer_names(connection) == ["Acme"]
        assert store.pending(connection) == [envelope]

    def test_a_change_and_its_event_rolled_back_leave_neither_the_row_nor_a_pending_event(
        self, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        insert_customer(connection, 1, "Acme")
        store.add(connection, an_envelope())
        connection.rollback()
        assert customer_names(connection) == []
        assert store.pending(connection) == []

    def test_an_added_event_is_invisible_to_other_connections_until_the_caller_commits(
        self, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        store.add(connection, an_envelope())
        other = store.connect()
        try:
            assert store.pending(other) == []
        finally:
            other.close()

    def test_the_write_order_is_kept(self, store: SqliteOutboxStore, connection: sqlite3.Connection) -> None:
        envelopes = [an_envelope(event_type=f"customer.event{index}") for index in range(5)]
        for envelope in envelopes:
            store.add(connection, envelope)
        connection.commit()
        assert store.pending(connection) == envelopes

    def test_a_published_event_is_no_longer_pending(
        self, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        first = an_envelope(event_type="customer.first")
        second = an_envelope(event_type="customer.second")
        store.add(connection, first)
        store.add(connection, second)
        connection.commit()
        store.mark_published(connection, first.event_id)
        assert store.pending(connection) == [second]

    def test_a_pending_event_survives_closing_every_connection_and_opening_a_new_store(
        self, database_path: Path, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        envelope = an_envelope()
        store.add(connection, envelope)
        connection.commit()
        connection.close()
        reopened = SqliteOutboxStore(database_path)
        fresh = reopened.connect()
        try:
            assert reopened.pending(fresh) == [envelope]
        finally:
            fresh.close()

    def test_create_table_runs_twice_without_harm(
        self, store: SqliteOutboxStore, connection: sqlite3.Connection
    ) -> None:
        envelope = an_envelope()
        store.add(connection, envelope)
        connection.commit()
        store.create_table(connection)
        assert store.pending(connection) == [envelope]

    def test_a_duplicate_id_is_refused(self, store: SqliteOutboxStore, connection: sqlite3.Connection) -> None:
        envelope = an_envelope()
        store.add(connection, envelope)
        with pytest.raises(SEOutboxStoreError):
            store.add(connection, envelope)

    def test_an_unknown_id_cannot_be_marked(self, store: SqliteOutboxStore, connection: sqlite3.Connection) -> None:
        with pytest.raises(SEOutboxStoreError):
            store.mark_published(connection, an_envelope().event_id)

    def test_an_unreachable_path_is_refused(self, tmp_path: Path) -> None:
        unreachable = SqliteOutboxStore(tmp_path / "missing" / "service.db")
        with pytest.raises(SEOutboxStoreError):
            unreachable.connect()
