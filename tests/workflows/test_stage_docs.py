"""Every page that shows how to start a stage gives the commit as ``ref=$(git rev-parse HEAD)`` (GH-13)."""

from __future__ import annotations

from pathlib import Path
from typing import List

import pytest

ROOT = Path(__file__).resolve().parents[2]
PAGES = [
    ".claude/rules/git-rules-and-deploy.md",
    ".claude/rules/TESTS-NOTICE.md",
    ".claude/skills/ticket-docs/SKILL.md",
    ".claude/harness-docs/HOWTO.md",
    "docs/technical/ci-cd-and-stages.md",
]
COMMAND = "gh workflow run stage.yml"
REF = "ref=$(git rev-parse HEAD)"


class TestStageDocs:
    @pytest.mark.parametrize("page", PAGES)
    def test_every_stage_command_gives_the_full_commit(self, page: str) -> None:
        lines = (ROOT / page).read_text(encoding="utf-8").splitlines()
        commands: List[str] = [line for line in lines if COMMAND in line]
        assert commands
        assert all(REF in line for line in commands)
