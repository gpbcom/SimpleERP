from __future__ import annotations

from enum import StrEnum

from erp_platform.models.health.enums import HealthState


class TestHealthState:
    def test_it_is_a_string_enum(self) -> None:
        assert issubclass(HealthState, StrEnum)

    def test_ok_is_the_string_ok(self) -> None:
        assert HealthState.OK == "ok"
        assert HealthState.OK.value == "ok"

    def test_its_members_are_unique(self) -> None:
        values = [member.value for member in HealthState]
        assert len(values) == len(set(values))
        assert HealthState("ok") is HealthState.OK
