from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import Optional

# First-party imports
from erp_models.errors.catalogs.exceptions import SEErrorCatalogUnknownCode

from erp_platform.models.problems.problem_details import ProblemDetails
from erp_platform.service.problems.exceptions import SEProblemUnknownCodeError
from erp_platform.storage.catalogs.error_code_repository import ErrorCodeRepository


class ProblemService:
    """Build the problem+json body of an error from its code.

    Attributes:
        catalog (ErrorCatalog): The error code catalogue, loaded once at construction.
        logger (Logger): Logger instance.

    Notes:
        - **The service takes no free text**, so no exception message or secret can reach a body (REQ-T05-03).
        - The title and the detail are the translation keys of the code's entry.
    """

    def __init__(self, error_codes_path: Path, logger: Optional[Logger] = None) -> None:
        """Initialise the service and load the catalogue.

        Args:
            error_codes_path (Path): The error code catalogue file.
            logger (Optional[Logger]): Logger instance.
        """
        self.logger = logger if logger else getLogger(__name__)
        self.catalog = ErrorCodeRepository(error_codes_path, self.logger).load()

    ############################
    # Publicly Exposed Methods #
    ############################

    def problem(self, code: str, status: int) -> ProblemDetails:
        """Build the problem body of one code.

        Args:
            code (str): The support reference of the error.
            status (int): The HTTP status of the answer.

        Returns:
            ProblemDetails: The body, made of the code's keys, the code and the status.

        Raises:
            SEProblemUnknownCodeError: When the code is not in the catalogue.
        """
        self.logger.debug("Building the problem of %s with status %d.", code, status)
        try:
            entry = self.catalog.resolve(code)
        except SEErrorCatalogUnknownCode as error:
            self.logger.error("Cannot build a problem: unknown error code %s.", code)
            raise SEProblemUnknownCodeError(
                f"Unknown error code: {code!r}. "  # noqa: E501
                "Must be a code of the error catalogue."
            ) from error
        return ProblemDetails(title=entry.title, status=status, detail=entry.why, code=code)
