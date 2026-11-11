from __future__ import annotations

# Standard library imports
from typing import Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.github.board_field import BoardField
from ticket_docs.models.github.exceptions import (
    SEBoardProjectInvalidFields,
    SEBoardProjectInvalidNumber,
    SEBoardProjectInvalidText,
)


class BoardProject(BaseModel):
    """The GitHub project board the tickets move on.

    Attributes:
        number (int): The project's number in its owner's projects.
        url (str): Its page.
        id (str): Its GraphQL node id.
        fields (Dict[str, BoardField]): Its fields, by their lower-case name.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    number: int = Field(description="The project's number in its owner's projects.", examples=[6])
    url: str = Field(description="Its page.", examples=["https://github.com/users/gpbcom/projects/6"])
    id: str = Field(description="Its GraphQL node id.", examples=["PVT_kwHOBZDE-c4Bq9-t"])
    fields: Dict[str, BoardField] = Field(
        default_factory=dict, description="Its fields, by their lower-case name.", examples=[{"status": {"id": "x"}}]
    )

    @field_validator("number", mode="before")
    def validate_number(cls, value: JsonValue) -> JsonValue:
        """Validate ``number``.

        Args:
            value (JsonValue): The raw project number.

        Returns:
            JsonValue: The number.

        Raises:
            SEBoardProjectInvalidNumber: When the value is not a positive whole number.
        """
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise SEBoardProjectInvalidNumber(
                f"Invalid number: {value!r}. "  # noqa: E501
                "Must be a positive whole number."
            )
        return value

    @field_validator("url", "id", mode="before")
    def validate_text(cls, value: JsonValue) -> JsonValue:
        """Validate ``url`` and ``id``.

        Args:
            value (JsonValue): The raw text.

        Returns:
            JsonValue: The text, stripped.

        Raises:
            SEBoardProjectInvalidText: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEBoardProjectInvalidText(
                f"Invalid text: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("fields", mode="before")
    def validate_fields(cls, value: JsonValue) -> JsonValue:
        """Validate ``fields``.

        Args:
            value (JsonValue): The raw fields, or ``None``.

        Returns:
            JsonValue: The fields, empty for ``None``.

        Raises:
            SEBoardProjectInvalidFields: When the value is not a mapping keyed by non-empty names.
        """
        if value is None:
            return {}
        if not isinstance(value, dict) or not all(isinstance(name, str) and name.strip() for name in value):
            raise SEBoardProjectInvalidFields(
                f"Invalid fields: {value!r}. "  # noqa: E501
                "Must map each field name to its id and options."
            )
        return value
