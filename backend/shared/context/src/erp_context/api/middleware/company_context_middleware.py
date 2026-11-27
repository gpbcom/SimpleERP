from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, Optional
from uuid import uuid4

# Third-party imports
from erp_models.ids.company_id import CompanyId
from erp_models.ids.exceptions import SECompanyIdInvalidValue
from starlette.types import ASGIApp, Message, Receive, Scope, Send

# First-party imports
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.api.problems.problem_response import ProblemResponse
from erp_context.models.context.context_config import ContextConfig
from erp_context.models.context.request_context import RequestContext
from erp_context.models.context.user_context import UserContext
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import SEAccessError, SEAccessNoCompanyError, SEAccessNoUserError
from erp_context.service.context.company_context_service import CompanyContextService


class CompanyContextMiddleware:
    """Refuse every request that names no company, and bind the context of the others.

    Attributes:
        WEBSOCKET_POLICY_VIOLATION (int): The close code sent to a refused websocket.
        app (ASGIApp): The application behind the middleware.
        config (ContextConfig): The header names and the public paths.
        context (CompanyContextService): Binds the context for the running request.
        builder (ProblemBuilder): Builds the problem+json body of a refusal.
        logger (Logger): Logger instance.

    Notes:
        - **It is a pure ASGI class, not a ``BaseHTTPMiddleware``,** so that the ContextVar is bound in the task that
          runs the route.
        - **Logs hold the code, the reason, the method, the path and the user id, and never another header value.**
          An invalid company is logged as invalid, never quoted.
    """

    WEBSOCKET_POLICY_VIOLATION: ClassVar[int] = 1008

    def __init__(
        self,
        app: ASGIApp,
        config: ContextConfig,
        context: CompanyContextService,
        builder: ProblemBuilder,
        logger: Optional[Logger] = None,
    ) -> None:
        """Keep what the middleware needs.

        Args:
            app (ASGIApp): The application behind the middleware.
            config (ContextConfig): The header names and the public paths.
            context (CompanyContextService): Binds the context for the running request.
            builder (ProblemBuilder): Builds the problem+json body of a refusal.
            logger (Optional[Logger]): Logger instance.
        """
        self.app = app
        self.config = config
        self.context = context
        self.builder = builder
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _headers(self, scope: Scope) -> Dict[str, str]:
        """Read the request headers by lower-case name.

        Args:
            scope (Scope): The ASGI scope.

        Returns:
            Dict[str, str]: The headers, the last value winning.
        """
        return {name.decode("latin-1").lower(): value.decode("latin-1") for name, value in scope.get("headers", [])}

    def _read(self, headers: Dict[str, str], name: str) -> Optional[str]:
        """Read one header, stripped, or ``None`` when absent or empty.

        Args:
            headers (Dict[str, str]): The headers by lower-case name.
            name (str): The header name.

        Returns:
            Optional[str]: The stripped value, or ``None``.
        """
        value = headers.get(name.lower())
        if value is None or not value.strip():
            return None
        return value.strip()

    def _company(self, raw: Optional[str]) -> CompanyId:
        """Build the company id of the request.

        Args:
            raw (Optional[str]): The company header value.

        Returns:
            CompanyId: The company id.

        Raises:
            SEAccessNoCompanyError: When the company is missing or refused by the company id type.
        """
        if raw is None:
            self.logger.debug("The request carries no company header.")
            raise SEAccessNoCompanyError(RefusalReason.NO_COMPANY, "The request names no company.")
        try:
            return CompanyId(value=raw)
        except SECompanyIdInvalidValue as error:
            self.logger.debug("The company header was invalid.")
            raise SEAccessNoCompanyError(RefusalReason.NO_COMPANY, "The company of the request is invalid.") from error

    async def _refuse(
        self,
        scope: Scope,
        receive: Receive,
        send: Send,
        error: SEAccessError,
        request_id: str,
        user_id: Optional[str],
    ) -> None:
        """Log a refusal and answer it in problem+json.

        Args:
            scope (Scope): The ASGI scope.
            receive (Receive): The ASGI receive channel.
            send (Send): The ASGI send channel.
            error (SEAccessError): The refusal.
            request_id (str): The request identifier, used as the instance.
            user_id (Optional[str]): The user id, when known.
        """
        problem = self.builder.build(error, request_id)
        self.logger.warning(
            "Refused %s %s with %s (%s), user %s.",
            scope.get("method", "-"),
            scope.get("path", "-"),
            problem.code,
            error.reason.value,
            user_id if user_id else "unknown",
        )
        await ProblemResponse.of(problem)(scope, receive, send)

    ############################
    # Publicly Exposed Methods #
    ############################

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        """Serve one ASGI call.

        Args:
            scope (Scope): The ASGI scope.
            receive (Receive): The ASGI receive channel.
            send (Send): The ASGI send channel.
        """
        scope_type = scope["type"]
        if scope_type == "lifespan":
            await self.app(scope, receive, send)
            return
        if scope_type != "http":
            self.logger.warning("Refused a %s connection: only http is served.", scope_type)
            if scope_type == "websocket":
                message: Message = {"type": "websocket.close", "code": self.WEBSOCKET_POLICY_VIOLATION}
                await send(message)
            return
        if scope.get("path", "") in self.config.public_paths:
            self.logger.debug("Public path %s passes without a company.", scope.get("path"))
            await self.app(scope, receive, send)
            return
        headers = self._headers(scope)
        request_id = self._read(headers, self.config.request_header) or uuid4().hex
        user_id = self._read(headers, self.config.user_header)
        try:
            company_id = self._company(self._read(headers, self.config.company_header))
            if user_id is None:
                self.logger.debug("The request carries no user header.")
                raise SEAccessNoUserError(RefusalReason.NO_USER, "The request has no user.")
        except SEAccessError as error:
            await self._refuse(scope, receive, send, error, request_id, user_id)
            return
        request_context = RequestContext(
            user=UserContext(user_id=user_id, company_id=company_id), request_id=request_id
        )
        token = self.context.bind(request_context)
        try:
            await self.app(scope, receive, send)
        finally:
            self.context.release(token)
