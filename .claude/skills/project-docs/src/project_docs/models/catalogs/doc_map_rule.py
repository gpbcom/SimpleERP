from __future__ import annotations

# Standard library imports
from typing import List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from project_docs.models.catalogs.exceptions import SEDocMapRuleInvalidChapters, SEDocMapRuleInvalidPaths


class DocMapRule(BaseModel):
    """One rule of the doc map: the paths it matches and the chapters they concern.

    Attributes:
        paths (List[str]): The globs of the paths, relative to the repository root.
        chapters (List[str]): The chapters these paths concern, empty when they have no documentation impact.

    Notes:
        A glob may hold ``{service}`` or ``{frontend}``, which captures one folder name and fills the same
        placeholder in the chapters.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    paths: List[str] = Field(
        description="The globs of the paths, relative to the repository root.", examples=[["services/{service}/*"]]
    )
    chapters: List[str] = Field(
        default_factory=list,
        description="The chapters these paths concern, empty when they have no documentation impact.",
        examples=[["docs/technical/services/{service}.md"]],
    )

    @field_validator("paths", mode="before")
    def validate_paths(cls, value: JsonValue) -> JsonValue:
        """Validate ``paths``.

        Args:
            value (JsonValue): The raw globs.

        Returns:
            JsonValue: The globs, stripped.

        Raises:
            SEDocMapRuleInvalidPaths: When the value is not a non-empty list of non-empty strings.
        """
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) and item.strip() for item in value)
        ):
            raise SEDocMapRuleInvalidPaths(
                f"Invalid paths: {value!r}. "  # noqa: E501
                "Must be a non-empty list of non-empty globs."
            )
        return [item.strip() for item in value if isinstance(item, str)]

    @field_validator("chapters", mode="before")
    def validate_chapters(cls, value: JsonValue) -> JsonValue:
        """Validate ``chapters``.

        Args:
            value (JsonValue): The raw chapters, or ``None``.

        Returns:
            JsonValue: The chapters, stripped, or an empty list.

        Raises:
            SEDocMapRuleInvalidChapters: When the value is not a list of non-empty strings.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise SEDocMapRuleInvalidChapters(
                f"Invalid chapters: {value!r}. "  # noqa: E501
                "Must be a list of non-empty chapter paths."
            )
        return [item.strip() for item in value if isinstance(item, str)]
