from __future__ import annotations

# Standard library imports
import os
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar

# Third-party imports
from erp_config.loading.app_config_loader import AppConfigLoader
from erp_config.loading.environment_overrides import EnvironmentOverrides
from erp_logging.setup.logging_setup import LoggingSetup
from fastapi import FastAPI

# First-party imports
from erp_platform.api.http.app_builder import AppBuilder
from erp_platform.models.config.platform_config import PlatformConfig


class AppFactory:
    """Build the FastAPI application that uvicorn serves.

    Attributes:
        SERVICE (str): The service tag written in every log record.
        CONFIG_PATH (str): The configuration file, relative to the working folder.
        LOGGER_PATH (str): The logger configuration file, relative to the working folder.
        ENV_PREFIX (str): The prefix of the environment variables that override the configuration.

    Notes:
        - uvicorn calls ``create`` through ``--factory``, so the service has no command line and no module-level
          application.
        - **An invalid configuration raises its own exception before the application exists**, so that uvicorn exits
          non-zero without serving. The loader logs the failure by type only, so no value reaches the logs.
    """

    SERVICE: ClassVar[str] = "platform"
    CONFIG_PATH: ClassVar[str] = "conf/app.yaml"
    LOGGER_PATH: ClassVar[str] = "conf/logger.yaml"
    ENV_PREFIX: ClassVar[str] = "erp"

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def create(cls) -> FastAPI:
        """Build the application from the configuration of the working folder.

        Returns:
            FastAPI: The platform application.

        Raises:
            SEInvalidConfigSectionException: If a configuration section refuses a value.
            SEAppConfigError: If the configuration file cannot be read or validated.
        """
        LoggingSetup(Path(cls.LOGGER_PATH), cls.SERVICE).configure()
        logger: Logger = getLogger(__name__)
        overrides = EnvironmentOverrides(cls.ENV_PREFIX, os.environ, logger)
        config = AppConfigLoader(PlatformConfig, Path(cls.CONFIG_PATH), overrides, logger).read()
        logger.info("Building the %s application.", cls.SERVICE)
        return AppBuilder(config, logger).build()
