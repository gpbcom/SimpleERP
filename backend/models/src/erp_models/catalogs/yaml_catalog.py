from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar, Self, Type

# Third-party imports
import yaml

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.catalogs.exceptions import SEYamlCatalogUnreadable


class YamlCatalog(FrozenErpModel):
    """The base of every catalogue loaded from ``conf/catalogs/``.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.

    Notes:
        - Each catalogue sets its own ``UNREADABLE``, preferably a subclass of ``SEYamlCatalogUnreadable`` so that
          callers can catch one type.
        - The catalogue is frozen because catalogue data does not change at run time.
        - The messages never quote the content of the file.
    """

    UNREADABLE: ClassVar[Type[Exception]] = SEYamlCatalogUnreadable

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def load(cls, path: Path) -> Self:
        """Load one catalogue from a YAML file.

        Args:
            path (Path): The YAML file to read.

        Returns:
            Self: The validated catalogue.

        Raises:
            Exception: ``UNREADABLE`` if the file cannot be read, parsed, or is not a mapping.
        """
        try:
            with path.open(encoding="utf-8") as file:
                content = yaml.safe_load(file)
        except (OSError, yaml.YAMLError) as error:
            raise cls.UNREADABLE(
                f"Unreadable catalogue: {path}. "  # noqa: E501
                f"The file could not be read as YAML ({type(error).__name__})."
            ) from error
        if not isinstance(content, dict):
            raise cls.UNREADABLE(
                f"Unreadable catalogue: {path}. "  # noqa: E501
                "It must be a YAML mapping."
            )
        return cls.model_validate(content)
