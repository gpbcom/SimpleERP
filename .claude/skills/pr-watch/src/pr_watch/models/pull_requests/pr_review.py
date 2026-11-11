from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import ReviewState
from pr_watch.models.pull_requests.exceptions import (
    SEPrReviewInvalidAuthor,
    SEPrReviewInvalidBody,
    SEPrReviewInvalidId,
    SEPrReviewInvalidLink,
    SEPrReviewInvalidState,
)
from pr_watch.models.validation.field_rules import FieldRules


class PrReview(BaseModel):
    """A review of a pull request.

    Attributes:
        id (int): The review's identifier.
        state (ReviewState): What the reviewer decided.
        author (str): The reviewer's login.
        body (str): The review's text, empty when it has none.
        link (str): The review on GitHub.
    """

    model_config = ConfigDict(extra="forbid")

    id: int = Field(description="The review's identifier.", examples=[301])
    state: ReviewState = Field(description="What the reviewer decided.", examples=["CHANGES_REQUESTED"])
    author: str = Field(description="The reviewer's login.", examples=["octocat"])
    body: str = Field(
        default="", description="The review's text, empty when it has none.", examples=["Please split this method."]
    )
    link: str = Field(
        description="The review on GitHub.",
        examples=["https://github.com/gpbcom/simple-erp/pull/7#pullrequestreview-301"],
    )

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw id.

        Returns:
            JsonValue: The id.

        Raises:
            SEPrReviewInvalidId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEPrReviewInvalidId, "id")

    @field_validator("state", mode="before")
    def validate_state(cls, value: JsonValue) -> JsonValue:
        """Validate ``state``.

        Args:
            value (JsonValue): The raw state.

        Returns:
            JsonValue: The state.

        Raises:
            SEPrReviewInvalidState: When the value is not a ``ReviewState``.
        """
        return FieldRules.member(value, SEPrReviewInvalidState, "state", ReviewState)

    @field_validator("author", mode="before")
    def validate_author(cls, value: JsonValue) -> JsonValue:
        """Validate ``author``.

        Args:
            value (JsonValue): The raw author.

        Returns:
            JsonValue: The author.

        Raises:
            SEPrReviewInvalidAuthor: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPrReviewInvalidAuthor, "author")

    @field_validator("body", mode="before")
    def validate_body(cls, value: JsonValue) -> JsonValue:
        """Validate ``body``.

        Args:
            value (JsonValue): The raw body, or ``None``.

        Returns:
            JsonValue: The body, or its default.

        Raises:
            SEPrReviewInvalidBody: When the value is not a string.
        """
        if value is None:
            return cls.model_fields["body"].get_default(call_default_factory=True)
        return FieldRules.free_text(value, SEPrReviewInvalidBody, "body")

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link.

        Returns:
            JsonValue: The link.

        Raises:
            SEPrReviewInvalidLink: When the value is not an http or https link.
        """
        return FieldRules.link(value, SEPrReviewInvalidLink, "link")
