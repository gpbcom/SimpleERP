from __future__ import annotations

from pathlib import Path

import yaml


class TestSkillFile:
    def _front_matter(self, skill_root: Path) -> dict:
        text = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n")
        return yaml.safe_load(text.split("---\n", 2)[1])

    def test_the_skill_is_named_progress_updates(self, skill_root: Path) -> None:
        assert self._front_matter(skill_root)["name"] == "progress-updates"

    def test_its_description_names_what_triggers_it(self, skill_root: Path) -> None:
        description = self._front_matter(skill_root)["description"].lower()
        for words in ("background", "subagent", "workflow", "every 2 minutes", "ci"):
            assert words in description

    def test_its_body_gives_the_steps_and_the_template(self, skill_root: Path) -> None:
        body = (skill_root / "SKILL.md").read_text(encoding="utf-8").split("---\n", 2)[2]
        for words in ("progress-updates watch --every 120", "progress-updates status", "Monitor", "TaskStop"):
            assert words in body
