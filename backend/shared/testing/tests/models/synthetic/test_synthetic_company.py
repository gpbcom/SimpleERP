from __future__ import annotations

import pytest
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from erp_testing.models.synthetic.exceptions import (
    SEInvalidSyntheticCompanyException,
    SESyntheticCompanyInvalidId,
    SESyntheticCompanyInvalidName,
    SESyntheticCompanyInvalidSector,
)
from erp_testing.models.synthetic.synthetic_company import SyntheticCompany
from pydantic import JsonValue, ValidationError


class TestSyntheticCompany:
    def valid(self) -> dict[str, JsonValue | CompanyId]:
        return {"id": CompanyId(value="C-1"), "name": "Acme", "sector": "sc01"}

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            SyntheticCompany()  # type: ignore[call-arg]

    def test_full_valid_construction(self) -> None:
        values = self.valid()
        values["name"] = "  Acme Works  "

        company = SyntheticCompany(**values)  # type: ignore[arg-type]

        assert company.id == CompanyId(value="C-1")
        assert company.name == "Acme Works"
        assert company.sector == "sc01"
        assert isinstance(company, FrozenErpModel)

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("id", SESyntheticCompanyInvalidId),
            ("name", SESyntheticCompanyInvalidName),
            ("sector", SESyntheticCompanyInvalidSector),
        ],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = None

        with pytest.raises(error):
            SyntheticCompany(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", 12, SESyntheticCompanyInvalidId),
            ("id", True, SESyntheticCompanyInvalidId),
            ("id", [], SESyntheticCompanyInvalidId),
            ("name", "", SESyntheticCompanyInvalidName),
            ("name", "   ", SESyntheticCompanyInvalidName),
            ("name", 12, SESyntheticCompanyInvalidName),
            ("name", True, SESyntheticCompanyInvalidName),
            ("sector", "", SESyntheticCompanyInvalidSector),
            ("sector", "sc1", SESyntheticCompanyInvalidSector),
            ("sector", "sc001", SESyntheticCompanyInvalidSector),
            ("sector", "SC01", SESyntheticCompanyInvalidSector),
            ("sector", "xx01", SESyntheticCompanyInvalidSector),
            ("sector", "sc01\n", SESyntheticCompanyInvalidSector),
            ("sector", 1, SESyntheticCompanyInvalidSector),
            ("sector", True, SESyntheticCompanyInvalidSector),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = value

        with pytest.raises(error) as raised:
            SyntheticCompany(**values)  # type: ignore[arg-type]

        assert isinstance(raised.value, SEInvalidSyntheticCompanyException)

    def test_rejects_unknown_keys(self) -> None:
        values = self.valid()
        values["other"] = "x"

        with pytest.raises(ValidationError):
            SyntheticCompany(**values)  # type: ignore[arg-type]

    def test_a_company_cannot_change_once_built(self) -> None:
        company = SyntheticCompany(**self.valid())  # type: ignore[arg-type]

        with pytest.raises(ValidationError):
            company.name = "Other"  # type: ignore[misc]

    def test_round_trip(self) -> None:
        company = SyntheticCompany(**self.valid())  # type: ignore[arg-type]

        assert company.model_dump(mode="json") == {"id": {"value": "C-1"}, "name": "Acme", "sector": "sc01"}
        assert SyntheticCompany.model_validate(company.model_dump(mode="json")) == company
        assert SyntheticCompany.model_validate_json(company.model_dump_json()) == company
