from __future__ import annotations


class SEInvalidOpaqueIdException(Exception):
    """Exception raised when an invalid OpaqueId is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
