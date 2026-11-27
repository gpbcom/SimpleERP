from __future__ import annotations

import pytest
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.rights.enums import PolicyEffect
from erp_context.service.rights.policy import Policy

from tests.service.rights.allow_action_policy import AllowActionPolicy


class TestPolicy:
    def test_a_policy_without_vote_cannot_be_instantiated(self) -> None:
        no_vote = type("NoVote", (Policy,), {})

        with pytest.raises(TypeError):
            no_vote()

    def test_a_policy_with_vote_can_be_instantiated(self, user: UserContext, record: RecordRef) -> None:
        assert AllowActionPolicy("write").vote(user, "read", record) is PolicyEffect.ABSTAIN

    def test_the_base_class_cannot_be_instantiated(self) -> None:
        with pytest.raises(TypeError):
            Policy()  # type: ignore[abstract]
