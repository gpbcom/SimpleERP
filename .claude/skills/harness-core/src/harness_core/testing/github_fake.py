from __future__ import annotations

# Standard library imports
from typing import Dict, List

# Third-party imports
import httpx
from pydantic import JsonValue


class GithubFake:
    """GitHub's REST API as an ``httpx.MockTransport`` handler: the answers a test sets, in GitHub's JSON shapes.

    Attributes:
        routes (Dict[str, JsonValue]): The answer of each route.
        paged (Dict[str, List[JsonValue]]): The pages of each route that answers in several pages.
        failures (Dict[str, int]): The error status of each route that fails.
        requests (List[httpx.Request]): Every request received, in order.

    Notes:
        - A route is a path plus its query without ``per_page`` and ``page``, its parameters sorted:
          ``/repos/o/r/deployments?environment=qa&sha=abc``.
        - A route with several pages answers with GitHub's ``Link`` header. Any other path answers 404 as GitHub
          does.
        - It lives in ``src`` so that every harness tool tests its GitHub calls against the same stand-in, and it
          stays silent because it answers every request.
    """

    def __init__(self) -> None:
        """Start with no route, no failure and no request."""
        self.routes: Dict[str, JsonValue] = {}
        self.paged: Dict[str, List[JsonValue]] = {}
        self.failures: Dict[str, int] = {}
        self.requests: List[httpx.Request] = []

    ############################
    # Publicly Exposed Methods #
    ############################

    def __call__(self, request: httpx.Request) -> httpx.Response:
        """Answer one request.

        Args:
            request (httpx.Request): The request.

        Returns:
            httpx.Response: The failure, the page, the answer or a 404, in that order of precedence.
        """
        self.requests.append(request)
        route = self.route(request)
        if route in self.failures:
            return httpx.Response(self.failures[route], json={"message": "Server Error"})
        if route in self.paged:
            pages = self.paged[route]
            number = int(request.url.params.get("page", "1"))
            headers = {}
            if number < len(pages):
                headers["Link"] = f'<{request.url.copy_set_param("page", str(number + 1))}>; rel="next"'
            return httpx.Response(200, json=pages[number - 1], headers=headers)
        if route in self.routes:
            return httpx.Response(200, json=self.routes[route])
        return httpx.Response(404, json={"message": "Not Found", "documentation_url": "https://docs.github.com/rest"})

    def route(self, request: httpx.Request) -> str:
        """Give the route of a request.

        Args:
            request (httpx.Request): The request.

        Returns:
            str: The path, then the sorted query without the paging parameters.
        """
        query = sorted(
            (name, value) for name, value in request.url.params.multi_items() if name not in {"per_page", "page"}
        )
        return request.url.path + ("?" + "&".join(f"{name}={value}" for name, value in query) if query else "")

    def transport(self) -> httpx.MockTransport:
        """Give a transport that sends every request to this stand-in."""
        return httpx.MockTransport(self)

    def paths(self) -> List[str]:
        """Give the path of every request received, in order."""
        return [request.url.path for request in self.requests]
