from __future__ import annotations

import logging
from pathlib import Path

from release_notes.storage.files.text_files import TextFiles


class TestTextFiles:
    def test_read_write_exists_and_delete(self, tmp_path: Path, logger: logging.Logger) -> None:
        files = TextFiles(tmp_path, logger)
        assert files.read("CHANGELOG.md") == ""
        assert not files.exists("CHANGELOG.md")
        files.write("CHANGELOG.md", "# Changelog\n")
        assert files.exists("CHANGELOG.md")
        assert files.read("CHANGELOG.md") == "# Changelog\n"
        files.delete("CHANGELOG.md")
        assert not files.exists("CHANGELOG.md")

    def test_names_lists_the_files_of_a_folder(self, tmp_path: Path, logger: logging.Logger) -> None:
        (tmp_path / "changelog.d" / "old").mkdir(parents=True)
        for name in ["README.md", "GH-2.fixed.md", "GH-10.added.md"]:
            (tmp_path / "changelog.d" / name).write_text("x\n", encoding="utf-8")
        files = TextFiles(tmp_path, logger)
        assert files.names("changelog.d") == ["GH-10.added.md", "GH-2.fixed.md", "README.md"]
        assert files.names("missing.d") == []
