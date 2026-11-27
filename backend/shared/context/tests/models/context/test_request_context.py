from __future__ import annotations

from typing import Dict

import pytest
from erp_context.models.context.exceptions import SERequestContextInvalidRequestId, SERequestContextInvalidUser
from erp_context.models.context.request_context import RequestContext
from erp_context.models.context.user_context import UserContext
from erp_models.ids.company_id import CompanyId
from pydantic import JsonValue, ValidationError


class TestRequestContext:
    def test_defaults(self) -> None:
        user = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        with pytest.raises(ValidationError):
            RequestContext.model_validate({})
        with pytest.raises(ValidationError):
            RequestContext.model_validate({"user": user})
        with pytest.raises(ValidationError):
            RequestContext.model_validate({"request_id": "R-1"})

    def test_full_valid_construction(self) -> None:
        user = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        context = RequestContext(user=user, request_id=" R-1 ")
        assert context.user == user
        assert context.request_id == "R-1"

    def test_none_becomes_the_default(self) -> None:
        assert all(field.is_required() for field in RequestContext.model_fields.values())

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("request_id", "", SERequestContextInvalidRequestId),
            ("request_id", "   ", SERequestContextInvalidRequestId),
            ("request_id", None, SERequestContextInvalidRequestId),
            ("request_id", 42, SERequestContextInvalidRequestId),
            ("request_id", True, SERequestContextInvalidRequestId),
            ("user", None, SERequestContextInvalidUser),
            ("user", "U-1", SERequestContextInvalidUser),
            ("user", 42, SERequestContextInvalidUser),
            ("user", True, SERequestContextInvalidUser),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {
            "user": {"user_id": "U-1", "company_id": {"value": "C-12"}},
            "request_id": "R-1",
        }
        data[name] = value
        with pytest.raises(error):
            RequestContext.model_validate(data)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RequestContext.model_validate(
                {"user": {"user_id": "U-1", "company_id": {"value": "C-12"}}, "request_id": "R-1", "unknown": 1}
            )

    def test_round_trip(self) -> None:
        user = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        context = RequestContext(user=user, request_id="R-1")
        assert RequestContext.model_validate(context.model_dump()) == context
        assert RequestContext.model_validate_json(context.model_dump_json()) == context

    def test_assignment_is_refused_because_the_model_is_frozen(self) -> None:
        user = UserContext(user_id="U-1", company_id=CompanyId(value="C-12"))
        context = RequestContext(user=user, request_id="R-1")
        with pytest.raises(ValidationError):
            context.request_id = "R-2"
