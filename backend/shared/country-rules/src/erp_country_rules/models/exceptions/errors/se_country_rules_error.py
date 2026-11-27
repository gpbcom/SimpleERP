from __future__ import annotations

# First-party imports
from erp_models.exceptions import SEError


class SECountryRulesError(SEError):
    """Base class for every error raised while reading a country rule."""
