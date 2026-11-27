from __future__ import annotations

from erp_testing.models.stand_in.exceptions.server.se_stand_in_server_error import SEStandInServerError


class SEStandInServerUnknownRouteError(SEStandInServerError):
    """Raised when a request matches no registered route."""
