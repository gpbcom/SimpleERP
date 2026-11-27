from __future__ import annotations

from enum import StrEnum
from typing import Dict

import pytest
from erp_platform.models.contracts.enums import ContractChangeKind


class TestContractChangeKind:
    def test_it_is_a_string_enum(self) -> None:
        assert issubclass(ContractChangeKind, StrEnum)

    def test_its_members_and_values_are_exactly_the_specified_ones(self) -> None:
        expected: Dict[str, str] = {
            "PATH_REMOVED": "path_removed",
            "OPERATION_REMOVED": "operation_removed",
            "PARAMETER_REMOVED": "parameter_removed",
            "SCHEMA_REMOVED": "schema_removed",
            "PROPERTY_REMOVED": "property_removed",
            "TYPE_CHANGED": "type_changed",
        }
        assert {member.name: member.value for member in ContractChangeKind} == expected

    @pytest.mark.parametrize(
        ("member", "value"),
        [(member, member.value) for member in ContractChangeKind],
    )
    def test_each_member_equals_its_string(self, member: ContractChangeKind, value: str) -> None:
        assert member == value
        assert ContractChangeKind(value) is member

    def test_its_members_are_unique(self) -> None:
        values = [member.value for member in ContractChangeKind]
        assert len(values) == len(set(values))

    def test_an_unknown_value_is_refused(self) -> None:
        with pytest.raises(ValueError, match="path_added"):
            ContractChangeKind("path_added")
