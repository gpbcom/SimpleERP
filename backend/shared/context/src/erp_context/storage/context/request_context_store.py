from __future__ import annotations

# Standard library imports
from contextvars import ContextVar, Token
from typing import ClassVar, Optional

# First-party imports
from erp_context.models.context.request_context import RequestContext


class RequestContextStore:
    """Carries the context of the current request down to the storage layer.

    Attributes:
        CURRENT (ContextVar[Optional[RequestContext]]): The context bound to the running request, or ``None``.

    Notes:
        - A ``ContextVar`` keeps concurrent requests apart: each asyncio task works on a copy of the context
          of the task that created it, so a value bound in one request is never seen by another.
        - **A value bound in a task does not leak back to its caller.**
        - It is a one-line holder, so it stays silent: the service layer logs.
    """

    CURRENT: ClassVar[ContextVar[Optional[RequestContext]]] = ContextVar("erp_request_context", default=None)

    ############################
    # Publicly Exposed Methods #
    ############################

    def set(self, context: RequestContext) -> Token[Optional[RequestContext]]:
        """Bind a context to the running request.

        Args:
            context (RequestContext): The context to bind.

        Returns:
            Token[Optional[RequestContext]]: The token that restores the previous value.
        """
        return self.CURRENT.set(context)

    def get(self) -> Optional[RequestContext]:
        """Read the context bound to the running request.

        Returns:
            Optional[RequestContext]: The bound context, or ``None`` when nothing is bound.
        """
        return self.CURRENT.get()

    def reset(self, token: Token[Optional[RequestContext]]) -> None:
        """Restore what was bound before a ``set``.

        Args:
            token (Token[Optional[RequestContext]]): The token returned by ``set``.
        """
        self.CURRENT.reset(token)
