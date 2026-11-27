from __future__ import annotations

from erp_testing.models.stand_in.exceptions.request.se_invalid_stand_in_request_exception import (
    SEInvalidStandInRequestException,
)


class SEStandInRequestInvalidHeaders(SEInvalidStandInRequestException):
    """Exception raised when an invalid ``headers`` is provided."""
