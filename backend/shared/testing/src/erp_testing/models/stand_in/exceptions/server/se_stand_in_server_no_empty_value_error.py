from __future__ import annotations

from erp_testing.models.stand_in.exceptions.server.se_stand_in_server_error import SEStandInServerError


class SEStandInServerNoEmptyValueError(SEStandInServerError):
    """Raised when a model has no valid empty value to answer with."""
