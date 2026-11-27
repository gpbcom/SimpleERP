from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.config.se_invalid_postgres_server_config_exception import (
    SEInvalidPostgresServerConfigException,
)


class SEPostgresServerConfigInvalidUser(SEInvalidPostgresServerConfigException):
    """Exception raised when an invalid ``user`` is provided."""
