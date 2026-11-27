from __future__ import annotations

from erp_testing.models.synthetic.exceptions.builder.se_synthetic_data_error import SESyntheticDataError


class SESyntheticSectorUnknownError(SESyntheticDataError):
    """Raised when a sector is not in the synthetic catalogue."""
