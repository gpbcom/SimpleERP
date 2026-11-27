from __future__ import annotations

from erp_context.models.context.exceptions.user_context.se_invalid_user_context_exception import (
    SEInvalidUserContextException,
)


class SEUserContextInvalidUserId(SEInvalidUserContextException):
    """Exception raised when an invalid ``user_id`` is provided."""
