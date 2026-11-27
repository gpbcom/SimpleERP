from __future__ import annotations

from erp_models.exceptions import SEInvalidModelException


class SEInvalidRecordRefException(SEInvalidModelException):
    """Exception raised when an invalid RecordRef is provided."""
