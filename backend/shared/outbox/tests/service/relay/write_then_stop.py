from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

from erp_outbox.storage.sqlite.sqlite_outbox_store import SqliteOutboxStore


def main() -> None:
    """Write a synthetic change and its event in one transaction, commit, then stop before any relay runs."""
    spec = importlib.util.spec_from_file_location("relay_helpers", Path(__file__).with_name("helpers.py"))
    assert spec is not None
    assert spec.loader is not None
    helpers = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helpers)

    store = SqliteOutboxStore(Path(sys.argv[1]))
    connection = store.connect()
    store.create_table(connection)
    helpers.create_customers(connection)
    helpers.write_change(connection, store, 1, helpers.an_envelope("customer.created"))
    connection.commit()
    os._exit(0)


if __name__ == "__main__":
    main()
