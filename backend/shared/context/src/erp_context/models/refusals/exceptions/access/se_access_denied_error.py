from __future__ import annotations

from typing import ClassVar

from erp_context.models.refusals.exceptions.access.se_access_error import SEAccessError


class SEAccessDeniedError(SEAccessError):
    """Raised when the rights refuse an action.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.
    """

    CODE: ClassVar[str] = "RIGHTS-DENIED-02"
