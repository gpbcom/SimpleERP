from __future__ import annotations

from decimal import Decimal
from typing import Dict, Type

import pytest
from erp_metering.models.calls.exceptions import (
    SEInvalidPaidCallException,
    SEPaidCallInvalidCompanyId,
    SEPaidCallInvalidConnector,
    SEPaidCallInvalidEstimatedCost,
    SEPaidCallInvalidFeature,
    SEPaidCallInvalidLegalDuty,
    SEPaidCallInvalidModule,
    SEPaidCallInvalidUserId,
)
from erp_metering.models.calls.paid_call import PaidCall
from erp_models.ids.company_id import CompanyId
from erp_models.money.money import Money
from pydantic import ValidationError


class TestPaidCall:
    VALID: Dict[str, object] = {
        "company_id": CompanyId(value="C-12"),
        "module": "sales",
        "feature": "invoice-ocr",
        "estimated_cost": Money(amount=Decimal("10.00"), currency="EUR"),
    }

    def test_defaults(self) -> None:
        call = PaidCall.model_validate(self.VALID)
        assert call.connector is None
        assert call.user_id is None
        assert call.legal_duty is False

    def test_full_valid_construction(self) -> None:
        call = PaidCall(
            company_id=CompanyId(value="C-12"),
            module=" sales ",
            feature="invoice-ocr",
            connector="ocr-provider",
            user_id="U-7",
            estimated_cost=Money(amount=Decimal("10.00"), currency="EUR"),
            legal_duty=True,
        )
        assert call.company_id == CompanyId(value="C-12")
        assert call.module == "sales"
        assert call.feature == "invoice-ocr"
        assert call.connector == "ocr-provider"
        assert call.user_id == "U-7"
        assert call.estimated_cost == Money(amount=Decimal("10.00"), currency="EUR")
        assert call.legal_duty is True

    @pytest.mark.parametrize(
        ("name", "expected"),
        [("connector", None), ("user_id", None), ("legal_duty", False)],
    )
    def test_none_becomes_the_default(self, name: str, expected: object) -> None:
        call = PaidCall.model_validate({**self.VALID, name: None})
        assert getattr(call, name) == expected

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("company_id", None, SEPaidCallInvalidCompanyId),
            ("company_id", 12, SEPaidCallInvalidCompanyId),
            ("module", "", SEPaidCallInvalidModule),
            ("module", "   ", SEPaidCallInvalidModule),
            ("module", True, SEPaidCallInvalidModule),
            ("module", None, SEPaidCallInvalidModule),
            ("feature", "", SEPaidCallInvalidFeature),
            ("feature", "  ", SEPaidCallInvalidFeature),
            ("feature", False, SEPaidCallInvalidFeature),
            ("feature", None, SEPaidCallInvalidFeature),
            ("connector", "", SEPaidCallInvalidConnector),
            ("connector", " ", SEPaidCallInvalidConnector),
            ("connector", True, SEPaidCallInvalidConnector),
            ("user_id", "", SEPaidCallInvalidUserId),
            ("user_id", "  ", SEPaidCallInvalidUserId),
            ("user_id", False, SEPaidCallInvalidUserId),
            ("estimated_cost", None, SEPaidCallInvalidEstimatedCost),
            ("estimated_cost", 10.0, SEPaidCallInvalidEstimatedCost),
            ("estimated_cost", "10.00 EUR", SEPaidCallInvalidEstimatedCost),
            ("estimated_cost", Money(amount=Decimal("-0.01"), currency="EUR"), SEPaidCallInvalidEstimatedCost),
            ("estimated_cost", {"amount": "-1", "currency": "EUR"}, SEPaidCallInvalidEstimatedCost),
            ("legal_duty", "yes", SEPaidCallInvalidLegalDuty),
            ("legal_duty", 1, SEPaidCallInvalidLegalDuty),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: object, error: Type[Exception]) -> None:
        with pytest.raises(error) as raised:
            PaidCall.model_validate({**self.VALID, name: value})
        assert isinstance(raised.value, SEInvalidPaidCallException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PaidCall.model_validate({**self.VALID, "unknown": "x"})

    def test_round_trip(self) -> None:
        call = PaidCall(
            company_id=CompanyId(value="C-12"),
            module="sales",
            feature="invoice-ocr",
            connector="ocr-provider",
            user_id="U-7",
            estimated_cost=Money(amount=Decimal("10.00"), currency="EUR"),
            legal_duty=True,
        )
        assert PaidCall.model_validate_json(call.model_dump_json()) == call
