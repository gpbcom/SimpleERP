from __future__ import annotations

from ticket_docs.models.permits.exceptions.squash_permit.se_invalid_squash_permit_exception import (
    SEInvalidSquashPermitException,
)


class SESquashPermitInvalidBranch(SEInvalidSquashPermitException):
    """Exception raised when an invalid ``branch`` is provided."""
