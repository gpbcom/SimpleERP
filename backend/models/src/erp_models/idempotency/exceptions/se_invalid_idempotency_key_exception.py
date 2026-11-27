from __future__ import annotations


class SEInvalidIdempotencyKeyException(Exception):
    """Exception raised when an invalid IdempotencyKey is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
