from __future__ import annotations

import sqlite3

from erp_models.ids.record_id import RecordId
from erp_outbox.models.exceptions import SEOutboxStoreError
from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore


class UnmarkableStore(SqliteOutboxStore):
    """A store that cannot mark an event, as after a stop between the publish and its mark."""

    def mark_published(self, connection: sqlite3.Connection, event_id: RecordId) -> None:
        """Refuse to mark the event."""
        raise SEOutboxStoreError("The process stopped before the event was marked.")
