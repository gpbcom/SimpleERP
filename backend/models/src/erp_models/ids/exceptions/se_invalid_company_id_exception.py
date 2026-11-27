from __future__ import annotations


class SEInvalidCompanyIdException(Exception):
    """Exception raised when an invalid CompanyId is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
