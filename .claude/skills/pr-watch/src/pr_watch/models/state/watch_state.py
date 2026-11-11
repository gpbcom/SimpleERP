from __future__ import annotations

# Standard library imports
from datetime import datetime
from typing import Dict, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.state.delivery_log import DeliveryLog
from pr_watch.models.state.exceptions import (
    SEWatchStateInvalidCursors,
    SEWatchStateInvalidDelivery,
    SEWatchStateInvalidLastChecked,
    SEWatchStateInvalidSnapshots,
    SEWatchStateInvalidUnwatched,
)
from pr_watch.models.state.pr_snapshot import PrSnapshot
from pr_watch.models.state.unwatched_pull_request import UnwatchedPullRequest
from pr_watch.models.validation.field_rules import FieldRules


class WatchState(BaseModel):
    """What the watcher remembers between two runs.

    Attributes:
        last_checked (Optional[datetime]): The end of the last run.
        delivery (DeliveryLog): When events reached their sessions.
        cursors (Dict[str, int]): The last comment read, by ``<watch id>|<comment source>``.
        snapshots (Dict[str, PrSnapshot]): The last state seen of each pull request, by watch.
        unwatched (Dict[str, UnwatchedPullRequest]): The open pull requests nobody watches, by
            ``<repository>#<number>``.

    Notes:
        A comment cursor is keyed ``<watch id>|<comment source>``: the identifiers of reviews, line comments and
        conversation comments come from different sequences.
    """

    model_config = ConfigDict(extra="forbid")

    last_checked: Optional[datetime] = Field(
        default=None, description="The end of the last run.", examples=["2026-11-10T09:10:00+01:00"]
    )
    delivery: DeliveryLog = Field(
        default_factory=DeliveryLog,
        description="When events reached their sessions.",
        examples=[{"notified": {"GH-12": "2026-11-10T09:10:00+01:00"}}],
    )
    cursors: Dict[str, int] = Field(
        default_factory=dict,
        description="The last comment read, by ``<watch id>|<comment source>``.",
        examples=[{"GH-12:gpbcom/simple-erp#7|inline": 9001}],
    )
    snapshots: Dict[str, PrSnapshot] = Field(
        default_factory=dict, description="The last state seen of each pull request, by watch.", examples=[{}]
    )
    unwatched: Dict[str, UnwatchedPullRequest] = Field(
        default_factory=dict,
        description="The open pull requests nobody watches, by ``<repository>#<number>``.",
        examples=[{}],
    )

    @field_validator("last_checked", mode="before")
    def validate_last_checked(cls, value: JsonValue) -> JsonValue:
        """Validate ``last_checked``.

        Args:
            value (JsonValue): The raw last checked, or ``None``.

        Returns:
            JsonValue: The last checked, or ``None``.

        Raises:
            SEWatchStateInvalidLastChecked: When the value is not a time with its time zone.
        """
        if value is None:
            return None
        return FieldRules.moment(value, SEWatchStateInvalidLastChecked, "last_checked")

    @field_validator("delivery", mode="before")
    def validate_delivery(cls, value: JsonValue) -> JsonValue:
        """Validate ``delivery``.

        Args:
            value (JsonValue): The raw delivery, or ``None``.

        Returns:
            JsonValue: The delivery, or its default.

        Raises:
            SEWatchStateInvalidDelivery: When the value is not a model or a mapping of its fields.
        """
        if value is None:
            return cls.model_fields["delivery"].get_default(call_default_factory=True)
        return FieldRules.nested(value, SEWatchStateInvalidDelivery, "delivery")

    @field_validator("cursors", mode="before")
    def validate_cursors(cls, value: JsonValue) -> JsonValue:
        """Validate ``cursors``.

        Args:
            value (JsonValue): The raw cursors, or ``None``.

        Returns:
            JsonValue: The cursors, or its default.

        Raises:
            SEWatchStateInvalidCursors: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["cursors"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SEWatchStateInvalidCursors, "cursors")

    @field_validator("snapshots", mode="before")
    def validate_snapshots(cls, value: JsonValue) -> JsonValue:
        """Validate ``snapshots``.

        Args:
            value (JsonValue): The raw snapshots, or ``None``.

        Returns:
            JsonValue: The snapshots, or its default.

        Raises:
            SEWatchStateInvalidSnapshots: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["snapshots"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SEWatchStateInvalidSnapshots, "snapshots")

    @field_validator("unwatched", mode="before")
    def validate_unwatched(cls, value: JsonValue) -> JsonValue:
        """Validate ``unwatched``.

        Args:
            value (JsonValue): The raw unwatched, or ``None``.

        Returns:
            JsonValue: The unwatched, or its default.

        Raises:
            SEWatchStateInvalidUnwatched: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["unwatched"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SEWatchStateInvalidUnwatched, "unwatched")
