from __future__ import annotations

# Standard library imports
from typing import ClassVar, List, Optional

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from harness_core.models.catalogs.yaml_catalog import YamlCatalog
from release_notes.models.catalogs.changelog_type import ChangelogType
from release_notes.models.catalogs.exceptions import (
    SEChangelogTypeCatalogInvalidBreakingMarker,
    SEChangelogTypeCatalogInvalidTypes,
    SEChangelogTypeCatalogUnreadable,
)


class ChangelogTypeCatalog(YamlCatalog):
    """The changelog fragment types, read from ``conf/changelog-types.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): The exception raised when the file cannot be read.
        types (List[ChangelogType]): The types, in the order CHANGELOG.md lists them.
        breaking_marker (str): The words that start a breaking change's fragment, which bumps the major version.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEChangelogTypeCatalogUnreadable

    types: List[ChangelogType] = Field(
        description="The types, in the order CHANGELOG.md lists them.",
        examples=[[{"name": "added", "heading": "Added", "bump": "minor"}]],
    )
    breaking_marker: str = Field(
        description="The words that start a breaking change's fragment.", examples=["**Breaking:**"]
    )

    @field_validator("types", mode="before")
    def validate_types(cls, value: JsonValue) -> JsonValue:
        """Validate ``types``.

        Args:
            value (JsonValue): The raw types.

        Returns:
            JsonValue: The types, each validated by ``ChangelogType``.

        Raises:
            SEChangelogTypeCatalogInvalidTypes: When the value is not a non-empty list, or a name appears twice.
        """
        if not isinstance(value, list) or not value:
            raise SEChangelogTypeCatalogInvalidTypes(
                f"Invalid types: {value!r}. "  # noqa: E501
                "Must be a non-empty list of types."
            )
        names = [item.get("name") for item in value if isinstance(item, dict)]
        if len(names) != len(set(map(str, names))):
            raise SEChangelogTypeCatalogInvalidTypes(
                f"Invalid types: {names!r}. "  # noqa: E501
                "Each name must appear once."
            )
        return value

    @field_validator("breaking_marker", mode="before")
    def validate_breaking_marker(cls, value: JsonValue) -> JsonValue:
        """Validate ``breaking_marker``.

        Args:
            value (JsonValue): The raw marker.

        Returns:
            JsonValue: The marker, stripped.

        Raises:
            SEChangelogTypeCatalogInvalidBreakingMarker: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEChangelogTypeCatalogInvalidBreakingMarker(
                f"Invalid breaking_marker: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    def names(self) -> List[str]:
        """Give the type names, in the catalogue's order."""
        return [kind.name for kind in self.types]

    def named(self, name: str) -> Optional[ChangelogType]:
        """Find a type by its name.

        Args:
            name (str): The type name, such as ``added``.

        Returns:
            Optional[ChangelogType]: The type, or ``None`` when the catalogue has none of that name.
        """
        return next((kind for kind in self.types if kind.name == name), None)
