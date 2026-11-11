from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import OperationKind
from pr_watch.models.events.exceptions import (
    SEOperationInvalidAt,
    SEOperationInvalidDetail,
    SEOperationInvalidKind,
    SEOperationInvalidLink,
    SEOperationInvalidPrId,
)
from pr_watch.models.validation.field_rules import FieldRules


class Operation(BaseModel):
    """One thing that happened to a watched pull request, seen by the watcher or done in the ticket's session.

    Attributes:
        at (datetime): When it happened.
        pr_id (str): The watch it belongs to.
        kind (OperationKind): What happened.
        detail (str): One line saying it.
        link (Optional[str]): The run, comment or commit it refers to.
    """

    model_config = ConfigDict(extra="forbid")

    at: datetime = Field(description="When it happened.", examples=["2026-11-10T09:10:00+01:00"])
    pr_id: str = Field(description="The watch it belongs to.", examples=["GH-12:gpbcom/simple-erp#7"])
    kind: OperationKind = Field(description="What happened.", examples=["detected"])
    detail: str = Field(description="One line saying it.", examples=["2 checks failed on 668501e0"])
    link: Optional[str] = Field(
        default=None,
        description="The run, comment or commit it refers to.",
        examples=["https://github.com/gpbcom/simple-erp/pull/7"],
    )

    @field_validator("at", mode="before")
    def validate_at(cls, value: JsonValue) -> JsonValue:
        """Validate ``at``.

        Args:
            value (JsonValue): The raw at.

        Returns:
            JsonValue: The at.

        Raises:
            SEOperationInvalidAt: When the value is not a time with its time zone.
        """
        return FieldRules.moment(value, SEOperationInvalidAt, "at")

    @field_validator("pr_id", mode="before")
    def validate_pr_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``pr_id``.

        Args:
            value (JsonValue): The raw pr id.

        Returns:
            JsonValue: The pr id.

        Raises:
            SEOperationInvalidPrId: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEOperationInvalidPrId, "pr_id")

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw kind.

        Returns:
            JsonValue: The kind.

        Raises:
            SEOperationInvalidKind: When the value is not a ``OperationKind``.
        """
        return FieldRules.member(value, SEOperationInvalidKind, "kind", OperationKind)

    @field_validator("detail", mode="before")
    def validate_detail(cls, value: JsonValue) -> JsonValue:
        """Validate ``detail``.

        Args:
            value (JsonValue): The raw detail.

        Returns:
            JsonValue: The detail.

        Raises:
            SEOperationInvalidDetail: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEOperationInvalidDetail, "detail")

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link, or ``None``.

        Returns:
            JsonValue: The link, or ``None``.

        Raises:
            SEOperationInvalidLink: When the value is not an http or https link.
        """
        if value is None:
            return None
        return FieldRules.link(value, SEOperationInvalidLink, "link")

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def key(self) -> str:
        """The ticket the operation belongs to."""
        return self.pr_id.split(":", 1)[0]
