"""A configuration section with plain values, for the tests of the loader."""

from __future__ import annotations

# First-party imports
from erp_config.models.config_section import ConfigSection

# Third-party imports
from pydantic import Field


class SampleServerSection(ConfigSection):
    """Where the sample service listens.

    Attributes:
        host (str): The host name.
        port (int): The port.
    """

    host: str = Field(default="localhost", description="The host the sample service listens on.")
    port: int = Field(default=8000, description="The port the sample service listens on.")
