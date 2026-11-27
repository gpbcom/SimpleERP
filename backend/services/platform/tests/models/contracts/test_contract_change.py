from __future__ import annotations

from typing import Dict

import pytest
from erp_platform.models.contracts.contract_change import ContractChange
from erp_platform.models.contracts.enums import ContractChangeKind
from erp_platform.models.contracts.exceptions import (
    SEContractChangeInvalidKind,
    SEContractChangeInvalidLocation,
    SEInvalidContractChangeException,
)
from pydantic import JsonValue, ValidationError


class TestContractChange:
    LOCATION = "#/components/schemas/Health/properties/status"

    def test_defaults(self) -> None:
        with pytest.raises(ValidationError):
            ContractChange.model_validate({})

    def test_full_valid_construction(self) -> None:
        change = ContractChange(kind=ContractChangeKind.PROPERTY_REMOVED, location=self.LOCATION)
        assert change.kind is ContractChangeKind.PROPERTY_REMOVED
        assert change.location == self.LOCATION
        from_strings = ContractChange.model_validate({"kind": "type_changed", "location": f"  {self.LOCATION}  "})
        assert from_strings.kind is ContractChangeKind.TYPE_CHANGED
        assert from_strings.location == self.LOCATION

    @pytest.mark.parametrize(
        ("name", "error"),
        [("kind", SEContractChangeInvalidKind), ("location", SEContractChangeInvalidLocation)],
    )
    def test_none_becomes_the_default(self, name: str, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"kind": "path_removed", "location": self.LOCATION}
        data[name] = None
        with pytest.raises(error):
            ContractChange.model_validate(data)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("kind", "", SEContractChangeInvalidKind),
            ("kind", "added", SEContractChangeInvalidKind),
            ("kind", "PATH_REMOVED", SEContractChangeInvalidKind),
            ("kind", 1, SEContractChangeInvalidKind),
            ("kind", True, SEContractChangeInvalidKind),
            ("kind", ["path_removed"], SEContractChangeInvalidKind),
            ("location", "", SEContractChangeInvalidLocation),
            ("location", "   ", SEContractChangeInvalidLocation),
            ("location", "/paths/health", SEContractChangeInvalidLocation),
            ("location", "#", SEContractChangeInvalidLocation),
            ("location", 1, SEContractChangeInvalidLocation),
            ("location", ["#/paths"], SEContractChangeInvalidLocation),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        data: Dict[str, JsonValue] = {"kind": "path_removed", "location": self.LOCATION}
        data[name] = value
        with pytest.raises(error):
            ContractChange.model_validate(data)

    @pytest.mark.parametrize("error", [SEContractChangeInvalidKind, SEContractChangeInvalidLocation])
    def test_the_field_exceptions_have_the_model_base(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidContractChangeException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ContractChange.model_validate({"kind": "path_removed", "location": self.LOCATION, "unknown": 1})

    def test_it_is_frozen(self) -> None:
        change = ContractChange(kind=ContractChangeKind.PATH_REMOVED, location=self.LOCATION)
        with pytest.raises(ValidationError):
            change.location = "#/paths"

    def test_round_trip(self) -> None:
        change = ContractChange(kind=ContractChangeKind.SCHEMA_REMOVED, location=self.LOCATION)
        assert ContractChange.model_validate(change.model_dump()) == change
        assert ContractChange.model_validate_json(change.model_dump_json()) == change
