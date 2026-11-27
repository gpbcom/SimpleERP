from __future__ import annotations

from typing import ClassVar

from erp_models.exceptions.se_exception import SEException


class SEError(SEException):
    """Base class for every error raised by a layer of a service, a library or a plugin.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.

    Notes:
        ``CODE`` is the support reference of D122: it is resolved through the error catalogue to the message the
        person sees.
    """

    CODE: ClassVar[str] = "SERVICE-FAILURE-01"
