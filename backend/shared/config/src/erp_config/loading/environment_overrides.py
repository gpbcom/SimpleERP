from __future__ import annotations

# Standard library imports
from copy import deepcopy
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Mapping, Optional

# Third-party imports
import yaml
from pydantic import JsonValue

# First-party imports
from erp_config.models.exceptions import SEAppConfigUnknownOverrideError


class EnvironmentOverrides:
    """Environment variables that replace the defaults written in a configuration file.

    Attributes:
        SEPARATOR (str): Text that separates the prefix and each path segment in a variable name.
        prefix (str): Prefix of the variables that apply, such as ``erp``.
        environ (Mapping[str, str]): The environment to read the variables from.
        logger (Logger): Logger instance.

    Notes:
        - A variable ``ERP__SERVER__PORT`` replaces the value at ``server.port``.
        - **Values are never logged**, because a value may name a secret store entry.
    """

    SEPARATOR: ClassVar[str] = "__"

    def __init__(self, prefix: str, environ: Mapping[str, str], logger: Optional[Logger] = None) -> None:
        """Create the overrides.

        Args:
            prefix (str): Prefix of the variables that apply, in any case.
            environ (Mapping[str, str]): The environment to read the variables from.
            logger (Optional[Logger]): Logger instance.
        """
        self.prefix = prefix
        self.environ = environ
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _parse(self, name: str) -> JsonValue:
        """Parse the value of one variable as YAML.

        Args:
            name (str): Name of the variable.

        Returns:
            JsonValue: The parsed value, or the raw text when it is not valid YAML.
        """
        text = self.environ[name]
        try:
            return yaml.safe_load(text)  # type: ignore[no-any-return]
        except yaml.YAMLError:
            self.logger.debug("Variable %s is not valid YAML, so its raw text is kept.", name)
            return text

    def _unknown(self, name: str, cause: Optional[Exception] = None) -> SEAppConfigUnknownOverrideError:
        """Log and build the error for a variable whose path does not exist.

        Args:
            name (str): Name of the variable.
            cause (Optional[Exception]): The exception that led here, if any.

        Returns:
            SEAppConfigUnknownOverrideError: The error to raise.
        """
        self.logger.error("Variable %s names a path the configuration does not hold.", name)
        error = SEAppConfigUnknownOverrideError(f"Unknown override: {name!r}. The path is not in the configuration.")
        error.__cause__ = cause
        return error

    def _replace(self, data: Dict[str, JsonValue], name: str) -> None:
        """Replace the value at the path of one variable.

        Args:
            data (Dict[str, JsonValue]): The data to change in place.
            name (str): Name of the variable.

        Raises:
            SEAppConfigUnknownOverrideError: If the path is absent or goes through a non-mapping.
        """
        segments = [part.lower() for part in name[len(self.prefix) + len(self.SEPARATOR) :].split(self.SEPARATOR)]
        node: JsonValue = data
        for segment in segments[:-1]:
            if not isinstance(node, dict) or segment not in node:
                raise self._unknown(name)
            node = node[segment]
        if not isinstance(node, dict) or segments[-1] not in node:
            raise self._unknown(name)
        node[segments[-1]] = self._parse(name)
        self.logger.debug("Applied variable %s.", name)

    ############################
    # Publicly Exposed Methods #
    ############################

    def variables(self) -> List[str]:
        """List the variables that apply.

        Returns:
            List[str]: The sorted names that start with the upper-case prefix and the separator.
        """
        start = self.prefix.upper() + self.SEPARATOR
        return sorted(name for name in self.environ if name.startswith(start))

    def apply(self, data: Dict[str, JsonValue]) -> Dict[str, JsonValue]:
        """Apply every variable to a copy of the data.

        Args:
            data (Dict[str, JsonValue]): The configuration read from the file, left unchanged.

        Returns:
            Dict[str, JsonValue]: A deep copy with the variables' values in place.

        Raises:
            SEAppConfigUnknownOverrideError: If a variable names a path the data does not hold.
        """
        result = deepcopy(data)
        names = self.variables()
        for name in names:
            self._replace(result, name)
        self.logger.info("Applied %d environment overrides.", len(names))
        return result
