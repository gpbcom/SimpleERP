from __future__ import annotations

# Third-party imports
from pydantic import BaseModel, ConfigDict


class ErpModel(BaseModel):
    """The base of every shared model.

    Attributes:
        model_config (ConfigDict): Pydantic configuration, which refuses unknown keys.
    """

    model_config = ConfigDict(extra="forbid")
