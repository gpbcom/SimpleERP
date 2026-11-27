from __future__ import annotations

from erp_models.times.exceptions.se_invalid_utc_timestamp_exception import SEInvalidUtcTimestampException


class SEUtcTimestampInvalidInstant(SEInvalidUtcTimestampException):
    """Exception raised when an invalid ``instant`` is provided."""
