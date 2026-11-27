from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Iterator

import pytest
from erp_lifecycle.runnables.runnable import Runnable
from erp_testing.models.postgres.exceptions import (
    SEPostgresBinariesNotFoundError,
    SEPostgresTestServerNotStartedError,
    SEPostgresTestServerStartFailedError,
)
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_binaries import PostgresBinaries
from erp_testing.postgres.postgres_test_server import PostgresTestServer

from tests.postgres.fake_postgres_binaries import FakePostgresBinaries


class TestPostgresTestServer:
    @pytest.fixture
    def real_binaries(self) -> str:
        try:
            return str(PostgresBinaries(PostgresServerConfig()).find())
        except SEPostgresBinariesNotFoundError:
            pytest.skip("No PostgreSQL binaries (initdb, pg_ctl, pg_isready, psql) were found on this machine.")

    @pytest.fixture
    def real_server(self, real_binaries: str) -> Iterator[PostgresTestServer]:
        server = PostgresTestServer(PostgresServerConfig(search_dirs=[real_binaries]))
        try:
            server.initialize()
            yield server
        finally:
            server.close()

    def isready(self, bin_dir: str, host: str, port: int) -> int:
        return subprocess.run(
            [str(Path(bin_dir) / "pg_isready"), "-h", host, "-p", str(port)], capture_output=True, check=False
        ).returncode

    def test_the_server_is_a_runnable(self) -> None:
        assert issubclass(PostgresTestServer, Runnable)

    def test_the_connection_is_refused_before_initialize(self) -> None:
        server = PostgresTestServer(PostgresServerConfig())
        with pytest.raises(SEPostgresTestServerNotStartedError):
            assert server.connection is None

    def test_close_is_safe_before_initialize_and_twice(self) -> None:
        server = PostgresTestServer(PostgresServerConfig())
        server.close()
        server.close()

    def test_a_server_never_ready_fails_and_close_removes_the_folder(self, tmp_path: Path) -> None:
        bin_dir = FakePostgresBinaries(tmp_path).write(tmp_path / "bin", {"pg_isready": 2})
        server = PostgresTestServer(PostgresServerConfig(search_dirs=[str(bin_dir)], start_timeout_s=0.2))
        with pytest.raises(SEPostgresTestServerStartFailedError):
            server.initialize()
        data_dir = Path(server.data_dir)
        server.close()
        assert not data_dir.exists()
        server.close()

    def test_a_started_server_accepts_connections(self, real_server: PostgresTestServer, real_binaries: str) -> None:
        connection = real_server.connection
        assert connection.host == "127.0.0.1"
        assert self.isready(real_binaries, connection.host, connection.port) == 0
        result = subprocess.run(
            [str(Path(real_binaries) / "psql"), connection.dsn, "-c", "select 1"], capture_output=True, check=False
        )
        assert result.returncode == 0

    def test_close_stops_the_server_and_removes_the_folder(self, real_binaries: str) -> None:
        server = PostgresTestServer(PostgresServerConfig(search_dirs=[real_binaries]))
        server.initialize()
        connection = server.connection
        data_dir = Path(server.data_dir)
        assert data_dir.exists()
        server.close()
        assert self.isready(real_binaries, connection.host, connection.port) != 0
        assert not data_dir.exists()
        server.close()
