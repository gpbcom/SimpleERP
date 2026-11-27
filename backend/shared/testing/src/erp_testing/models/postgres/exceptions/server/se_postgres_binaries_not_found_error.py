from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.server.se_postgres_test_server_error import SEPostgresTestServerError


class SEPostgresBinariesNotFoundError(SEPostgresTestServerError):
    """Raised when no PostgreSQL server binaries are found in the search folders."""
