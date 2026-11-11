from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, Self

# Third-party imports
import yaml
from pydantic import BaseModel, ConfigDict

# First-party imports
from harness_core.models.catalogs.exceptions import SEYamlCatalogUnreadable


class YamlCatalog(BaseModel):
    """Data kept in a YAML file instead of in code.

    Attributes:
        UNREADABLE (type[Exception]): The exception a subclass raises when its file cannot be read.

    Notes:
        A subclass declares its fields and its own ``UNREADABLE`` exception, so that the error names the catalogue.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEYamlCatalogUnreadable

    model_config = ConfigDict(extra="forbid", frozen=True)

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def load(cls, path: Path) -> Self:
        """Load and validate a catalogue file.

        Args:
            path (Path): The YAML file.

        Returns:
            Self: The validated catalogue.

        Raises:
            Exception: The subclass's ``UNREADABLE`` exception, when the file is missing or is not valid YAML.
        """
        try:
            with path.open(encoding="utf-8") as handle:
                data = yaml.safe_load(handle)
        except (OSError, yaml.YAMLError) as error:
            raise cls.UNREADABLE(
                f"The catalogue {path} cannot be read. "  # noqa: E501
                f"The error was {type(error).__name__}."
            ) from error
        return cls.model_validate(data)
