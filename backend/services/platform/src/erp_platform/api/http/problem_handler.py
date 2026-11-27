from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, Optional

# Third-party imports
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHttpException
from starlette.requests import Request
from starlette.responses import JSONResponse

# First-party imports
from erp_platform.service.problems.problem_service import ProblemService


class ProblemHandler:
    """Answer every failure of the platform API in problem+json.

    Attributes:
        MEDIA_TYPE (str): The media type of every answer.
        ROUTE_CODE (str): The code of an unknown path.
        METHOD_CODE (str): The code of a method the path does not allow.
        REQUEST_CODE (str): The code of an invalid request.
        INTERNAL_CODE (str): The code of any other failure.
        HTTP_CODES (Dict[int, str]): The code of each HTTP status that has its own.
        problem_service (ProblemService): Builds the body of an answer from its code.
        logger (Logger): Logger instance.

    Notes:
        - **No message of an exception reaches a body or a log**: the broad handler logs ``type(error).__name__``
          only, because a message may quote a secret (REQ-T05-03).
        - The refusals of ``erp_context`` keep their own handler, registered by the application factory.
    """

    MEDIA_TYPE: ClassVar[str] = "application/problem+json"
    ROUTE_CODE: ClassVar[str] = "PLATFORM-ROUTE-01"
    METHOD_CODE: ClassVar[str] = "PLATFORM-METHOD-01"
    REQUEST_CODE: ClassVar[str] = "PLATFORM-REQUEST-01"
    INTERNAL_CODE: ClassVar[str] = "PLATFORM-INTERNAL-01"
    HTTP_CODES: ClassVar[Dict[int, str]] = {404: ROUTE_CODE, 405: METHOD_CODE}

    def __init__(self, problem_service: ProblemService, logger: Optional[Logger] = None) -> None:
        """Keep the problem service.

        Args:
            problem_service (ProblemService): Builds the body of an answer from its code.
            logger (Optional[Logger]): Logger instance.
        """
        self.problem_service = problem_service
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _respond(self, code: str, status: int) -> JSONResponse:
        """Build the problem+json answer of one code.

        Args:
            code (str): The support reference of the error.
            status (int): The HTTP status of the answer.

        Returns:
            JSONResponse: The answer, with the problem media type.
        """
        problem = self.problem_service.problem(code, status)
        return JSONResponse(
            status_code=status,
            content=problem.model_dump(mode="json"),
            media_type=self.MEDIA_TYPE,
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def register(self, app: FastAPI) -> None:
        """Add the three handlers to the application.

        Args:
            app (FastAPI): The application to cover.
        """
        app.add_exception_handler(StarletteHttpException, self.handle_http)
        app.add_exception_handler(RequestValidationError, self.handle_validation)
        app.add_exception_handler(Exception, self.handle_unexpected)
        self.logger.debug("Registered the problem+json handlers.")

    async def handle_http(self, request: Request, error: Exception) -> JSONResponse:
        """Answer an HTTP error such as an unknown path or a wrong method.

        Args:
            request (Request): The failed request, never read.
            error (Exception): The HTTP exception.

        Returns:
            JSONResponse: The problem of the status, or the internal code for a status without its own.
        """
        status = error.status_code if isinstance(error, StarletteHttpException) else 500
        code = self.HTTP_CODES.get(status, self.INTERNAL_CODE)
        self.logger.info("Answered an HTTP %d with the code %s.", status, code)
        return self._respond(code, status if 400 <= status <= 599 else 500)

    async def handle_validation(self, request: Request, error: Exception) -> JSONResponse:
        """Answer an invalid request.

        Args:
            request (Request): The failed request, never read.
            error (Exception): The validation error, never quoted.

        Returns:
            JSONResponse: The 422 problem.
        """
        self.logger.info("Answered an invalid request with the code %s.", self.REQUEST_CODE)
        return self._respond(self.REQUEST_CODE, 422)

    async def handle_unexpected(self, request: Request, error: Exception) -> JSONResponse:
        """Answer any other failure.

        Args:
            request (Request): The failed request, never read.
            error (Exception): The failure, of which only the type is logged.

        Returns:
            JSONResponse: The 500 problem.
        """
        self.logger.error("Unexpected failure of type %s.", type(error).__name__)
        return self._respond(self.INTERNAL_CODE, 500)
