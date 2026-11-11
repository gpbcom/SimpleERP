from __future__ import annotations

from pr_watch.models.watch.exceptions.se_invalid_registry_exception import SEInvalidRegistryException


class SERegistryInvalidPullRequests(SEInvalidRegistryException):
    """Exception raised when an invalid ``pull_requests`` is provided."""
