from __future__ import annotations

# Standard library imports
from typing import List, Optional

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.checks.exceptions import (
    SERebaseProbeResultInvalidBaseSha,
    SERebaseProbeResultInvalidConflictFiles,
    SERebaseProbeResultInvalidError,
    SERebaseProbeResultInvalidHeadSha,
    SERebaseProbeResultInvalidMessages,
)
from pr_watch.models.validation.field_rules import FieldRules


class RebaseProbeResult(BaseModel):
    """Whether a pull request's head merges into its base, tried without touching any working tree.

    Attributes:
        head_sha (Optional[str]): The head commit tried.
        base_sha (Optional[str]): The base commit tried.
        conflict_files (List[str]): The files that conflict, empty when the merge is clean.
        messages (str): What git said about the conflicts.
        error (Optional[str]): Why the probe could not run, ``None`` when it did.
    """

    model_config = ConfigDict(extra="forbid")

    head_sha: Optional[str] = Field(default=None, description="The head commit tried.", examples=["668501e0d3a1"])
    base_sha: Optional[str] = Field(default=None, description="The base commit tried.", examples=["08a71846"])
    conflict_files: List[str] = Field(
        default_factory=list,
        description="The files that conflict, empty when the merge is clean.",
        examples=[["src/a.py"]],
    )
    messages: str = Field(
        default="",
        description="What git said about the conflicts.",
        examples=["CONFLICT (content): Merge conflict in src/a.py"],
    )
    error: Optional[str] = Field(
        default=None,
        description="Why the probe could not run, ``None`` when it did.",
        examples=["git fetch exited 128"],
    )

    @field_validator("head_sha", mode="before")
    def validate_head_sha(cls, value: JsonValue) -> JsonValue:
        """Validate ``head_sha``.

        Args:
            value (JsonValue): The raw head sha, or ``None``.

        Returns:
            JsonValue: The head sha, or ``None``.

        Raises:
            SERebaseProbeResultInvalidHeadSha: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SERebaseProbeResultInvalidHeadSha, "head_sha")

    @field_validator("base_sha", mode="before")
    def validate_base_sha(cls, value: JsonValue) -> JsonValue:
        """Validate ``base_sha``.

        Args:
            value (JsonValue): The raw base sha, or ``None``.

        Returns:
            JsonValue: The base sha, or ``None``.

        Raises:
            SERebaseProbeResultInvalidBaseSha: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SERebaseProbeResultInvalidBaseSha, "base_sha")

    @field_validator("conflict_files", mode="before")
    def validate_conflict_files(cls, value: JsonValue) -> JsonValue:
        """Validate ``conflict_files``.

        Args:
            value (JsonValue): The raw conflict files, or ``None``.

        Returns:
            JsonValue: The conflict files, or its default.

        Raises:
            SERebaseProbeResultInvalidConflictFiles: When the value is not a list of non-empty strings.
        """
        if value is None:
            return cls.model_fields["conflict_files"].get_default(call_default_factory=True)
        return FieldRules.texts(value, SERebaseProbeResultInvalidConflictFiles, "conflict_files")

    @field_validator("messages", mode="before")
    def validate_messages(cls, value: JsonValue) -> JsonValue:
        """Validate ``messages``.

        Args:
            value (JsonValue): The raw messages, or ``None``.

        Returns:
            JsonValue: The messages, or its default.

        Raises:
            SERebaseProbeResultInvalidMessages: When the value is not a string.
        """
        if value is None:
            return cls.model_fields["messages"].get_default(call_default_factory=True)
        return FieldRules.free_text(value, SERebaseProbeResultInvalidMessages, "messages")

    @field_validator("error", mode="before")
    def validate_error(cls, value: JsonValue) -> JsonValue:
        """Validate ``error``.

        Args:
            value (JsonValue): The raw error, or ``None``.

        Returns:
            JsonValue: The error, or ``None``.

        Raises:
            SERebaseProbeResultInvalidError: When the value is not a non-empty string.
        """
        if value is None:
            return None
        return FieldRules.text(value, SERebaseProbeResultInvalidError, "error")
