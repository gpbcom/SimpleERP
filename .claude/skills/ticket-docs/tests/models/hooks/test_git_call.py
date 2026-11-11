from __future__ import annotations

from pathlib import Path
from typing import Dict

import pytest
from pydantic import JsonValue

from ticket_docs.models.hooks.exceptions import (
    SEGitCallInvalidArguments,
    SEGitCallInvalidDirectory,
    SEGitCallInvalidSubcommand,
)
from ticket_docs.models.hooks.git_call import GitCall


class TestGitCall:
    VALID: Dict[str, JsonValue] = {"subcommand": "push", "arguments": ["origin", "develop"], "directory": "/repo"}

    def test_defaults(self) -> None:
        assert GitCall(subcommand="status", directory="/repo").arguments == []

    def test_full_valid_construction(self) -> None:
        call = GitCall.model_validate(self.VALID)
        assert (call.subcommand, call.arguments, call.directory) == ("push", ["origin", "develop"], Path("/repo"))

    @pytest.mark.parametrize("name", ["arguments"])
    def test_none_becomes_the_default(self, name: str) -> None:
        assert getattr(GitCall.model_validate({**self.VALID, name: None}), name) == []

    @pytest.mark.parametrize(
        ("name", "value", "error"),
        [
            ("subcommand", "", SEGitCallInvalidSubcommand),
            ("subcommand", 3, SEGitCallInvalidSubcommand),
            ("arguments", "origin develop", SEGitCallInvalidArguments),
            ("arguments", ["origin", 3], SEGitCallInvalidArguments),
            ("directory", "", SEGitCallInvalidDirectory),
            ("directory", None, SEGitCallInvalidDirectory),
        ],
    )
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None:
        with pytest.raises(error):
            GitCall.model_validate({**self.VALID, name: value})

    def test_rejects_unknown_keys(self) -> None:
        with pytest.raises(ValueError, match="extra"):
            GitCall.model_validate({**self.VALID, "env": {}})

    def test_round_trip(self) -> None:
        call = GitCall.model_validate(self.VALID)
        assert GitCall.model_validate(call.model_dump()) == call
