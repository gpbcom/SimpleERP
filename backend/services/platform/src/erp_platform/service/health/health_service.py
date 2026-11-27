from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from erp_platform.models.health.enums import HealthState
from erp_platform.models.health.health_status import HealthStatus


class HealthService:
    """Answer whether the service is alive.

    Attributes:
        logger (Logger): Logger instance.
    """

    def __init__(self, logger: Optional[Logger] = None) -> None:
        """Create the service.

        Args:
            logger (Optional[Logger]): Logger instance, a module logger when omitted.
        """
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def check(self) -> HealthStatus:
        """Check the health of the service.

        Returns:
            HealthStatus: The status, ``ok`` while the process answers.
        """
        self.logger.debug("Health check answered %s.", HealthState.OK.value)
        return HealthStatus(status=HealthState.OK)
