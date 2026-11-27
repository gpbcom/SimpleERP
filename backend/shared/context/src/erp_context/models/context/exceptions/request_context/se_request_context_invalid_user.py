from __future__ import annotations

from erp_context.models.context.exceptions.request_context.se_invalid_request_context_exception import (
    SEInvalidRequestContextException,
)


class SERequestContextInvalidUser(SEInvalidRequestContextException):
    """Exception raised when an invalid ``user`` is provided."""
