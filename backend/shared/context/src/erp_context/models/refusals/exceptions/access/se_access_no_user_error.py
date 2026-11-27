from __future__ import annotations

from typing import ClassVar

from erp_context.models.refusals.exceptions.access.se_access_error import SEAccessError


class SEAccessNoUserError(SEAccessError):
    """Raised when a request has no authenticated user.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.
    """

    CODE: ClassVar[str] = "CONTEXT-USER-01"
