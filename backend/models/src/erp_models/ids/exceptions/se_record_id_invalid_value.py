from __future__ import annotations

from erp_models.ids.exceptions.se_invalid_record_id_exception import SEInvalidRecordIdException


class SERecordIdInvalidValue(SEInvalidRecordIdException):
    """Exception raised when an invalid ``value`` is provided."""
