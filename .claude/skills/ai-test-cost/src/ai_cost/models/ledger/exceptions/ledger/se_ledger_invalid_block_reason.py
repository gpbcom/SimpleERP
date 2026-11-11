from __future__ import annotations

from ai_cost.models.ledger.exceptions.ledger.se_invalid_ledger_exception import SEInvalidLedgerException


class SELedgerInvalidBlockReason(SEInvalidLedgerException):
    """Exception raised when an invalid ``block_reason`` is provided."""
