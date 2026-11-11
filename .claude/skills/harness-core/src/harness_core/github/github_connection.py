from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional

# Third-party imports
import httpx
from pydantic import JsonValue

# First-party imports
from harness_core.github.exceptions import SEGithubRequestFailedError
from harness_core.github.json_payload import JsonPayload


class GithubConnection:
    """One HTTP client to the GitHub REST API, shared by the readers of a run of a harness tool.

    Attributes:
        PAGE_SIZE (int): Items asked for per page, GitHub's largest.
        TIMEOUT_S (float): The longest one request may take.
        MAX_PAGES (int): The most pages read for one list.
        client (httpx.AsyncClient): The HTTP client, the token in its headers.
        logger (Logger): Logger instance.

    Notes:
        - **The token goes into the client's headers only**: it is never logged, and an error names the path and
          the status, never the request.
        - A list is read page after page through the ``Link: rel="next"`` header.
        - Nothing retries here: the caller decides what a failed request means.
    """

    PAGE_SIZE: ClassVar[int] = 100
    TIMEOUT_S: ClassVar[float] = 30.0
    MAX_PAGES: ClassVar[int] = 20

    def __init__(
        self,
        api_url: str,
        api_version: str,
        token: str,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        logger: Optional[Logger] = None,
    ) -> None:
        """Open the HTTP client.

        Args:
            api_url (str): The REST API root, such as ``https://api.github.com``.
            api_version (str): The REST API version sent in ``X-GitHub-Api-Version``.
            token (str): The GitHub token.
            transport (Optional[httpx.AsyncBaseTransport]): The transport, a stand-in in tests.
            logger (Optional[Logger]): Logger instance.
        """
        self.client = httpx.AsyncClient(
            base_url=api_url,
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": api_version,
                "Authorization": f"Bearer {token}",
            },
            transport=transport,
            timeout=self.TIMEOUT_S,
        )
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    async def _response(self, url: str, params: Optional[Dict[str, str]]) -> httpx.Response:
        """Send one GET request and check its status.

        Args:
            url (str): A path under the API root, or the full link of a next page.
            params (Optional[Dict[str, str]]): The query, ``None`` for a next page link.

        Returns:
            httpx.Response: The successful response.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        try:
            response = await self.client.get(url, params=params)
        except httpx.HTTPError as error:
            self.logger.error("GitHub could not be reached for %s: %s.", url, type(error).__name__)
            raise SEGithubRequestFailedError(
                f"GitHub could not be reached for {url}. "  # noqa: E501
                f"The error was {type(error).__name__}."
            ) from error
        if response.is_error:
            self.logger.error("GitHub answered %d for %s.", response.status_code, url)
            raise SEGithubRequestFailedError(f"GitHub answered {response.status_code} for {url}.")
        return response

    ############################
    # Publicly Exposed Methods #
    ############################

    async def get(self, path: str, params: Optional[Dict[str, str]] = None) -> JsonValue:
        """Read one resource.

        Args:
            path (str): The path under the API root.
            params (Optional[Dict[str, str]]): The query.

        Returns:
            JsonValue: The resource.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        response = await self._response(path, params or {})
        payload: JsonValue = response.json()
        self.logger.debug("Read %s.", path)
        return payload

    async def pages(
        self, path: str, params: Optional[Dict[str, str]] = None, key: str = ""
    ) -> List[Dict[str, JsonValue]]:
        """Read every page of a list.

        Args:
            path (str): The path under the API root.
            params (Optional[Dict[str, str]]): The query.
            key (str): The key of the list in each page, empty when the page is the list itself.

        Returns:
            List[Dict[str, JsonValue]]: The items of every page, in GitHub's order.

        Raises:
            SEGithubRequestFailedError: When GitHub cannot be reached or answers with an error.
        """
        items: List[Dict[str, JsonValue]] = []
        url: Optional[str] = path
        query: Optional[Dict[str, str]] = {**(params or {}), "per_page": str(self.PAGE_SIZE)}
        pages = 0
        while url is not None and pages < self.MAX_PAGES:
            response = await self._response(url, query)
            payload: JsonValue = response.json()
            items.extend(JsonPayload.objects(payload.get(key) if key and isinstance(payload, dict) else payload))
            url = response.links.get("next", {}).get("url")
            query = None
            pages += 1
        if url is not None:
            self.logger.warning("%s has more than %d pages: the rest is not read.", path, self.MAX_PAGES)
        self.logger.debug("Read %d items of %s in %d pages.", len(items), path, pages)
        return items

    async def aclose(self) -> None:
        """Close the HTTP client."""
        await self.client.aclose()
