from __future__ import annotations

# Third-party imports
from pydantic import ConfigDict

# First-party imports
from erp_models.base.erp_model import ErpModel


class FrozenErpModel(ErpModel):
    """The base of the shared models that must not change once built.

    Attributes:
        model_config (ConfigDict): Pydantic configuration, which refuses unknown keys and assignment.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)
