from __future__ import annotations

from typing import Dict, List, Union

import pytest
from erp_config.models.config_section import ConfigSection
from erp_platform.models.config.exceptions import (
    SEInvalidPlatformConfigException,
    SEPlatformConfigInvalidErrorCodesPath,
    SEPlatformConfigInvalidPublicPaths,
)
from erp_platform.models.config.platform_config import PlatformConfig
from pydantic import JsonValue, ValidationError


class TestPlatformConfig:
    def test_defaults(self) -> None:
        config = PlatformConfig()
        assert config.public_paths == ["/v1/health"]
        assert config.error_codes_path == "conf/catalogs/error_codes.yaml"

    def test_it_is_a_configuration_section(self) -> None:
        assert issubclass(PlatformConfig, ConfigSection)

    @pytest.mark.parametrize("name", ["host", "port"])
    def test_the_address_and_the_port_are_uvicorns_not_the_services(self, name: str) -> None:
        assert name not in PlatformConfig.model_fields

    def test_full_valid_construction(self) -> None:
        config = PlatformConfig(public_paths=["/v1/health", "/v1/ready"], error_codes_path="  conf/other.yaml  ")
        assert config.public_paths == ["/v1/health", "/v1/ready"]
        assert config.error_codes_path == "conf/other.yaml"

    @pytest.mark.parametrize("name", ["public_paths", "error_codes_path"])
    def test_none_becomes_the_default(self, name: str) -> None:
        config = PlatformConfig.model_validate({name: None})
        assert getattr(config, name) == PlatformConfig.model_fields[name].get_default(call_default_factory=True)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("public_paths", "/v1/health", SEPlatformConfigInvalidPublicPaths),
            ("public_paths", [""], SEPlatformConfigInvalidPublicPaths),
            ("public_paths", ["   "], SEPlatformConfigInvalidPublicPaths),
            ("public_paths", ["v1/health"], SEPlatformConfigInvalidPublicPaths),
            ("public_paths", ["/v1/health", 3], SEPlatformConfigInvalidPublicPaths),
            ("public_paths", [None], SEPlatformConfigInvalidPublicPaths),
            ("public_paths", 7, SEPlatformConfigInvalidPublicPaths),
            ("error_codes_path", "", SEPlatformConfigInvalidErrorCodesPath),
            ("error_codes_path", "   ", SEPlatformConfigInvalidErrorCodesPath),
            ("error_codes_path", 5, SEPlatformConfigInvalidErrorCodesPath),
            ("error_codes_path", True, SEPlatformConfigInvalidErrorCodesPath),
            ("error_codes_path", ["a"], SEPlatformConfigInvalidErrorCodesPath),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            PlatformConfig.model_validate({name: value})

    @pytest.mark.parametrize("error", [SEPlatformConfigInvalidPublicPaths, SEPlatformConfigInvalidErrorCodesPath])
    def test_the_field_exceptions_share_the_model_base(self, error: type[Exception]) -> None:
        assert issubclass(error, SEInvalidPlatformConfigException)

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            PlatformConfig.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        config = PlatformConfig(public_paths=["/v1/health", "/v1/ready"], error_codes_path="conf/other.yaml")
        data: Dict[str, Union[str, List[str]]] = config.model_dump()
        assert PlatformConfig.model_validate(data) == config
        assert PlatformConfig.model_validate_json(config.model_dump_json()) == config
