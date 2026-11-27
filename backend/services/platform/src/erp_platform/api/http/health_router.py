from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# Third-party imports
from fastapi import APIRouter

# First-party imports
from erp_platform.models.health.health_status import HealthStatus
from erp_platform.service.health.health_service import HealthService


class HealthRouter:
    """The HTTP route that tells whether the service is alive.

    Attributes:
        health_service (HealthService): Answers the health check.
        logger (Logger): Logger instance.
        api_router (APIRouter): The router holding ``GET /health``.

    Notes:
        The ``/v1`` prefix is added by the application builder, not here.
    """

    def __init__(self, health_service: HealthService, logger: Optional[Logger] = None) -> None:
        """Create the router and register its route.

        Args:
            health_service (HealthService): Answers the health check.
            logger (Optional[Logger]): Logger instance, a module logger when omitted.
        """
        self.health_service = health_service
        self.logger = logger if logger else getLogger(__name__)
        self.api_router = APIRouter()
        self.api_router.add_api_route("/health", self.get_health, methods=["GET"], response_model=HealthStatus)

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def router(self) -> APIRouter:
        """Return the router to include in the application.

        Returns:
            APIRouter: The router with ``GET /health``.
        """
        self.logger.debug("Router of %d routes handed out.", len(self.api_router.routes))
        return self.api_router

    def get_health(self) -> HealthStatus:
        """Answer the health check.

        Returns:
            HealthStatus: The status given by the health service.
        """
        status = self.health_service.check()
        self.logger.debug("Health answered %s.", status.status.value)
        return status
