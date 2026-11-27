from __future__ import annotations

import sqlite3

from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.company_id import CompanyId
from erp_outbox.storage.outbox_store import OutboxStore


def create_customers(connection: sqlite3.Connection) -> None:
    """Create the synthetic ``customers`` table the caller's change writes to."""
    connection.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    connection.commit()


def an_envelope(event_type: str = "customer.created", company: str = "C-12") -> EventEnvelope:
    """Build a synthetic event with only its required fields."""
    return EventEnvelope(event_type=event_type, company_id=CompanyId(value=company))


def write_change(
    connection: sqlite3.Connection,
    store: OutboxStore[sqlite3.Connection],
    customer_id: int,
    envelope: EventEnvelope,
) -> None:
    """Write a synthetic customer and its event in the caller's open transaction, without committing."""
    connection.execute("INSERT INTO customers (id, name) VALUES (?, ?)", (customer_id, f"Customer {customer_id}"))
    store.add(connection, envelope)


def count_customers(connection: sqlite3.Connection) -> int:
    """Count the synthetic customers."""
    row = connection.execute("SELECT COUNT(*) FROM customers").fetchone()
    return int(row[0])
