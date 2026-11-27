from __future__ import annotations


class SEInvalidStandInRequestException(Exception):
    """Exception raised when an invalid StandInRequest is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
