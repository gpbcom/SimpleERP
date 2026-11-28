"""A worker worktree runs no Git LFS filter after ``start``, and the main checkout keeps its own.

Claude Code checks a worker out with the LFS files as pointers, but the repository's filter stays on: every git command
that met a racily clean pointer ran ``git-lfs`` again (100 % CPU in every wave), and ``start``'s reset to a newer commit
downloaded the images it changed. Here the LFS filter logs the folder it runs in, works in the main checkout as
``git-lfs`` would on a pointer, and fails anywhere else: any run of it in a worker fails the command.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List

from tests.harness.ticket_tree.helpers import git, make_repo, run, run_json

POINTER = "version https://git-lfs.github.com/spec/v1\noid sha256:{}\nsize 1\n"
IMAGE = "docs/image.png"
FILTER_LOG = "lfs-filter.log"
NO_LFS = [
    "-c",
    "filter.lfs.smudge=",
    "-c",
    "filter.lfs.clean=",
    "-c",
    "filter.lfs.process=",
    "-c",
    "filter.lfs.required=false",
]


class TestTicketTreeWorkerLfs:
    def repository_with_an_lfs_image(self, tmp_path: Path) -> Path:
        main = make_repo(tmp_path)
        (main / IMAGE).parent.mkdir(parents=True, exist_ok=True)
        (main / IMAGE).write_text(POINTER.format("0" * 64), encoding="utf-8")
        (main / ".gitattributes").write_text("*.png filter=lfs diff=lfs merge=lfs -text\n", encoding="utf-8")
        git(main, *NO_LFS, "add", IMAGE, ".gitattributes")
        git(main, *NO_LFS, "commit", "-m", "an image stored in LFS")
        assert run(main, "prepare").returncode == 0
        log = tmp_path / FILTER_LOG
        command = f"""sh -c 'pwd >> "{log}"; [ "$(pwd)" = "{main.resolve()}" ] || exit 1; cat'"""
        git(main, "config", "filter.lfs.smudge", command)
        git(main, "config", "filter.lfs.clean", command)
        git(main, "config", "filter.lfs.required", "true")
        return main

    def worker_as_claude_code_makes_it(self, main: Path, name: str, start: str = "HEAD") -> Path:
        """Add a worker worktree whose LFS files are pointers, as Claude Code checks them out."""
        path = main.parent / name
        git(main, *NO_LFS, "worktree", "add", "-b", f"worktree-{name}", str(path), start)
        return path

    def change_the_image(self, main: Path) -> str:
        """Commit a new version of the image on the shared branch, as when develop moved, and return the old head."""
        old = git(main, "rev-parse", "HEAD")
        (main / IMAGE).write_text(POINTER.format("1" * 64), encoding="utf-8")
        git(main, *NO_LFS, "commit", "-am", "a new image")
        return old

    def filter_runs(self, main: Path) -> List[str]:
        log = main.parent / FILTER_LOG
        return log.read_text(encoding="utf-8").splitlines() if log.is_file() else []

    def test_start_runs_no_lfs_filter_on_a_racily_clean_pointer(self, tmp_path: Path) -> None:
        main = self.repository_with_an_lfs_image(tmp_path)
        worker = self.worker_as_claude_code_makes_it(main, "w1")
        (worker / IMAGE).touch()
        result = run(worker, "start")
        assert result.returncode == 0, result.stderr
        assert '"lfs": "off"' in result.stdout
        assert (worker / IMAGE).read_text(encoding="utf-8") == POINTER.format("0" * 64)
        assert str(worker.resolve()) not in self.filter_runs(main)

    def test_start_moves_a_worker_to_a_newer_image_without_downloading_it(self, tmp_path: Path) -> None:
        main = self.repository_with_an_lfs_image(tmp_path)
        old = self.change_the_image(main)
        worker = self.worker_as_claude_code_makes_it(main, "w1", old)
        started = run_json(worker, "start")
        assert started["moved_from"] == old
        assert (worker / IMAGE).read_text(encoding="utf-8") == POINTER.format("1" * 64)
        assert str(worker.resolve()) not in self.filter_runs(main)

    def test_every_later_git_command_of_the_worker_runs_no_lfs_filter(self, tmp_path: Path) -> None:
        main = self.repository_with_an_lfs_image(tmp_path)
        worker = self.worker_as_claude_code_makes_it(main, "w1")
        assert run(worker, "start").returncode == 0
        (worker / IMAGE).touch()
        (worker / "b.png").write_text("a new image\n", encoding="utf-8")
        status = git(worker, "--no-optional-locks", "status", "--porcelain").splitlines()
        assert "?? b.png" in status
        assert not [line for line in status if IMAGE in line]
        handoff = run(worker, "handoff", "--task", "K01")
        assert handoff.returncode == 0, handoff.stderr
        assert str(worker.resolve()) not in self.filter_runs(main)

    def test_the_main_checkout_keeps_its_lfs_filter(self, tmp_path: Path) -> None:
        main = self.repository_with_an_lfs_image(tmp_path)
        worker = self.worker_as_claude_code_makes_it(main, "w1")
        assert run(worker, "start").returncode == 0
        assert git(main, "config", "--get", "filter.lfs.required") == "true"
        assert git(worker, "config", "--get", "filter.lfs.clean") == ""
        smudged = subprocess.run(
            ["git", "cat-file", "--filters", f"HEAD:{IMAGE}"], cwd=main, capture_output=True, text=True, check=False
        )
        assert smudged.returncode == 0, smudged.stderr
        assert self.filter_runs(main)[-1] == str(main.resolve())

    def test_a_worker_holding_the_images_keeps_the_filter(self, tmp_path: Path) -> None:
        main = self.repository_with_an_lfs_image(tmp_path)
        pointer = POINTER.format("0" * 64).replace("\n", "\\n")
        git(main, "config", "filter.lfs.clean", f"sh -c 'cat >/dev/null; printf \"{pointer}\"'")
        git(main, "config", "filter.lfs.smudge", "cat")
        worker = self.worker_as_claude_code_makes_it(main, "w1")
        (worker / IMAGE).write_bytes(b"\x89PNG\r\n\x1a\n")
        started = run_json(worker, "start")
        assert started["lfs"] == "kept"
        scopes = git(worker, "config", "--show-scope", "--get-regexp", "^filter[.]lfs[.]").splitlines()
        assert not [line for line in scopes if line.startswith("worktree")]
