from __future__ import annotations

import logging
from pathlib import Path
from typing import List, Tuple

import pytest

from harness_core.shell.shell_command_splitter import ShellCommandSplitter
from ticket_docs.service.hooks.git_invocations import GitInvocations


class TestGitInvocations:
    @pytest.mark.parametrize(
        ("command", "calls"),
        [
            ("git status", [("status", [], ".")]),
            ("git -C sub -c core.pager=cat push origin develop", [("push", ["origin", "develop"], "sub")]),
            ("cd sub && git commit -m 'x y'", [("commit", ["-m", "x y"], "sub")]),
            ("cd /abs && cd rel; git add -A", [("add", ["-A"], "/abs/rel")]),
            ("env -u X GIT_TRACE=1 /usr/bin/git --no-pager log", [("log", [], ".")]),
            ("echo git push origin master", []),
            ("git commit -m \"$(cat <<'EOF'\ngit push origin develop\nEOF\n)\"", [("commit", ["-m"], ".")]),
            ("bash -c 'git push origin master'", [("push", ["origin", "master"], ".")]),
            ("git", []),
        ],
    )
    def test_each_git_call_is_found_with_its_folder(
        self, logger: logging.Logger, tmp_path: Path, command: str, calls: List[Tuple[str, List[str], str]]
    ) -> None:
        found = GitInvocations(ShellCommandSplitter(logger), logger).calls(command, tmp_path)
        assert len(found) == len(calls)
        for call, (name, arguments, folder) in zip(found, calls, strict=True):
            assert (call.subcommand, call.arguments[: len(arguments)]) == (name, arguments)
            assert call.directory == (tmp_path / folder).resolve()
