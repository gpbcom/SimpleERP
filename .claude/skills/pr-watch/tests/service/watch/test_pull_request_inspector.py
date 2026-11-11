from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Iterator

import pytest

from harness_core.github.github_connection import GithubConnection
from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import ChecksStatus, EventKind, PullRequestStatus
from pr_watch.models.state.watch_state import WatchState
from pr_watch.models.watch.ticket_watch import TicketWatch
from pr_watch.service.watch.event_detector import EventDetector
from pr_watch.service.watch.pull_request_inspector import PullRequestInspector
from tests.stand_ins.git_sandbox import GitSandbox
from tests.stand_ins.helpers import (
    API,
    NOW,
    a_watch,
    check_run_payload,
    comment_payload,
    open_pull_request_routes,
    pull_request_payload,
    review_payload,
)


class TestPullRequestInspector:
    @pytest.fixture
    def connection(self, catalog: WatchCatalog, fake: GithubFake, runner: asyncio.Runner) -> Iterator[GithubConnection]:
        connection = GithubConnection(
            catalog.github.api_url, catalog.github.api_version, "secret-token", fake.transport()
        )
        yield connection
        runner.run(connection.aclose())

    @pytest.fixture
    def inspector(self, connection: GithubConnection, catalog: WatchCatalog) -> PullRequestInspector:
        return PullRequestInspector(connection, EventDetector(catalog.github, catalog.timing), catalog.github)

    @pytest.fixture
    def watch(self, tmp_path: Path) -> TicketWatch:
        return a_watch(GitSandbox(tmp_path).build(conflict=True))

    def test_an_open_pull_request_gives_its_events_and_its_snapshot(
        self, inspector: PullRequestInspector, watch: TicketWatch, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes.update(
            open_pull_request_routes(
                checks=[check_run_payload(1, "unit", "failure")],
                reviews=[review_payload(5, "CHANGES_REQUESTED", body="Split it.")],
            )
        )
        state = WatchState()
        pull_request, events = runner.run(inspector.inspect(watch, state, NOW))
        assert pull_request.status == PullRequestStatus.OPEN
        assert sorted(event.kind for event in events) == sorted(
            [EventKind.REBASE_CONFLICT, EventKind.CHECKS_FAILED, EventKind.CHANGES_REQUESTED]
        )
        snapshot = state.snapshots[watch.id]
        assert snapshot.ci.checks == ChecksStatus.FAILED
        assert snapshot.rebase is not None
        assert snapshot.rebase.conflict_files == ["a.txt"]

    def test_the_first_read_of_comments_only_sets_the_cursors(
        self, inspector: PullRequestInspector, watch: TicketWatch, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes.update(open_pull_request_routes(comments=[comment_payload(11, "Old remark.")]))
        state = WatchState()
        _, first = runner.run(inspector.inspect(watch, state, NOW))
        assert EventKind.REVIEW_COMMENTS not in {event.kind for event in first}
        assert state.cursors[f"{watch.id}|inline"] == 11
        comments = [comment_payload(11, "Old remark."), comment_payload(12, "New remark.")]
        reviews = [review_payload(3, "COMMENTED", body="Overall fine.")]
        fake.routes.update(open_pull_request_routes(comments=comments, reviews=reviews))
        _, second = runner.run(inspector.inspect(watch, state, NOW))
        ids = sorted(event.id for event in second if event.kind == EventKind.REVIEW_COMMENTS)
        assert ids == [f"{watch.id}|comment:inline:12", f"{watch.id}|comment:review:3"]

    def test_a_merged_pull_request_has_no_event(
        self, inspector: PullRequestInspector, watch: TicketWatch, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/pulls/7"] = pull_request_payload(state="closed", merged=True)
        state = WatchState()
        pull_request, events = runner.run(inspector.inspect(watch, state, NOW))
        assert (pull_request.status, events, state.snapshots) == (PullRequestStatus.MERGED, [], {})
