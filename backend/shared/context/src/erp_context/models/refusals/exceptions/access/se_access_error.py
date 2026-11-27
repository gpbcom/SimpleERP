from __future__ import annotations

from typing import ClassVar

from erp_models.exceptions import SEError

from erp_context.models.refusals.enums import RefusalReason


class SEAccessError(SEError):
    """Base class for every error raised when a request is refused.

    Attributes:
        CODE (str): The code of the error pattern that the problem+json handler reads.
        reason (RefusalReason): Why the request was refused.

    Notes:
        The reason, not the class, selects the refusal code of the catalogue, so that the response is built from data.
    """

    CODE: ClassVar[str] = "RIGHTS-DENIED-01"

    def __init__(self, reason: RefusalReason, message: str) -> None:
        """Keep the reason with the message.

        Args:
            reason (RefusalReason): Why the request was refused.
            message (str): The message of the error.
        """
        super().__init__(message)
        self.reason = reason
