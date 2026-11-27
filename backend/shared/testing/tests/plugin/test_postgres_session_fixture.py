from __future__ import annotations

import pytest
from erp_testing.models.postgres.exceptions import SEPostgresBinariesNotFoundError
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from erp_testing.postgres.postgres_binaries import PostgresBinaries


class TestPostgresSessionFixture:
    def test_the_server_is_started_once_for_a_whole_session(self, pytester: pytest.Pytester) -> None:
        try:
            PostgresBinaries(PostgresServerConfig()).find()
        except SEPostgresBinariesNotFoundError:
            pytest.skip("The PostgreSQL binaries are not installed.")
        seen = pytester.path / "seen.txt"
        pytester.makeconftest(
            "from erp_testing.plugin.testing_plugin import TestingPlugin\n"
            "\n"
            "\n"
            "def pytest_configure(config):\n"
            "    config.pluginmanager.register(TestingPlugin(), 'erp-testing')\n"
        )
        pytester.makepyfile(
            test_inner=(
                "def test_first(postgres_server):\n"
                f"    with open({str(seen)!r}, 'a', encoding='utf-8') as out:\n"
                "        out.write(f'{postgres_server.connection.port} {postgres_server.data_dir}\\n')\n"
                "\n"
                "\n"
                "def test_second(postgres_server):\n"
                f"    with open({str(seen)!r}, 'a', encoding='utf-8') as out:\n"
                "        out.write(f'{postgres_server.connection.port} {postgres_server.data_dir}\\n')\n"
            )
        )

        result = pytester.runpytest_subprocess("-p", "no:cacheprovider")

        result.assert_outcomes(passed=2)
        lines = seen.read_text(encoding="utf-8").splitlines()
        assert len(lines) == 2
        assert len(set(lines)) == 1
