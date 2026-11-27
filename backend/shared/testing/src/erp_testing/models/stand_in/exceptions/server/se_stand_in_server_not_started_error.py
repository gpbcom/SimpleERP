from __future__ import annotations

from erp_testing.models.stand_in.exceptions.server.se_stand_in_server_error import SEStandInServerError


class SEStandInServerNotStartedError(SEStandInServerError):
    """Raised when a stand-in server is used before it has started."""
