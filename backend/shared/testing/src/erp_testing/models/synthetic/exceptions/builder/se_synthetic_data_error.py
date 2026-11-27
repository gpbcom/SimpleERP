from __future__ import annotations

from erp_models.exceptions import SEError


class SESyntheticDataError(SEError):
    """Base class for every error raised while building synthetic data."""
