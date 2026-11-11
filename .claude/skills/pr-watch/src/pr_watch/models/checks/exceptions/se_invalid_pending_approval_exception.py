from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidPendingApprovalException(SEPrWatchError):
    """Exception raised when an invalid PendingApproval is provided."""
