from __future__ import annotations

from pr_watch.models.state.exceptions.se_invalid_pr_snapshot_exception import SEInvalidPrSnapshotException


class SEPrSnapshotInvalidCi(SEInvalidPrSnapshotException):
    """Exception raised when an invalid ``ci`` is provided."""
