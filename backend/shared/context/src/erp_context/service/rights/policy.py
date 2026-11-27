from __future__ import annotations

# Standard library imports
from abc import ABC, abstractmethod

# First-party imports
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.rights.enums import PolicyEffect


class Policy(ABC):
    """One rule a service gives to the rights library.

    Notes:
        The library ships no policy, because it holds no business rule. Each service writes its own and passes
        them to ``RightsService``.
    """

    ############################
    # Publicly Exposed Methods #
    ############################

    @abstractmethod
    def vote(self, user: UserContext, action: str, record: RecordRef) -> PolicyEffect:
        """Give the opinion of the policy on one action.

        Args:
            user (UserContext): Who acts.
            action (str): What the user wants to do.
            record (RecordRef): The record concerned.

        Returns:
            PolicyEffect: ``ALLOW``, ``DENY``, or ``ABSTAIN`` when the policy has no opinion.
        """
