from __future__ import annotations


class SEInvalidMoneyException(Exception):
    """Exception raised when an invalid Money is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
