from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_cost_ledger_exception import SEInvalidCostLedgerException


class SECostLedgerInvalidSpentUsd(SEInvalidCostLedgerException):
    """Exception raised when an invalid ``spent_usd`` is provided."""
