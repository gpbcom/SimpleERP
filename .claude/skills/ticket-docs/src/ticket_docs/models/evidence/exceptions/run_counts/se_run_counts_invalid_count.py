from __future__ import annotations

from ticket_docs.models.evidence.exceptions.run_counts.se_invalid_run_counts_exception import (
    SEInvalidRunCountsException,
)


class SERunCountsInvalidCount(SEInvalidRunCountsException):
    """Exception raised when an invalid ``tests``, ``failures`` or ``errors`` is provided."""
