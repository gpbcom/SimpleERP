from __future__ import annotations

from erp_context.models.context.exceptions.record_ref.se_invalid_record_ref_exception import SEInvalidRecordRefException


class SERecordRefInvalidRecordId(SEInvalidRecordRefException):
    """Exception raised when an invalid ``record_id`` is provided."""
