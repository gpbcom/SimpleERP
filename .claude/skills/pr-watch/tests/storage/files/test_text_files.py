from __future__ import annotations

from pathlib import Path

from pr_watch.storage.files.text_files import TextFiles


class TestTextFiles:
    def test_a_missing_file_reads_as_none(self, tmp_path: Path) -> None:
        assert TextFiles().read(tmp_path / "missing.json") is None

    def test_a_write_creates_the_folders_and_leaves_no_temporary_file(self, tmp_path: Path) -> None:
        path = tmp_path / "a" / "b" / "state.json"
        TextFiles().write(path, "{}")
        TextFiles().write(path, '{"x": 1}')
        assert TextFiles().read(path) == '{"x": 1}'
        assert [child.name for child in path.parent.iterdir()] == ["state.json"]

    def test_lines_are_appended(self, tmp_path: Path) -> None:
        path = tmp_path / "log" / "operations.jsonl"
        TextFiles().append_line(path, "one")
        TextFiles().append_line(path, "two")
        assert path.read_text(encoding="utf-8") == "one\ntwo\n"
