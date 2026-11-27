from __future__ import annotations


class SEInvalidEventEnvelopeException(Exception):
    """Exception raised when an invalid EventEnvelope is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
