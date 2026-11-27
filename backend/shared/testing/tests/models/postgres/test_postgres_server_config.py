from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_testing.models.postgres.exceptions import (
    SEPostgresServerConfigInvalidDatabase,
    SEPostgresServerConfigInvalidSearchDirs,
    SEPostgresServerConfigInvalidStartTimeoutS,
    SEPostgresServerConfigInvalidUser,
)
from erp_testing.models.postgres.postgres_server_config import PostgresServerConfig
from pydantic import JsonValue, ValidationError


class TestPostgresServerConfig:
    def test_defaults(self) -> None:
        config = PostgresServerConfig()
        assert config.search_dirs == ["/usr/lib/postgresql"]
        assert config.database == "erp_test"
        assert config.user == "erp_test"
        assert config.start_timeout_s == 30.0

    def test_the_bounds_of_the_start_timeout(self) -> None:
        assert PostgresServerConfig.START_TIMEOUT_S_MIN == 0.1
        assert PostgresServerConfig.START_TIMEOUT_S_MAX == 300.0

    def test_full_valid_construction(self) -> None:
        config = PostgresServerConfig(search_dirs=["/opt/pg", "/usr/bin"], database="db", user="me", start_timeout_s=5)
        assert config.search_dirs == ["/opt/pg", "/usr/bin"]
        assert config.database == "db"
        assert config.user == "me"
        assert config.start_timeout_s == 5.0

    @pytest.mark.parametrize("name", ["search_dirs", "database", "user", "start_timeout_s"])
    def test_none_becomes_the_default(self, name: str) -> None:
        config = PostgresServerConfig.model_validate({name: None})
        assert getattr(config, name) == getattr(PostgresServerConfig(), name)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("search_dirs", "/usr/lib/postgresql", SEPostgresServerConfigInvalidSearchDirs),
            ("search_dirs", [1], SEPostgresServerConfigInvalidSearchDirs),
            ("search_dirs", [""], SEPostgresServerConfigInvalidSearchDirs),
            ("search_dirs", ["  "], SEPostgresServerConfigInvalidSearchDirs),
            ("database", 5, SEPostgresServerConfigInvalidDatabase),
            ("database", "", SEPostgresServerConfigInvalidDatabase),
            ("database", "   ", SEPostgresServerConfigInvalidDatabase),
            ("user", 5, SEPostgresServerConfigInvalidUser),
            ("user", "", SEPostgresServerConfigInvalidUser),
            ("user", "   ", SEPostgresServerConfigInvalidUser),
            ("start_timeout_s", "5", SEPostgresServerConfigInvalidStartTimeoutS),
            ("start_timeout_s", True, SEPostgresServerConfigInvalidStartTimeoutS),
            ("start_timeout_s", 0.05, SEPostgresServerConfigInvalidStartTimeoutS),
            ("start_timeout_s", 300.5, SEPostgresServerConfigInvalidStartTimeoutS),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: Type[Exception]) -> None:
        data: Dict[str, JsonValue] = {name: value}
        with pytest.raises(error):
            PostgresServerConfig.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PostgresServerConfig.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        config = PostgresServerConfig(search_dirs=["/opt/pg"], database="db", user="me", start_timeout_s=2.5)
        assert PostgresServerConfig.model_validate(config.model_dump()) == config
        assert PostgresServerConfig.model_validate_json(config.model_dump_json()) == config
