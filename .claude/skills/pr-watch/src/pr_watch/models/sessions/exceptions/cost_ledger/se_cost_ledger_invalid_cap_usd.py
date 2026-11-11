from __future__ import annotations

from pr_watch.models.sessions.exceptions.se_invalid_cost_ledger_exception import SEInvalidCostLedgerException


class SECostLedgerInvalidCapUsd(SEInvalidCostLedgerException):
    """Exception raised when an invalid ``cap_usd`` is provided."""
