from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# Third-party imports
from starlette.requests import Request

# First-party imports
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.api.problems.problem_response import ProblemResponse
from erp_context.models.refusals.exceptions import SEAccessError
from erp_context.service.context.company_context_service import CompanyContextService


class RefusalHandler:
    """Answer a refused request in problem+json.

    Attributes:
        builder (ProblemBuilder): Builds the problem of a refusal.
        context (CompanyContextService): Where the request identifier is read.
        logger (Logger): Logger instance.

    Notes:
        Register it with ``app.add_exception_handler(SEAccessError, handler)``. The refusal itself was already logged
        by ``RightsService``.
    """

    def __init__(
        self, builder: ProblemBuilder, context: CompanyContextService, logger: Optional[Logger] = None
    ) -> None:
        """Keep the builder and the context service.

        Args:
            builder (ProblemBuilder): Builds the problem of a refusal.
            context (CompanyContextService): Where the request identifier is read.
            logger (Optional[Logger]): Logger instance.
        """
        self.builder = builder
        self.context = context
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    async def __call__(self, request: Request, error: SEAccessError) -> ProblemResponse:
        """Answer one refusal.

        Args:
            request (Request): The refused request, never read.
            error (SEAccessError): The refusal.

        Returns:
            ProblemResponse: The problem+json response, with the status of the catalogue entry.
        """
        current = self.context.peek()
        problem = self.builder.build(error, current.request_id if current else None)
        self.logger.info("Answered a refused request with the code %s.", problem.code)
        return ProblemResponse.of(problem)
