from __future__ import annotations

# Standard library imports
import re
from logging import Logger, getLogger
from pathlib import Path
from typing import ClassVar, Dict, Optional, Pattern

# First-party imports
from erp_country_rules.models.config.country_rules_config import CountryRulesConfig
from erp_country_rules.models.exceptions import SECountryPackNotFoundError, SECountryPackUnreadable
from erp_country_rules.models.packs.country_pack import CountryPack


class CountryPackRepository:
    """Reads a country's pack catalogue from disk, and nothing else.

    Attributes:
        PACK_FILE_NAME (str): The name of the pack file inside a country's folder.
        COUNTRY_PATTERN (Pattern[str]): The shape of a country code, two ASCII letters.
        config (CountryRulesConfig): The configuration, which holds the packs folder.
        packs (Dict[str, CountryPack]): The packs already loaded, by upper-case country.
        logger (Logger): Logger instance.

    Notes:
        - **The country is checked before any path is built**, which guards against path traversal.
        - A pack that failed to load is not kept, so the next call reads the file again.
    """

    PACK_FILE_NAME: ClassVar[str] = "rules.yaml"
    COUNTRY_PATTERN: ClassVar[Pattern[str]] = re.compile(r"[A-Z]{2}", re.ASCII)

    def __init__(self, config: CountryRulesConfig, logger: Optional[Logger] = None) -> None:
        """Initialise the repository.

        Args:
            config (CountryRulesConfig): The configuration, which holds the packs folder.
            logger (Optional[Logger]): Logger instance.
        """
        self.config = config
        self.packs: Dict[str, CountryPack] = {}
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Publicly Exposed Methods #
    ############################

    def get(self, country: str) -> CountryPack:
        """Get the pack of one country, reading its file the first time.

        Args:
            country (str): The country code, in any case and with or without spaces around it.

        Returns:
            CountryPack: The pack of the country.

        Raises:
            SECountryPackNotFoundError: If the country is not two ASCII letters, or has no pack file.
            SECountryPackUnreadable: If the pack file cannot be read or is invalid.
        """
        code = country.strip().upper()
        if not self.COUNTRY_PATTERN.fullmatch(code):
            self.logger.error("Refused a country that is not two ASCII letters.")
            raise SECountryPackNotFoundError(
                f"Invalid country: {country!r}. "  # noqa: E501
                "Must be two ASCII letters."
            )
        kept = self.packs.get(code)
        if kept is not None:
            self.logger.debug("Country pack %s already loaded.", code)
            return kept
        path: Path = self.config.packs_dir / code.lower() / self.PACK_FILE_NAME
        if not path.is_file():
            self.logger.error("No country pack file for %s.", code)
            raise SECountryPackNotFoundError(f"No country pack found for {code}.")
        try:
            pack = CountryPack.load(path)
        except SECountryPackUnreadable as error:
            self.logger.error("Country pack %s is unreadable: %s.", code, type(error).__name__)
            raise
        self.packs[code] = pack
        self.logger.info("Loaded country pack %s version %s with %d rules.", code, pack.version, len(pack.rules))
        return pack
