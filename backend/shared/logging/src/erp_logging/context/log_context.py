from __future__ import annotations

# Standard library imports
from contextvars import ContextVar
from typing import ClassVar, Optional


class LogContext:
    """The company and the request that the current context is working for.

    Attributes:
        COMPANY (ContextVar[Optional[str]]): The opaque id of the company, ``None`` when unbound.
        REQUEST (ContextVar[Optional[str]]): The id of the request, ``None`` when unbound.

    Notes:
        - Values live in ``contextvars``, so each asyncio task and each thread context reads its own values.
        - **A value bound in a child task never leaks to its caller.**
        - The company is an opaque id and is stored as given.
        - This class is silent, because it runs for every request.
    """

    COMPANY: ClassVar[ContextVar[Optional[str]]] = ContextVar("erp_logging_company", default=None)
    REQUEST: ClassVar[ContextVar[Optional[str]]] = ContextVar("erp_logging_request", default=None)

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def bind(cls, company: Optional[str], request: Optional[str]) -> None:
        """Bind the company and the request to the current context.

        Args:
            company (Optional[str]): The opaque company id.
            request (Optional[str]): The request id.
        """
        cls.COMPANY.set(company)
        cls.REQUEST.set(request)

    @classmethod
    def clear(cls) -> None:
        """Reset the company and the request of the current context."""
        cls.COMPANY.set(None)
        cls.REQUEST.set(None)

    @classmethod
    def company(cls) -> Optional[str]:
        """Return the company bound to the current context.

        Returns:
            Optional[str]: The company id, or ``None``.
        """
        return cls.COMPANY.get()

    @classmethod
    def request(cls) -> Optional[str]:
        """Return the request bound to the current context.

        Returns:
            Optional[str]: The request id, or ``None``.
        """
        return cls.REQUEST.get()
