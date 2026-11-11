from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import JsonValue

from ai_cost.models.settings.caller_environment import CallerEnvironment
from ai_cost.models.settings.exceptions import (
    SECallerEnvironmentInvalidApiKeyId,
    SECallerEnvironmentInvalidCallerCwd,
)


class TestCallerEnvironment:
    def test_defaults(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("AI_COST_CALLER_CWD", raising=False)
        monkeypatch.delenv("AI_COST_API_KEY_ID", raising=False)
        environment = CallerEnvironment()
        assert (environment.caller_cwd, environment.api_key_id) == (Path.cwd(), None)

    def test_full_valid_construction(self, tmp_path: Path) -> None:
        environment = CallerEnvironment(caller_cwd=tmp_path, api_key_id=" apikey_01Rj2N8SVvo6BePZj99NhmiT ")
        assert (environment.caller_cwd, environment.api_key_id) == (tmp_path, "apikey_01Rj2N8SVvo6BePZj99NhmiT")

    def test_the_environment_sets_the_harmless_values(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("AI_COST_CALLER_CWD", str(tmp_path))
        monkeypatch.setenv("AI_COST_API_KEY_ID", "apikey_01")
        monkeypatch.setenv("AI_COST_DEFAULT_CAP_USD", "1000")
        assert CallerEnvironment().model_dump() == {"caller_cwd": tmp_path, "api_key_id": "apikey_01"}

    def test_none_becomes_the_default(self) -> None:
        environment = CallerEnvironment.model_validate({"caller_cwd": None, "api_key_id": None})
        assert (environment.caller_cwd, environment.api_key_id) == (Path.cwd(), None)

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("caller_cwd", "", SECallerEnvironmentInvalidCallerCwd),
            ("caller_cwd", 3, SECallerEnvironmentInvalidCallerCwd),
            ("api_key_id", " ", SECallerEnvironmentInvalidApiKeyId),
            ("api_key_id", 3, SECallerEnvironmentInvalidApiKeyId),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            CallerEnvironment.model_validate({name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            CallerEnvironment.model_validate({"default_cap_usd": "1000"})

    def test_round_trip(self, tmp_path: Path) -> None:
        environment = CallerEnvironment(caller_cwd=tmp_path, api_key_id="apikey_01")
        assert CallerEnvironment.model_validate(environment.model_dump()) == environment
