from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.server.se_postgres_test_server_error import SEPostgresTestServerError


class SEPostgresTestServerStartFailedError(SEPostgresTestServerError):
    """Raised when the PostgreSQL test server does not start in time."""
