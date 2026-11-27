from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.config.se_invalid_postgres_server_config_exception import (
    SEInvalidPostgresServerConfigException,
)


class SEPostgresServerConfigInvalidStartTimeoutS(SEInvalidPostgresServerConfigException):
    """Exception raised when an invalid ``start_timeout_s`` is provided."""
