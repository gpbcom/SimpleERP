"""A whole configuration, for the tests of the loader."""

from __future__ import annotations

from erp_config.models.config_section import ConfigSection

# Third-party imports
from pydantic import Field

# First-party imports
from backend.shared.config.tests.loading.app_config_loader.sample_mail_section import SampleMailSection
from backend.shared.config.tests.loading.app_config_loader.sample_server_section import SampleServerSection


class SampleAppConfig(ConfigSection):
    """The configuration of the sample service.

    Attributes:
        server (SampleServerSection): Where it listens.
        mail (SampleMailSection): How it sends mail.
    """

    server: SampleServerSection = Field(default_factory=SampleServerSection, description="The server section.")
    mail: SampleMailSection = Field(default_factory=SampleMailSection, description="The mail section.")
