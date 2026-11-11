from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidCostLedgerException(SEPrWatchError):
    """Exception raised when an invalid CostLedger is provided."""
