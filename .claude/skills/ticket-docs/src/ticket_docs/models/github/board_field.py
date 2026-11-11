from __future__ import annotations

# Standard library imports
from typing import Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.github.exceptions import SEBoardFieldInvalidId, SEBoardFieldInvalidOptions


class BoardField(BaseModel):
    """A field of the GitHub project board, such as Status.

    Attributes:
        id (str): The field's GraphQL node id.
        options (Dict[str, str]): The id of each option of a single-select field, by its name.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(description="The field's GraphQL node id.", examples=["PVTSSF_lAHOBZDE-c4Bq9-tzhpSuG0"])
    options: Dict[str, str] = Field(
        default_factory=dict,
        description="The id of each option of a single-select field, by its name.",
        examples=[{"In progress": "63440315"}],
    )

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw node id.

        Returns:
            JsonValue: The id, stripped.

        Raises:
            SEBoardFieldInvalidId: When the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise SEBoardFieldInvalidId(
                f"Invalid id: {value!r}. "  # noqa: E501
                "Must be a GraphQL node id."
            )
        return value.strip()

    @field_validator("options", mode="before")
    def validate_options(cls, value: JsonValue) -> JsonValue:
        """Validate ``options``.

        Args:
            value (JsonValue): The raw options, or ``None``.

        Returns:
            JsonValue: The options, empty for ``None``.

        Raises:
            SEBoardFieldInvalidOptions: When the value is not a mapping of non-empty names to string ids.
        """
        if value is None:
            return {}
        if not isinstance(value, dict) or not all(
            isinstance(name, str) and name.strip() and isinstance(option, str) and option.strip()
            for name, option in value.items()
        ):
            raise SEBoardFieldInvalidOptions(
                f"Invalid options: {value!r}. "  # noqa: E501
                "Must map each option name to its id, both as text."
            )
        return value
