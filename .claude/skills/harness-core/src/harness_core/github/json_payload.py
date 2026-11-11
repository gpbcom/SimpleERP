from __future__ import annotations

# Standard library imports
from typing import Dict, List

# Third-party imports
from pydantic import JsonValue


class JsonPayload:
    """Walks the JSON that GitHub answers with.

    Notes:
        A missing or mistyped part becomes an empty object or list, so that the model built from it reports the
        field that is wrong rather than a ``KeyError``.
    """

    def __init__(self) -> None:
        """Declare the constructor of a class that only holds class methods."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def child(cls, value: JsonValue, key: str) -> Dict[str, JsonValue]:
        """Give the object under a key.

        Args:
            value (JsonValue): An object.
            key (str): The key.

        Returns:
            Dict[str, JsonValue]: The object under the key, empty when there is none.
        """
        found = value.get(key) if isinstance(value, dict) else None
        return found if isinstance(found, dict) else {}

    @classmethod
    def objects(cls, value: JsonValue) -> List[Dict[str, JsonValue]]:
        """Give the objects of a list.

        Args:
            value (JsonValue): A list.

        Returns:
            List[Dict[str, JsonValue]]: Its objects, leaving out anything else.
        """
        return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []

    @classmethod
    def text(cls, value: JsonValue, key: str) -> str:
        """Give the string under a key.

        Args:
            value (JsonValue): An object.
            key (str): The key.

        Returns:
            str: The string, empty when the key is missing, ``null`` or not a string.
        """
        found = value.get(key) if isinstance(value, dict) else None
        return found if isinstance(found, str) else ""
