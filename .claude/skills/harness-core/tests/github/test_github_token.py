from __future__ import annotations

from pathlib import Path

import pytest

from harness_core.github.exceptions import SEGithubError, SEGithubTokenMissingError
from harness_core.github.github_token import GithubToken
from harness_core.testing.fake_program import FakeProgram


class TestGithubToken:
    @pytest.fixture(autouse=True)
    def fake_gh(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeProgram:
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        monkeypatch.setenv("PATH", f"{tmp_path / 'bin'}:/usr/bin:/bin")
        return FakeProgram(tmp_path / "bin")

    def test_the_variable_wins(self, monkeypatch: pytest.MonkeyPatch, fake_gh: FakeProgram) -> None:
        fake_gh.write("gh", "echo from-gh")
        monkeypatch.setenv("GITHUB_TOKEN", " from-variable ")
        assert GithubToken().read() == "from-variable"

    def test_the_github_cli_gives_the_token(self, fake_gh: FakeProgram) -> None:
        fake_gh.write("gh", '[ "$*" = "auth token" ] && echo from-gh')
        assert GithubToken().read() == "from-gh"

    def test_a_logged_out_github_cli_is_reported(self, fake_gh: FakeProgram) -> None:
        fake_gh.write("gh", "echo 'not logged in' >&2; exit 1")
        with pytest.raises(SEGithubTokenMissingError, match="GITHUB_TOKEN"):
            GithubToken().read()

    def test_a_missing_github_cli_is_reported(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
        monkeypatch.setenv("PATH", str(tmp_path / "empty"))
        with pytest.raises(SEGithubTokenMissingError):
            GithubToken().read()
        assert issubclass(SEGithubTokenMissingError, SEGithubError)
