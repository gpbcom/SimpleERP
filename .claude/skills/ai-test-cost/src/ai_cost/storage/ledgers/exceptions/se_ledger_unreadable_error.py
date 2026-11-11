from __future__ import annotations

from ai_cost.storage.ledgers.exceptions.se_ledger_store_error import SELedgerStoreError


class SELedgerUnreadableError(SELedgerStoreError):
    """Raised when a ledger file cannot be read or is not a valid ledger."""
