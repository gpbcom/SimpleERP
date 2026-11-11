from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# Third-party imports
from pydantic import JsonValue

from harness_core.github.github_connection import GithubConnection
from harness_core.github.json_payload import JsonPayload

# First-party imports
from harness_core.models.branches.branch_name import BranchName
from harness_core.models.branches.exceptions import SEInvalidBranchNameException
from pr_watch.models.enums import CommentSource, MergeableState, PullRequestStatus, ReviewState
from pr_watch.models.pull_requests.pr_comment import PrComment
from pr_watch.models.pull_requests.pr_review import PrReview
from pr_watch.models.pull_requests.pull_request_branches import PullRequestBranches
from pr_watch.models.pull_requests.pull_request_state import PullRequestState
from pr_watch.models.pull_requests.pull_request_timeline import PullRequestTimeline
from pr_watch.models.state.unwatched_pull_request import UnwatchedPullRequest


class PullRequestReader:
    """Reads the pull requests of one GitHub repository: their state, reviews and comments.

    Attributes:
        CLOSES_PATTERN (re.Pattern[str]): A ``Closes #<n>`` line, and its kin, in a pull request's description.
        connection (GithubConnection): The HTTP client.
        repository (str): The repository, ``<owner>/<name>``.
        logger (Logger): Logger instance.

    Notes:
        - GitHub says ``closed`` for a merged pull request too, so ``merged`` decides between the two.
        - A ``mergeable_state`` GitHub has not computed yet, or one this tool does not know, reads as ``unknown``.
    """

    CLOSES_PATTERN: ClassVar[re.Pattern[str]] = re.compile(r"\b(?:closes|fixes|resolves)\s+#(\d+)\b", re.IGNORECASE)

    def __init__(self, connection: GithubConnection, repository: str, logger: Optional[Logger] = None) -> None:
        """Set the repository.

        Args:
            connection (GithubConnection): The HTTP client.
            repository (str): The repository, ``<owner>/<name>``.
            logger (Optional[Logger]): Logger instance.
        """
        self.connection = connection
        self.repository = repository
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _status(self, data: Dict[str, JsonValue]) -> PullRequestStatus:
        """Tell where a pull request stands.

        Args:
            data (Dict[str, JsonValue]): The pull request as GitHub describes it.

        Returns:
            PullRequestStatus: Merged, closed without merge, or open.
        """
        if data.get("merged") is True or JsonPayload.text(data, "merged_at"):
            return PullRequestStatus.MERGED
        if JsonPayload.text(data, "state") == PullRequestStatus.CLOSED:
            return PullRequestStatus.CLOSED
        return PullRequestStatus.OPEN

    def _mergeable(self, data: Dict[str, JsonValue]) -> MergeableState:
        """Read what GitHub says of merging a pull request.

        Args:
            data (Dict[str, JsonValue]): The pull request as GitHub describes it.

        Returns:
            MergeableState: The state, ``unknown`` when GitHub gives none this tool knows.
        """
        value = JsonPayload.text(data, "mergeable_state")
        return MergeableState(value) if value in {state.value for state in MergeableState} else MergeableState.UNKNOWN

    def _ticket(self, data: Dict[str, JsonValue]) -> Optional[str]:
        """Find the ticket a pull request names.

        Args:
            data (Dict[str, JsonValue]): The pull request as GitHub describes it.

        Returns:
            Optional[str]: ``GH-<n>`` from its head branch, else from a ``Closes #<n>`` line, else ``None``.
        """
        try:
            ticket = BranchName.parse(JsonPayload.text(JsonPayload.child(data, "head"), "ref") or "-").ticket
        except SEInvalidBranchNameException:
            ticket = None
        if ticket is None:
            closes = self.CLOSES_PATTERN.search(JsonPayload.text(data, "body"))
            ticket = f"GH-{closes.group(1)}" if closes else None
        return ticket

    def _comment(self, data: Dict[str, JsonValue], source: CommentSource) -> PrComment:
        """Build a comment from GitHub's description of it.

        Args:
            data (Dict[str, JsonValue]): The comment.
            source (CommentSource): Where it was written.

        Returns:
            PrComment: The comment.
        """
        return PrComment(
            id=data.get("id"),
            source=source,
            author=JsonPayload.text(JsonPayload.child(data, "user"), "login"),
            body=JsonPayload.text(data, "body"),
            link=data.get("html_url"),
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    async def pull_request(self, number: int) -> PullRequestState:
        """Read a pull request.

        Args:
            number (int): Its number.

        Returns:
            PullRequestState: What GitHub says of it now.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        payload = await self.connection.get(f"/repos/{self.repository}/pulls/{number}")
        data = payload if isinstance(payload, dict) else {}
        head = JsonPayload.child(data, "head")
        state = PullRequestState(
            title=data.get("title"),
            status=self._status(data),
            author=JsonPayload.text(JsonPayload.child(data, "user"), "login"),
            branches=PullRequestBranches(
                head_ref=head.get("ref"),
                head_sha=head.get("sha"),
                base_ref=JsonPayload.child(data, "base").get("ref"),
                mergeable=self._mergeable(data),
            ),
            timeline=PullRequestTimeline(
                opened_on=data.get("created_at"),
                closed_on=data.get("closed_at"),
                merge_commit=data.get("merge_commit_sha") if self._status(data) == PullRequestStatus.MERGED else None,
            ),
        )
        self.logger.debug("%s#%d is %s.", self.repository, number, state.status.value)
        return state

    async def open_pull_requests(self) -> List[UnwatchedPullRequest]:
        """List the repository's open pull requests.

        Returns:
            List[UnwatchedPullRequest]: Each one, with the ticket it names when it names one.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items = await self.connection.pages(f"/repos/{self.repository}/pulls", {"state": PullRequestStatus.OPEN.value})
        pull_requests = [
            UnwatchedPullRequest(
                repository=self.repository,
                number=item.get("number"),
                title=item.get("title"),
                ticket=self._ticket(item),
                updated_on=item.get("updated_at"),
            )
            for item in items
        ]
        self.logger.debug("%s has %d open pull requests.", self.repository, len(pull_requests))
        return pull_requests

    async def reviews(self, number: int) -> List[PrReview]:
        """List the submitted reviews of a pull request.

        Args:
            number (int): Its number.

        Returns:
            List[PrReview]: Each review, oldest first, leaving out the ones not submitted yet.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items = await self.connection.pages(f"/repos/{self.repository}/pulls/{number}/reviews")
        known = {state.value for state in ReviewState}
        reviews = [
            PrReview(
                id=item.get("id"),
                state=item.get("state"),
                author=JsonPayload.text(JsonPayload.child(item, "user"), "login"),
                body=JsonPayload.text(item, "body"),
                link=item.get("html_url"),
            )
            for item in items
            if JsonPayload.text(item, "state") in known and JsonPayload.text(item, "state") != ReviewState.PENDING
        ]
        self.logger.debug("%s#%d has %d reviews.", self.repository, number, len(reviews))
        return reviews

    async def comments(self, number: int) -> List[PrComment]:
        """List the comments of a pull request: on lines of its diff, and in its conversation.

        Args:
            number (int): Its number.

        Returns:
            List[PrComment]: The line comments, then the conversation comments, each oldest first.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        inline = await self.connection.pages(f"/repos/{self.repository}/pulls/{number}/comments")
        conversation = await self.connection.pages(f"/repos/{self.repository}/issues/{number}/comments")
        comments = [self._comment(item, CommentSource.INLINE) for item in inline]
        comments += [self._comment(item, CommentSource.CONVERSATION) for item in conversation]
        self.logger.debug("%s#%d has %d comments.", self.repository, number, len(comments))
        return comments
