from __future__ import annotations

import logging
from pathlib import Path

import pytest

from harness_core.testing.fake_program import FakeProgram
from harness_core.testing.git_sandbox import GitSandbox
from project_docs.service.checks.mermaid_check import MermaidCheck
from project_docs.storage.files.document_files import DocumentFiles
from project_docs.storage.mermaid.mermaid_renderer import MermaidRenderer
from tests.helpers import STAMP


class TestMermaidCheck:
    def check(self, sandbox: GitSandbox, logger: logging.Logger) -> MermaidCheck:
        return MermaidCheck(DocumentFiles(sandbox.root, logger), MermaidRenderer(logger), logger)

    @pytest.fixture
    def fake_mmdc(self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeProgram:
        monkeypatch.setenv("PATH", f"{tmp_path / 'bin'}:/usr/bin:/bin")
        fake = FakeProgram(tmp_path / "bin")
        fake.write("mmdc", 'if grep -q broken "$3"; then echo "Parse error on line 2" >&2; exit 1; fi; touch "$5"')
        return fake

    def test_without_mmdc_nothing_is_printed_and_a_warning_is_logged(
        self,
        sandbox: GitSandbox,
        logger: logging.Logger,
        monkeypatch: pytest.MonkeyPatch,
        caplog: pytest.LogCaptureFixture,
    ) -> None:
        monkeypatch.setenv("PATH", "/usr/bin:/bin")
        caplog.set_level(logging.WARNING)
        assert self.check(sandbox, logger).problems() == []
        assert "mmdc" in caplog.text

    def test_blocks_that_render_have_no_problem(
        self, sandbox: GitSandbox, logger: logging.Logger, fake_mmdc: FakeProgram
    ) -> None:
        assert self.check(sandbox, logger).problems() == []

    def test_a_block_that_does_not_render_is_reported_with_its_line(
        self, sandbox: GitSandbox, logger: logging.Logger, fake_mmdc: FakeProgram
    ) -> None:
        sandbox.write(
            "docs/technical/api.md",
            f"# API\n\n```mermaid\nflowchart LR\n    broken -->\n```\n\n```bash\nbroken\n```\n\n{STAMP}\n",
        )
        assert self.check(sandbox, logger).problems() == [
            "docs/technical/api.md:3: Mermaid block does not render: Parse error on line 2"
        ]
