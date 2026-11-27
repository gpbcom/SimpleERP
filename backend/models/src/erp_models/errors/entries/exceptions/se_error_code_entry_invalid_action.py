from __future__ import annotations

from erp_models.errors.entries.exceptions.se_invalid_error_code_entry_exception import SEInvalidErrorCodeEntryException


class SEErrorCodeEntryInvalidAction(SEInvalidErrorCodeEntryException):
    """Exception raised when an invalid ``action`` is provided."""
