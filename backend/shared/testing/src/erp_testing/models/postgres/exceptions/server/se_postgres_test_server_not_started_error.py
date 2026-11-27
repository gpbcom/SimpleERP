from __future__ import annotations

# First-party imports
from erp_testing.models.postgres.exceptions.server.se_postgres_test_server_error import SEPostgresTestServerError


class SEPostgresTestServerNotStartedError(SEPostgresTestServerError):
    """Raised when the PostgreSQL test server is used before it is started."""
