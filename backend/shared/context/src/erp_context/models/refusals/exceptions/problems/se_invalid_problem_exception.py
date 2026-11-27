from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidProblemException(SEInvalidModelException):
    """Exception raised when an invalid Problem is provided.

    Notes:
        It does not subclass ``ValueError``, so that Pydantic does not wrap it in a ``ValidationError``.
    """
