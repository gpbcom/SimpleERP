from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from logging.config import dictConfig
from pathlib import Path
from typing import Dict, Optional

# Third-party imports
import yaml

# First-party imports
from erp_logging.models.exceptions import SELoggingConfigInvalidError, SELoggingConfigUnreadableError


class LoggingSetup:
    """Apply the logger configuration of one service.

    Attributes:
        config_path (Path): The ``logger.yaml`` to read.
        service (str): The name of the service that writes the records.
        logs_dir (Path): The folder that holds every log file.
        logger (Logger): Logger instance.

    Notes:
        - The service is injected so that one reference file serves every service.
        - ``disable_existing_loggers`` defaults to ``False``, so that loggers created before the setup keep writing.
        - **Every handler file is moved to ``logs_dir``**, whatever folder the file names, so that a service never
          writes outside its own ``logs/``.
    """

    def __init__(
        self,
        config_path: Path,
        service: str,
        logs_dir: Optional[Path] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Create the setup.

        Args:
            config_path (Path): The ``logger.yaml`` to read.
            service (str): The name of the service.
            logs_dir (Optional[Path]): The folder of the log files. Defaults to ``logs``.
            logger (Optional[Logger]): Logger instance.
        """
        self.config_path = config_path
        self.service = service
        self.logs_dir = logs_dir if logs_dir is not None else Path("logs")
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _read(self) -> Dict[str, object]:
        """Read the configuration file.

        Returns:
            Dict[str, object]: The parsed mapping.

        Raises:
            SELoggingConfigUnreadableError: If the file cannot be read or is not a YAML mapping.
        """
        self.logger.debug("Reading the logger configuration %s.", self.config_path)
        try:
            with self.config_path.open(encoding="utf-8") as stream:
                content = yaml.safe_load(stream)
        except (OSError, yaml.YAMLError) as error:
            self.logger.error("Cannot read the logger configuration %s: %s.", self.config_path, type(error).__name__)
            raise SELoggingConfigUnreadableError(
                f"Invalid logger configuration: {str(self.config_path)!r}. "  # noqa: E501
                "Must be a readable YAML file."
            ) from error
        if not isinstance(content, dict):
            self.logger.error("The logger configuration %s is not a mapping.", self.config_path)
            raise SELoggingConfigUnreadableError(
                f"Invalid logger configuration: {str(self.config_path)!r}. "  # noqa: E501
                "Must hold a YAML mapping."
            )
        return {str(key): value for key, value in content.items()}

    def _set_service(self, config: Dict[str, object]) -> None:
        """Set the service of the ``context`` filter.

        Args:
            config (Dict[str, object]): The configuration, changed in place.

        Raises:
            SELoggingConfigInvalidError: If the ``context`` filter is missing.
        """
        filters = config.get("filters")
        context = filters.get("context") if isinstance(filters, dict) else None
        if not isinstance(context, dict):
            self.logger.error("The logger configuration %s has no context filter.", self.config_path)
            raise SELoggingConfigInvalidError(
                f"Invalid filters: {filters!r}. "  # noqa: E501
                "Must define the context filter."
            )
        context["service"] = self.service
        config.setdefault("disable_existing_loggers", False)
        self.logger.debug("Set the service of the context filter to %s.", self.service)

    def _move_files(self, config: Dict[str, object]) -> None:
        """Move every handler file into the logs folder, and create it.

        Args:
            config (Dict[str, object]): The configuration, changed in place.
        """
        handlers = config.get("handlers")
        if isinstance(handlers, dict):
            for handler in handlers.values():
                if isinstance(handler, dict) and isinstance(handler.get("filename"), str):
                    handler["filename"] = str(self.logs_dir / Path(handler["filename"]).name)
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.logger.debug("Log files go to %s.", self.logs_dir)

    def _apply(self, config: Dict[str, object]) -> None:
        """Apply the configuration to the logging module.

        Args:
            config (Dict[str, object]): The configuration to apply.

        Raises:
            SELoggingConfigInvalidError: If ``dictConfig`` refuses the configuration.
        """
        try:
            dictConfig(config)
        except (ValueError, TypeError, AttributeError, ImportError) as error:
            self.logger.error("The logger configuration %s is refused: %s.", self.config_path, type(error).__name__)
            raise SELoggingConfigInvalidError(
                f"Invalid logger configuration: {str(self.config_path)!r}. "  # noqa: E501
                "Must be accepted by dictConfig."
            ) from error

    ############################
    # Publicly Exposed Methods #
    ############################

    def configure(self) -> None:
        """Configure logging for the service.

        Raises:
            SELoggingConfigUnreadableError: If the file cannot be read.
            SELoggingConfigInvalidError: If the configuration is refused.
        """
        config = self._read()
        self._set_service(config)
        self._move_files(config)
        self._apply(config)
        self.logger.info("Configured logging for %s from %s.", self.service, self.config_path)
