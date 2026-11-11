from __future__ import annotations

from ticket_docs.models.issues.exceptions.reference_kind.se_invalid_reference_kind_exception import (
    SEInvalidReferenceKindException,
)


class SEReferenceKindInvalidPatterns(SEInvalidReferenceKindException):
    """Exception raised when an invalid ``patterns`` is provided."""
