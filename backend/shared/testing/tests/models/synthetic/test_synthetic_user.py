from __future__ import annotations

import pytest
from erp_models.base.frozen_erp_model import FrozenErpModel
from erp_models.ids.company_id import CompanyId
from erp_models.ids.record_id import RecordId
from erp_testing.models.synthetic.exceptions import (
    SEInvalidSyntheticUserException,
    SESyntheticUserInvalidCompanyId,
    SESyntheticUserInvalidEmail,
    SESyntheticUserInvalidId,
    SESyntheticUserInvalidName,
)
from erp_testing.models.synthetic.synthetic_user import SyntheticUser
from pydantic import JsonValue, ValidationError


class TestSyntheticUser:
    def valid(self) -> dict[str, JsonValue | CompanyId | RecordId]:
        return {
            "id": RecordId(value="U-1"),
            "company_id": CompanyId(value="C-1"),
            "name": "Ada Martin",
            "email": "ada.martin@example.com",
        }

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            SyntheticUser()  # type: ignore[call-arg]

    def test_full_valid_construction(self) -> None:
        values = self.valid()
        values["name"] = "  Ada Martin  "

        user = SyntheticUser(**values)  # type: ignore[arg-type]

        assert user.id == RecordId(value="U-1")
        assert user.company_id == CompanyId(value="C-1")
        assert user.name == "Ada Martin"
        assert user.email == "ada.martin@example.com"
        assert isinstance(user, FrozenErpModel)

    @pytest.mark.parametrize(
        ("name", "error"),
        [
            ("id", SESyntheticUserInvalidId),
            ("company_id", SESyntheticUserInvalidCompanyId),
            ("name", SESyntheticUserInvalidName),
            ("email", SESyntheticUserInvalidEmail),
        ],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = None

        with pytest.raises(error):
            SyntheticUser(**values)  # type: ignore[arg-type]

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("id", 12, SESyntheticUserInvalidId),
            ("id", True, SESyntheticUserInvalidId),
            ("id", [], SESyntheticUserInvalidId),
            ("company_id", 12, SESyntheticUserInvalidCompanyId),
            ("company_id", True, SESyntheticUserInvalidCompanyId),
            ("company_id", [], SESyntheticUserInvalidCompanyId),
            ("name", "", SESyntheticUserInvalidName),
            ("name", "   ", SESyntheticUserInvalidName),
            ("name", 12, SESyntheticUserInvalidName),
            ("name", True, SESyntheticUserInvalidName),
            ("email", "", SESyntheticUserInvalidEmail),
            ("email", 12, SESyntheticUserInvalidEmail),
            ("email", True, SESyntheticUserInvalidEmail),
            ("email", "someone@gmail.com", SESyntheticUserInvalidEmail),
            ("email", "someone@example.com.evil.io", SESyntheticUserInvalidEmail),
            ("email", "someone.example.com", SESyntheticUserInvalidEmail),
            ("email", "a@b@example.com", SESyntheticUserInvalidEmail),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        values = self.valid()
        values[name] = value

        with pytest.raises(error) as raised:
            SyntheticUser(**values)  # type: ignore[arg-type]

        assert isinstance(raised.value, SEInvalidSyntheticUserException)

    @pytest.mark.parametrize(
        "email",
        [
            "ada@example.com",
            "ada@example.net",
            "ada@example.org",
            "ada@mail.test",
            "ada@erp.example",
            "ada@bad.invalid",
            "ada@box.localhost",
        ],
    )
    def test_an_address_on_a_reserved_domain_is_accepted(self, email: str) -> None:
        values = self.valid()
        values["email"] = email

        assert SyntheticUser(**values).email == email  # type: ignore[arg-type]

    def test_rejects_unknown_keys(self) -> None:
        values = self.valid()
        values["other"] = "x"

        with pytest.raises(ValidationError):
            SyntheticUser(**values)  # type: ignore[arg-type]

    def test_round_trip(self) -> None:
        user = SyntheticUser(**self.valid())  # type: ignore[arg-type]

        assert user.model_dump(mode="json") == {
            "id": {"value": "U-1"},
            "company_id": {"value": "C-1"},
            "name": "Ada Martin",
            "email": "ada.martin@example.com",
        }
        assert SyntheticUser.model_validate(user.model_dump(mode="json")) == user
        assert SyntheticUser.model_validate_json(user.model_dump_json()) == user
