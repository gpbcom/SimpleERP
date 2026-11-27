from __future__ import annotations

# Standard library imports
from logging import Logger
from random import Random
from typing import ClassVar, Optional

# Third-party imports
from erp_models.ids.company_id import CompanyId

# First-party imports
from erp_testing.models.synthetic.exceptions import SESyntheticSectorUnknownError
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.models.synthetic.synthetic_company import SyntheticCompany
from erp_testing.synthetic.synthetic_builder import SyntheticBuilder


class CompanyBuilder(SyntheticBuilder[SyntheticCompany]):
    """Build generated companies of one sector, from the words of the catalogue.

    Attributes:
        ID_PREFIX (str): The prefix of every generated company identifier.
        ID_BITS (int): The number of random bits of an identifier.
        NAME_WORDS_MIN (int): The fewest words of a company name.
        NAME_WORDS_MAX (int): The most words of a company name.
        catalog (SyntheticCatalog): The words a company is made of.
        sector (str): The sector code of every company built.
        random (Random): The generator, seeded by the sector and the seed.
        logger (Logger): Logger instance.

    Notes:
        - **The sequence is the same for the same sector and seed**, because the generator is seeded by both.
        - The identifiers are built from the generator's bits, so they repeat for the same seed and differ between
          two builds with overwhelming probability.
    """

    ID_PREFIX: ClassVar[str] = "C-"
    ID_BITS: ClassVar[int] = 64
    NAME_WORDS_MIN: ClassVar[int] = 2
    NAME_WORDS_MAX: ClassVar[int] = 3

    def __init__(self, catalog: SyntheticCatalog, sector: str, seed: int = 0, logger: Optional[Logger] = None) -> None:
        """Create the builder.

        Args:
            catalog (SyntheticCatalog): The words a company is made of.
            sector (str): The sector code of every company built.
            seed (int): The seed of the sequence.
            logger (Optional[Logger]): Logger to use.
        """
        super().__init__(logger)
        self.catalog = catalog
        self.sector = sector
        self.random = Random(f"{sector}:{seed}")

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self) -> SyntheticCompany:
        """Build the next company of the sequence.

        Returns:
            SyntheticCompany: The company, with a generated identifier and name.

        Raises:
            SESyntheticSectorUnknownError: When the sector is not in the catalogue.
        """
        if self.sector not in self.catalog.sectors:
            self.logger.error("Unknown synthetic sector %s.", self.sector)
            raise SESyntheticSectorUnknownError(
                f"Unknown sector: {self.sector!r}. "  # noqa: E501
                "Must be one of the sectors of the synthetic catalogue."
            )
        company_id = CompanyId(value=f"{self.ID_PREFIX}{self.random.getrandbits(self.ID_BITS):016x}")
        count = self.random.randint(self.NAME_WORDS_MIN, self.NAME_WORDS_MAX)
        name = " ".join(self.random.choice(self.catalog.company_words) for _ in range(count))
        self.logger.debug("Built synthetic company %s in sector %s.", company_id.value, self.sector)
        return SyntheticCompany(id=company_id, name=name, sector=self.sector)
