from __future__ import annotations

from erp_models.exceptions import SEError


class SEMeteringError(SEError):
    """Base class for every error raised while metering a paid call."""
