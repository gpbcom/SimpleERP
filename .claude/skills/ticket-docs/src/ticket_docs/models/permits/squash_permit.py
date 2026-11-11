from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from typing import ClassVar, Pattern

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.permits.exceptions import (
    SESquashPermitInvalidBranch,
    SESquashPermitInvalidExpiresAt,
    SESquashPermitInvalidHash,
    SESquashPermitInvalidTicket,
)


class SquashPermit(BaseModel):
    """The human's one-shot permission to commit a GIT-4 squash, which adds tests and code together.

    Attributes:
        TICKET_PATTERN (Pattern[str]): A ticket key, ``GH-<issue number>``.
        HASH_PATTERN (Pattern[str]): A full object hash.
        ticket (str): The ticket whose branch is squashed.
        branch (str): The branch the squash is committed on.
        head (str): The commit the squash sits on, after ``git reset --soft <base>``.
        tree (str): The tree of the staged squash, as ``git write-tree`` gives it.
        expires_at (datetime): When the permit stops counting, with its time zone.

    Notes:
        ``git-gate`` lets a commit add tests together with production code only when the branch, ``HEAD`` and the
        staged tree are exactly these, before ``expires_at``, and deletes the permit then (TEST-7, GIT-4).
    """

    TICKET_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^GH-\d+$")
    HASH_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^[0-9a-f]{40}$")

    model_config = ConfigDict(extra="forbid", frozen=True)

    ticket: str = Field(description="The ticket whose branch is squashed.", examples=["GH-12"])
    branch: str = Field(description="The branch the squash is committed on.", examples=["feature/GH-12-customers"])
    head: str = Field(description="The commit the squash sits on.", examples=["a" * 40])
    tree: str = Field(description="The tree of the staged squash.", examples=["b" * 40])
    expires_at: datetime = Field(description="When the permit stops counting.", examples=["2026-11-10T12:30:00+00:00"])

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket key.

        Returns:
            JsonValue: The ticket key.

        Raises:
            SESquashPermitInvalidTicket: When the value is not ``GH-<n>``.
        """
        if not isinstance(value, str) or not cls.TICKET_PATTERN.match(value.strip()):
            raise SESquashPermitInvalidTicket(
                f"Invalid ticket: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value.strip()

    @field_validator("branch", mode="before")
    def validate_branch(cls, value: JsonValue) -> JsonValue:
        """Validate ``branch``.

        Args:
            value (JsonValue): The raw branch name.

        Returns:
            JsonValue: The branch name, stripped.

        Raises:
            SESquashPermitInvalidBranch: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SESquashPermitInvalidBranch(
                f"Invalid branch: {value!r}. "  # noqa: E501
                "Must be a non-empty branch name."
            )
        return value.strip()

    @field_validator("head", "tree", mode="before")
    def validate_hash(cls, value: JsonValue) -> JsonValue:
        """Validate ``head`` and ``tree``.

        Args:
            value (JsonValue): The raw hash.

        Returns:
            JsonValue: The hash, in lower case.

        Raises:
            SESquashPermitInvalidHash: When the value is not a full 40-character hash.
        """
        if not isinstance(value, str) or not cls.HASH_PATTERN.match(value.strip().lower()):
            raise SESquashPermitInvalidHash(
                f"Invalid hash: {value!r}. "  # noqa: E501
                "Must be a full 40-character object hash."
            )
        return value.strip().lower()

    @field_validator("expires_at", mode="before")
    def validate_expires_at(cls, value: JsonValue) -> JsonValue:
        """Validate ``expires_at``.

        Args:
            value (JsonValue): The raw moment, a ``datetime`` or an ISO 8601 text.

        Returns:
            JsonValue: The moment, with its time zone.

        Raises:
            SESquashPermitInvalidExpiresAt: When the value is not a moment with a time zone.
        """
        text = value.isoformat() if isinstance(value, datetime) else value
        try:
            moment = datetime.fromisoformat(text.strip()) if isinstance(text, str) else None
        except ValueError:
            moment = None
        if moment is None or moment.tzinfo is None:
            raise SESquashPermitInvalidExpiresAt(
                f"Invalid expires_at: {value!r}. "  # noqa: E501
                "Must be an ISO 8601 moment with its time zone."
            )
        return moment.isoformat()
