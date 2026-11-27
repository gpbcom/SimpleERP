from __future__ import annotations

from erp_testing.factories.postgres.postgres_test_server_factory import PostgresTestServerFactory
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_test_server import PostgresTestServer


class TestPostgresTestServerFactory:
    def test_it_builds_a_server_that_is_not_started(self) -> None:
        server = PostgresTestServerFactory(PostgresServerConfig(database="other")).create()
        assert isinstance(server, PostgresTestServer)
        server.close()

    def test_each_call_builds_a_new_server(self) -> None:
        factory = PostgresTestServerFactory(PostgresServerConfig())
        assert factory.create() is not factory.create()
