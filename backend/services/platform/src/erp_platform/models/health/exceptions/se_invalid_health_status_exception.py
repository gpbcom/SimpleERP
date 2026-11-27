from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidHealthStatusException(SEInvalidModelException):
    """Exception raised when an invalid HealthStatus is provided.

    Notes:
        It does not subclass ``ValueError``, so that Pydantic does not wrap it in a ``ValidationError``.
    """
