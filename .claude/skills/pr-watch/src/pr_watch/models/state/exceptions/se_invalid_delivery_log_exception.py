from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidDeliveryLogException(SEPrWatchError):
    """Exception raised when an invalid DeliveryLog is provided."""
