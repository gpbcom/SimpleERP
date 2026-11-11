from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from pydantic import JsonValue

from pr_watch.models.enums import EventKind
from pr_watch.models.validation.field_rules import FieldRules
from pr_watch.models.watch.pull_request_ref import PullRequestRef


class TestFieldRules:
    @pytest.mark.parametrize(
        ("rule", "value", "expected"),
        [
            ("text", "  hello ", "hello"),
            ("free_text", "", ""),
            ("ticket", " GH-12 ", "GH-12"),
            ("slug", "gpbcom/simple-erp", "gpbcom/simple-erp"),
            ("link", "https://github.com/x", "https://github.com/x"),
            ("integer", 0, 0),
            ("identifier", 3, 3),
            ("amount", 2.5, 2.5),
            ("flag", False, False),
            ("moment", "2026-11-10T09:00:00+01:00", "2026-11-10T09:00:00+01:00"),
            ("moment", "2026-11-10T08:00:00Z", "2026-11-10T08:00:00+00:00"),
            ("path", " /tmp/x ", "/tmp/x"),
            ("mapping", {"a": 1}, {"a": 1}),
            ("sequence", [1, 2], [1, 2]),
            ("texts", [" a ", "b"], ["a", "b"]),
            ("nested", {"a": 1}, {"a": 1}),
        ],
    )
    def test_a_good_value_passes(self, rule: str, value: JsonValue, expected: JsonValue) -> None:
        assert getattr(FieldRules, rule)(value, ValueError, "field") == expected

    @pytest.mark.parametrize(
        ("rule", "value"),
        [
            ("text", " "),
            ("text", 3),
            ("free_text", None),
            ("ticket", "ARE-12"),
            ("slug", "simple-erp"),
            ("link", "github.com/x"),
            ("integer", -1),
            ("integer", True),
            ("identifier", 0),
            ("amount", "1"),
            ("amount", False),
            ("flag", 1),
            ("moment", "2026-11-10T09:00:00"),
            ("moment", "yesterday"),
            ("moment", 3),
            ("path", ""),
            ("mapping", {1: "a"}),
            ("sequence", "ab"),
            ("texts", ["a", ""]),
            ("nested", "x"),
        ],
    )
    def test_a_bad_value_raises_the_fields_own_error(self, rule: str, value: JsonValue) -> None:
        with pytest.raises(KeyError, match="Invalid field"):
            getattr(FieldRules, rule)(value, KeyError, "field")

    def test_a_member_must_be_one_of_its_enum(self) -> None:
        assert FieldRules.member("qa_waiting", ValueError, "kind", EventKind) == "qa_waiting"
        with pytest.raises(ValueError, match="Must be one of"):
            FieldRules.member("jenkins_failed", ValueError, "kind", EventKind)

    def test_python_objects_come_back_in_their_json_form(self) -> None:
        moment = datetime(2026, 11, 10, 9, 0, tzinfo=UTC)
        reference = PullRequestRef(repository="gpbcom/simple-erp", number=7, root="/r")
        assert FieldRules.moment(moment, ValueError, "at") == "2026-11-10T09:00:00+00:00"
        assert FieldRules.path(Path("/tmp/x"), ValueError, "root") == "/tmp/x"
        assert FieldRules.nested(reference, ValueError, "pull_request") == {
            "repository": "gpbcom/simple-erp",
            "number": 7,
            "root": "/r",
        }

    def test_a_naive_time_is_refused(self) -> None:
        with pytest.raises(ValueError, match="time zone"):
            FieldRules.moment(datetime(2026, 11, 10, 9, 0), ValueError, "at")
