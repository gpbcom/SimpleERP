from __future__ import annotations

# First-party imports
from erp_config.models.exceptions.sections.se_invalid_config_section_exception import SEInvalidConfigSectionException


class SEConfigSectionInvalidKey(SEInvalidConfigSectionException):
    """Exception raised when an invalid ``_key`` field is provided."""
