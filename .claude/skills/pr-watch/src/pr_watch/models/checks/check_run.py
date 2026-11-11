from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.exceptions import (
    SECheckRunInvalidConclusion,
    SECheckRunInvalidId,
    SECheckRunInvalidLink,
    SECheckRunInvalidName,
    SECheckRunInvalidSuiteId,
)
from pr_watch.models.enums import CheckConclusion
from pr_watch.models.validation.field_rules import FieldRules


class CheckRun(BaseModel):
    """A check run reported on a commit.

    Attributes:
        id (int): The check run's identifier.
        name (str): Its name.
        conclusion (Optional[CheckConclusion]): How it ended, ``None`` while it runs.
        link (Optional[str]): The check run on GitHub.
        suite_id (Optional[int]): The check suite it belongs to, shared with its workflow run.
    """

    model_config = ConfigDict(extra="forbid")

    id: int = Field(description="The check run's identifier.", examples=[501])
    name: str = Field(description="Its name.", examples=["unit"])
    conclusion: Optional[CheckConclusion] = Field(
        default=None, description="How it ended, ``None`` while it runs.", examples=["failure"]
    )
    link: Optional[str] = Field(
        default=None, description="The check run on GitHub.", examples=["https://github.com/gpbcom/simple-erp/runs/501"]
    )
    suite_id: Optional[int] = Field(
        default=None, description="The check suite it belongs to, shared with its workflow run.", examples=[77]
    )

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw id.

        Returns:
            JsonValue: The id.

        Raises:
            SECheckRunInvalidId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SECheckRunInvalidId, "id")

    @field_validator("name", mode="before")
    def validate_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``name``.

        Args:
            value (JsonValue): The raw name.

        Returns:
            JsonValue: The name.

        Raises:
            SECheckRunInvalidName: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SECheckRunInvalidName, "name")

    @field_validator("conclusion", mode="before")
    def validate_conclusion(cls, value: JsonValue) -> JsonValue:
        """Validate ``conclusion``.

        Args:
            value (JsonValue): The raw conclusion, or ``None``.

        Returns:
            JsonValue: The conclusion, or ``None``.

        Raises:
            SECheckRunInvalidConclusion: When the value is not a ``CheckConclusion``.
        """
        if value is None:
            return None
        return FieldRules.member(value, SECheckRunInvalidConclusion, "conclusion", CheckConclusion)

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link, or ``None``.

        Returns:
            JsonValue: The link, or ``None``.

        Raises:
            SECheckRunInvalidLink: When the value is not an http or https link.
        """
        if value is None:
            return None
        return FieldRules.link(value, SECheckRunInvalidLink, "link")

    @field_validator("suite_id", mode="before")
    def validate_suite_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``suite_id``.

        Args:
            value (JsonValue): The raw suite id, or ``None``.

        Returns:
            JsonValue: The suite id, or ``None``.

        Raises:
            SECheckRunInvalidSuiteId: When the value is not a positive integer.
        """
        if value is None:
            return None
        return FieldRules.identifier(value, SECheckRunInvalidSuiteId, "suite_id")
