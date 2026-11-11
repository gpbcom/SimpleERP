from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from ticket_docs.models.evidence.exceptions import SERunCountsInvalidCount


class RunCounts(BaseModel):
    """The test counts of a run's report.

    Attributes:
        tests (int): How many tests ran.
        failures (int): How many failed an assertion.
        errors (int): How many could not run, such as a collection error.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    tests: int = Field(default=0, description="How many tests ran.", examples=[12])
    failures: int = Field(default=0, description="How many failed an assertion.", examples=[1])
    errors: int = Field(default=0, description="How many could not run, such as a collection error.", examples=[0])

    @field_validator("tests", "failures", "errors", mode="before")
    def validate_count(cls, value: JsonValue) -> JsonValue:
        """Validate ``tests``, ``failures`` and ``errors``.

        Args:
            value (JsonValue): The raw count, or ``None``.

        Returns:
            JsonValue: The count, ``0`` for ``None``.

        Raises:
            SERunCountsInvalidCount: When the value is not a whole number of zero or more.
        """
        if value is None:
            return 0
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SERunCountsInvalidCount(
                f"Invalid count: {value!r}. "  # noqa: E501
                "Must be a whole number of zero or more."
            )
        return value

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def passed(self) -> int:
        """How many tests passed, never below zero."""
        return max(self.tests - self.failures - self.errors, 0)
