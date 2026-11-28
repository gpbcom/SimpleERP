from __future__ import annotations

# Standard library imports
from pathlib import Path
from typing import List

# Third-party imports
import pytest

# First-party imports
from tests.ci.bruno_collection.helpers import (
    COLLECTION,
    CREATE_FILE,
    GET_FILE,
    HEALTH_FILE,
    OPENAPI,
    SERVICE,
    check,
    generate,
    paths_of,
    run_script,
    spec,
    write_service,
)


class TestCheck:
    def fresh(self, root: Path) -> None:
        write_service(root)
        assert generate(root).returncode == 0

    def test_a_fresh_collection_passes(self, tmp_path: Path) -> None:
        self.fresh(tmp_path)

        result = check(tmp_path)

        assert result.returncode == 0, result.stdout + result.stderr

    def test_an_operation_added_to_the_openapi_fails_and_names_the_file(self, tmp_path: Path) -> None:
        self.fresh(tmp_path)
        document = spec()
        paths_of(document)["/v1/ping"] = {"get": {"operationId": "ping", "summary": "Ping", "responses": {}}}
        write_service(tmp_path, document)

        result = check(tmp_path)

        assert result.returncode == 1
        assert f"{COLLECTION}/requests/default/ping.bru" in result.stdout
        assert "bruno_collection.py generate" in result.stdout

    def test_an_operation_removed_from_the_openapi_fails_and_names_the_file(self, tmp_path: Path) -> None:
        self.fresh(tmp_path)
        document = spec()
        del paths_of(document)["/health"]
        write_service(tmp_path, document)

        result = check(tmp_path)

        assert result.returncode == 1
        assert HEALTH_FILE in result.stdout

    def test_an_operation_renamed_in_the_openapi_fails_and_names_both_files(self, tmp_path: Path) -> None:
        self.fresh(tmp_path)
        document = spec()
        paths_of(document)["/health"] = {"get": {"operationId": "liveness", "summary": "Health", "responses": {}}}
        write_service(tmp_path, document)

        result = check(tmp_path)

        assert result.returncode == 1
        assert HEALTH_FILE in result.stdout
        assert f"{COLLECTION}/requests/default/liveness.bru" in result.stdout

    @pytest.mark.parametrize("file", [HEALTH_FILE, GET_FILE, CREATE_FILE, f"{COLLECTION}/bruno.json"])
    def test_a_hand_edited_generated_file_fails_and_is_named(self, tmp_path: Path, file: str) -> None:
        self.fresh(tmp_path)
        path = tmp_path / file
        path.write_text(path.read_text(encoding="utf-8") + "\n# edited\n", encoding="utf-8")

        result = check(tmp_path)

        assert result.returncode == 1
        assert file in result.stdout

    def test_an_extra_file_in_requests_fails_and_is_named(self, tmp_path: Path) -> None:
        self.fresh(tmp_path)
        extra = f"{COLLECTION}/requests/default/extra.bru"
        (tmp_path / extra).write_text("meta {\n  name: Extra\n}\n", encoding="utf-8")

        result = check(tmp_path)

        assert result.returncode == 1
        assert extra in result.stdout

    @pytest.mark.parametrize("name", ["tests/smoke.bru", "environments/local.bru"])
    def test_a_changed_file_outside_the_generated_ones_passes(self, tmp_path: Path, name: str) -> None:
        self.fresh(tmp_path)
        path = tmp_path / COLLECTION / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("one\n", encoding="utf-8")
        before = check(tmp_path)
        path.write_text("two\n", encoding="utf-8")

        after = check(tmp_path)

        assert before.returncode == 0, before.stdout
        assert after.returncode == 0, after.stdout

    def test_no_collection_means_nothing_to_check(self, tmp_path: Path) -> None:
        write_service(tmp_path)

        result = check(tmp_path)

        assert result.returncode == 0
        assert "nothing to check" in result.stdout.lower()

    @pytest.mark.parametrize("damage", ["missing", "unreadable"])
    def test_a_missing_or_unreadable_openapi_with_a_collection_fails(self, tmp_path: Path, damage: str) -> None:
        self.fresh(tmp_path)
        document = tmp_path / SERVICE / OPENAPI
        if damage == "missing":
            document.unlink()
        else:
            document.write_text("{not json", encoding="utf-8")

        result = check(tmp_path)

        assert result.returncode == 1

    @pytest.mark.parametrize(
        "arguments",
        [
            [],
            ["unknown"],
            ["check"],
            ["generate"],
            ["check", "--service"],
            ["check", "--bogus", "x"],
        ],
    )
    def test_bad_arguments_exit_2_with_a_usage_line(self, tmp_path: Path, arguments: List[str]) -> None:
        result = run_script(tmp_path, *arguments)

        assert result.returncode == 2
        assert "usage" in (result.stdout + result.stderr).lower()
