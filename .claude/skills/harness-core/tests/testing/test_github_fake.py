from __future__ import annotations

import httpx

from harness_core.testing.github_fake import GithubFake


class TestGithubFake:
    def test_an_unknown_path_answers_404_as_github_does(self) -> None:
        fake = GithubFake()
        with httpx.Client(transport=fake.transport(), base_url="https://api.github.com") as client:
            response = client.get("/repos/o/r/issues/1/comments")
        assert response.status_code == 404
        assert fake.paths() == ["/repos/o/r/issues/1/comments"]

    def test_a_route_ignores_the_paging_parameters_and_sorts_the_query(self) -> None:
        fake = GithubFake()
        fake.routes["/x?a=1&b=2"] = {"ok": True}
        with httpx.Client(transport=fake.transport(), base_url="https://api.github.com") as client:
            response = client.get("/x", params={"b": "2", "a": "1", "per_page": "100", "page": "1"})
        assert response.json() == {"ok": True}

    def test_pages_are_linked_and_failures_answer_their_status(self) -> None:
        fake = GithubFake()
        fake.paged["/list"] = [[1], [2]]
        fake.failures["/broken"] = 502
        with httpx.Client(transport=fake.transport(), base_url="https://api.github.com") as client:
            first = client.get("/list")
            second = client.get(first.links["next"]["url"])
            broken = client.get("/broken")
        assert first.json() == [1]
        assert second.json() == [2]
        assert "next" not in second.links
        assert broken.status_code == 502
