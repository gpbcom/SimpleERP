from __future__ import annotations

from ticket_docs.models.permits.exceptions.squash_permit.se_invalid_squash_permit_exception import (
    SEInvalidSquashPermitException,
)


class SESquashPermitInvalidHash(SEInvalidSquashPermitException):
    """Exception raised when an invalid ``head`` or ``tree`` is provided."""
