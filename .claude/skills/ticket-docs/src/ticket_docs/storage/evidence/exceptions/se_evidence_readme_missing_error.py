from __future__ import annotations

from ticket_docs.storage.evidence.exceptions.se_evidence_store_error import SEEvidenceStoreError


class SEEvidenceReadmeMissingError(SEEvidenceStoreError):
    """Raised when an evidence folder has no README.md."""
