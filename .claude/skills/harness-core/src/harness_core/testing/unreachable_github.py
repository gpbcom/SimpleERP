from __future__ import annotations

# Third-party imports
import httpx


class UnreachableGithub:
    """A GitHub whose host name does not resolve, as an ``httpx.MockTransport`` handler.

    Attributes:
        attempts (int): How many requests were tried.

    Notes:
        It stays silent because it answers every request.
    """

    def __init__(self) -> None:
        """Start with no attempt."""
        self.attempts = 0

    ############################
    # Publicly Exposed Methods #
    ############################

    def __call__(self, request: httpx.Request) -> httpx.Response:
        """Fail one request as a name resolution failure does.

        Args:
            request (httpx.Request): The request.

        Returns:
            httpx.Response: Never.

        Raises:
            httpx.ConnectError: Always.
        """
        self.attempts += 1
        raise httpx.ConnectError("[Errno -2] Name or service not known", request=request)
