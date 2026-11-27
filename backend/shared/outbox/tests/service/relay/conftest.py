from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterator

import pytest
from erp_outbox.storage.publishers.recording_publisher import RecordingPublisher
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore

from backend.shared.outbox.tests.service.relay.helpers import create_customers


@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    return tmp_path / "service.db"


@pytest.fixture
def store(database_path: Path) -> SqliteOutboxStore:
    return SqliteOutboxStore(database_path)


@pytest.fixture
def publisher() -> RecordingPublisher:
    return RecordingPublisher()


@pytest.fixture
def caller(store: SqliteOutboxStore) -> Iterator[sqlite3.Connection]:
    connection = store.connect()
    store.create_table(connection)
    create_customers(connection)
    yield connection
    connection.close()
