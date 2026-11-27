from __future__ import annotations


class SEInvalidYamlCatalogException(Exception):
    """Exception raised when an invalid YamlCatalog is provided.

    Notes:
        It subclasses ``Exception`` and not ``ValueError``, so that Pydantic does not wrap it in a
        ``ValidationError``.
    """
