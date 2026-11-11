from __future__ import annotations

# Standard library imports
import re
from datetime import datetime
from enum import StrEnum
from pathlib import Path
from typing import ClassVar, Tuple

# Third-party imports
from pydantic import BaseModel, JsonValue


class FieldRules:
    """The checks that the models' field validators share.

    Attributes:
        TICKET_PATTERN (re.Pattern[str]): A ticket key, ``GH-<issue number>``.
        SLUG_PATTERN (re.Pattern[str]): A GitHub repository, ``<owner>/<name>``.
        LINK_PREFIXES (Tuple[str, ...]): The schemes a link may start with.

    Notes:
        - Each validator keeps its own exception and passes it here, so that the error still names the model and the
          field while the rule itself is written once.
        - A nested model, a time or a path is handed back in its JSON form, so that Pydantic converts it the same way
          whether the value came from Python or from a file.
    """

    TICKET_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^GH-\d+$")
    SLUG_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"^[\w.-]+/[\w.-]+$")
    LINK_PREFIXES: ClassVar[Tuple[str, ...]] = ("https://", "http://")

    def __init__(self) -> None:
        """Declare the constructor of a class that only holds class methods."""

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def text(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a non-empty string.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The string, stripped.

        Raises:
            Exception: The field's exception, when the value is not a non-empty string.
        """
        if not isinstance(value, str) or not value.strip():
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @classmethod
    def free_text(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a string that may be empty.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The string, as it is.

        Raises:
            Exception: The field's exception, when the value is not a string.
        """
        if not isinstance(value, str):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a string."
            )
        return value

    @classmethod
    def ticket(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a ticket key.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The key, stripped.

        Raises:
            Exception: The field's exception, when the value is not ``GH-<n>``.
        """
        if not isinstance(value, str) or not cls.TICKET_PATTERN.match(value.strip()):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must look like GH-12."
            )
        return value.strip()

    @classmethod
    def slug(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a GitHub repository name.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The name, stripped.

        Raises:
            Exception: The field's exception, when the value is not ``<owner>/<name>``.
        """
        if not isinstance(value, str) or not cls.SLUG_PATTERN.match(value.strip()):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must look like gpbcom/simple-erp."
            )
        return value.strip()

    @classmethod
    def link(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a web link.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The link, stripped.

        Raises:
            Exception: The field's exception, when the value is not an ``http`` or ``https`` link.
        """
        if not isinstance(value, str) or not value.strip().startswith(cls.LINK_PREFIXES):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an http or https link."
            )
        return value.strip()

    @classmethod
    def integer(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a whole number that is zero or more.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The number.

        Raises:
            Exception: The field's exception, when the value is not an integer of zero or more.
        """
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be an integer of zero or more."
            )
        return value

    @classmethod
    def identifier(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a positive whole number, such as an identifier or a count of minutes.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The number.

        Raises:
            Exception: The field's exception, when the value is not a positive integer.
        """
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a positive integer."
            )
        return value

    @classmethod
    def amount(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a number that is zero or more, such as an amount in USD.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The number.

        Raises:
            Exception: The field's exception, when the value is not a number of zero or more.
        """
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0:
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a number of zero or more."
            )
        return value

    @classmethod
    def flag(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a boolean.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The boolean.

        Raises:
            Exception: The field's exception, when the value is not a boolean.
        """
        if not isinstance(value, bool):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a boolean."
            )
        return value

    @classmethod
    def moment(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a time that carries its time zone.

        Args:
            value (JsonValue): The raw value, a ``datetime`` or an ISO 8601 string.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The time as an ISO 8601 string.

        Raises:
            Exception: The field's exception, when the value is not a time with its time zone.
        """
        moment = value if isinstance(value, datetime) else None
        if isinstance(value, str):
            try:
                moment = datetime.fromisoformat(value.strip())
            except ValueError as error_found:
                raise error(
                    f"Invalid {field}: {value!r}. "  # noqa: E501
                    "Must be an ISO 8601 time."
                ) from error_found
        if moment is None or moment.tzinfo is None:
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a time with its time zone."
            )
        return moment.isoformat()

    @classmethod
    def path(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a file system path.

        Args:
            value (JsonValue): The raw value, a ``Path`` or a non-empty string.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The path as a string.

        Raises:
            Exception: The field's exception, when the value is neither a path nor a non-empty string.
        """
        if isinstance(value, Path):
            return str(value)
        if not isinstance(value, str) or not value.strip():
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a path."
            )
        return value.strip()

    @classmethod
    def member(cls, value: JsonValue, error: type[Exception], field: str, enum: type[StrEnum]) -> JsonValue:
        """Check a value of a fixed set.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.
            enum (type[StrEnum]): The set of values.

        Returns:
            JsonValue: The value.

        Raises:
            Exception: The field's exception, when the value is not one of the set.
        """
        allowed = [member.value for member in enum]
        if not isinstance(value, str) or value not in allowed:
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                f"Must be one of {allowed}."
            )
        return value

    @classmethod
    def nested(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a nested model.

        Args:
            value (JsonValue): The raw value, a model or a mapping of its fields.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The fields of the nested model.

        Raises:
            Exception: The field's exception, when the value is neither a model nor a mapping.
        """
        if isinstance(value, BaseModel):
            dumped: JsonValue = value.model_dump(mode="json")
            return dumped
        if not isinstance(value, dict):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a mapping of the nested model's fields."
            )
        return value

    @classmethod
    def mapping(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a mapping keyed by strings.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The mapping.

        Raises:
            Exception: The field's exception, when the value is not a mapping keyed by strings.
        """
        if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a mapping keyed by strings."
            )
        return value

    @classmethod
    def sequence(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a list.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The list.

        Raises:
            Exception: The field's exception, when the value is not a list.
        """
        if not isinstance(value, list):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a list."
            )
        return value

    @classmethod
    def texts(cls, value: JsonValue, error: type[Exception], field: str) -> JsonValue:
        """Check a list of non-empty strings.

        Args:
            value (JsonValue): The raw value.
            error (type[Exception]): The field's own exception.
            field (str): The field's name.

        Returns:
            JsonValue: The strings, stripped.

        Raises:
            Exception: The field's exception, when the value is not a list of non-empty strings.
        """
        if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
            raise error(
                f"Invalid {field}: {value!r}. "  # noqa: E501
                "Must be a list of non-empty strings."
            )
        return [str(item).strip() for item in value]
