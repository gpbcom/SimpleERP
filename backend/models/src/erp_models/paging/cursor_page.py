from __future__ import annotations

# Standard library imports
from typing import List, Optional

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.paging.exceptions import SECursorPageInvalidItems, SECursorPageInvalidNextCursor


class CursorPage[ItemT](FrozenErpModel):
    """One page of a list paged by a cursor.

    Attributes:
        items (List[ItemT]): The items of this page.
        next_cursor (Optional[str]): The opaque cursor of the next page, or None on the last page.

    Notes:
        - The cursor is opaque: its encoding belongs to the service that pages, and callers only hand it back.
        - The last page has no cursor.
    """

    items: List[ItemT] = Field(default_factory=list, description="The items of this page.")
    next_cursor: Optional[str] = Field(
        default=None, description="The opaque cursor of the next page, or None on the last page."
    )

    @field_validator("items", mode="before")
    def validate_items(cls, value: JsonValue) -> JsonValue:
        """Validate ``items``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The list, or the default when None.

        Raises:
            SECursorPageInvalidItems: When it is not a list.
        """
        if value is None:
            return cls.model_fields["items"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SECursorPageInvalidItems(
                f"Invalid items: {value!r}. "  # noqa: E501
                "Must be a list."
            )
        return value

    @field_validator("next_cursor", mode="before")
    def validate_next_cursor(cls, value: JsonValue) -> JsonValue:
        """Validate ``next_cursor``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The stripped text, or None.

        Raises:
            SECursorPageInvalidNextCursor: When it is not a non-empty text.
        """
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, str) or not value.strip():
            raise SECursorPageInvalidNextCursor(
                f"Invalid next_cursor: {value!r}. "  # noqa: E501
                "Must be a non-empty text or None."
            )
        return value.strip()

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def has_more(self) -> bool:
        """Tell whether another page follows.

        Returns:
            bool: True when ``next_cursor`` is set.
        """
        return self.next_cursor is not None
