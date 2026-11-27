from __future__ import annotations

import json
from pathlib import Path

import pytest
from erp_platform.models.contracts.exceptions import SEOpenApiDocumentError, SEOpenApiDocumentUnreadableError
from erp_platform.storage.contracts.open_api_document_repository import OpenApiDocumentRepository


class TestOpenApiDocumentRepository:
    def test_a_written_document_is_read_back(self, tmp_path: Path) -> None:
        document = {"openapi": "3.1.0", "info": {"title": "Platform", "version": "1"}, "paths": {}}
        path = tmp_path / "openapi.json"
        path.write_text(json.dumps(document), encoding="utf-8")

        assert OpenApiDocumentRepository().read(path) == document

    def test_non_ascii_text_is_kept(self, tmp_path: Path) -> None:
        summary = "Facturation été €"
        path = tmp_path / "openapi.json"
        path.write_text(json.dumps({"info": {"summary": summary}}, ensure_ascii=False), encoding="utf-8")

        assert OpenApiDocumentRepository().read(path)["info"] == {"summary": summary}

    def test_the_key_order_of_the_file_is_kept(self, tmp_path: Path) -> None:
        path = tmp_path / "openapi.json"
        path.write_text('{"zeta": 1, "alpha": 2, "mid": 3}', encoding="utf-8")

        assert list(OpenApiDocumentRepository().read(path)) == ["zeta", "alpha", "mid"]

    def test_a_missing_file_is_refused(self, tmp_path: Path) -> None:
        with pytest.raises(SEOpenApiDocumentUnreadableError):
            OpenApiDocumentRepository().read(tmp_path / "missing.json")

    @pytest.mark.parametrize("content", ["{not json", "", "[]", '"text"', "42", "null"])
    def test_an_unreadable_document_is_refused(self, tmp_path: Path, content: str) -> None:
        path = tmp_path / "openapi.json"
        path.write_text(content, encoding="utf-8")

        with pytest.raises(SEOpenApiDocumentUnreadableError):
            OpenApiDocumentRepository().read(path)

    def test_a_file_that_is_not_utf_8_is_refused(self, tmp_path: Path) -> None:
        path = tmp_path / "openapi.json"
        path.write_bytes(b'{"a": "\xff\xfe"}')

        with pytest.raises(SEOpenApiDocumentUnreadableError):
            OpenApiDocumentRepository().read(path)

    def test_invalid_json_keeps_its_cause(self, tmp_path: Path) -> None:
        path = tmp_path / "openapi.json"
        path.write_text("{not json", encoding="utf-8")

        with pytest.raises(SEOpenApiDocumentUnreadableError) as raised:
            OpenApiDocumentRepository().read(path)

        assert isinstance(raised.value.__cause__, json.JSONDecodeError)

    def test_a_missing_file_keeps_its_cause(self, tmp_path: Path) -> None:
        with pytest.raises(SEOpenApiDocumentUnreadableError) as raised:
            OpenApiDocumentRepository().read(tmp_path / "missing.json")

        assert isinstance(raised.value.__cause__, OSError)

    def test_the_unreadable_error_is_an_open_api_document_error(self) -> None:
        assert issubclass(SEOpenApiDocumentUnreadableError, SEOpenApiDocumentError)

    def test_the_repository_has_no_write(self) -> None:
        assert not hasattr(OpenApiDocumentRepository(), "write")
