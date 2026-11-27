from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidUserContextException(SEInvalidModelException):
    """Exception raised when an invalid UserContext is provided."""
