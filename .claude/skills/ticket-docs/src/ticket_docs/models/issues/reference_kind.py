from __future__ import annotations

# Standard library imports
import re
from typing import Dict, List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.issues.exceptions import SEReferenceKindInvalidPaths, SEReferenceKindInvalidPatterns


class ReferenceKind(BaseModel):
    """One kind of reference a ticket may give, such as the specifications or the harness rules.

    Attributes:
        paths (List[str]): The repository paths of this kind: a folder ending with a slash, or one file.
        patterns (Dict[str, str]): The regular expressions a reference ID of this kind matches in full, by name.

    Notes:
        A reference's kind is found from the path of its permalink, so a ticket can mix kinds in one table.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    paths: List[str] = Field(
        description="The repository paths of this kind: a folder ending with a slash, or one file.",
        examples=[["docs/specs/"]],
    )
    patterns: Dict[str, str] = Field(
        description="The regular expressions a reference ID of this kind matches in full, by name.",
        examples=[{"feature": r"f\d{2}"}],
    )

    @field_validator("paths", mode="before")
    def validate_paths(cls, value: JsonValue) -> JsonValue:
        """Validate ``paths``.

        Args:
            value (JsonValue): The raw paths.

        Returns:
            JsonValue: The paths.

        Raises:
            SEReferenceKindInvalidPaths: When the value is not a non-empty list of non-empty paths.
        """
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) and item.strip() for item in value)
        ):
            raise SEReferenceKindInvalidPaths(
                f"Invalid paths: {value!r}. "  # noqa: E501
                "Must be a non-empty list of folders ending with a slash or file paths."
            )
        return value

    @field_validator("patterns", mode="before")
    def validate_patterns(cls, value: JsonValue) -> JsonValue:
        """Validate ``patterns``.

        Args:
            value (JsonValue): The raw patterns.

        Returns:
            JsonValue: The patterns.

        Raises:
            SEReferenceKindInvalidPatterns: When the value is not a non-empty mapping of names to regular
                expressions that compile.
        """
        if (
            not isinstance(value, dict)
            or not value
            or not all(isinstance(pattern, str) and pattern.strip() for pattern in value.values())
        ):
            raise SEReferenceKindInvalidPatterns(
                f"Invalid patterns: {value!r}. "  # noqa: E501
                "Must map each ID name to a non-empty regular expression."
            )
        try:
            for pattern in value.values():
                re.compile(str(pattern))
        except re.error as error:
            raise SEReferenceKindInvalidPatterns(
                f"Invalid patterns: {value!r}. "  # noqa: E501
                f"A regular expression does not compile: {error}."
            ) from error
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    def covers(self, path: str) -> bool:
        """Tell whether a repository path is of this kind.

        Args:
            path (str): The path, relative to the repository root.

        Returns:
            bool: ``True`` when it sits in one of the folders, or is one of the files.
        """
        return any(path.startswith(prefix) if prefix.endswith("/") else path == prefix for prefix in self.paths)

    def matches(self, identifier: str) -> bool:
        """Tell whether a reference ID has the shape of this kind.

        Args:
            identifier (str): The ID, such as ``br-f01-07`` or ``GIT-6``.

        Returns:
            bool: ``True`` when one of the patterns matches it in full.
        """
        return any(re.fullmatch(pattern, identifier) for pattern in self.patterns.values())
