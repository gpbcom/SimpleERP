from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Optional

# Third-party imports
import erp_context
from erp_context.api.middleware.company_context_middleware import CompanyContextMiddleware
from erp_context.api.problems.problem_builder import ProblemBuilder
from erp_context.models.context.context_config import ContextConfig
from erp_context.models.refusals.refusal_catalog import RefusalCatalog
from erp_context.service.context.company_context_service import CompanyContextService
from erp_context.storage.context.request_context_store import RequestContextStore
from fastapi import FastAPI

# First-party imports
from erp_platform.api.http.health_router import HealthRouter
from erp_platform.api.http.problem_handler import ProblemHandler
from erp_platform.models.config.platform_config import PlatformConfig
from erp_platform.service.health.health_service import HealthService
from erp_platform.service.problems.problem_service import ProblemService


class AppBuilder:
    """Build the FastAPI application of the platform service.

    Attributes:
        API_PREFIX (str): The prefix of every route.
        REFUSAL_CODES_FILE (str): The file name of the refusal catalogue of ``erp_context``.
        config (PlatformConfig): The platform configuration.
        logger (Logger): Logger instance.

    Notes:
        - **A request without a company is refused by the ``erp_context`` middleware**, with its own problem+json
          code. The paths of ``config.public_paths`` are left out through the middleware's own ``public_paths``.
        - The refusal catalogue is read beside the error catalogue when it is there, else from the folder of the
          ``erp_context`` library in the source tree.
    """

    API_PREFIX: ClassVar[str] = "/v1"
    REFUSAL_CODES_FILE: ClassVar[str] = "refusal_codes.yaml"

    def __init__(self, config: PlatformConfig, logger: Optional[Logger] = None) -> None:
        """Keep the configuration.

        Args:
            config (PlatformConfig): The platform configuration.
            logger (Optional[Logger]): Logger instance.
        """
        self.config = config
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _refusal_codes_path(self) -> Path:
        """Find the refusal catalogue file.

        Returns:
            Path: The file beside the error catalogue, else the one shipped with ``erp_context``.
        """
        beside = Path(self.config.error_codes_path).parent / self.REFUSAL_CODES_FILE
        if beside.is_file():
            self.logger.debug("Refusal catalogue found beside the error catalogue.")
            return beside
        self.logger.debug("Refusal catalogue taken from the erp_context library.")
        return Path(erp_context.__file__).resolve().parents[2] / "conf" / "catalogs" / self.REFUSAL_CODES_FILE

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self) -> FastAPI:
        """Build the application.

        Returns:
            FastAPI: The application with ``/v1/health``, the problem+json handlers and the company middleware.
        """
        app = FastAPI()
        health_router = HealthRouter(HealthService(self.logger), self.logger)
        app.include_router(health_router.router, prefix=self.API_PREFIX)
        problem_service = ProblemService(Path(self.config.error_codes_path), self.logger)
        ProblemHandler(problem_service, self.logger).register(app)
        catalog = RefusalCatalog.load(self._refusal_codes_path())
        app.add_middleware(
            CompanyContextMiddleware,
            config=ContextConfig(public_paths=self.config.public_paths),
            context=CompanyContextService(RequestContextStore(), self.logger),
            builder=ProblemBuilder(catalog, self.logger),
            logger=self.logger,
        )
        self.logger.info("Built the platform application with %d public paths.", len(self.config.public_paths))
        return app
