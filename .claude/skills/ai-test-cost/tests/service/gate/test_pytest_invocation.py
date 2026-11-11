from __future__ import annotations

import logging
from typing import Dict, List

import pytest

from ai_cost.service.gate.pytest_invocation import PytestInvocation


class TestPytestInvocation:
    @pytest.mark.parametrize(
        ("words", "exported", "paid"),
        [
            (["pytest", "-m", "llm"], {}, True),
            (["uv", "run", "pytest", "tests", "-m", "not slow and llm"], {}, True),
            (["python", "-m", "pytest", "-qm", "llm"], {}, True),
            (["pytest", "-mllm"], {}, True),
            (["pytest", "-m=llm"], {}, True),
            (["pytest", "--markexpr", "smoke or llm"], {}, True),
            (["pytest", "--markexpr=llm"], {}, True),
            (["pytest", "tests", "--llm"], {}, True),
            (["PYTEST_ADDOPTS=-m llm", "pytest"], {}, True),
            (["env", "-u", "HOME", "PYTEST_ADDOPTS=--llm", "uv", "run", "pytest"], {}, True),
            (["pytest", "tests"], {"PYTEST_ADDOPTS": "-q -m llm"}, True),
            (["pytest", "-m", "(llm)"], {}, True),
            (["pytest", "-m", "not llm"], {}, False),
            (["pytest", "-m", "slow and not llm"], {}, False),
            (["pytest", "-m", "llmish"], {}, False),
            (["pytest", "-q", "tests/llm"], {}, False),
            (["pytest", "-p", "no:cacheprovider", "tests"], {}, False),
            (["git", "commit", "-m", "run pytest -m llm"], {}, False),
            (["grep", "-m", "llm", "notes.md"], {}, False),
            (["PYTEST_ADDOPTS=-m llm", "git", "status"], {}, False),
        ],
    )
    def test_a_pytest_command_is_paid_when_it_selects_the_llm_marker(
        self, logger: logging.Logger, words: List[str], exported: Dict[str, str], paid: bool
    ) -> None:
        assert (PytestInvocation(logger).reason(words, exported) is not None) is paid
