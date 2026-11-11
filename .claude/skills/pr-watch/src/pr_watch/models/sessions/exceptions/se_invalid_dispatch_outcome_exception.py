from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidDispatchOutcomeException(SEPrWatchError):
    """Exception raised when an invalid DispatchOutcome is provided."""
