from __future__ import annotations

# Standard library imports
from logging import Logger
from typing import Optional

# First-party imports
from erp_testing.factories.helper_factory import HelperFactory
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_test_server import PostgresTestServer


class PostgresTestServerFactory(HelperFactory[PostgresTestServer]):
    """Factory that builds PostgreSQL test servers.

    Attributes:
        config (PostgresServerConfig): The settings every server is built with.
        logger (Logger): Logger instance.
    """

    def __init__(self, config: PostgresServerConfig, logger: Optional[Logger] = None) -> None:
        """Create the factory.

        Args:
            config (PostgresServerConfig): The settings of the servers to build.
            logger (Optional[Logger]): Logger to use. A logger named after the module is created when it is ``None``.
        """
        super().__init__(logger)
        self.config = config

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self) -> PostgresTestServer:
        """Build a PostgreSQL test server.

        Returns:
            PostgresTestServer: A new server, not yet initialised.
        """
        self.logger.debug("Creating a PostgreSQL test server for database %s.", self.config.database)
        return PostgresTestServer(self.config, self.logger)
