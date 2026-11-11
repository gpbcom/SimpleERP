from __future__ import annotations

import logging
from typing import List

import pytest

from harness_core.shell.shell_command_splitter import ShellCommandSplitter


class TestShellCommandSplitter:
    @pytest.mark.parametrize(
        ("command", "words"),
        [
            ("git status", [["git", "status"]]),
            ("cd app && pytest -m 'not slow and llm'", [["cd", "app"], ["pytest", "-m", "not slow and llm"]]),
            ("a; b || c | d & e", [["a"], ["b"], ["c"], ["d"], ["e"]]),
            ("a\nb", [["a"], ["b"]]),
            ("pytest \\\n  -m llm", [["pytest", "-m", "llm"]]),
            ('echo "one\ntwo"', [["echo", "one\ntwo"]]),
            (
                "bash -c 'cd app && pytest -m llm'",
                [["bash", "-c", "cd app && pytest -m llm"], ["cd", "app"], ["pytest", "-m", "llm"]],
            ),
            ('sh -ec "pytest --llm"', [["sh", "-ec", "pytest --llm"], ["pytest", "--llm"]]),
            ("env A=1 bash -c 'x y'", [["env", "A=1", "bash", "-c", "x y"], ["x", "y"]]),
            ("nohup sh -c 'x; y'", [["nohup", "sh", "-c", "x; y"], ["x"], ["y"]]),
            ("PYTEST_ADDOPTS='-m llm' pytest", [["PYTEST_ADDOPTS=-m llm", "pytest"]]),
            ("pytest -q 2>&1 | tail", [["pytest", "-q", "2", ">&", "1"], ["tail"]]),
        ],
    )
    def test_a_command_splits_into_its_simple_commands(
        self, logger: logging.Logger, command: str, words: List[List[str]]
    ) -> None:
        assert ShellCommandSplitter(logger).commands(command) == words

    def test_an_unbalanced_quote_still_gives_the_words(self, logger: logging.Logger) -> None:
        assert ShellCommandSplitter(logger).commands("pytest -m 'llm") == [["pytest", "-m", "'llm"]]

    @pytest.mark.parametrize(
        ("command", "kept"),
        [
            ("python3 - <<'PY'\nprint('pytest -m llm')\nPY", "python3 - "),
            ("cat > notes.md <<EOF\npytest -m llm\nEOF\ngit add notes.md", "cat > notes.md \ngit add notes.md"),
            ("bash <<'EOF'\npytest -m llm\nEOF", "bash <<'EOF'\npytest -m llm\nEOF"),
        ],
    )
    def test_here_documents_fed_to_programs_that_are_not_shells_are_dropped(
        self, logger: logging.Logger, command: str, kept: str
    ) -> None:
        assert ShellCommandSplitter(logger).without_data(command) == kept
