from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from release_notes.models.catalogs.exceptions import (
    SEChangelogTypeInvalidBump,
    SEChangelogTypeInvalidHeading,
    SEChangelogTypeInvalidName,
)
from release_notes.models.enums import VersionBump


class ChangelogType(BaseModel):
    """One changelog fragment type (Keep a Changelog), its CHANGELOG heading and the version part it bumps.

    Attributes:
        NAME_PATTERN (re.Pattern[str]): A type name, lower-case letters only.
        name (str): The type, as written in a fragment's file name.
        heading (str): The ``###`` heading of its CHANGELOG subsection.
        bump (VersionBump): The semantic version part it bumps.
    """

    NAME_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^[a-z]+$")

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(description="The type, as written in a fragment's file name.", examples=["added"])
    heading: str = Field(description="The heading of its CHANGELOG subsection.", examples=["Added"])
    bump: VersionBump = Field(description="The semantic version part it bumps.", examples=["minor"])

    @field_validator("name", mode="before")
    def validate_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``name``.

        Args:
            value (JsonValue): The raw name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SEChangelogTypeInvalidName: When the value is not lower-case letters.
        """
        if not isinstance(value, str) or not cls.NAME_PATTERN.match(value.strip()):
            raise SEChangelogTypeInvalidName(
                f"Invalid name: {value!r}. "  # noqa: E501
                "Must be lower-case letters, such as added."
            )
        return value.strip()

    @field_validator("heading", mode="before")
    def validate_heading(cls, value: JsonValue) -> JsonValue:
        """Validate ``heading``.

        Args:
            value (JsonValue): The raw heading.

        Returns:
            JsonValue: The heading, stripped.

        Raises:
            SEChangelogTypeInvalidHeading: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEChangelogTypeInvalidHeading(
                f"Invalid heading: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("bump", mode="before")
    def validate_bump(cls, value: JsonValue) -> JsonValue:
        """Validate ``bump``.

        Args:
            value (JsonValue): The raw bump.

        Returns:
            JsonValue: The bump.

        Raises:
            SEChangelogTypeInvalidBump: When the value is not a ``VersionBump``.
        """
        if not isinstance(value, str) or value not in {bump.value for bump in VersionBump}:
            raise SEChangelogTypeInvalidBump(
                f"Invalid bump: {value!r}. "  # noqa: E501
                f"Must be one of {[bump.value for bump in VersionBump]}."
            )
        return value
