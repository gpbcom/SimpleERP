from __future__ import annotations

from erp_context.models.refusals.exceptions.codes.se_invalid_refusal_code_exception import SEInvalidRefusalCodeException


class SERefusalCodeInvalidTitleKey(SEInvalidRefusalCodeException):
    """Exception raised when an invalid ``title_key`` is provided."""
