from __future__ import annotations

# Standard library imports
import re
from typing import ClassVar, List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from release_notes.models.fragments.exceptions import (
    SEChangelogFragmentInvalidLines,
    SEChangelogFragmentInvalidTicket,
    SEChangelogFragmentInvalidTypeName,
)


class ChangelogFragment(BaseModel):
    """One ticket's changelog fragment, ``changelog.d/GH-<n>.<type>.md``.

    Attributes:
        TICKET_PATTERN (re.Pattern[str]): A ticket key, ``GH-<n>``.
        TYPE_PATTERN (re.Pattern[str]): A type name, lower-case letters.
        LINES_MIN (int): The fewest lines a fragment holds.
        LINES_MAX (int): The most lines a fragment holds.
        ticket (str): The ticket, from the file name.
        type_name (str): The type, from the file name.
        lines (List[str]): The fragment's non-empty lines, in the changelog's voice.
    """

    TICKET_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^GH-(\d+)$")
    TYPE_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^[a-z]+$")
    LINES_MIN: ClassVar[int] = 1
    LINES_MAX: ClassVar[int] = 3

    model_config = ConfigDict(extra="forbid", frozen=True)

    ticket: str = Field(description="The ticket, from the file name.", examples=["GH-12"])
    type_name: str = Field(description="The type, from the file name.", examples=["added"])
    lines: List[str] = Field(
        description="The fragment's non-empty lines.", examples=[["Customers can be archived from their page."]]
    )

    @field_validator("ticket", mode="before")
    def validate_ticket(cls, value: JsonValue) -> JsonValue:
        """Validate ``ticket``.

        Args:
            value (JsonValue): The raw ticket key.

        Returns:
            JsonValue: The ticket key.

        Raises:
            SEChangelogFragmentInvalidTicket: When the value is not ``GH-<n>``.
        """
        if not isinstance(value, str) or not cls.TICKET_PATTERN.match(value):
            raise SEChangelogFragmentInvalidTicket(
                f"Invalid ticket: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value

    @field_validator("type_name", mode="before")
    def validate_type_name(cls, value: JsonValue) -> JsonValue:
        """Validate ``type_name``.

        Args:
            value (JsonValue): The raw type name.

        Returns:
            JsonValue: The type name.

        Raises:
            SEChangelogFragmentInvalidTypeName: When the value is not lower-case letters.
        """
        if not isinstance(value, str) or not cls.TYPE_PATTERN.match(value):
            raise SEChangelogFragmentInvalidTypeName(
                f"Invalid type_name: {value!r}. "  # noqa: E501
                "Must be lower-case letters, such as added."
            )
        return value

    @field_validator("lines", mode="before")
    def validate_lines(cls, value: JsonValue) -> JsonValue:
        """Validate ``lines``.

        Args:
            value (JsonValue): The raw lines.

        Returns:
            JsonValue: The lines, stripped.

        Raises:
            SEChangelogFragmentInvalidLines: When the value is not a list of one to three non-empty strings.
        """
        if (
            not isinstance(value, list)
            or not cls.LINES_MIN <= len(value) <= cls.LINES_MAX
            or not all(isinstance(line, str) and line.strip() for line in value)
        ):
            raise SEChangelogFragmentInvalidLines(
                f"Invalid lines: {value!r}. "  # noqa: E501
                f"Must be {cls.LINES_MIN} to {cls.LINES_MAX} non-empty lines."
            )
        return [line.strip() for line in value if isinstance(line, str)]

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def number(self) -> int:
        """The issue number of the ticket."""
        return int(self.ticket.removeprefix("GH-"))

    @property
    def file_name(self) -> str:
        """The fragment's file name in ``changelog.d/``."""
        return f"{self.ticket}.{self.type_name}.md"

    def starts_with(self, marker: str) -> bool:
        """Tell whether the fragment's text starts with a marker, such as the breaking change one.

        Args:
            marker (str): The marker.

        Returns:
            bool: ``True`` when the first line starts with it.
        """
        return self.lines[0].startswith(marker)
