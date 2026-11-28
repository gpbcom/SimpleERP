from __future__ import annotations

# Standard library imports
import json
from pathlib import Path

# Third-party imports
import pytest

# First-party imports
from tests.ci.bruno_collection.helpers import (
    COLLECTION,
    CREATE_FILE,
    EXAMPLE_EMAIL,
    GET_FILE,
    HEALTH_FILE,
    OWNED_FILES,
    PASSWORD,
    SERVICE_NAME,
    TOKEN,
    generate,
    generated_files,
    paths_of,
    snapshot,
    spec,
    write_service,
)


class TestGenerate:
    def test_one_request_file_is_written_per_operation(self, tmp_path: Path) -> None:
        write_service(tmp_path)

        result = generate(tmp_path)

        assert result.returncode == 0, result.stderr
        assert generated_files(tmp_path) == sorted(OWNED_FILES)

    def test_bruno_json_names_the_collection(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        content = json.loads((tmp_path / COLLECTION / "bruno.json").read_text(encoding="utf-8"))

        assert content == {
            "version": "1",
            "name": SERVICE_NAME,
            "type": "collection",
            "ignore": ["node_modules", ".git"],
        }

    def test_collection_docs_say_it_is_generated(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        content = (tmp_path / COLLECTION / "collection.bru").read_text(encoding="utf-8")

        assert "docs {" in content
        assert "generated" in content.lower()
        assert "bruno_collection.py generate" in content

    @pytest.mark.parametrize(
        ("file", "method", "url"),
        [
            (HEALTH_FILE, "get", "{{baseUrl}}/health"),
            (GET_FILE, "get", "{{baseUrl}}/v1/customers/{{customer_id}}"),
            (CREATE_FILE, "post", "{{baseUrl}}/v1/customers"),
        ],
    )
    def test_a_request_uses_its_method_and_url(self, tmp_path: Path, file: str, method: str, url: str) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        content = (tmp_path / file).read_text(encoding="utf-8")

        assert f"{method} {{" in content
        assert f"url: {url}" in content
        assert "auth: none" in content
        assert "type: http" in content
        assert "seq: 1" in content

    def test_a_request_is_named_after_its_summary(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        assert "name: Get one customer" in (tmp_path / GET_FILE).read_text(encoding="utf-8")

    def test_a_query_parameter_is_a_disabled_empty_entry(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        content = (tmp_path / GET_FILE).read_text(encoding="utf-8")

        assert "params:query" in content
        assert "~expand:" in content

    def test_a_json_body_is_an_empty_skeleton(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)

        content = (tmp_path / CREATE_FILE).read_text(encoding="utf-8")

        assert "body:json" in content
        assert "{}" in content

    @pytest.mark.parametrize("secret", [PASSWORD, TOKEN, EXAMPLE_EMAIL, "everything", "bearerAuth"])
    def test_nothing_from_the_examples_defaults_or_security_is_copied(self, tmp_path: Path, secret: str) -> None:
        write_service(tmp_path)
        assert generate(tmp_path).returncode == 0

        for name in generated_files(tmp_path):
            assert secret not in (tmp_path / name).read_text(encoding="utf-8"), name

    def test_the_output_is_identical_across_runs(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        assert generate(tmp_path).returncode == 0
        first = snapshot(tmp_path)

        generate(tmp_path)

        assert snapshot(tmp_path) == first

    def test_the_output_has_lf_line_endings(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        assert generate(tmp_path).returncode == 0

        for name, content in snapshot(tmp_path).items():
            assert b"\r" not in content, name

    def test_a_request_whose_operation_disappeared_is_removed(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)
        document = spec()
        del paths_of(document)["/health"]
        write_service(tmp_path, document)

        result = generate(tmp_path)

        assert result.returncode == 0, result.stderr
        assert not (tmp_path / HEALTH_FILE).exists()
        assert (tmp_path / GET_FILE).exists()

    def test_tests_environments_and_gitignore_are_left_untouched(self, tmp_path: Path) -> None:
        write_service(tmp_path)
        generate(tmp_path)
        kept = {
            f"{COLLECTION}/tests/smoke.bru": "hand written test\n",
            f"{COLLECTION}/environments/local.bru": "vars {\n  baseUrl: http://localhost\n}\n",
            f"{COLLECTION}/.gitignore": "secrets.bru\n",
        }
        for name, content in kept.items():
            path = tmp_path / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        result = generate(tmp_path)

        assert result.returncode == 0, result.stderr
        for name, content in kept.items():
            assert (tmp_path / name).read_text(encoding="utf-8") == content
