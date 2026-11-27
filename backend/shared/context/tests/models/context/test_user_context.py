from __future__ import annotations

from typing import Dict

import pytest
from erp_context.models.context.exceptions import SEUserContextInvalidCompanyId, SEUserContextInvalidUserId
from erp_context.models.context.user_context import UserContext
from erp_models.ids.company_id import CompanyId
from pydantic import JsonValue, ValidationError


class TestUserContext:
    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            UserContext.model_validate({})
        with pytest.raises(ValidationError):
            UserContext.model_validate({"user_id": "U-1"})
        with pytest.raises(ValidationError):
            UserContext.model_validate({"company_id": CompanyId(value="C-12")})

    def test_full_valid_construction(self) -> None:
        context = UserContext(user_id="  U-1 ", company_id=CompanyId(value="C-12"))
        assert context.user_id == "U-1"
        assert context.company_id == CompanyId(value="C-12")

    def test_none_becomes_the_default(self) -> None:
        assert all(field.is_required() for field in UserContext.model_fields.values())

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("user_id", "", SEUserContextInvalidUserId),
            ("user_id", "   ", SEUserContextInvalidUserId),
            ("user_id", None, SEUserContextInvalidUserId),
            ("user_id", 42, SEUserContextInvalidUserId),
            ("user_id", True, SEUserContextInvalidUserId),
            ("company_id", None, SEUserContextInvalidCompanyId),
            ("company_id", 42, SEUserContextInvalidCompanyId),
            ("company_id", True, SEUserContextInvalidCompanyId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"user_id": "U-1", "company_id": {"value": "C-12"}}
        data[name] = value
        with pytest.raises(error):
            UserContext.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            UserContext.model_validate({"user_id": "U-1", "company_id": {"value": "C-12"}, "unknown": 1})

    def test_round_trip(self) -> None:
        context = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        assert UserContext.model_validate(context.model_dump()) == context
        assert UserContext.model_validate_json(context.model_dump_json()) == context

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        context = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        with pytest.raises(ValidationError):
            context.user_id = "U-2"
