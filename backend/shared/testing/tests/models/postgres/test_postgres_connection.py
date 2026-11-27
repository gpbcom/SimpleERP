from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_testing.models.postgres.exceptions import (
    SEPostgresConnectionInvalidDatabase,
    SEPostgresConnectionInvalidHost,
    SEPostgresConnectionInvalidPort,
    SEPostgresConnectionInvalidUser,
)
from erp_testing.models.postgres.postgres_connection import PostgresConnection
from pydantic import JsonValue, ValidationError


class TestPostgresConnection:
    VALID: Dict[str, JsonValue] = {"host": "127.0.0.1", "port": 5433, "database": "erp_test", "user": "erp_test"}

    def test_the_bounds_of_the_port(self) -> None:
        assert PostgresConnection.PORT_MIN == 1
        assert PostgresConnection.PORT_MAX == 65535

    def test_full_valid_construction(self) -> None:
        connection = PostgresConnection.model_validate(self.VALID)
        assert connection.host == "127.0.0.1"
        assert connection.port == 5433
        assert connection.database == "erp_test"
        assert connection.user == "erp_test"

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("host", SEPostgresConnectionInvalidHost),
            ("port", SEPostgresConnectionInvalidPort),
            ("database", SEPostgresConnectionInvalidDatabase),
            ("user", SEPostgresConnectionInvalidUser),
        ],
    )
    def test_none_is_refused_because_no_field_has_a_default(self, name: str, error: Type[Exception]) -> None:
        data = {**self.VALID, name: None}
        with pytest.raises(error):
            PostgresConnection.model_validate(data)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("host", 5, SEPostgresConnectionInvalidHost),
            ("host", "", SEPostgresConnectionInvalidHost),
            ("host", "  ", SEPostgresConnectionInvalidHost),
            ("port", "5432", SEPostgresConnectionInvalidPort),
            ("port", True, SEPostgresConnectionInvalidPort),
            ("port", 0, SEPostgresConnectionInvalidPort),
            ("port", 65536, SEPostgresConnectionInvalidPort),
            ("database", 5, SEPostgresConnectionInvalidDatabase),
            ("database", "", SEPostgresConnectionInvalidDatabase),
            ("user", 5, SEPostgresConnectionInvalidUser),
            ("user", "  ", SEPostgresConnectionInvalidUser),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: Type[Exception]) -> None:
        data = {**self.VALID, name: value}
        with pytest.raises(error):
            PostgresConnection.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PostgresConnection.model_validate({**self.VALID, "unknown": 1})

    def test_round_trip(self) -> None:
        connection = PostgresConnection.model_validate(self.VALID)
        assert PostgresConnection.model_validate(connection.model_dump()) == connection
        assert PostgresConnection.model_validate_json(connection.model_dump_json()) == connection

    def test_the_dsn_has_no_password(self) -> None:
        connection = PostgresConnection.model_validate(self.VALID)
        assert connection.dsn == "postgresql://erp_test@127.0.0.1:5433/erp_test"

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        connection = PostgresConnection.model_validate(self.VALID)
        with pytest.raises(ValidationError):
            connection.port = 1
