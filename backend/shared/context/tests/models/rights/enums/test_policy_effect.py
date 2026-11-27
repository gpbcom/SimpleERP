from __future__ import annotations

from typing import List

import pytest
from erp_context.models.rights.enums import PolicyEffect


class TestPolicyEffect:
    def test_the_members_are_allow_deny_and_abstain(self) -> None:
        assert [member.name for member in PolicyEffect] == ["ALLOW", "DENY", "ABSTAIN"]

    def test_the_values_are_unique(self) -> None:
        values: List[str] = [member.value for member in PolicyEffect]
        assert len(values) == len(set(values))

    @pytest.mark.parametrize(
        ("member", "value"),
        [(PolicyEffect.ALLOW, "allow"), (PolicyEffect.DENY, "deny"), (PolicyEffect.ABSTAIN, "abstain")],
    )
    def test_each_value_round_trips(self, member: PolicyEffect, value: str) -> None:
        assert member.value == value
        assert PolicyEffect(value) is member

    def test_an_unknown_value_is_refused(self) -> None:
        with pytest.raises(ValueError, match="maybe"):
            PolicyEffect("maybe")
