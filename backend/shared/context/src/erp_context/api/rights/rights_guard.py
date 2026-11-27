from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from erp_context.models.context.record_ref import RecordRef
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.service.rights.rights_service import RightsService


class RightsGuard:
    """Check the rights of the current user from an HTTP route.

    Attributes:
        rights (RightsService): The one place a decision is made.
        context (CompanyContextService): Where the current user is read.
        logger (Logger): Logger instance.

    Notes:
        **The guard holds no rule of its own.** It hands the user, the action and the record to
        ``RightsService.enforce``, so that HTTP and a direct call give the same decision.
    """

    def __init__(self, rights: RightsService, context: CompanyContextService, logger: Optional[Logger] = None) -> None:
        """Keep the services.

        Args:
            rights (RightsService): The one place a decision is made.
            context (CompanyContextService): Where the current user is read.
            logger (Optional[Logger]): Logger instance.
        """
        self.rights = rights
        self.context = context
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def check(self, action: str, record: RecordRef) -> None:
        """Check that the current user may do one action on one record.

        Args:
            action (str): The action asked for.
            record (RecordRef): The record concerned.

        Raises:
            SEAccessError: When the action is refused, or when no company context is bound.
        """
        user = self.context.current().user
        self.logger.debug("Checking the action %s of the current user.", action)
        self.rights.enforce(user, action, record)
