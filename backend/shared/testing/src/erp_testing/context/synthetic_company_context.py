from __future__ import annotations

# Standard library imports
from contextvars import Token
from logging import Logger, getLogger
from types import TracebackType
from typing import List, Optional, Type

# Third-party imports
from erp_context.models.context.request_context import RequestContext
from erp_context.models.context.user_context import UserContext
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore

# First-party imports
from erp_testing.models.synthetic import SyntheticCompany, SyntheticUser


class SyntheticCompanyContext:
    """Make a synthetic company and user the current request context for the length of a ``with`` block.

    Attributes:
        company (SyntheticCompany): The company the context acts in.
        user (SyntheticUser): The user the context acts for.
        service (CompanyContextService): T0.09's service, which binds and releases the context.
        tokens (List[Token[Optional[RequestContext]]]): The tokens that restore the contexts bound by ``__enter__``.
        logger (Logger): Logger instance.

    Notes:
        - It uses T0.09's public API only, so a test sees the context exactly as a request would.
        - **Each ``__enter__`` keeps its token on a stack**, so nested uses, even of one instance, restore the outer
          context in order.
        - Logs hold ids only, never the name or the e-mail address of the user.
    """

    def __init__(self, company: SyntheticCompany, user: SyntheticUser, logger: Optional[Logger] = None) -> None:
        """Keep the company and the user.

        Args:
            company (SyntheticCompany): The company the context acts in.
            user (SyntheticUser): The user the context acts for.
            logger (Optional[Logger]): Logger instance.
        """
        self.company = company
        self.user = user
        self.logger = logger if logger else getLogger(__name__)
        self.service = CompanyContextService(RequestContextStore(), self.logger)
        self.tokens: List[Token[Optional[RequestContext]]] = []

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def context(self) -> RequestContext:
        """Build T0.09's context for the company id and the user id.

        Returns:
            RequestContext: The context of the synthetic user in the synthetic company.
        """
        self.logger.debug("Building the context of company %s.", self.company.id.value)
        return RequestContext(
            user=UserContext(user_id=self.user.id.value, company_id=self.company.id),
            request_id=f"synthetic-{self.company.id.value}",
        )

    def __enter__(self) -> SyntheticCompanyContext:
        """Bind the context, keeping the token that restores the previous one.

        Returns:
            SyntheticCompanyContext: This object.
        """
        self.tokens.append(self.service.bind(self.context))
        self.logger.debug("Entered the context of user %s.", self.user.id.value)
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Restore the previous context, whatever happened in the block.

        Args:
            exc_type (Optional[Type[BaseException]]): The exception type raised in the block, if any.
            exc_value (Optional[BaseException]): The exception raised in the block, if any.
            traceback (Optional[TracebackType]): Its traceback, if any.
        """
        self.service.release(self.tokens.pop())
        self.logger.debug("Left the context of user %s.", self.user.id.value)
