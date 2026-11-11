from __future__ import annotations

from ai_cost.models.ledger.exceptions.ledger.se_invalid_ledger_exception import SEInvalidLedgerException


class SELedgerInvalidRuns(SEInvalidLedgerException):
    """Exception raised when an invalid ``runs`` is provided."""
