from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.configuration.exceptions import (
    SETimingConfigInvalidIntervalMinutes,
    SETimingConfigInvalidOperationsShown,
    SETimingConfigInvalidQaWaitMinutes,
    SETimingConfigInvalidRenotifyMinutes,
)
from pr_watch.models.validation.field_rules import FieldRules


class TimingConfig(BaseModel):
    """How often the watcher runs and how long it waits before it acts again.

    Attributes:
        interval_minutes (int): Minutes between two runs of the timer.
        renotify_minutes (int): Minutes before a ticket whose events still wait is notified again.
        qa_wait_minutes (int): Minutes a qa approval may wait before it becomes an event.
        operations_shown (int): Operations listed in the summary page.

    Notes:
        The values are minutes, read from ``conf/watch.yaml``.
    """

    model_config = ConfigDict(extra="forbid")

    interval_minutes: int = Field(description="Minutes between two runs of the timer.", examples=[10])
    renotify_minutes: int = Field(
        description="Minutes before a ticket whose events still wait is notified again.", examples=[60]
    )
    qa_wait_minutes: int = Field(
        description="Minutes a qa approval may wait before it becomes an event.", examples=[30]
    )
    operations_shown: int = Field(description="Operations listed in the summary page.", examples=[60])

    @field_validator("interval_minutes", mode="before")
    def validate_interval_minutes(cls, value: JsonValue) -> JsonValue:
        """Validate ``interval_minutes``.

        Args:
            value (JsonValue): The raw interval minutes.

        Returns:
            JsonValue: The interval minutes.

        Raises:
            SETimingConfigInvalidIntervalMinutes: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SETimingConfigInvalidIntervalMinutes, "interval_minutes")

    @field_validator("renotify_minutes", mode="before")
    def validate_renotify_minutes(cls, value: JsonValue) -> JsonValue:
        """Validate ``renotify_minutes``.

        Args:
            value (JsonValue): The raw renotify minutes.

        Returns:
            JsonValue: The renotify minutes.

        Raises:
            SETimingConfigInvalidRenotifyMinutes: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SETimingConfigInvalidRenotifyMinutes, "renotify_minutes")

    @field_validator("qa_wait_minutes", mode="before")
    def validate_qa_wait_minutes(cls, value: JsonValue) -> JsonValue:
        """Validate ``qa_wait_minutes``.

        Args:
            value (JsonValue): The raw qa wait minutes.

        Returns:
            JsonValue: The qa wait minutes.

        Raises:
            SETimingConfigInvalidQaWaitMinutes: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SETimingConfigInvalidQaWaitMinutes, "qa_wait_minutes")

    @field_validator("operations_shown", mode="before")
    def validate_operations_shown(cls, value: JsonValue) -> JsonValue:
        """Validate ``operations_shown``.

        Args:
            value (JsonValue): The raw operations shown.

        Returns:
            JsonValue: The operations shown.

        Raises:
            SETimingConfigInvalidOperationsShown: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SETimingConfigInvalidOperationsShown, "operations_shown")
