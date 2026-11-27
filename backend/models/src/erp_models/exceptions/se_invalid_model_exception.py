from __future__ import annotations

from typing import ClassVar

from erp_models.exceptions.se_exception import SEException


class SEInvalidModelException(SEException):
    """Exception raised when an invalid model is provided.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.

    Notes:
        ``CODE`` is the support reference of D122: it is resolved through the error catalogue to the message the
        person sees.
    """

    CODE: ClassVar[str] = "INVALID-INPUT-01"
