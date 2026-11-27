from __future__ import annotations

# Standard library imports
from typing import ClassVar, List

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.postgres.exceptions import (
    SEPostgresServerConfigInvalidDatabase,
    SEPostgresServerConfigInvalidSearchDirs,
    SEPostgresServerConfigInvalidStartTimeoutS,
    SEPostgresServerConfigInvalidUser,
)


class PostgresServerConfig(BaseModel):
    """The settings of the PostgreSQL test server.

    Attributes:
        model_config (ConfigDict): Refuses unknown keys and validates defaults.
        START_TIMEOUT_S_MIN (float): The shortest start timeout, in seconds.
        START_TIMEOUT_S_MAX (float): The longest start timeout, in seconds.
        search_dirs (List[str]): The folders searched for the PostgreSQL server binaries.
        database (str): The name of the database created for the tests.
        user (str): The name of the superuser of the test server.
        start_timeout_s (float): How long to wait for the server to accept connections, in seconds.
    """

    model_config = ConfigDict(extra="forbid", validate_default=True)

    START_TIMEOUT_S_MIN: ClassVar[float] = 0.1
    START_TIMEOUT_S_MAX: ClassVar[float] = 300.0

    search_dirs: List[str] = Field(
        default=["/usr/lib/postgresql"], description="The folders searched for the PostgreSQL server binaries."
    )
    database: str = Field(default="erp_test", description="The name of the database created for the tests.")
    user: str = Field(default="erp_test", description="The name of the superuser of the test server.")
    start_timeout_s: float = Field(
        default=30.0, description="How long to wait for the server to accept connections, in seconds."
    )

    @field_validator("search_dirs", mode="before")
    def validate_search_dirs(cls, value: JsonValue) -> JsonValue:
        """Validate ``search_dirs``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The folders, stripped, or the default when ``None``.

        Raises:
            SEPostgresServerConfigInvalidSearchDirs: If it is not a list of non-empty strings.
        """
        if value is None:
            return cls.model_fields["search_dirs"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SEPostgresServerConfigInvalidSearchDirs(
                f"Invalid search_dirs: {value!r}. "  # noqa: E501
                "Must be a list of non-empty strings."
            )
        folders: List[JsonValue] = []
        for item in value:
            if not isinstance(item, str) or not item.strip():
                raise SEPostgresServerConfigInvalidSearchDirs(
                    f"Invalid search_dirs: {value!r}. "  # noqa: E501
                    "Must be a list of non-empty strings."
                )
            folders.append(item.strip())
        return folders

    @field_validator("database", mode="before")
    def validate_database(cls, value: JsonValue) -> JsonValue:
        """Validate ``database``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The name, stripped, or the default when ``None``.

        Raises:
            SEPostgresServerConfigInvalidDatabase: If it is not a non-empty string.
        """
        if value is None:
            return cls.model_fields["database"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEPostgresServerConfigInvalidDatabase(
                f"Invalid database: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("user", mode="before")
    def validate_user(cls, value: JsonValue) -> JsonValue:
        """Validate ``user``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The name, stripped, or the default when ``None``.

        Raises:
            SEPostgresServerConfigInvalidUser: If it is not a non-empty string.
        """
        if value is None:
            return cls.model_fields["user"].get_default(call_default_factory=True)
        if not isinstance(value, str) or not value.strip():
            raise SEPostgresServerConfigInvalidUser(
                f"Invalid user: {value!r}. "  # noqa: E501
                "Must be a non-empty string."
            )
        return value.strip()

    @field_validator("start_timeout_s", mode="before")
    def validate_start_timeout_s(cls, value: JsonValue) -> JsonValue:
        """Validate ``start_timeout_s``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The timeout, or the default when ``None``.

        Raises:
            SEPostgresServerConfigInvalidStartTimeoutS: If it is not a number within the bounds.
        """
        if value is None:
            return cls.model_fields["start_timeout_s"].get_default(call_default_factory=True)
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not cls.START_TIMEOUT_S_MIN <= value <= cls.START_TIMEOUT_S_MAX
        ):
            raise SEPostgresServerConfigInvalidStartTimeoutS(
                f"Invalid start_timeout_s: {value!r}. "  # noqa: E501
                f"Must be in [{cls.START_TIMEOUT_S_MIN}, {cls.START_TIMEOUT_S_MAX}]."
            )
        return float(value)
