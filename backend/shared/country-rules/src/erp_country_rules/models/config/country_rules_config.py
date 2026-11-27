from __future__ import annotations

# Standard library imports
from pathlib import Path

from erp_models.base.frozen_erp_model import FrozenErpModel

# Third-party imports
from pydantic import ConfigDict, Field, JsonValue, field_validator

# First-party imports
from erp_country_rules.models.exceptions import SECountryRulesConfigInvalidPacksDir


class CountryRulesConfig(FrozenErpModel):
    """The configuration section that tells the library where the country packs are.

    Attributes:
        model_config (ConfigDict): Refuses unknown keys and assignment, and validates the defaults.
        packs_dir (Path): The folder that holds one country pack per country.
    """

    model_config = ConfigDict(extra="forbid", frozen=True, validate_default=True)

    packs_dir: Path = Field(default=Path("packs/countries"), description="The folder that holds the country packs.")

    @field_validator("packs_dir", mode="before")
    def validate_packs_dir(cls, value: JsonValue) -> JsonValue:
        """Validate ``packs_dir``.

        Args:
            value (JsonValue): The raw input.

        Returns:
            JsonValue: The default for ``None``, otherwise the stripped path.

        Raises:
            SECountryRulesConfigInvalidPacksDir: If the value is neither a path nor a non-empty string.
        """
        if value is None:
            return str(cls.model_fields["packs_dir"].get_default(call_default_factory=True))
        if isinstance(value, Path):
            return str(value)
        if isinstance(value, str) and value.strip():
            return value.strip()
        raise SECountryRulesConfigInvalidPacksDir(
            f"Invalid packs_dir: {value!r}. "  # noqa: E501
            "Must be a path or a non-empty string."
        )
