from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, List, Optional, Pattern

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator, model_validator

# First-party imports
from harness_core.models.branches.branch_name import BranchName
from ticket_docs.models.enums import Expectation, RunKind, RunPlace
from ticket_docs.models.evidence.exceptions import (
    SERunRequestInvalidCheck,
    SERunRequestInvalidCommand,
    SERunRequestInvalidExpectation,
    SERunRequestInvalidKind,
    SERunRequestInvalidRunId,
    SERunRequestInvalidTicket,
    SERunRequestInvalidWhat,
    SERunRequestInvalidWhere,
    SERunRequestNoCommand,
)


class RunRequest(BaseModel):
    """What ``ticket-docs record-run`` is asked to record.

    Attributes:
        CHECK_PATTERN (Pattern[str]): A check name: lower-case words joined by hyphens.
        RUN_ID_PATTERN (Pattern[str]): A GitHub Actions run id.
        ticket (str): The ticket, ``GH-<n>``.
        kind (RunKind): What the run tests.
        where (RunPlace): Where it runs.
        check (str): The check's name, the end of the folder name.
        what (str): What the run proves.
        expectation (Expectation): Whether it must fail (tests before the code) or pass.
        command (List[str]): The command to run, empty for an Actions run.
        run_id (Optional[str]): The Actions run to read, instead of a command.

    Notes:
        The check name becomes part of a folder name, so it never holds a slash or a dot.
    """

    CHECK_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    RUN_ID_PATTERN: ClassVar[Pattern[str]] = re.compile(r"^\d+$")

    model_config = ConfigDict(extra="forbid", frozen=True)

    ticket: str = Field(description="The ticket.", examples=["GH-12"])
    kind: RunKind = Field(description="What the run tests.", examples=["unit"])
    where: RunPlace = Field(description="Where it runs.", examples=["local"])
    check: str = Field(description="The check's name, the end of the folder name.", examples=["tdd-red-storage"])
    what: str = Field(description="What the run proves.", examples=["The storage tests before the code"])
    expectation: Expectation = Field(
        default=Expectation.GREEN, description="Whether it must fail or pass.", examples=["red"]
    )
    command: List[str] = Field(
        default_factory=list, description="The command to run.", examples=[["pytest", "-q", "tests"]]
    )
    run_id: Optional[str] = Field(default=None, description="The Actions run to read.", examples=["12345678"])

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket key.

        Returns:
            JsonValue: The key.

        Raises:
            SERunRequestInvalidTicket: When the value is not ``GH-<n>``.
        """
        if not isinstance(value, str) or not BranchName.TICKET_PATTERN.match(value.strip()):
            raise SERunRequestInvalidTicket(
                f"Invalid ticket: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value.strip()

    @field_validator("kind", mode="before")
    def validate_kind(cls, value: JsonValue) -> JsonValue:
        """Validate ``kind``.

        Args:
            value (JsonValue): The raw kind.

        Returns:
            JsonValue: The kind.

        Raises:
            SERunRequestInvalidKind: When the value is not a ``RunKind``.
        """
        if value not in {kind.value for kind in RunKind}:
            raise SERunRequestInvalidKind(
                f"Invalid kind: {value!r}. "  # noqa: E501
                f"Must be one of {[kind.value for kind in RunKind]}."
            )
        return value

    @field_validator("where", mode="before")
    def validate_where(cls, value: JsonValue) -> JsonValue:
        """Validate ``where``.

        Args:
            value (JsonValue): The raw place.

        Returns:
            JsonValue: The place.

        Raises:
            SERunRequestInvalidWhere: When the value is not a ``RunPlace``.
        """
        if value not in {place.value for place in RunPlace}:
            raise SERunRequestInvalidWhere(
                f"Invalid where: {value!r}. "  # noqa: E501
                f"Must be one of {[place.value for place in RunPlace]}."
            )
        return value

    @field_validator("check", mode="before")
    def validate_check(cls, value: JsonValue) -> JsonValue:
        """Validate ``check``.

        Args:
            value (JsonValue): The raw check name.

        Returns:
            JsonValue: The name.

        Raises:
            SERunRequestInvalidCheck: When the value is not lower-case words joined by hyphens.
        """
        if not isinstance(value, str) or not cls.CHECK_PATTERN.match(value):
            raise SERunRequestInvalidCheck(
                f"Invalid check: {value!r}. "  # noqa: E501
                "Must be lower-case words joined by hyphens, such as tdd-red-storage."
            )
        return value

    @field_validator("what", mode="before")
    def validate_what(cls, value: JsonValue) -> JsonValue:
        """Validate ``what``.

        Args:
            value (JsonValue): The raw text.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SERunRequestInvalidWhat: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SERunRequestInvalidWhat(
                f"Invalid what: {value!r}. "  # noqa: E501
                "Must say what the run proves."
            )
        return value.strip()

    @field_validator("expectation", mode="before")
    def validate_expectation(cls, value: JsonValue) -> JsonValue:
        """Validate ``expectation``.

        Args:
            value (JsonValue): The raw expectation, or ``None``.

        Returns:
            JsonValue: The expectation, ``green`` for ``None``.

        Raises:
            SERunRequestInvalidExpectation: When the value is not an ``Expectation``.
        """
        if value is None:
            return Expectation.GREEN.value
        if value not in {expectation.value for expectation in Expectation}:
            raise SERunRequestInvalidExpectation(
                f"Invalid expectation: {value!r}. "  # noqa: E501
                f"Must be one of {[expectation.value for expectation in Expectation]}."
            )
        return value

    @field_validator("command", mode="before")
    def validate_command(cls, value: JsonValue) -> JsonValue:
        """Validate ``command``.

        Args:
            value (JsonValue): The raw command words, or ``None``.

        Returns:
            JsonValue: The words, an empty list for ``None``.

        Raises:
            SERunRequestInvalidCommand: When the value is not a list of strings.
        """
        if value is None:
            return []
        if not isinstance(value, list) or not all(isinstance(word, str) for word in value):
            raise SERunRequestInvalidCommand(
                f"Invalid command: {value!r}. "  # noqa: E501
                "Must be a list of words."
            )
        return value

    @field_validator("run_id", mode="before")
    def validate_run_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``run_id``.

        Args:
            value (JsonValue): The raw run id, or ``None``.

        Returns:
            JsonValue: The id, or ``None``.

        Raises:
            SERunRequestInvalidRunId: When the value is not a number.
        """
        if value is None:
            return None
        if not isinstance(value, str) or not cls.RUN_ID_PATTERN.match(value):
            raise SERunRequestInvalidRunId(
                f"Invalid run_id: {value!r}. "  # noqa: E501
                "Must be the number of a GitHub Actions run."
            )
        return value

    @model_validator(mode="after")
    def validate_command_or_run(self) -> RunRequest:
        """Check that the request names a command or an Actions run, not both.

        Returns:
            RunRequest: The request.

        Raises:
            SERunRequestNoCommand: When neither or both are given.
        """
        if bool(self.command) == (self.run_id is not None):
            raise SERunRequestNoCommand(
                "Give either a command after -- or --run-id. "  # noqa: E501
                "Exactly one of them is needed."
            )
        return self
