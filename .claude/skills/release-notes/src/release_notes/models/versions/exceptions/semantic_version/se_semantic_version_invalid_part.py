from __future__ import annotations

from release_notes.models.versions.exceptions.semantic_version.se_invalid_semantic_version_exception import (
    SEInvalidSemanticVersionException,
)


class SESemanticVersionInvalidPart(SEInvalidSemanticVersionException):
    """Exception raised when an invalid ``major``, ``minor`` or ``patch`` is provided."""
