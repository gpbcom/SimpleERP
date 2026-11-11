from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.testing.fake_program import FakeProgram
from project_docs.storage.mermaid.mermaid_renderer import MermaidRenderer


class TestMermaidRenderer:
    @pytest.fixture
    def fake_mmdc(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeProgram:
        monkeypatch.setenv("PATH", f"{tmp_path / 'bin'}:/usr/bin:/bin")
        return FakeProgram(tmp_path / "bin")

    def test_without_mmdc_on_the_path_nothing_can_render(
        self, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        monkeypatch.setenv("PATH", "/usr/bin:/bin")
        assert not MermaidRenderer(logger).available()

    def test_a_block_that_renders_gives_no_error_and_reaches_mmdc_as_a_file(
        self, fake_mmdc: FakeProgram, tmp_path: Path, logger: logging.Logger
    ) -> None:
        seen = tmp_path / "seen.mmd"
        fake_mmdc.write("mmdc", f'[ "$1 $2 $4" = "-q -i -o" ] && cp "$3" {seen} && touch "$5"')
        renderer = MermaidRenderer(logger)
        assert renderer.available()
        assert renderer.render("flowchart LR\n    A --> B\n") is None
        assert seen.read_text(encoding="utf-8") == "flowchart LR\n    A --> B\n"

    def test_a_block_that_fails_gives_the_last_line_mmdc_printed(
        self, fake_mmdc: FakeProgram, logger: logging.Logger
    ) -> None:
        fake_mmdc.write("mmdc", "echo 'Rendering' ; echo 'Error: Parse error on line 2:' >&2 ; echo '' >&2 ; exit 1")
        assert MermaidRenderer(logger).render("flowchart LR\n    A -->\n") == "Error: Parse error on line 2:"

    def test_a_failure_without_output_names_the_exit_code(self, fake_mmdc: FakeProgram, logger: logging.Logger) -> None:
        fake_mmdc.write("mmdc", "exit 3")
        assert MermaidRenderer(logger).render("x\n") == "mmdc exited with code 3."
