from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, Tuple

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from release_notes.models.enums import VersionBump
from release_notes.models.versions.exceptions import SEInvalidSemanticVersionException, SESemanticVersionInvalidPart


class SemanticVersion(BaseModel):
    """A semantic version, ``major.minor.patch``.

    Attributes:
        PATTERN (re.Pattern[str]): The text of a version, without a leading ``v`` or a pre-release suffix.
        major (int): Bumped by a breaking change.
        minor (int): Bumped by a new feature.
        patch (int): Bumped by a fix.

    Notes:
        Versions compare by ``key``, their three numbers, so ``0.10.0`` comes after ``0.9.1``.
    """

    PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")

    model_config = ConfigDict(extra="forbid", frozen=True)

    major: int = Field(default=0, description="Bumped by a breaking change.", examples=[1])
    minor: int = Field(default=0, description="Bumped by a new feature.", examples=[4])
    patch: int = Field(default=0, description="Bumped by a fix.", examples=[2])

    @field_validator("major", "minor", "patch", mode="before")
    def validate_part(cls, value: JsonValue) -> JsonValue:
        """Validate ``major``, ``minor`` and ``patch``.

        Args:
            value (JsonValue): The raw number, or ``None``.

        Returns:
            JsonValue: The number, or 0.

        Raises:
            SESemanticVersionInvalidPart: When the value is not a whole number of at least 0.
        """
        if value is None:
            return 0
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SESemanticVersionInvalidPart(
                f"Invalid version part: {value!r}. "  # noqa: E501
                "Must be a whole number of at least 0."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def parse(cls, text: str) -> SemanticVersion:
        """Read a version.

        Args:
            text (str): The version, such as ``1.4.2``.

        Returns:
            SemanticVersion: The version.

        Raises:
            SEInvalidSemanticVersionException: When the text is not ``x.y.z``.
        """
        match = cls.PATTERN.match(text.strip())
        if match is None:
            raise SEInvalidSemanticVersionException(
                f"Invalid version: {text!r}. "  # noqa: E501
                "Must look like 1.4.2."
            )
        return cls(major=int(match.group(1)), minor=int(match.group(2)), patch=int(match.group(3)))

    @property
    def key(self) -> Tuple[int, int, int]:
        """The three numbers, to compare and sort versions."""
        return (self.major, self.minor, self.patch)

    def bumped(self, bump: VersionBump) -> SemanticVersion:
        """Give the next version for a bump.

        Args:
            bump (VersionBump): The part to bump.

        Returns:
            SemanticVersion: The version with that part bumped and the lower parts reset.
        """
        match bump:
            case VersionBump.MAJOR:
                return SemanticVersion(major=self.major + 1)
            case VersionBump.MINOR:
                return SemanticVersion(major=self.major, minor=self.minor + 1)
            case _:
                return SemanticVersion(major=self.major, minor=self.minor, patch=self.patch + 1)

    def __str__(self) -> str:
        """Write the version as ``major.minor.patch``."""
        return f"{self.major}.{self.minor}.{self.patch}"
