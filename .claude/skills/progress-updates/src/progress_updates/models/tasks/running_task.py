from __future__ import annotations

# Standard library imports
from typing import Optional, Self

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator, model_validator

# First-party imports
from progress_updates.models.enums import TaskSource, TaskState
from progress_updates.models.tasks.exceptions import (
    SERunningTaskDoneAboveTotal,
    SERunningTaskInvalidDetail,
    SERunningTaskInvalidDone,
    SERunningTaskInvalidName,
    SERunningTaskInvalidSource,
    SERunningTaskInvalidState,
    SERunningTaskInvalidTotal,
)


class RunningTask(BaseModel):
    """One task an update reports: what it is, where it was found, its state and how far it got.

    Attributes:
        name (str): What the task is, such as ``K03 mermaid`` or ``research agent``.
        source (TaskSource): Where the task was found.
        state (TaskState): Its state.
        detail (str): Its last meaningful output or what it waits for, on one line.
        done (Optional[int]): How many items are done, when it counts.
        total (Optional[int]): How many items there are, when it counts.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(description="What the task is.", examples=["K03 mermaid"])
    source: TaskSource = Field(description="Where the task was found.", examples=["background"])
    state: TaskState = Field(description="The task's state.", examples=["running"])
    detail: str = Field(default="", description="Its last meaningful output, on one line.", examples=["batch 4"])
    done: Optional[int] = Field(default=None, description="How many items are done.", examples=[4])
    total: Optional[int] = Field(default=None, description="How many items there are.", examples=[9])

    @field_validator("name", mode="before")
    def validate_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``name``.

        Args:
            value (JsonValue): The raw name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            SERunningTaskInvalidName: When the name is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SERunningTaskInvalidName(
                f"Invalid name: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("source", mode="before")
    def validate_source(cls, value: JsonValue) -> JsonValue:
        """Validate ``source``.

        Args:
            value (JsonValue): The raw source.

        Returns:
            JsonValue: The source.

        Raises:
            SERunningTaskInvalidSource: When the value is not a known source.
        """
        sources = [source.value for source in TaskSource]
        if value not in sources:
            raise SERunningTaskInvalidSource(
                f"Invalid source: {value!r}. "  # noqa: E501
                f"Must be one of {sources}."
            )
        return value

    @field_validator("state", mode="before")
    def validate_state(cls, value: JsonValue) -> JsonValue:
        """Validate ``state``.

        Args:
            value (JsonValue): The raw state.

        Returns:
            JsonValue: The state.

        Raises:
            SERunningTaskInvalidState: When the value is not a known state.
        """
        states = [state.value for state in TaskState]
        if value not in states:
            raise SERunningTaskInvalidState(
                f"Invalid state: {value!r}. "  # noqa: E501
                f"Must be one of {states}."
            )
        return value

    @field_validator("detail", mode="before")
    def validate_detail(cls, value: JsonValue) -> JsonValue:
        """Validate ``detail``.

        Args:
            value (JsonValue): The raw detail.

        Returns:
            JsonValue: The detail on one line, stripped, or the default when ``None``.

        Raises:
            SERunningTaskInvalidDetail: When the value is not a string.
        """
        if value is None:
            return cls.model_fields["detail"].get_default(call_default_factory=True)
        if not isinstance(value, str):
            raise SERunningTaskInvalidDetail(
                f"Invalid detail: {value!r}. "  # noqa: E501
                "Must be a string."
            )
        return " ".join(value.split())

    @field_validator("done", mode="before")
    def validate_done(cls, value: JsonValue) -> JsonValue:
        """Validate ``done``.

        Args:
            value (JsonValue): The raw count.

        Returns:
            JsonValue: The count, or ``None``.

        Raises:
            SERunningTaskInvalidDone: When the value is not a whole number of 0 or more.
        """
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SERunningTaskInvalidDone(
                f"Invalid done: {value!r}. "  # noqa: E501
                "Must be a whole number of 0 or more."
            )
        return value

    @field_validator("total", mode="before")
    def validate_total(cls, value: JsonValue) -> JsonValue:
        """Validate ``total``.

        Args:
            value (JsonValue): The raw count.

        Returns:
            JsonValue: The count, or ``None``.

        Raises:
            SERunningTaskInvalidTotal: When the value is not a whole number of 1 or more.
        """
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise SERunningTaskInvalidTotal(
                f"Invalid total: {value!r}. "  # noqa: E501
                "Must be a whole number of 1 or more."
            )
        return value

    @model_validator(mode="after")
    def validate_counts(self) -> Self:
        """Check that ``done`` is not above ``total``.

        Returns:
            Self: The task.

        Raises:
            SERunningTaskDoneAboveTotal: When both are set and ``done`` is above ``total``.
        """
        if self.done is not None and self.total is not None and self.done > self.total:
            raise SERunningTaskDoneAboveTotal(
                f"Invalid counts: {self.done} done of {self.total}. "  # noqa: E501
                "Done must not be above the total."
            )
        return self
