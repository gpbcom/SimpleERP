from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import Optional

# First-party imports
from erp_context.models.refusals.exceptions import SEAccessError
from erp_context.models.refusals.problem import Problem
from erp_context.models.refusals.refusal_catalog import RefusalCatalog


class ProblemBuilder:
    """Build the problem+json body of a refused request.

    Attributes:
        catalog (RefusalCatalog): The catalogue of refusal codes.
        logger (Logger): Logger instance.

    Notes:
        **The body is filled from the catalogue only.** The message of the error and every value of the request stay
        out of it, so that no secret reaches the caller.
    """

    def __init__(self, catalog: RefusalCatalog, logger: Optional[Logger] = None) -> None:
        """Keep the catalogue.

        Args:
            catalog (RefusalCatalog): The catalogue of refusal codes.
            logger (Optional[Logger]): Logger instance.
        """
        self.catalog = catalog
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self, error: SEAccessError, request_id: Optional[str]) -> Problem:
        """Build the problem of one refusal.

        Args:
            error (SEAccessError): The refusal.
            request_id (Optional[str]): The identifier of the request, used as the instance.

        Returns:
            Problem: The problem, with the fields of the catalogue entry of the reason.
        """
        entry = self.catalog.code_for(error.reason)
        self.logger.debug("Built the problem %s for a refused request.", entry.code)
        return Problem(
            title=entry.title_key,
            status=entry.status,
            detail=entry.why_key,
            code=entry.code,
            action=entry.action_key,
            reference=entry.reference,
            instance=request_id,
        )
