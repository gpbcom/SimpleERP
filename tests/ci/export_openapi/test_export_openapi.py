from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import ClassVar, List

import pytest


class TestExportOpenapi:
    SCRIPT: ClassVar[Path] = Path(__file__).resolve().parents[3] / ".github" / "scripts" / "export_openapi.py"

    def run_script(self, args: List[str], work_dir: Path, source: Path) -> subprocess.CompletedProcess[str]:
        assert self.SCRIPT.is_file(), f"{self.SCRIPT} does not exist."
        env = {**os.environ, "PYTHONPATH": str(source)}
        return subprocess.run(
            [sys.executable, str(self.SCRIPT), *args],
            cwd=work_dir,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )

    def test_the_document_is_written_next_to_the_service(self, service: Path, work_dir: Path) -> None:
        result = self.run_script([str(service)], work_dir, service / "src")
        assert result.returncode == 0
        assert (service / "openapi.json").is_file()

    def test_the_exact_text_is_indented_unescaped_and_ends_with_a_newline(self, service: Path, work_dir: Path) -> None:
        self.run_script([str(service)], work_dir, service / "src")
        expected = (
            "{\n"
            '  "openapi": "3.1.0",\n'
            '  "info": {\n'
            '    "title": "Sample éè service",\n'
            '    "version": "1"\n'
            "  },\n"
            '  "paths": {},\n'
            '  "zeta": "café"\n'
            "}\n"
        )
        assert (service / "openapi.json").read_bytes() == expected.encode("utf-8")

    def test_the_configuration_is_read_from_the_service_folder(self, service: Path, work_dir: Path) -> None:
        result = self.run_script([str(service)], work_dir, service / "src")
        assert result.returncode == 0
        assert "Sample éè service" in (service / "openapi.json").read_text(encoding="utf-8")

    def test_it_says_what_it_wrote_and_never_prints_the_document(self, service: Path, work_dir: Path) -> None:
        result = self.run_script([str(service)], work_dir, service / "src")
        assert result.stdout.strip() == f"Wrote {service}/openapi.json."
        assert "3.1.0" not in result.stdout
        assert result.stderr == ""

    def test_running_it_again_gives_the_same_file(self, service: Path, work_dir: Path) -> None:
        self.run_script([str(service)], work_dir, service / "src")
        first = (service / "openapi.json").read_bytes()
        result = self.run_script([str(service)], work_dir, service / "src")
        assert result.returncode == 0
        assert (service / "openapi.json").read_bytes() == first

    def test_a_missing_folder_argument_is_refused(self, service: Path, work_dir: Path) -> None:
        result = self.run_script([], work_dir, service / "src")
        assert result.returncode == 2
        assert result.stdout == ""
        assert len(result.stderr.strip().splitlines()) == 1

    @pytest.mark.parametrize(
        "fixture_name",
        ["no_package_service", "two_packages_service", "broken_import_service", "failing_factory_service"],
    )
    def test_a_service_that_cannot_be_exported_is_refused_with_one_line(
        self, fixture_name: str, request: pytest.FixtureRequest, work_dir: Path
    ) -> None:
        folder: Path = request.getfixturevalue(fixture_name)
        result = self.run_script([str(folder)], work_dir, folder / "src")
        assert result.returncode == 2
        assert result.stdout == ""
        assert len(result.stderr.strip().splitlines()) == 1
        assert not (folder / "openapi.json").exists()
