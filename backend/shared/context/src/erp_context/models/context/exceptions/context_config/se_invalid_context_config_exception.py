from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidContextConfigException(SEInvalidModelException):
    """Exception raised when an invalid ContextConfig is provided."""
