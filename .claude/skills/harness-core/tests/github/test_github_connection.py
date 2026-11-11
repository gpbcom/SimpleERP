from __future__ import annotations

import asyncio
import logging

import httpx
import pytest
from pydantic import JsonValue

from harness_core.github.exceptions import SEGithubError, SEGithubRequestFailedError
from harness_core.github.github_connection import GithubConnection
from harness_core.testing.github_fake import GithubFake
from harness_core.testing.unreachable_github import UnreachableGithub
from tests.github.helpers import API_URL, API_VERSION, REPOSITORY_PATH


class TestGithubConnection:
    async def get(self, transport: httpx.MockTransport, path: str) -> JsonValue:
        connection = GithubConnection(API_URL, API_VERSION, "secret-token", transport)
        try:
            return await connection.get(path)
        finally:
            await connection.aclose()

    async def pages(self, transport: httpx.MockTransport, path: str, key: str) -> JsonValue:
        connection = GithubConnection(API_URL, API_VERSION, "secret-token", transport)
        try:
            return list(await connection.pages(path, {"state": "open"}, key))
        finally:
            await connection.aclose()

    def test_a_request_carries_the_api_headers(self) -> None:
        fake = GithubFake()
        fake.routes[f"{REPOSITORY_PATH}/pulls/7"] = {"number": 7}
        assert asyncio.run(self.get(fake.transport(), f"{REPOSITORY_PATH}/pulls/7")) == {"number": 7}
        headers = fake.requests[0].headers
        assert headers["Authorization"] == "Bearer secret-token"
        assert headers["Accept"] == "application/vnd.github+json"
        assert headers["X-GitHub-Api-Version"] == API_VERSION
        assert str(fake.requests[0].url).startswith(API_URL)

    def test_every_page_is_read(self) -> None:
        fake = GithubFake()
        fake.paged[f"{REPOSITORY_PATH}/pulls?state=open"] = [[{"id": 1}, {"id": 2}], [{"id": 3}]]
        items = asyncio.run(self.pages(fake.transport(), f"{REPOSITORY_PATH}/pulls", ""))
        assert items == [{"id": 1}, {"id": 2}, {"id": 3}]
        assert fake.requests[0].url.params["per_page"] == "100"

    def test_the_list_is_read_under_its_key(self) -> None:
        fake = GithubFake()
        fake.routes[f"{REPOSITORY_PATH}/commits/x/check-runs?state=open"] = {
            "total_count": 1,
            "check_runs": [{"id": 5}],
        }
        items = asyncio.run(self.pages(fake.transport(), f"{REPOSITORY_PATH}/commits/x/check-runs", "check_runs"))
        assert items == [{"id": 5}]

    def test_an_error_status_names_the_path_and_never_the_token(self, caplog: pytest.LogCaptureFixture) -> None:
        fake = GithubFake()
        fake.failures[f"{REPOSITORY_PATH}/pulls/7"] = 503
        caplog.set_level(logging.DEBUG)
        with pytest.raises(SEGithubRequestFailedError, match="503"):
            asyncio.run(self.get(fake.transport(), f"{REPOSITORY_PATH}/pulls/7"))
        assert "secret-token" not in caplog.text

    def test_an_unreachable_github_is_reported_once(self) -> None:
        unreachable = UnreachableGithub()
        with pytest.raises(SEGithubRequestFailedError, match="ConnectError"):
            asyncio.run(self.get(httpx.MockTransport(unreachable), f"{REPOSITORY_PATH}/pulls/7"))
        assert unreachable.attempts == 1

    def test_every_github_failure_shares_one_base_class(self) -> None:
        assert issubclass(SEGithubRequestFailedError, SEGithubError)
