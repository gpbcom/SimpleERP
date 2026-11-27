from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidRefusalCodeException(SEInvalidModelException):
    """Exception raised when an invalid RefusalCode is provided.

    Notes:
        It does not subclass ``ValueError``, so that Pydantic does not wrap it in a ``ValidationError``.
    """
