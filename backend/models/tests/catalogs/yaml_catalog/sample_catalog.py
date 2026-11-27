from __future__ import annotations

from typing import ClassVar, List, Type

from erp_models.catalogs.yaml_catalog import YamlCatalog
from pydantic import Field, JsonValue, field_validator

from tests.catalogs.yaml_catalog.se_sample_catalog_invalid_names import SESampleCatalogInvalidNames
from tests.catalogs.yaml_catalog.se_sample_catalog_unreadable import SESampleCatalogUnreadable


class SampleCatalog(YamlCatalog):
    """A small catalogue used to test ``YamlCatalog``.

    Attributes:
        UNREADABLE (Type[Exception]): The exception ``load`` raises when the file cannot be read.
        names (List[str]): The names the sample catalogue lists.
    """

    UNREADABLE: ClassVar[Type[Exception]] = SESampleCatalogUnreadable

    names: List[str] = Field(default_factory=list, description="The names the sample catalogue lists.")

    @field_validator("names", mode="before")
    def validate_names(cls, value: JsonValue) -> JsonValue:
        """Validate ``names``.

        Args:
            value (JsonValue): The raw value.

        Returns:
            JsonValue: The list with each name stripped.

        Raises:
            SESampleCatalogInvalidNames: If the value is not a list of non-empty texts.
        """
        if value is None:
            return cls.model_fields["names"].get_default(call_default_factory=True)
        if not isinstance(value, list):
            raise SESampleCatalogInvalidNames(f"Invalid names: {value!r}. Must be a list of texts.")
        stripped: List[JsonValue] = []
        for item in value:
            if not isinstance(item, str) or not item.strip():
                raise SESampleCatalogInvalidNames(f"Invalid names: {value!r}. Each name must be a non-empty text.")
            stripped.append(item.strip())
        return stripped
