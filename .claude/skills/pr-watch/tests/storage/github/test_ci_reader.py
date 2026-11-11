from __future__ import annotations

import asyncio
from datetime import datetime
from typing import Iterator

import pytest

from harness_core.github.github_connection import GithubConnection
from harness_core.testing.github_fake import GithubFake
from pr_watch.models.configuration.watch_catalog import WatchCatalog
from pr_watch.models.enums import CheckConclusion, DeploymentState
from pr_watch.storage.github.ci_reader import CiReader
from tests.stand_ins.helpers import (
    API,
    HEAD_REF,
    HEAD_SHA,
    REPOSITORY,
    check_run_payload,
    deployment_routes,
    workflow_run_payload,
)


class TestCiReader:
    @pytest.fixture
    def connection(self, catalog: WatchCatalog, fake: GithubFake, runner: asyncio.Runner) -> Iterator[GithubConnection]:
        connection = GithubConnection(
            catalog.github.api_url, catalog.github.api_version, "secret-token", fake.transport()
        )
        yield connection
        runner.run(connection.aclose())

    @pytest.fixture
    def reader(self, connection: GithubConnection) -> CiReader:
        return CiReader(connection, REPOSITORY)

    def test_check_runs_are_read_with_their_suite(
        self, reader: CiReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/commits/{HEAD_SHA}/check-runs"] = {
            "total_count": 2,
            "check_runs": [check_run_payload(1, "unit", "failure", suite=5), check_run_payload(2, "lint", None)],
        }
        runs = runner.run(reader.check_runs(HEAD_SHA))
        assert [(run.name, run.conclusion, run.suite_id) for run in runs] == [
            ("unit", CheckConclusion.FAILURE, 5),
            ("lint", None, 77),
        ]

    def test_workflow_runs_are_named_by_their_file(
        self, reader: CiReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/actions/runs?branch={HEAD_REF}&head_sha={HEAD_SHA}"] = {
            "workflow_runs": [workflow_run_payload(9, "stage.yml", "failure")]
        }
        runs = runner.run(reader.workflow_runs(HEAD_REF, HEAD_SHA))
        assert [(run.id, run.workflow, run.conclusion) for run in runs] == [(9, "stage.yml", CheckConclusion.FAILURE)]

    def test_the_latest_status_of_each_stage_is_read(
        self, reader: CiReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes.update(deployment_routes("dev", 31, "success"))
        fake.routes[f"{API}/deployments?environment=qa&sha={HEAD_SHA}"] = []
        deployments = runner.run(reader.deployments(HEAD_SHA, ["dev", "qa"]))
        assert [(item.environment, item.deployment_id, item.state) for item in deployments] == [
            ("dev", 31, DeploymentState.SUCCESS)
        ]
        assert deployments[0].link is not None

    def test_a_deployment_without_status_has_no_state(
        self, reader: CiReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/deployments?environment=dev&sha={HEAD_SHA}"] = [{"id": 32}]
        fake.routes[f"{API}/deployments/32/statuses"] = []
        assert runner.run(reader.deployments(HEAD_SHA, ["dev"]))[0].state is None

    def test_pending_approvals_wait_since_their_timer_or_their_run(
        self, reader: CiReader, fake: GithubFake, runner: asyncio.Runner
    ) -> None:
        fake.routes[f"{API}/actions/runs?head_sha={HEAD_SHA}&status=waiting"] = {
            "workflow_runs": [workflow_run_payload(41, "stage.yml", None, status="waiting")]
        }
        fake.routes[f"{API}/actions/runs/41/pending_deployments"] = [
            {"environment": {"name": "qa"}, "wait_timer_started_at": "2026-11-10T07:00:00Z"},
            {"environment": {"name": "dev"}, "wait_timer_started_at": None},
        ]
        approvals = runner.run(reader.pending_approvals(HEAD_SHA))
        assert [(item.run_id, item.environment, item.waiting_since) for item in approvals] == [
            (41, "qa", datetime.fromisoformat("2026-11-10T07:00:00+00:00")),
            (41, "dev", datetime.fromisoformat("2026-11-10T08:00:00+00:00")),
        ]
