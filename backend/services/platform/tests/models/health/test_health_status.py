from __future__ import annotations

import json
from typing import Dict

import pytest
from erp_platform.models.health.enums import HealthState
from erp_platform.models.health.exceptions import SEHealthStatusInvalidStatus, SEInvalidHealthStatusException
from erp_platform.models.health.health_status import HealthStatus
from pydantic import JsonValue, ValidationError


class TestHealthStatus:
    def test_defaults(self) -> None:
        assert HealthStatus().status is HealthState.OK

    def test_full_valid_construction(self) -> None:
        assert HealthStatus(status=HealthState.OK).status is HealthState.OK
        assert HealthStatus.model_validate({"status": "ok"}).status is HealthState.OK

    def test_none_becomes_the_default(self) -> None:
        assert HealthStatus.model_validate({"status": None}).status is HealthState.OK

    @pytest.mark.parametrize("value", ["", "   ", "down", "OK", 1, True, ["ok"]])
    def test_rejects_bad_values(self, value: JsonValue) -> None:
        with pytest.raises(SEHealthStatusInvalidStatus):
            HealthStatus.model_validate({"status": value})

    def test_the_field_exception_has_the_model_base(self) -> None:
        assert issubclass(SEHealthStatusInvalidStatus, SEInvalidHealthStatusException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            HealthStatus.model_validate({"unknown": 1})

    def test_it_is_frozen(self) -> None:
        status = HealthStatus()
        with pytest.raises(ValidationError):
            status.status = HealthState.OK

    def test_it_serialises_to_status_ok(self) -> None:
        assert json.loads(HealthStatus().model_dump_json()) == {"status": "ok"}

    def test_round_trip(self) -> None:
        status = HealthStatus()
        data: Dict[str, HealthState] = status.model_dump()
        assert HealthStatus.model_validate(data) == status
        assert HealthStatus.model_validate_json(status.model_dump_json()) == status
