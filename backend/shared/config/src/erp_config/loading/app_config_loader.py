from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from pathlib import Path
from typing import Dict, Optional, Type

# Third-party imports
import yaml
from pydantic import JsonValue, ValidationError

# First-party imports
from erp_config.loading.environment_overrides import EnvironmentOverrides
from erp_config.models.config_section import ConfigSection
from erp_config.models.exceptions import (
    SEAppConfigInvalidError,
    SEAppConfigMissingDefaultError,
    SEAppConfigUnreadableError,
    SEInvalidConfigSectionException,
)


class AppConfigLoader[T: ConfigSection]:
    """Read ``conf/app.yaml``, apply the environment overrides and validate the result.

    Attributes:
        model (Type[T]): The configuration model the file is validated against.
        path (Path): The configuration file.
        overrides (EnvironmentOverrides): The environment variables that replace values of the file.
        logger (Logger): Logger instance.

    Notes:
        - **Every default is written out in the file** (D413): the file is the one place a reader sees every setting,
          so a field the file omits is refused rather than filled silently by the model.
        - The method is ``read`` and not ``load``, because ``YamlCatalog.load`` means something else.
        - **Neither values nor the configuration are ever logged**, because a value may name a vault entry (D240).
          A validation error is logged by its type only, because its text may quote the input.
    """

    def __init__(
        self, model: Type[T], path: Path, overrides: EnvironmentOverrides, logger: Optional[Logger] = None
    ) -> None:
        """Create the loader.

        Args:
            model (Type[T]): The configuration model.
            path (Path): The configuration file.
            overrides (EnvironmentOverrides): The environment variables that apply.
            logger (Optional[Logger]): Logger instance.
        """
        self.model = model
        self.path = path
        self.overrides = overrides
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _read_file(self) -> Dict[str, JsonValue]:
        """Read the file as a YAML mapping.

        Returns:
            Dict[str, JsonValue]: The content of the file.

        Raises:
            SEAppConfigUnreadableError: If the file cannot be read, is not YAML or is not a mapping.
        """
        try:
            with self.path.open(encoding="utf-8") as stream:
                data = yaml.safe_load(stream)
        except (OSError, yaml.YAMLError) as error:
            self.logger.error("Cannot read the configuration file %s: %s.", self.path, type(error).__name__)
            raise SEAppConfigUnreadableError(
                f"Unreadable configuration: {str(self.path)!r}. Must be a readable YAML file."
            ) from error
        if not isinstance(data, dict):
            self.logger.error("The configuration file %s is not a mapping.", self.path)
            raise SEAppConfigUnreadableError(f"Unreadable configuration: {str(self.path)!r}. Must hold a YAML mapping.")
        self.logger.debug("Read the configuration file %s.", self.path)
        return data

    def _check_defaults(self, model: Type[ConfigSection], data: Dict[str, JsonValue], prefix: str) -> None:
        """Check that every field of a model is written in the data, recursing into sections.

        Args:
            model (Type[ConfigSection]): The section to check.
            data (Dict[str, JsonValue]): The data of that section.
            prefix (str): The dotted path of the section, empty for the root.

        Raises:
            SEAppConfigMissingDefaultError: If a field is absent.
        """
        for name, field in model.model_fields.items():
            path = f"{prefix}{name}"
            if name not in data:
                self.logger.error("The configuration file %s does not write the default of %s.", self.path, path)
                raise SEAppConfigMissingDefaultError(
                    f"Missing default: {path!r}. Must be written in the configuration file."
                )
            annotation = field.annotation
            value = data[name]
            if isinstance(annotation, type) and issubclass(annotation, ConfigSection) and isinstance(value, dict):
                self._check_defaults(annotation, value, f"{path}.")

    def _validate(self, data: Dict[str, JsonValue]) -> T:
        """Validate the data against the model.

        Args:
            data (Dict[str, JsonValue]): The data with the overrides applied.

        Returns:
            T: The validated configuration.

        Raises:
            SEAppConfigInvalidError: If the data does not match the model.
            SEInvalidConfigSectionException: If a section refuses a value, passed on unchanged.
        """
        try:
            return self.model.model_validate(data)
        except ValidationError as error:
            self.logger.error("The configuration is invalid: %s.", type(error).__name__)
            raise SEAppConfigInvalidError(
                f"Invalid configuration: {str(self.path)!r}. Must match {self.model.__name__}."
            ) from error
        except SEInvalidConfigSectionException as error:
            self.logger.error("A configuration section refused a value: %s.", type(error).__name__)
            raise

    ############################
    # Publicly Exposed Methods #
    ############################

    def read(self) -> T:
        """Read the file, apply the overrides and validate the result.

        Returns:
            T: The validated configuration.

        Raises:
            SEAppConfigUnreadableError: If the file cannot be read.
            SEAppConfigMissingDefaultError: If a field is not written in the file.
            SEAppConfigUnknownOverrideError: If a variable names a path the file does not hold.
            SEAppConfigInvalidError: If the data does not match the model.
        """
        data = self._read_file()
        self._check_defaults(self.model, data, "")
        merged = self.overrides.apply(data)
        config = self._validate(merged)
        self.logger.info(
            "Read the %s configuration from %s with %d overrides.",
            self.model.__name__,
            self.path,
            len(self.overrides.variables()),
        )
        return config
