from __future__ import annotations

from typing import Dict, Type

import pytest
from erp_context.models.refusals.enums import RefusalReason
from erp_context.models.refusals.exceptions import (
    SERefusalCodeInvalidActionKey,
    SERefusalCodeInvalidCode,
    SERefusalCodeInvalidReason,
    SERefusalCodeInvalidReference,
    SERefusalCodeInvalidStatus,
    SERefusalCodeInvalidTitleKey,
    SERefusalCodeInvalidWhyKey,
)
from erp_context.models.refusals.refusal_code import RefusalCode
from pydantic import JsonValue, ValidationError


class TestRefusalCode:
    VALID: Dict[str, JsonValue] = {
        "reason": "no-company",
        "code": "ACCESS-COMPANY-01",
        "status": 400,
        "title_key": "errors.access_company_01.title",
        "why_key": "errors.access_company_01.why",
        "action_key": "errors.access_company_01.action",
        "reference": "ACCESS-COMPANY-01",
    }

    ERRORS: Dict[str, Type[Exception]] = {
        "reason": SERefusalCodeInvalidReason,
        "code": SERefusalCodeInvalidCode,
        "status": SERefusalCodeInvalidStatus,
        "title_key": SERefusalCodeInvalidTitleKey,
        "why_key": SERefusalCodeInvalidWhyKey,
        "action_key": SERefusalCodeInvalidActionKey,
        "reference": SERefusalCodeInvalidReference,
    }

    BAD_PATTERNS = ["", "   ", 12, True, ["SITE-CLOSE-01"], "SITE-CLOSE", "SITE-CLOSE-1", "site-close-01", "SITE--01"]
    BAD_KEYS = ["", "   ", 12, True, ["errors.a"], "Errors.a", "errors a", "Close the site first.", "a-b"]

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            RefusalCode.model_validate({})
        for name in self.VALID:
            partial = {key: value for key, value in self.VALID.items() if key != name}
            with pytest.raises(ValidationError):
                RefusalCode.model_validate(partial)

    def test_full_valid_construction(self) -> None:
        code = RefusalCode(
            reason=RefusalReason.NO_COMPANY,
            code=" ACCESS-COMPANY-01 ",
            status=400,
            title_key=" errors.access_company_01.title ",
            why_key="errors.access_company_01.why",
            action_key="errors.access_company_01.action",
            reference=" ACCESS-COMPANY-01",
        )

        assert code.reason is RefusalReason.NO_COMPANY
        assert code.code == "ACCESS-COMPANY-01"
        assert code.status == 400
        assert code.title_key == "errors.access_company_01.title"
        assert code.reference == "ACCESS-COMPANY-01"

    @pytest.mark.parametrize("name", list(VALID))
    def test_none_becomes_the_default(self, name: str) -> None:
        values: Dict[str, JsonValue] = {**self.VALID, name: None}

        with pytest.raises(self.ERRORS[name]):
            RefusalCode.model_validate(values)

    @pytest.mark.parametrize(
        ("name", "value"),
        [
            *[("code", value) for value in BAD_PATTERNS],
            *[("reference", value) for value in BAD_PATTERNS],
            *[(name, value) for value in BAD_KEYS for name in ("title_key", "why_key", "action_key")],
            *[("status", value) for value in (True, False, "403", 403.0, 399, 600, 0, -1, [403])],
            *[("reason", value) for value in ("", "unknown", 3, True, ["no-company"])],
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue) -> None:
        values: Dict[str, JsonValue] = {**self.VALID, name: value}

        with pytest.raises(self.ERRORS[name]):
            RefusalCode.model_validate(values)

    @pytest.mark.parametrize("status", [400, 403, 599])
    def test_the_status_bounds_are_accepted(self, status: int) -> None:
        assert RefusalCode.model_validate({**self.VALID, "status": status}).status == status

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            RefusalCode.model_validate({**self.VALID, "other": "x"})

    def test_round_trip(self) -> None:
        code = RefusalCode.model_validate(self.VALID)

        assert RefusalCode.model_validate(code.model_dump()) == code
        assert RefusalCode.model_validate_json(code.model_dump_json()) == code

    def test_the_code_is_frozen(self) -> None:
        code = RefusalCode.model_validate(self.VALID)

        with pytest.raises(ValidationError):
            code.status = 403
