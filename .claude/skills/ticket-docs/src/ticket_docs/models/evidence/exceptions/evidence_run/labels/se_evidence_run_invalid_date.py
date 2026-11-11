from __future__ import annotations

from ticket_docs.models.evidence.exceptions.evidence_run.se_invalid_evidence_run_exception import (
    SEInvalidEvidenceRunException,
)


class SEEvidenceRunInvalidDate(SEInvalidEvidenceRunException):
    """Exception raised when an invalid ``date`` is provided."""
