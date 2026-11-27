from __future__ import annotations

from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.rights.enums import PolicyEffect
from erp_context.service.rights.policy import Policy


class AllowActionPolicy(Policy):
    """A policy that allows one action and abstains on every other."""

    def __init__(self, action: str) -> None:
        self.action = action

    def vote(self, user: UserContext, action: str, record: RecordRef) -> PolicyEffect:
        return PolicyEffect.ALLOW if action == self.action else PolicyEffect.ABSTAIN
