from __future__ import annotations

from typing import List, Optional

import httpx
from pydantic import JsonValue


class UsageReportHandler:
    """Stands in for the Anthropic usage report endpoint behind an ``httpx.MockTransport``.

    Attributes:
        pages (List[JsonValue]): The bodies served in turn, the last one repeated.
        status_code (int): The status of every answer.
        failure (Optional[Exception]): Raised instead of answering, for a transport failure.
        requests (List[httpx.Request]): Each request received.
    """

    def __init__(self, pages: List[JsonValue], status_code: int = 200, failure: Optional[Exception] = None) -> None:
        self.pages = pages
        self.status_code = status_code
        self.failure = failure
        self.requests: List[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        if self.failure is not None:
            raise self.failure
        page = self.pages[min(len(self.requests), len(self.pages)) - 1]
        return httpx.Response(self.status_code, json=page)
