from __future__ import annotations

from erp_models.idempotency.exceptions.se_invalid_idempotency_key_exception import SEInvalidIdempotencyKeyException


class SEIdempotencyKeyInvalidValue(SEInvalidIdempotencyKeyException):
    """Exception raised when an invalid ``value`` is provided."""
