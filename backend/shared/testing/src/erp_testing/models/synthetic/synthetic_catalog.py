from __future__ import annotations

# Standard library imports
import re
from pathlib import Path
from typing import ClassVar, List, Optional, Tuple, Type

# Third-party imports
from erp_models.catalogs.yaml_catalog import YamlCatalog
from pydantic import Field, JsonValue, field_validator

# First-party imports
from erp_testing.models.synthetic.exceptions import (
    SESyntheticCatalogInvalidCompanyWords,
    SESyntheticCatalogInvalidEmailDomain,
    SESyntheticCatalogInvalidFirstNames,
    SESyntheticCatalogInvalidLastNames,
    SESyntheticCatalogInvalidSectors,
    SESyntheticCatalogUnreadable,
)


class SyntheticCatalog(YamlCatalog):
    """The synthetic data catalogue: the words every generated company, person and address is made of.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.
        DEFAULT_PATH (Path): The shipped catalogue, ``conf/catalogs/synthetic.yaml`` of ``erp-testing``.
        RESERVED_DOMAINS (Tuple[str, ...]): The domains RFC 2606 reserves for examples.
        RESERVED_SUFFIXES (Tuple[str, ...]): The top-level domains RFC 2606 reserves for tests.
        SECTOR_PATTERN (str): The pattern of a sector code.
        sectors (List[str]): The sector codes, one per sector folder of the specifications.
        company_words (List[str]): The invented words a company name is made of.
        first_names (List[str]): The invented first names of the generated users.
        last_names (List[str]): The invented last names of the generated users.
        email_domain (str): The reserved domain of every generated e-mail address.

    Notes:
        - **The e-mail domain must be reserved**, so that no generated address can ever reach a real mailbox.
        - ``is_reserved_domain`` holds the rule once, for the catalogue and for ``SyntheticUser``.
        - ``None`` has no default to become, so it is refused with the field's exception.
    """

    UNREADABLE: ClassVar[Type[Exception]] = SESyntheticCatalogUnreadable
    DEFAULT_PATH: ClassVar[Path] = Path(__file__).resolve().parents[4] / "conf" / "catalogs" / "synthetic.yaml"
    RESERVED_DOMAINS: ClassVar[Tuple[str, ...]] = ("example.com", "example.net", "example.org")
    RESERVED_SUFFIXES: ClassVar[Tuple[str, ...]] = (".test", ".example", ".invalid", ".localhost")
    SECTOR_PATTERN: ClassVar[str] = r"sc[0-9]{2}"

    sectors: List[str] = Field(description="The sector codes, such as sc01, one per sector of the specifications.")
    company_words: List[str] = Field(description="The invented words a company name is made of.")
    first_names: List[str] = Field(description="The invented first names of the generated users.")
    last_names: List[str] = Field(description="The invented last names of the generated users.")
    email_domain: str = Field(description="The reserved domain of every generated e-mail address.")

    @field_validator("sectors", mode="before")
    def validate_sectors(cls, value: JsonValue) -> JsonValue:
        """Validate ``sectors``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The sector codes, unchanged.

        Raises:
            SESyntheticCatalogInvalidSectors: When it is not a non-empty list of distinct sector codes.
        """
        if (
            not isinstance(value, list)
            or not value
            or not all(isinstance(item, str) and re.fullmatch(cls.SECTOR_PATTERN, item) for item in value)
            or len(value) != len(set(value))
        ):
            raise SESyntheticCatalogInvalidSectors(
                f"Invalid sectors: {value!r}. "  # noqa: E501
                "Must be a non-empty list of distinct codes such as sc01."
            )
        return value

    @field_validator("company_words", mode="before")
    def validate_company_words(cls, value: JsonValue) -> JsonValue:
        """Validate ``company_words``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The words, stripped.

        Raises:
            SESyntheticCatalogInvalidCompanyWords: When it is not a non-empty list of non-empty texts.
        """
        words = cls._stripped_words(value)
        if words is None:
            raise SESyntheticCatalogInvalidCompanyWords(
                f"Invalid company_words: {value!r}. "  # noqa: E501
                "Must be a non-empty list of non-empty texts."
            )
        return list(words)

    @field_validator("first_names", mode="before")
    def validate_first_names(cls, value: JsonValue) -> JsonValue:
        """Validate ``first_names``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The names, stripped.

        Raises:
            SESyntheticCatalogInvalidFirstNames: When it is not a non-empty list of non-empty texts.
        """
        names = cls._stripped_words(value)
        if names is None:
            raise SESyntheticCatalogInvalidFirstNames(
                f"Invalid first_names: {value!r}. "  # noqa: E501
                "Must be a non-empty list of non-empty texts."
            )
        return list(names)

    @field_validator("last_names", mode="before")
    def validate_last_names(cls, value: JsonValue) -> JsonValue:
        """Validate ``last_names``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The names, stripped.

        Raises:
            SESyntheticCatalogInvalidLastNames: When it is not a non-empty list of non-empty texts.
        """
        names = cls._stripped_words(value)
        if names is None:
            raise SESyntheticCatalogInvalidLastNames(
                f"Invalid last_names: {value!r}. "  # noqa: E501
                "Must be a non-empty list of non-empty texts."
            )
        return list(names)

    @field_validator("email_domain", mode="before")
    def validate_email_domain(cls, value: JsonValue) -> JsonValue:
        """Validate ``email_domain``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The domain, stripped.

        Raises:
            SESyntheticCatalogInvalidEmailDomain: When it is not a text, or not a reserved domain.
        """
        if not isinstance(value, str) or not cls.is_reserved_domain(value.strip()):
            raise SESyntheticCatalogInvalidEmailDomain(
                f"Invalid email_domain: {value!r}. "  # noqa: E501
                f"Must be one of {list(cls.RESERVED_DOMAINS)} or end with one of {list(cls.RESERVED_SUFFIXES)}."
            )
        return value.strip()

    ############################
    # Internal Helpers Methods #
    ############################

    @classmethod
    def _stripped_words(cls, value: JsonValue) -> Optional[List[str]]:
        """Strip a list of texts, which must hold at least one and no empty one.

        Args:
            value (JsonValue): The raw input.

        Returns:
            Optional[List[str]]: The stripped texts, or ``None`` when the input is not a valid list.
        """
        if not isinstance(value, list) or not value:
            return None
        words: List[str] = []
        for item in value:
            if not isinstance(item, str) or not item.strip():
                return None
            words.append(item.strip())
        return words

    ############################
    # Publicly Exposed Methods #
    ############################

    @classmethod
    def is_reserved_domain(cls, domain: str) -> bool:
        """Tell whether a domain is reserved for examples and tests.

        Args:
            domain (str): The domain to check, such as ``simpleerp.test``.

        Returns:
            bool: ``True`` when it is one of ``RESERVED_DOMAINS`` or ends with one of ``RESERVED_SUFFIXES``.
        """
        lowered = domain.lower()
        return lowered in cls.RESERVED_DOMAINS or lowered.endswith(cls.RESERVED_SUFFIXES)
