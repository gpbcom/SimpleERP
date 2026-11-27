from __future__ import annotations

from erp_testing.models.synthetic.exceptions.builder.se_synthetic_data_error import SESyntheticDataError
from erp_testing.models.synthetic.exceptions.builder.se_synthetic_sector_unknown_error import (
    SESyntheticSectorUnknownError,
)
from erp_testing.models.synthetic.exceptions.catalog.names.se_synthetic_catalog_invalid_first_names import (
    SESyntheticCatalogInvalidFirstNames,
)
from erp_testing.models.synthetic.exceptions.catalog.names.se_synthetic_catalog_invalid_last_names import (
    SESyntheticCatalogInvalidLastNames,
)
from erp_testing.models.synthetic.exceptions.catalog.se_invalid_synthetic_catalog_exception import (
    SEInvalidSyntheticCatalogException,
)
from erp_testing.models.synthetic.exceptions.catalog.se_synthetic_catalog_invalid_company_words import (
    SESyntheticCatalogInvalidCompanyWords,
)
from erp_testing.models.synthetic.exceptions.catalog.se_synthetic_catalog_invalid_email_domain import (
    SESyntheticCatalogInvalidEmailDomain,
)
from erp_testing.models.synthetic.exceptions.catalog.se_synthetic_catalog_invalid_sectors import (
    SESyntheticCatalogInvalidSectors,
)
from erp_testing.models.synthetic.exceptions.catalog.se_synthetic_catalog_unreadable import SESyntheticCatalogUnreadable
from erp_testing.models.synthetic.exceptions.company.se_invalid_synthetic_company_exception import (
    SEInvalidSyntheticCompanyException,
)
from erp_testing.models.synthetic.exceptions.company.se_synthetic_company_invalid_id import SESyntheticCompanyInvalidId
from erp_testing.models.synthetic.exceptions.company.se_synthetic_company_invalid_name import (
    SESyntheticCompanyInvalidName,
)
from erp_testing.models.synthetic.exceptions.company.se_synthetic_company_invalid_sector import (
    SESyntheticCompanyInvalidSector,
)
from erp_testing.models.synthetic.exceptions.user.se_invalid_synthetic_user_exception import (
    SEInvalidSyntheticUserException,
)
from erp_testing.models.synthetic.exceptions.user.se_synthetic_user_invalid_company_id import (
    SESyntheticUserInvalidCompanyId,
)
from erp_testing.models.synthetic.exceptions.user.se_synthetic_user_invalid_email import SESyntheticUserInvalidEmail
from erp_testing.models.synthetic.exceptions.user.se_synthetic_user_invalid_id import SESyntheticUserInvalidId
from erp_testing.models.synthetic.exceptions.user.se_synthetic_user_invalid_name import SESyntheticUserInvalidName

__all__ = [
    "SEInvalidSyntheticCatalogException",
    "SEInvalidSyntheticCompanyException",
    "SEInvalidSyntheticUserException",
    "SESyntheticCatalogInvalidCompanyWords",
    "SESyntheticCatalogInvalidEmailDomain",
    "SESyntheticCatalogInvalidFirstNames",
    "SESyntheticCatalogInvalidLastNames",
    "SESyntheticCatalogInvalidSectors",
    "SESyntheticCatalogUnreadable",
    "SESyntheticCompanyInvalidId",
    "SESyntheticCompanyInvalidName",
    "SESyntheticCompanyInvalidSector",
    "SESyntheticDataError",
    "SESyntheticSectorUnknownError",
    "SESyntheticUserInvalidCompanyId",
    "SESyntheticUserInvalidEmail",
    "SESyntheticUserInvalidId",
    "SESyntheticUserInvalidName",
]
