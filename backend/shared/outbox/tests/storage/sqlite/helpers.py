from __future__ import annotations

# Standard library imports
import sqlite3
from typing import List

# First-party imports
from erp_models.events.event_envelope import EventEnvelope
from erp_models.ids.company_id import CompanyId

COMPANY = "C-TEST-1"


def create_customers_table(connection: sqlite3.Connection) -> None:
    """Create the synthetic ``customers`` table that stands for the caller's change, and commit."""
    connection.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
    connection.commit()


def insert_customer(connection: sqlite3.Connection, customer_id: int, name: str) -> None:
    """Insert one synthetic customer in the connection's open transaction."""
    connection.execute("INSERT INTO customers (id, name) VALUES (?, ?)", (customer_id, name))


def customer_names(connection: sqlite3.Connection) -> List[str]:
    """Return the names of the customers the connection sees, ordered by id."""
    return [row[0] for row in connection.execute("SELECT name FROM customers ORDER BY id")]


def an_envelope(event_type: str = "customer.created", company: str = COMPANY) -> EventEnvelope:
    """Build a synthetic envelope with a fresh id."""
    return EventEnvelope(event_type=event_type, company_id=CompanyId(value=company), payload={"name": "Acme"})
