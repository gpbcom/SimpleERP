from __future__ import annotations

from typing import Dict, Optional, Type

import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.rights.exceptions import (
    SERightsDecisionInconsistent,
    SERightsDecisionInvalidAllowed,
    SERightsDecisionInvalidReason,
)
from erp_context.models.rights.rights_decision import RightsDecision
from pydantic import JsonValue, ValidationError


class TestRightsDecision:
    def test_defaults(self) -> None:
        decision = RightsDecision(allowed=True)
        assert decision.allowed is True
        assert decision.reason is None

    def test_full_valid_construction(self) -> None:
        decision = RightsDecision(allowed=False, reason=RefusalReason.POLICY_DENIED)
        assert decision.allowed is False
        assert decision.reason is RefusalReason.POLICY_DENIED

    def test_none_becomes_the_default(self) -> None:
        decision = RightsDecision.model_validate({"allowed": True, "reason": None})
        assert decision.reason is None

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("allowed", "yes", SERightsDecisionInvalidAllowed),
            ("allowed", 1, SERightsDecisionInvalidAllowed),
            ("allowed", None, SERightsDecisionInvalidAllowed),
            ("reason", 42, SERightsDecisionInvalidReason),
            ("reason", True, SERightsDecisionInvalidReason),
            ("reason", "not-a-reason", SERightsDecisionInvalidReason),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: Type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"allowed": False, "reason": RefusalReason.NO_POLICY.value}
        data[name] = value
        with pytest.raises(error):
            RightsDecision.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RightsDecision.model_validate({"allowed": True, "unknown": 1})

    @pytest.mark.parametrize("reason", [None, RefusalReason.NO_POLICY])
    def test_round_trip(self, reason: Optional[RefusalReason]) -> None:
        decision = RightsDecision(allowed=reason is None, reason=reason)
        assert RightsDecision.model_validate(decision.model_dump()) == decision
        assert RightsDecision.model_validate_json(decision.model_dump_json()) == decision

    def test_an_allowed_decision_with_a_reason_is_inconsistent(self) -> None:
        with pytest.raises(SERightsDecisionInconsistent):
            RightsDecision(allowed=True, reason=RefusalReason.POLICY_DENIED)

    def test_a_refused_decision_without_a_reason_is_inconsistent(self) -> None:
        with pytest.raises(SERightsDecisionInconsistent):
            RightsDecision(allowed=False)

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        decision = RightsDecision(allowed=True)
        with pytest.raises(ValidationError):
            decision.allowed = False
