from __future__ import annotations

import asyncio
import logging
from typing import List

import pytest

from harness_core.github.exceptions import SEGithubRequestFailedError
from harness_core.github.github_connection import GithubConnection
from harness_core.testing.github_fake import GithubFake
from release_notes.models.catalogs.github_coordinates import GithubCoordinates
from release_notes.storage.github.issue_comments import IssueComments


class TestIssueComments:
    PATH = "/repos/gpbcom/simple-erp/issues/7/comments"

    async def bodies(self, fake: GithubFake, logger: logging.Logger) -> List[str]:
        connection = GithubConnection("https://api.github.com", "2022-11-28", "secret-token", fake.transport(), logger)
        try:
            coordinates = GithubCoordinates(owner="gpbcom", repository="simple-erp")
            return await IssueComments(connection, coordinates, logger).bodies(7)
        finally:
            await connection.aclose()

    def test_every_comment_body_is_read_in_order_across_pages(self, logger: logging.Logger) -> None:
        fake = GithubFake()
        fake.paged[self.PATH] = [[{"id": 1, "body": "first"}, {"id": 2, "body": None}], [{"id": 3, "body": "third"}]]
        assert asyncio.run(self.bodies(fake, logger)) == ["first", "", "third"]
        assert fake.paths() == [self.PATH, self.PATH]

    def test_a_github_failure_is_raised(self, logger: logging.Logger) -> None:
        fake = GithubFake()
        fake.failures[self.PATH] = 502
        with pytest.raises(SEGithubRequestFailedError):
            asyncio.run(self.bodies(fake, logger))
