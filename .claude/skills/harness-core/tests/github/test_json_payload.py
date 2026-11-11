from __future__ import annotations

from harness_core.github.json_payload import JsonPayload


class TestJsonPayload:
    def test_a_missing_or_mistyped_part_becomes_empty(self) -> None:
        assert JsonPayload.child({"head": {"ref": "x"}}, "head") == {"ref": "x"}
        assert JsonPayload.child({"head": "x"}, "head") == {}
        assert JsonPayload.child(["head"], "head") == {}
        assert JsonPayload.objects([{"id": 1}, 2, "x"]) == [{"id": 1}]
        assert JsonPayload.objects({"id": 1}) == []
        assert JsonPayload.text({"body": None}, "body") == ""
        assert JsonPayload.text({"body": "hi"}, "body") == "hi"
