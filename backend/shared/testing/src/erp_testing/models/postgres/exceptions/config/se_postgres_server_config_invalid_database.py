from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.config.se_invalid_postgres_server_config_exception import (
    SEInvalidPostgresServerConfigException,
)


class SEPostgresServerConfigInvalidDatabase(SEInvalidPostgresServerConfigException):
    """Exception raised when an invalid ``database`` is provided."""
