from __future__ import annotations

# Standard library imports
from contextvars import Token
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from erp_context.models.context.request_context import RequestContext
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessNoCompanyError
from erp_context.storage.context.request_context_store import RequestContextStore


class CompanyContextService:
    """Bind the company and the user of a request, and read them back.

    Attributes:
        store (RequestContextStore): Where the context of the running request is held.
        logger (Logger): Logger instance.

    Notes:
        - The api layer binds the context, and the service layer reads it with ``current``.
        - **Logs hold the company id and the request id only, never the user's token.**
        - ``peek`` is a one-line predicate, so it stays silent.
    """

    def __init__(self, store: RequestContextStore, logger: Optional[Logger] = None) -> None:
        """Keep the store.

        Args:
            store (RequestContextStore): Where the context is held.
            logger (Optional[Logger]): Logger instance.
        """
        self.store = store
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def bind(self, context: RequestContext) -> Token[Optional[RequestContext]]:
        """Bind a context to the running request.

        Args:
            context (RequestContext): The context to bind.

        Returns:
            Token[Optional[RequestContext]]: The token that ``release`` needs.
        """
        self.logger.debug(
            "Binding the context of company %s for request %s.",
            context.user.company_id.value,
            context.request_id,
        )
        return self.store.set(context)

    def release(self, token: Token[Optional[RequestContext]]) -> None:
        """Restore what was bound before ``bind``.

        Args:
            token (Token[Optional[RequestContext]]): The token returned by ``bind``.
        """
        self.logger.debug("Releasing the bound context.")
        self.store.reset(token)

    def peek(self) -> Optional[RequestContext]:
        """Read the bound context, if any.

        Returns:
            Optional[RequestContext]: The bound context, or ``None`` when nothing is bound.
        """
        return self.store.get()

    def current(self) -> RequestContext:
        """Read the bound context, which must exist.

        Returns:
            RequestContext: The bound context.

        Raises:
            SEAccessNoCompanyError: When nothing is bound.
        """
        context = self.store.get()
        if context is None:
            self.logger.error("No company context is bound to the running request.")
            raise SEAccessNoCompanyError(RefusalReason.NO_COMPANY, "No company context is bound to the request.")
        return context
