from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import ClassVar

# First-party imports
from tests.ci.release_notes.helpers import RULE, TICKET, TICKET_TITLE, USE_CASE, git, make_repo, run, write_reports


class TestReleaseNotes:
    VERSION: ClassVar[str] = "0.2.0"
    FOLDER: ClassVar[Path] = Path("docs/releases/v0.2.0")

    def write(self, root: Path, reports: Path, *args: str) -> None:
        result = run(root, "write", "--version", self.VERSION, "--reports", str(reports), *args)
        assert result.returncode == 0, result.stderr

    def test_the_changelog_lists_each_commit_of_each_pull_request_by_kind(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        self.write(root, write_reports(tmp_path), "--date", "2026-11-20")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        assert changelog.startswith("# Changelog\n\nEvery release of SimpleERP")
        assert f"## [v{self.VERSION}](docs/releases/v{self.VERSION}/RELEASE_NOTES.md) - 2026-11-20" in changelog
        assert "### 🎫 Tickets" in changelog
        assert f"- {TICKET}: {TICKET_TITLE} (#7)" in changelog
        assert "### 🧰 Harness" in changelog
        assert "- Harness: every branch gets a verdict (#8)" in changelog
        assert "an old change" not in changelog

    def test_a_new_release_goes_on_top_of_the_previous_ones(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        (root / "CHANGELOG.md").write_text("# Changelog\n\nIntro.\n\n## [v0.1.0](x) - 2026-11-01\n\n- old\n")
        self.write(root, write_reports(tmp_path))
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        assert changelog.startswith("# Changelog\n\nIntro.\n\n## [v0.2.0]")
        assert changelog.index("## [v0.2.0]") < changelog.index("## [v0.1.0]")

    def test_the_unreleased_section_stays_on_top(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        (root / "CHANGELOG.md").write_text(
            "# Changelog\n\nIntro.\n\n## [Unreleased]\n\nSoon.\n\n## [v0.1.0](x)\n\n- old\n"
        )
        self.write(root, write_reports(tmp_path))
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        assert changelog.index("## [Unreleased]") < changelog.index("## [v0.2.0]") < changelog.index("## [v0.1.0]")
        assert "Soon.\n\n## [v0.2.0]" in changelog

    def test_the_release_notes_name_the_tickets_delivered_and_what_they_deliver(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        self.write(root, write_reports(tmp_path))
        notes = (root / self.FOLDER / "RELEASE_NOTES.md").read_text(encoding="utf-8")
        assert notes.startswith(f"# 🚀 SimpleERP v{self.VERSION}")
        assert f"| [{TICKET}](../../tickets/{TICKET}/EXPLAIN.md) | {TICKET_TITLE} | {USE_CASE}<br>{RULE} |" in notes
        assert "[🧪 Full test report](TEST_REPORT.md)" in notes
        assert "v0.1.0" in notes

    def test_the_test_report_sums_every_suite_of_ci(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        self.write(root, write_reports(tmp_path))
        report = (root / self.FOLDER / "TEST_REPORT.md").read_text(encoding="utf-8")
        assert report.startswith(f"# 🧪 Test report: SimpleERP v{self.VERSION}")
        assert "✅ Every test passed" in report
        assert "| ✅ python-repository/repository | 9 | 0 | 1 | 2.5 s |" in report
        assert "| ✅ python-service-sales/service-sales | 9 | 0 | 1 |" in report
        assert "| ✅ ts-frontend-backoffice/frontend-backoffice | 12 | 0 | 0 |" in report
        assert "| ✅ ts-frontend-packages-api/frontend-packages-api | 8 | 0 | 1 |" in report
        assert "| ➖ ts-frontend-packages-tokens/frontend-packages-tokens (no test ran) | 0 | 0 | 0 |" in report  # noqa: RUF001
        assert (root / self.FOLDER / "tests" / "test-report-python-repository" / "repository.xml").is_file()

    def test_a_failed_test_shows_in_the_report(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        self.write(root, write_reports(tmp_path, errors=2))
        report = (root / self.FOLDER / "TEST_REPORT.md").read_text(encoding="utf-8")
        assert "❌ 2 failed" in report
        assert "| ❌ python-repository/repository | 7 | 2 | 1 |" in report

    def test_no_release_without_its_test_reports(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        (tmp_path / "empty").mkdir()
        result = run(root, "write", "--version", self.VERSION, "--reports", str(tmp_path / "empty"))
        assert result.returncode == 1
        assert "without its tests" in result.stderr
        assert not (root / "CHANGELOG.md").exists()
        assert not (root / self.FOLDER).exists()

    def test_the_first_release_starts_after_master(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        git(root, "tag", "-d", "v0.1.0")
        assert run(root, "write", "--version", "0.1.0", "--reports", str(write_reports(tmp_path))).returncode == 0
        assert "an old change (#1)" in (root / "CHANGELOG.md").read_text(encoding="utf-8")

    def test_a_gh_ticket_commit_is_filed_under_the_tickets(self, tmp_path: Path) -> None:
        root = make_repo(tmp_path)
        (root / "gh.txt").write_text("x\n", encoding="utf-8")
        git(root, "add", "gh.txt")
        git(root, "commit", "-q", "-m", "[GH-12] feat: store a customer with its VAT number")
        self.write(root, write_reports(tmp_path))
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
        tickets = changelog.split("### 🎫 Tickets", 1)[1].split("###", 1)[0]
        assert "[GH-12] feat: store a customer with its VAT number" in tickets
