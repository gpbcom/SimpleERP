from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import Optional

# First-party imports
from erp_testing.factories.helper_factory import HelperFactory
from erp_testing.stand_in.stand_in_server import StandInServer


class StandInServerFactory(HelperFactory[StandInServer]):
    """Factory that builds stand-in servers.

    Attributes:
        host (str): The address each server binds.
        port (int): The port each server binds, ``0`` for a free one.
        logger (Logger): Logger instance.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 0, logger: Optional[Logger] = None) -> None:
        """Create the factory.

        Args:
            host (str): The address each server binds.
            port (int): The port each server binds, ``0`` for a free one.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        super().__init__(logger)
        self.host = host
        self.port = port

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self) -> StandInServer:
        """Build a new stand-in server.

        Returns:
            StandInServer: A server, not yet initialised.
        """
        self.logger.debug("Creating a stand-in server on %s:%d.", self.host, self.port)
        return StandInServer(self.host, self.port, self.logger)
