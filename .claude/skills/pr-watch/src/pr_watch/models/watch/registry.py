from __future__ import annotations

# Standard library imports
from typing import Dict

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.exceptions import (
    SERegistryInvalidPullRequests,
)
from pr_watch.models.watch.ticket_watch import TicketWatch


class Registry(BaseModel):
    """Every pull request the watcher knows, open or closed.

    Attributes:
        pull_requests (Dict[str, TicketWatch]): Each watch, by its identifier.
    """

    model_config = ConfigDict(extra="forbid")

    pull_requests: Dict[str, TicketWatch] = Field(
        default_factory=dict, description="Each watch, by its identifier.", examples=[{}]
    )

    @field_validator("pull_requests", mode="before")
    def validate_pull_requests(cls, value: JsonValue) -> JsonValue:
        """Validate ``pull_requests``.

        Args:
            value (JsonValue): The raw pull requests, or ``None``.

        Returns:
            JsonValue: The pull requests, or its default.

        Raises:
            SERegistryInvalidPullRequests: When the value is not a mapping keyed by strings.
        """
        if value is None:
            return cls.model_fields["pull_requests"].get_default(call_default_factory=True)
        return FieldRules.mapping(value, SERegistryInvalidPullRequests, "pull_requests")
