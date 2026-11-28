from __future__ import annotations

# Standard library imports
from pathlib import Path

# First-party imports
from tests.harness.tickets.file_lock.helpers import (
    DOCS,
    HELM,
    LOCK,
    PACKS,
    make_file_lock_repo,
    write_plan_with_files,
)
from tests.harness.tickets.helpers import APPROVED, SHARED_BRANCH, git, lines, open_ticket, run


class TestTicketsFileLock:
    def test_a_ticket_waits_while_an_open_ticket_of_another_area_plans_the_same_file(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, [LOCK, "infra/helm/Chart.yaml"])
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, ["packs/countries/fr.yaml", LOCK])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 1
        assert lines(result) == [f"{HELM} is open in {main} and changes {LOCK} too: wait for it (file lock)."]

    def test_a_file_the_open_ticket_already_changed_locks_it_too(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, ["infra/helm/Chart.yaml"])
        open_ticket(main, HELM, [f"docs/tickets/{HELM}/", "infra/helm/Chart.yaml", LOCK])
        write_plan_with_files(main, PACKS, APPROVED, [LOCK])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 1
        assert LOCK in result.stdout
        assert HELM in result.stdout

    def test_a_folder_of_one_plan_locks_the_files_under_it_in_the_other(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, ["docs/technical/delivery/"])
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, ["docs/technical/delivery/ci-cd-and-stages.md"])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 1
        assert "docs/technical/delivery/ci-cd-and-stages.md" in result.stdout

    def test_tickets_whose_plans_share_no_file_may_start_together(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, ["infra/helm/Chart.yaml"])
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, ["packs/countries/fr.yaml"])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 0, result.stdout
        assert result.stdout == ""

    def test_a_ticket_committed_but_not_merged_still_locks_the_files_of_its_plan(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, [LOCK])
        git(main, "checkout", "-q", "-b", SHARED_BRANCH)
        git(main, "add", "-A")
        git(main, "commit", "-q", "-m", f"{HELM}: finished, pull request open")
        write_plan_with_files(main, PACKS, APPROVED, [LOCK])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 1
        assert lines(result) == [
            f"{HELM} is committed on {SHARED_BRANCH}, not merged yet, and changes {LOCK} too: wait for it (file lock)."
        ]

    def test_a_file_of_a_ticket_already_merged_does_not_count(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, [LOCK])
        (main / "docs" / "tickets" / HELM / "EXPLAIN.md").write_text("# Explain\n", encoding="utf-8")
        git(main, "add", "-A")
        git(main, "commit", "-q", "-m", f"{HELM}: merged")
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, [LOCK])
        result = run(main, "check", "--ticket", PACKS)
        assert result.returncode == 0, result.stdout
        assert result.stdout == ""

    def test_force_starts_despite_a_shared_file_and_still_names_it(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, [LOCK])
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, [LOCK])
        result = run(main, "check", "--ticket", PACKS, "--force")
        assert result.returncode == 0
        assert "file lock" in result.stdout

    def test_next_leaves_out_a_ticket_whose_plan_shares_a_file_with_an_open_one(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, HELM, APPROVED, [LOCK])
        open_ticket(main, HELM)
        write_plan_with_files(main, PACKS, APPROVED, [LOCK])
        write_plan_with_files(main, DOCS, APPROVED, ["infra/terraform/main.tf"])
        assert lines(run(main, "next", HELM, PACKS, DOCS)) == [DOCS]

    def test_next_never_returns_two_tickets_whose_plans_share_a_file(self, tmp_path: Path) -> None:
        main = make_file_lock_repo(tmp_path)
        write_plan_with_files(main, PACKS, APPROVED, [LOCK, "packs/countries/fr.yaml"])
        write_plan_with_files(main, DOCS, APPROVED, ["infra/terraform/main.tf", LOCK])
        result = run(main, "next", PACKS, DOCS)
        assert lines(result) == [PACKS]
        assert f"{DOCS} waits for {PACKS}" in result.stderr
