from __future__ import annotations

# Standard library imports
import datetime
from decimal import Decimal
from logging import Logger, getLogger
from typing import Optional, Union

# Third-party imports
from erp_models.money.money import Money

# First-party imports
from erp_country_rules.models.exceptions import SECountryRuleNotFoundError, SECountryRuleNotInForceError
from erp_country_rules.models.packs.country_pack import CountryPack
from erp_country_rules.models.rules.country_rule import CountryRule
from erp_country_rules.models.rules.rule_version import RuleVersion
from erp_country_rules.storage.packs.country_pack_repository import CountryPackRepository


class CountryRules:
    """The rules library: the value of a legal rule in force on the date of a fact.

    Attributes:
        repository (CountryPackRepository): Where the country packs are read.
        logger (Logger): Logger instance.

    Notes:
        - **The library only reads values and computes nothing with them.**
        - A rule is read for every fact, so there is no INFO line, and the value is never logged.
    """

    def __init__(self, repository: CountryPackRepository, logger: Optional[Logger] = None) -> None:
        """Initialise the library.

        Args:
            repository (CountryPackRepository): Where the country packs are read.
            logger (Optional[Logger]): Logger instance.
        """
        self.repository = repository
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _find_rule(self, pack: CountryPack, rule: str) -> CountryRule:
        """Find a rule of a pack by its name.

        Args:
            pack (CountryPack): The pack of the country.
            rule (str): The name of the rule.

        Returns:
            CountryRule: The rule.

        Raises:
            SECountryRuleNotFoundError: If the pack has no rule of that name.
        """
        for candidate in pack.rules:
            if candidate.rule == rule:
                return candidate
        self.logger.error("Rule %s not found for country %s.", rule, pack.country)
        raise SECountryRuleNotFoundError(f"No rule {rule!r} found for country {pack.country}.")

    def _find_version(self, found: CountryRule, country: str, date: datetime.date) -> RuleVersion:
        """Find the version of a rule in force on a date.

        Args:
            found (CountryRule): The rule.
            country (str): The country code, for the message.
            date (datetime.date): The date of the fact.

        Returns:
            RuleVersion: The version in force.

        Raises:
            SECountryRuleNotInForceError: If no version is in force on that date.
        """
        for version in found.versions:
            if version.valid_from <= date and (version.valid_to is None or date <= version.valid_to):
                return version
        self.logger.error("Rule %s of country %s has no version in force on the requested date.", found.rule, country)
        raise SECountryRuleNotInForceError(
            f"Rule {found.rule!r} of country {country} is not in force on {date.isoformat()}."
        )

    ############################
    # Publicly Exposed Methods #
    ############################

    def value(self, rule: str, country: str, date: datetime.date) -> Union[Money, Decimal]:
        """Get the value of a rule in force on a date.

        Args:
            rule (str): The name of the rule.
            country (str): The country code.
            date (datetime.date): The date of the fact.

        Returns:
            Union[Money, Decimal]: The value in force on that date.

        Raises:
            SECountryPackNotFoundError: If the country has no pack.
            SECountryRuleNotFoundError: If the pack has no rule of that name.
            SECountryRuleNotInForceError: If no version is in force on that date.
        """
        pack = self.repository.get(country)
        version = self._find_version(self._find_rule(pack, rule), pack.country, date)
        self.logger.debug(
            "Read rule %s for %s on %s from version %s.", rule, pack.country, date.isoformat(), version.valid_from
        )
        return version.value
