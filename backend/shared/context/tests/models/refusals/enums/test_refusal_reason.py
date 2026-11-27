from __future__ import annotations

from enum import StrEnum
from typing import Dict

import pytest
from erp_context.models.refusals.enums import RefusalReason


class TestRefusalReason:
    VALUES: Dict[str, str] = {
        "NO_COMPANY": "no-company",
        "NO_USER": "no-user",
        "NO_POLICY": "no-policy",
        "POLICY_DENIED": "policy-denied",
        "OTHER_COMPANY": "other-company",
    }

    def test_it_is_a_string_enum(self) -> None:
        assert issubclass(RefusalReason, StrEnum)

    def test_the_members_are_the_five_reasons(self) -> None:
        assert {member.name: member.value for member in RefusalReason} == self.VALUES

    def test_the_values_are_unique(self) -> None:
        values = [member.value for member in RefusalReason]

        assert len(values) == len(set(values))

    @pytest.mark.parametrize(("name", "value"), list(VALUES.items()))
    def test_each_value_round_trips(self, name: str, value: str) -> None:
        assert RefusalReason(value) is RefusalReason[name]
        assert RefusalReason[name].value == value
        assert str(RefusalReason[name]) == value

    def test_an_unknown_value_is_refused(self) -> None:
        with pytest.raises(ValueError, match="not a valid RefusalReason"):
            RefusalReason("unknown")
