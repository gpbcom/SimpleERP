from __future__ import annotations

# Standard library imports
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.events.exceptions import (
    SEEventDetailInvalidExcerpt,
    SEEventDetailInvalidLink,
    SEEventDetailInvalidTitle,
)
from pr_watch.models.validation.field_rules import FieldRules


class EventDetail(BaseModel):
    """What an event says, for the session and the summary page.

    Attributes:
        title (str): One line saying it.
        link (Optional[str]): The run, deployment or comment it comes from.
        excerpt (Optional[str]): The lines that show it.
    """

    model_config = ConfigDict(extra="forbid")

    title: str = Field(description="One line saying it.", examples=["2 checks failed on 668501e0"])
    link: Optional[str] = Field(
        default=None,
        description="The run, deployment or comment it comes from.",
        examples=["https://github.com/gpbcom/simple-erp/actions/runs/1"],
    )
    excerpt: Optional[str] = Field(default=None, description="The lines that show it.", examples=["ci / unit: failure"])

    @field_validator("title", mode="before")
    def validate_title(cls, value: JsonValue) -> JsonValue:
        """Validate ``title``.

        Args:
            value (JsonValue): The raw title.

        Returns:
            JsonValue: The title.

        Raises:
            SEEventDetailInvalidTitle: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEEventDetailInvalidTitle, "title")

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link, or ``None``.

        Returns:
            JsonValue: The link, or ``None``.

        Raises:
            SEEventDetailInvalidLink: When the value is not an http or https link.
        """
        if value is None:
            return None
        return FieldRules.link(value, SEEventDetailInvalidLink, "link")

    @field_validator("excerpt", mode="before")
    def validate_excerpt(cls, value: JsonValue) -> JsonValue:
        """Validate ``excerpt``.

        Args:
            value (JsonValue): The raw excerpt, or ``None``.

        Returns:
            JsonValue: The excerpt, or ``None``.

        Raises:
            SEEventDetailInvalidExcerpt: When the value is not a string.
        """
        if value is None:
            return None
        return FieldRules.free_text(value, SEEventDetailInvalidExcerpt, "excerpt")
