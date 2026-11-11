from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class CommentSource(StrEnum):
    """Where a comment on a pull request was written.

    Attributes:
        REVIEW: The text of a review.
        INLINE: A comment on a line of the diff.
        CONVERSATION: A comment in the pull request's conversation.
    """

    REVIEW = "review"
    INLINE = "inline"
    CONVERSATION = "conversation"
