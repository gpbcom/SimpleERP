from __future__ import annotations

# Standard library imports
import re
import unicodedata
from logging import Logger
from random import Random
from typing import ClassVar, Optional

# Third-party imports
from erp_models.ids.record_id import RecordId

# First-party imports
from erp_testing.models.synthetic.synthetic_catalog import SyntheticCatalog
from erp_testing.models.synthetic.synthetic_company import SyntheticCompany
from erp_testing.models.synthetic.synthetic_user import SyntheticUser
from erp_testing.synthetic.synthetic_builder import SyntheticBuilder


class UserBuilder(SyntheticBuilder[SyntheticUser]):
    """Build generated users of one generated company, from the names of the catalogue.

    Attributes:
        ID_PREFIX (str): The prefix of every generated user identifier.
        ID_BITS (int): The number of random bits of an identifier.
        NOT_LOCAL_PART (str): The pattern of the characters left out of an e-mail address.
        catalog (SyntheticCatalog): The names and the domain a user is made of.
        company (SyntheticCompany): The company every user built belongs to.
        random (Random): The generator, seeded by the company identifier and the seed.
        built_count (int): The number of users built so far.
        logger (Logger): Logger instance.

    Notes:
        - **The sequence is the same for the same company and seed.**
        - **Two addresses of one builder always differ**, because the address ends with the count of users built.
    """

    ID_PREFIX: ClassVar[str] = "U-"
    ID_BITS: ClassVar[int] = 64
    NOT_LOCAL_PART: ClassVar[str] = r"[^a-z0-9]"

    def __init__(
        self, catalog: SyntheticCatalog, company: SyntheticCompany, seed: int = 0, logger: Optional[Logger] = None
    ) -> None:
        """Create the builder.

        Args:
            catalog (SyntheticCatalog): The names and the domain a user is made of.
            company (SyntheticCompany): The company every user built belongs to.
            seed (int): The seed of the sequence.
            logger (Optional[Logger]): Logger to use.
        """
        super().__init__(logger)
        self.catalog = catalog
        self.company = company
        self.random = Random(f"{company.id.value}:{seed}")
        self.built_count = 0

    ############################
    # Internal Helpers Methods #
    ############################

    def _local_part(self, first_name: str, last_name: str) -> str:
        """Make the part of an address before the ``@``.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.

        Returns:
            str: Lower-case ASCII letters and digits, with the count of users built.
        """
        text = unicodedata.normalize("NFKD", f"{first_name}.{last_name}").encode("ascii", "ignore").decode("ascii")
        cleaned = re.sub(self.NOT_LOCAL_PART, "", text.lower())
        self.logger.debug("Made an address local part of %d characters.", len(cleaned))
        return f"{cleaned}{self.built_count}"

    ############################
    # Publicly Exposed Methods #
    ############################

    def build(self) -> SyntheticUser:
        """Build the next user of the sequence.

        Returns:
            SyntheticUser: The user, with a generated identifier, name and address.
        """
        user_id = RecordId(value=f"{self.ID_PREFIX}{self.random.getrandbits(self.ID_BITS):016x}")
        first_name = self.random.choice(self.catalog.first_names)
        last_name = self.random.choice(self.catalog.last_names)
        self.built_count += 1
        email = f"{self._local_part(first_name, last_name)}@{self.catalog.email_domain}"
        self.logger.debug("Built synthetic user %s of company %s.", user_id.value, self.company.id.value)
        return SyntheticUser(id=user_id, company_id=self.company.id, name=f"{first_name} {last_name}", email=email)
