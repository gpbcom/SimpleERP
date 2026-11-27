from __future__ import annotations


class SEInvalidStandInRouteException(Exception):
    """Exception raised when an invalid StandInRoute is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
