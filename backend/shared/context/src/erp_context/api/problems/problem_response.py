from __future__ import annotations

# Third-party imports
from starlette.responses import JSONResponse

# First-party imports
from erp_context.models.refusals.problem import Problem


class ProblemResponse(JSONResponse):
    """The HTTP response of a refused request, in problem+json.

    Attributes:
        media_type (str): The problem+json media type.
    """

    media_type = "application/problem+json"

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def of(cls, problem: Problem) -> ProblemResponse:
        """Build the response of one problem.

        Args:
            problem (Problem): The problem to send.

        Returns:
            ProblemResponse: The response, with the status of the problem.
        """
        return cls(status_code=problem.status, content=problem.model_dump(exclude_none=True))
