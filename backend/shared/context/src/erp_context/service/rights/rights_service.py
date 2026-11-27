from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# First-party imports
from erp_context.models.context.record_ref import RecordRef
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessDeniedError
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.models.rights.enums import PolicyEffect
from erp_context.models.rights.rights_decision import RightsDecision
from erp_context.service.rights.policy import Policy


class RightsService:
    """Decide whether a user may do an action on a record.

    Attributes:
        policies (List[Policy]): The policies the service gives, evaluated for every decision.
        catalog (RefusalCatalog): The refusal codes, to name each refusal in the log.
        logger (Logger): Logger instance.

    Notes:
        - **Deny wins**: a single ``DENY`` vote refuses the action whatever the others say, so that adding a policy
          can restrict a right but never silently widen one.
        - **The default is a refusal**: when no policy allows the action, it is refused as ``NO_POLICY``. A missing
          rule must never grant access.
        - A record of another company is refused before any policy is asked.
        - Logs hold ids only, never the content of a record.
    """

    def __init__(self, policies: List[Policy], catalog: RefusalCatalog, logger: Optional[Logger] = None) -> None:
        """Keep the policies and the catalogue.

        Args:
            policies (List[Policy]): The policies to evaluate.
            catalog (RefusalCatalog): The refusal codes.
            logger (Optional[Logger]): Logger instance.
        """
        self.policies = policies
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _refuse(self, reason: RefusalReason, user: UserContext, action: str, record: RecordRef) -> RightsDecision:
        """Log one refusal and build its decision.

        Args:
            reason (RefusalReason): Why the action is refused.
            user (UserContext): Who acts.
            action (str): What the user wants to do.
            record (RecordRef): The record concerned.

        Returns:
            RightsDecision: The refused decision.
        """
        self.logger.warning(
            "Access refused with code %s, reason %s, user %s, company %s, action %s, record %s %s of company %s.",
            self.catalog.code_for(reason).code,
            reason,
            user.user_id,
            user.company_id.value,
            action,
            record.record_type,
            record.record_id,
            record.company_id.value,
        )
        return RightsDecision(allowed=False, reason=reason)

    ############################
    # Publicly Exposed Methods #
    ############################

    def decide(self, user: UserContext, action: str, record: RecordRef) -> RightsDecision:
        """Decide one request and log every refusal.

        Args:
            user (UserContext): Who acts.
            action (str): What the user wants to do.
            record (RecordRef): The record concerned.

        Returns:
            RightsDecision: The decision, with its reason when refused.
        """
        if record.company_id != user.company_id:
            return self._refuse(RefusalReason.OTHER_COMPANY, user, action, record)
        denied = False
        granted = False
        for policy in self.policies:
            match policy.vote(user, action, record):
                case PolicyEffect.DENY:
                    denied = True
                case PolicyEffect.ALLOW:
                    granted = True
                case PolicyEffect.ABSTAIN:
                    pass
        if denied:
            return self._refuse(RefusalReason.POLICY_DENIED, user, action, record)
        if granted:
            self.logger.debug(
                "Access allowed for user %s, action %s, record %s %s.",
                user.user_id,
                action,
                record.record_type,
                record.record_id,
            )
            return RightsDecision(allowed=True)
        return self._refuse(RefusalReason.NO_POLICY, user, action, record)

    def allowed(self, user: UserContext, action: str, record: RecordRef) -> bool:
        """Tell whether one request is permitted.

        Args:
            user (UserContext): Who acts.
            action (str): What the user wants to do.
            record (RecordRef): The record concerned.

        Returns:
            bool: ``True`` when permitted.
        """
        return self.decide(user, action, record).allowed

    def enforce(self, user: UserContext, action: str, record: RecordRef) -> None:
        """Raise when one request is refused.

        Args:
            user (UserContext): Who acts.
            action (str): What the user wants to do.
            record (RecordRef): The record concerned.

        Raises:
            SEAccessDeniedError: When the request is refused.
        """
        decision = self.decide(user, action, record)
        if decision.allowed or decision.reason is None:
            return
        message = f"Access denied: {decision.reason}."
        self.logger.error("Raising access denied for reason %s, user %s.", decision.reason, user.user_id)
        raise SEAccessDeniedError(decision.reason, message)
