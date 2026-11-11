from __future__ import annotations

# Standard library imports
from typing import ClassVar, List

# Third-party imports
from pydantic import Field, JsonValue, field_validator

# First-party imports
from ai_cost.models.commands.exceptions import (
    SEPaidCommandCatalogInvalidPaidCommands,
    SEPaidCommandCatalogUnreadable,
)
from ai_cost.models.commands.paid_command import PaidCommand
from harness_core.models.catalogs.yaml_catalog import YamlCatalog


class PaidCommandCatalog(YamlCatalog):
    """The shell commands that call a paid AI, read from ``conf/paid-commands.yaml``.

    Attributes:
        UNREADABLE (type[Exception]): Raised when the file cannot be read.
        paid_commands (List[PaidCommand]): Each paid command.
    """

    UNREADABLE: ClassVar[type[Exception]] = SEPaidCommandCatalogUnreadable

    paid_commands: List[PaidCommand] = Field(default_factory=list, description="Each paid command.", examples=[[]])

    @field_validator("paid_commands", mode="before")
    def validate_paid_commands(cls, value: JsonValue) -> JsonValue:
        """Validate ``paid_commands``.

        Args:
            value (JsonValue): The raw commands.

        Returns:
            JsonValue: The commands, or the default for ``None``.

        Raises:
            SEPaidCommandCatalogInvalidPaidCommands: When the value is not a list.
        """
        if value is None:
            return []
        if not isinstance(value, list):
            raise SEPaidCommandCatalogInvalidPaidCommands(
                f"Invalid paid_commands: {value!r}. "  # noqa: E501
                "Must be a list of commands."
            )
        return value
