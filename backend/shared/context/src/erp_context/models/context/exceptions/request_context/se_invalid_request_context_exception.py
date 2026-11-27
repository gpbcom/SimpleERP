from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidRequestContextException(SEInvalidModelException):
    """Exception raised when an invalid RequestContext is provided."""
