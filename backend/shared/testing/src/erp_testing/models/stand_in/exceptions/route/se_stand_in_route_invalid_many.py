from __future__ import annotations

from erp_testing.models.stand_in.exceptions.route.se_invalid_stand_in_route_exception import (
    SEInvalidStandInRouteException,
)


class SEStandInRouteInvalidMany(SEInvalidStandInRouteException):
    """Exception raised when an invalid ``many`` is provided."""
