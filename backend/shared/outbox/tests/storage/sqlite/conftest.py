from __future__ import annotations

# Standard library imports
import sqlite3
from pathlib import Path
from typing import Iterator

# Third-party imports
import pytest
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore

# First-party imports
from backend.shared.outbox.tests.storage.sqlite.helpers import create_customers_table


@pytest.fixture
def database_path(tmp_path: Path) -> Path:
    return tmp_path / "service.db"


@pytest.fixture
def store(database_path: Path) -> SqliteOutboxStore:
    return SqliteOutboxStore(database_path)


@pytest.fixture
def connection(database_path: Path, store: SqliteOutboxStore) -> Iterator[sqlite3.Connection]:
    caller = sqlite3.connect(database_path, autocommit=False)
    create_customers_table(caller)
    store.create_table(caller)
    yield caller
    caller.close()
