from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.company_id import CompanyId
from erp_outbox.service.factories.relay_factory import RelayFactory
from erp_outbox.service.factories.sqlite.sqlite_relay_factory import SqliteRelayFactory
from erp_outbox.service.relay.outbox_relay import OutboxRelay
from erp_outbox.storage.publishers.recording_publisher import RecordingPublisher
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore


class TestSqliteRelayFactory:
    def test_create_returns_an_outbox_relay(self, tmp_path: Path) -> None:
        factory = SqliteRelayFactory(tmp_path / "outbox.db", RecordingPublisher())
        assert isinstance(factory.create(), OutboxRelay)

    def test_the_relay_it_creates_publishes_the_events_pending_in_that_database(self, tmp_path: Path) -> None:
        path = tmp_path / "outbox.db"
        envelope = EventEnvelope(event_type="audit.entry.appended", company_id=CompanyId(value="C-12"))
        connection = sqlite3.connect(path, autocommit=False)
        try:
            store = SqliteOutboxStore(path)
            store.create_table(connection)
            store.add(connection, envelope)
            connection.commit()
        finally:
            connection.close()
        publisher = RecordingPublisher()
        SqliteRelayFactory(path, publisher).create().execute()
        assert publisher.published == [envelope]

    def test_two_create_calls_return_two_distinct_relays(self, tmp_path: Path) -> None:
        factory = SqliteRelayFactory(tmp_path / "outbox.db", RecordingPublisher())
        assert factory.create() is not factory.create()

    def test_the_abstract_relay_factory_cannot_be_instantiated(self) -> None:
        with pytest.raises(TypeError):
            RelayFactory()  # type: ignore[abstract]
