from __future__ import annotations

from erp_context.models.context.exceptions.user_context.se_invalid_user_context_exception import (
    SEInvalidUserContextException,
)


class SEUserContextInvalidCompanyId(SEInvalidUserContextException):
    """Exception raised when an invalid ``company_id`` is provided."""
