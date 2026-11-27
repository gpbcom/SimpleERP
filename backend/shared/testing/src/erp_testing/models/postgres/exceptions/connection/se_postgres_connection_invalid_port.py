from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.connection.se_invalid_postgres_connection_exception import (
    SEInvalidPostgresConnectionException,
)


class SEPostgresConnectionInvalidPort(SEInvalidPostgresConnectionException):
    """Exception raised when an invalid ``port`` is provided."""
