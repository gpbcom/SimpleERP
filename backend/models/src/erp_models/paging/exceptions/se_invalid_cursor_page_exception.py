from __future__ import annotations


class SEInvalidCursorPageException(Exception):
    """Exception raised when an invalid CursorPage is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
