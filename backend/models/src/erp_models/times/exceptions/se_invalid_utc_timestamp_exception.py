from __future__ import annotations


class SEInvalidUtcTimestampException(Exception):
    """Exception raised when an invalid UtcTimestamp is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
