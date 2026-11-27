from __future__ import annotations


class SEInvalidRecordIdException(Exception):
    """Exception raised when an invalid RecordId is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
