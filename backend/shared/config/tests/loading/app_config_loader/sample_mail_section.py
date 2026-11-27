"""A configuration section with a secret store entry, for the tests of the loader."""

from __future__ import annotations

# Standard library imports
from typing import Optional

# First-party imports
from erp_config.models.config_section import ConfigSection

# Third-party imports
from pydantic import Field


class SampleMailSection(ConfigSection):
    """How the sample service sends mail.

    Attributes:
        sender (str): The sender address.
        password_key (Optional[str]): The name of the secret store entry that holds the password.
    """

    sender: str = Field(default="erp@example.org", description="The address mail is sent from.")
    password_key: Optional[str] = Field(
        default="mail/smtp-password", description="The secret store entry that holds the SMTP password."
    )
