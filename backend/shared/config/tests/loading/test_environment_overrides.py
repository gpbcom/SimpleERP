from __future__ import annotations

import logging
from typing import Dict, List

import pytest
from erp_config.loading.environment_overrides import EnvironmentOverrides
from erp_config.models.exceptions import SEAppConfigUnknownOverrideError
from pydantic import JsonValue


class TestEnvironmentOverrides:
    def a_config(self) -> Dict[str, JsonValue]:
        return {"server": {"port": 8000, "debug": False, "name": "erp", "db": {"pool": {"size": 5}}}}

    def test_an_environment_value_replaces_the_default(self) -> None:
        result = EnvironmentOverrides("erp", {"ERP__SERVER__PORT": "6543"}).apply(self.a_config())
        assert result["server"]["port"] == 6543  # type: ignore[index]
        assert isinstance(result["server"]["port"], int)  # type: ignore[index]

    @pytest.mark.parametrize(
        ("field", "text", "expected"),
        [("port", "6543", 6543), ("debug", "true", True), ("name", "billing", "billing")],
    )
    def test_values_are_parsed_as_yaml(self, field: str, text: str, expected: JsonValue) -> None:
        result = EnvironmentOverrides("erp", {f"ERP__SERVER__{field.upper()}": text}).apply(self.a_config())
        assert result["server"][field] == expected  # type: ignore[index]

    def test_a_nested_path_is_replaced(self) -> None:
        result = EnvironmentOverrides("erp", {"ERP__SERVER__DB__POOL__SIZE": "20"}).apply(self.a_config())
        assert result["server"]["db"]["pool"]["size"] == 20  # type: ignore[index]

    @pytest.mark.parametrize("name", ["OTHER__SERVER__PORT", "ERPX__SERVER__PORT"])
    def test_variables_of_another_prefix_are_ignored(self, name: str) -> None:
        overrides = EnvironmentOverrides("erp", {name: "1"})
        assert overrides.variables() == []
        assert overrides.apply(self.a_config()) == self.a_config()

    def test_the_input_data_is_not_mutated(self) -> None:
        data = self.a_config()
        EnvironmentOverrides("erp", {"ERP__SERVER__PORT": "6543"}).apply(data)
        assert data == self.a_config()

    def test_variables_are_sorted(self) -> None:
        environ = {"ERP__SERVER__PORT": "1", "ERP__SERVER__DEBUG": "true", "ERP__SERVER__NAME": "x", "HOME": "/"}
        expected: List[str] = ["ERP__SERVER__DEBUG", "ERP__SERVER__NAME", "ERP__SERVER__PORT"]
        assert EnvironmentOverrides("erp", environ).variables() == expected

    @pytest.mark.parametrize("name", ["ERP__SERVER__MISSING", "ERP__NOSECTION__PORT"])
    def test_an_unknown_path_is_refused(self, name: str) -> None:
        with pytest.raises(SEAppConfigUnknownOverrideError) as raised:
            EnvironmentOverrides("erp", {name: "s3cr3t-entry"}).apply(self.a_config())
        assert name in str(raised.value)
        assert "s3cr3t-entry" not in str(raised.value)

    def test_a_path_through_a_scalar_is_refused(self) -> None:
        with pytest.raises(SEAppConfigUnknownOverrideError):
            EnvironmentOverrides("erp", {"ERP__SERVER__PORT__DEEPER": "1"}).apply(self.a_config())

    def test_an_override_value_is_never_logged(self, caplog: pytest.LogCaptureFixture) -> None:
        with caplog.at_level(logging.DEBUG):
            EnvironmentOverrides("erp", {"ERP__SERVER__NAME": "s3cr3t-entry"}).apply(self.a_config())
        assert "ERP__SERVER__NAME" in caplog.text
        assert "s3cr3t-entry" not in caplog.text
