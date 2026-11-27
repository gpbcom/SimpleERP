from __future__ import annotations

from typing import List

import pytest
from erp_context.models.context.context_config import ContextConfig
from erp_context.models.context.exceptions import (
    SEContextConfigInvalidCompanyHeader,
    SEContextConfigInvalidPublicPaths,
    SEContextConfigInvalidRequestHeader,
    SEContextConfigInvalidUserHeader,
)
from pydantic import JsonValue, ValidationError


class TestContextConfig:
    def test_defaults(self) -> None:
        config = ContextConfig()
        assert config.company_header == "X-Company-Id"
        assert config.user_header == "X-User-Id"
        assert config.request_header == "X-Request-Id"
        assert config.public_paths == []

    def test_full_valid_construction(self) -> None:
        paths: List[str] = ["/health", "/docs"]
        config = ContextConfig(company_header="X-Co", user_header="X-Us", request_header="X-Rq", public_paths=paths)
        assert config.company_header == "X-Co"
        assert config.user_header == "X-Us"
        assert config.request_header == "X-Rq"
        assert config.public_paths == paths

    @pytest.mark.parametrize(
        ("name", "default"),
        [
            ("company_header", "X-Company-Id"),
            ("user_header", "X-User-Id"),
            ("request_header", "X-Request-Id"),
            ("public_paths", []),
        ],
    )
    def test_none_becomes_the_default(self, name: str, default: JsonValue) -> None:
        config = ContextConfig.model_validate({name: None})
        assert getattr(config, name) == default

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("company_header", "", SEContextConfigInvalidCompanyHeader),
            ("company_header", "   ", SEContextConfigInvalidCompanyHeader),
            ("company_header", 42, SEContextConfigInvalidCompanyHeader),
            ("company_header", True, SEContextConfigInvalidCompanyHeader),
            ("user_header", "", SEContextConfigInvalidUserHeader),
            ("user_header", "   ", SEContextConfigInvalidUserHeader),
            ("user_header", 42, SEContextConfigInvalidUserHeader),
            ("user_header", True, SEContextConfigInvalidUserHeader),
            ("request_header", "", SEContextConfigInvalidRequestHeader),
            ("request_header", "   ", SEContextConfigInvalidRequestHeader),
            ("request_header", 42, SEContextConfigInvalidRequestHeader),
            ("request_header", True, SEContextConfigInvalidRequestHeader),
            ("public_paths", "/health", SEContextConfigInvalidPublicPaths),
            ("public_paths", 42, SEContextConfigInvalidPublicPaths),
            ("public_paths", True, SEContextConfigInvalidPublicPaths),
            ("public_paths", ["health"], SEContextConfigInvalidPublicPaths),
            ("public_paths", [""], SEContextConfigInvalidPublicPaths),
            ("public_paths", ["/ok", 42], SEContextConfigInvalidPublicPaths),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            ContextConfig.model_validate({name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValidationError):
            ContextConfig.model_validate({"unknown": 1})

    def test_round_trip(self) -> None:
        config = ContextConfig(company_header="X-Co", public_paths=["/health"])
        assert ContextConfig.model_validate(config.model_dump()) == config
        assert ContextConfig.model_validate_json(config.model_dump_json()) == config
