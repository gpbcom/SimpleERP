from __future__ import annotations

from ticket_docs.models.evidence.exceptions.evidence_run.se_invalid_evidence_run_exception import (
    SEInvalidEvidenceRunException,
)


class SEEvidenceRunInvalidText(SEInvalidEvidenceRunException):
    """Exception raised when an invalid ``what``, ``command``, ``branch`` or ``result`` is provided."""
