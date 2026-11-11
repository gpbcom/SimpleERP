from __future__ import annotations

import asyncio
from typing import Dict, Iterator

import pytest
from pydantic import JsonValue

from harness_core.github.github_connection import GithubConnection
from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import CommentSource, MergeableState, PullRequestStatus, ReviewState
from pr_watch.storage.github.pull_request_reader import PullRequestReader
from tests.stand_ins.helpers import (
    API,
    HEAD_REF,
    HEAD_SHA,
    REPOSITORY,
    comment_payload,
    pull_request_payload,
    review_payload,
)


class TestPullRequestReader:
    @pytest.fixture
    def connection(self, catalog: WatchCatalog, fake: GithubFake, runner: asyncio.Runner) -> Iterator[GithubConnection]:
        connection = GithubConnection(
            catalog.github.api_url, catalog.github.api_version, "secret-token", fake.transport()
        )
        yield connection
        runner.run(connection.aclose())

    @pytest.fixture
    def reader(self, connection: GithubConnection) -> PullRequestReader:
        return PullRequestReader(connection, REPOSITORY)

    def test_an_open_pull_request_is_read(
        self, reader: PullRequestReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/pulls/7"] = pull_request_payload(mergeable="dirty")
        state = runner.run(reader.pull_request(7))
        assert state.status == PullRequestStatus.OPEN
        assert (state.branches.head_ref, state.branches.head_sha, state.branches.base_ref) == (
            HEAD_REF,
            HEAD_SHA,
            "develop",
        )
        assert state.branches.mergeable == MergeableState.DIRTY
        assert state.author == "gpbcom"
        assert state.timeline.merge_commit is None

    @pytest.mark.parametrize(
        ("state", "merged", "status"),
        [("closed", True, PullRequestStatus.MERGED), ("closed", False, PullRequestStatus.CLOSED)],
    )
    def test_a_closed_pull_request_is_merged_only_when_github_says_so(
        self,
        reader: PullRequestReader,
        fake: GithubFake,
        runner: asyncio.Runner,
        state: str,
        merged: bool,
        status: PullRequestStatus,
    ) -> None:
        fake.routes[f"{API}/pulls/7"] = pull_request_payload(state=state, merged=merged)
        read = runner.run(reader.pull_request(7))
        assert read.status == status
        assert read.timeline.closed_on is not None
        assert (read.timeline.merge_commit is not None) == merged

    def test_a_mergeable_state_not_computed_yet_reads_as_unknown(
        self, reader: PullRequestReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/pulls/7"] = pull_request_payload(mergeable=None)
        assert runner.run(reader.pull_request(7)).branches.mergeable == MergeableState.UNKNOWN

    def test_open_pull_requests_name_their_ticket(
        self, reader: PullRequestReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        by_branch = pull_request_payload()
        head: JsonValue = {"ref": "dependabot/uv/x", "sha": HEAD_SHA}
        by_body: Dict[str, JsonValue] = {**pull_request_payload(), "number": 8, "head": head}
        nothing: Dict[str, JsonValue] = {**by_body, "number": 9, "body": None}
        fake.routes[f"{API}/pulls?state=open"] = [by_branch, by_body, nothing]
        found = runner.run(reader.open_pull_requests())
        assert [(item.number, item.ticket) for item in found] == [(7, "GH-12"), (8, "GH-12"), (9, None)]

    def test_reviews_leave_out_the_ones_not_submitted(
        self, reader: PullRequestReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/pulls/7/reviews"] = [
            review_payload(1, "CHANGES_REQUESTED", body="Split it."),
            review_payload(2, "PENDING"),
            {**review_payload(3, "APPROVED"), "body": None},
        ]
        reviews = runner.run(reader.reviews(7))
        assert [(review.id, review.state, review.body) for review in reviews] == [
            (1, ReviewState.CHANGES_REQUESTED, "Split it."),
            (3, ReviewState.APPROVED, ""),
        ]

    def test_comments_come_from_the_diff_and_the_conversation(
        self, reader: PullRequestReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/pulls/7/comments"] = [comment_payload(11, "Rename this.")]
        fake.routes[f"{API}/issues/7/comments"] = [comment_payload(21, "Any news?")]
        comments = runner.run(reader.comments(7))
        assert [(comment.id, comment.source) for comment in comments] == [
            (11, CommentSource.INLINE),
            (21, CommentSource.CONVERSATION),
        ]
