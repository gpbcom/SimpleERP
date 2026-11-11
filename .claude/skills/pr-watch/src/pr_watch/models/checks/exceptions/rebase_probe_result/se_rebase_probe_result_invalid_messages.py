from __future__ import annotations

from pr_watch.models.checks.exceptions.se_invalid_rebase_probe_result_exception import (
    SEInvalidRebaseProbeResultException,
)


class SERebaseProbeResultInvalidMessages(SEInvalidRebaseProbeResultException):
    """Exception raised when an invalid ``messages`` is provided."""
