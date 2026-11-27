from __future__ import annotations

from typing import ClassVar


class SEException(Exception):
    """Base class for every exception raised by SimpleERP.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.

    Notes:
        ``CODE`` is the support reference of D122: it is resolved through the error catalogue to the message the
        person sees.
    """

    CODE: ClassVar[str] = "UNEXPECTED-ERROR-01"
