from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict, Field, JsonValue, field_validator

# First-party imports
from pr_watch.models.enums import CommentSource
from pr_watch.models.pull_requests.exceptions import (
    SEPrCommentInvalidAuthor,
    SEPrCommentInvalidBody,
    SEPrCommentInvalidId,
    SEPrCommentInvalidLink,
    SEPrCommentInvalidSource,
)
from pr_watch.models.validation.field_rules import FieldRules


class PrComment(BaseModel):
    """A comment on a pull request: on a line of its diff, in its conversation, or the text of a review.

    Attributes:
        id (int): The comment's identifier.
        source (CommentSource): Where the comment was written.
        author (str): The author's login.
        body (str): The comment's text.
        link (str): The comment on GitHub.
    """

    model_config = ConfigDict(extra="forbid")

    id: int = Field(description="The comment's identifier.", examples=[9001])
    source: CommentSource = Field(description="Where the comment was written.", examples=["inline"])
    author: str = Field(description="The author's login.", examples=["octocat"])
    body: str = Field(description="The comment's text.", examples=["This name is misleading."])
    link: str = Field(
        description="The comment on GitHub.", examples=["https://github.com/gpbcom/simple-erp/pull/7#discussion_r9001"]
    )

    @field_validator("id", mode="before")
    def validate_id(cls, value: JsonValue) -> JsonValue:
        """Validate ``id``.

        Args:
            value (JsonValue): The raw id.

        Returns:
            JsonValue: The id.

        Raises:
            SEPrCommentInvalidId: When the value is not a positive integer.
        """
        return FieldRules.identifier(value, SEPrCommentInvalidId, "id")

    @field_validator("source", mode="before")
    def validate_source(cls, value: JsonValue) -> JsonValue:
        """Validate ``source``.

        Args:
            value (JsonValue): The raw source.

        Returns:
            JsonValue: The source.

        Raises:
            SEPrCommentInvalidSource: When the value is not a ``CommentSource``.
        """
        return FieldRules.member(value, SEPrCommentInvalidSource, "source", CommentSource)

    @field_validator("author", mode="before")
    def validate_author(cls, value: JsonValue) -> JsonValue:
        """Validate ``author``.

        Args:
            value (JsonValue): The raw author.

        Returns:
            JsonValue: The author.

        Raises:
            SEPrCommentInvalidAuthor: When the value is not a non-empty string.
        """
        return FieldRules.text(value, SEPrCommentInvalidAuthor, "author")

    @field_validator("body", mode="before")
    def validate_body(cls, value: JsonValue) -> JsonValue:
        """Validate ``body``.

        Args:
            value (JsonValue): The raw body.

        Returns:
            JsonValue: The body.

        Raises:
            SEPrCommentInvalidBody: When the value is not a string.
        """
        return FieldRules.free_text(value, SEPrCommentInvalidBody, "body")

    @field_validator("link", mode="before")
    def validate_link(cls, value: JsonValue) -> JsonValue:
        """Validate ``link``.

        Args:
            value (JsonValue): The raw link.

        Returns:
            JsonValue: The link.

        Raises:
            SEPrCommentInvalidLink: When the value is not an http or https link.
        """
        return FieldRules.link(value, SEPrCommentInvalidLink, "link")
