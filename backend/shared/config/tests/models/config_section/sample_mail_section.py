from __future__ import annotations

# Standard library imports
from typing import Optional

# First-party imports
from erp_config.models.config_section import ConfigSection

# Third-party imports
from pydantic import Field


class SampleMailSection(ConfigSection):
    """A configuration section with one plain field and one vault entry name, used to test ``ConfigSection``."""

    sender: str = Field(default="erp@example.org", description="The address mail is sent from.")
    password_key: Optional[str] = Field(default=None, description="The vault entry holding the SMTP password.")
