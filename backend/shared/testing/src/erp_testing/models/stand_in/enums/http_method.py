from __future__ import annotations

# Standard library imports
from enum import StrEnum, unique


@unique
class HttpMethod(StrEnum):
    """The HTTP methods a stand-in server answers.

    Attributes:
        GET (str): Read a resource.
        POST (str): Create a resource.
        PUT (str): Replace a resource.
        PATCH (str): Change part of a resource.
        DELETE (str): Remove a resource.
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
