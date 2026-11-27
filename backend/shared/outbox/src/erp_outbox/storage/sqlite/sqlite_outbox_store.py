from __future__ import annotations

# Standard library imports
import sqlite3
from datetime import UTC, datetime
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, List, Optional

# First-party imports
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.record_id import RecordId

from erp_outbox.models.exceptions import SEOutboxStoreError
from erp_outbox.storage.outbox_store import OutboxStore


class SqliteOutboxStore(OutboxStore[sqlite3.Connection]):
    """The outbox kept in a table of a SQLite database.

    Attributes:
        CREATE_SQL (str): Creates the table when missing.
        INSERT_SQL (str): Writes one event.
        PENDING_SQL (str): Reads the unpublished events in write order.
        MARK_SQL (str): Sets the published time of one event.
        database_path (Path): The database file.
        logger (Logger): Logger instance.

    Notes:
        - The table has ``sequence``, an autoincrement key that gives the write order, ``event_id``, unique, the
          envelope as JSON in ``envelope``, and ``published_at``, a UTC ISO 8601 text that is NULL until published.
        - ``connect`` opens with ``autocommit=False``, so the caller's change and ``add`` share one transaction.
        - **A payload is never logged.**
    """

    CREATE_SQL: ClassVar[str] = (
        "CREATE TABLE IF NOT EXISTS outbox ("
        "sequence INTEGER PRIMARY KEY AUTOINCREMENT, "
        "event_id TEXT NOT NULL UNIQUE, "
        "envelope TEXT NOT NULL, "
        "published_at TEXT)"
    )
    INSERT_SQL: ClassVar[str] = "INSERT INTO outbox (event_id, envelope) VALUES (?, ?)"
    PENDING_SQL: ClassVar[str] = "SELECT envelope FROM outbox WHERE published_at IS NULL ORDER BY sequence"
    MARK_SQL: ClassVar[str] = "UPDATE outbox SET published_at = ? WHERE event_id = ? AND published_at IS NULL"

    def __init__(self, database_path: Path, logger: Optional[Logger] = None) -> None:
        """Keep the database path.

        Args:
            database_path (Path): The database file.
            logger (Optional[Logger]): Logger instance.
        """
        self.database_path = database_path
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def connect(self) -> sqlite3.Connection:
        """Open a connection whose transactions the caller commits.

        Returns:
            sqlite3.Connection: A new connection, opened with ``autocommit=False``.

        Raises:
            SEOutboxStoreError: When the database cannot be opened.
        """
        try:
            connection = sqlite3.connect(self.database_path, autocommit=False)
        except sqlite3.Error as error:
            self.logger.error("Cannot open the outbox database: %s.", type(error).__name__)
            raise SEOutboxStoreError(f"Cannot open the outbox database: {self.database_path}.") from error
        self.logger.debug("Opened the outbox database %s.", self.database_path)
        return connection

    def create_table(self, connection: sqlite3.Connection) -> None:
        """Create the outbox table when it does not exist yet, and commit.

        Args:
            connection (sqlite3.Connection): The connection to create it with.

        Raises:
            SEOutboxStoreError: When the table cannot be created.
        """
        try:
            connection.execute(self.CREATE_SQL)
            connection.commit()
        except sqlite3.Error as error:
            self.logger.error("Cannot create the outbox table: %s.", type(error).__name__)
            raise SEOutboxStoreError("Cannot create the outbox table.") from error
        self.logger.debug("The outbox table is ready.")

    def add(self, connection: sqlite3.Connection, envelope: EventEnvelope) -> None:
        """Write one event inside the caller's open transaction, without committing or rolling back.

        Args:
            connection (sqlite3.Connection): The connection of the caller's transaction.
            envelope (EventEnvelope): The event to keep.

        Raises:
            SEOutboxStoreError: When the identifier already exists or the write fails.
        """
        event_id = envelope.event_id.value
        try:
            connection.execute(self.INSERT_SQL, (event_id, envelope.model_dump_json()))
        except sqlite3.Error as error:
            self.logger.error("Cannot add event %s: %s.", event_id, type(error).__name__)
            raise SEOutboxStoreError(f"Cannot add event {event_id}.") from error
        self.logger.debug("Added event %s to the caller's transaction.", event_id)

    def pending(self, connection: sqlite3.Connection) -> List[EventEnvelope]:
        """Read the events not published yet.

        Args:
            connection (sqlite3.Connection): The connection to read with.

        Returns:
            List[EventEnvelope]: The unpublished events, in write order.

        Raises:
            SEOutboxStoreError: When the table cannot be read.
        """
        try:
            rows = connection.execute(self.PENDING_SQL).fetchall()
        except sqlite3.Error as error:
            self.logger.error("Cannot read the pending events: %s.", type(error).__name__)
            raise SEOutboxStoreError("Cannot read the pending events.") from error
        self.logger.debug("Read %d pending events.", len(rows))
        return [EventEnvelope.model_validate_json(row[0]) for row in rows]

    def mark_published(self, connection: sqlite3.Connection, event_id: RecordId) -> None:
        """Mark one event as published and commit.

        Args:
            connection (sqlite3.Connection): The connection to write with.
            event_id (RecordId): The identifier of the event.

        Raises:
            SEOutboxStoreError: When the event is unknown or already published, or the write fails.
        """
        published_at = datetime.now(UTC).isoformat()
        try:
            updated = connection.execute(self.MARK_SQL, (published_at, event_id.value)).rowcount
            if updated != 1:
                connection.rollback()
                self.logger.error("Cannot mark event %s: it is not pending.", event_id.value)
                raise SEOutboxStoreError(f"Cannot mark event {event_id.value}: it is not pending.")
            connection.commit()
        except sqlite3.Error as error:
            self.logger.error("Cannot mark event %s: %s.", event_id.value, type(error).__name__)
            raise SEOutboxStoreError(f"Cannot mark event {event_id.value}.") from error
        self.logger.info("Marked event %s as published.", event_id.value)
