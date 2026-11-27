from __future__ import annotations

import json
import logging
import re
import sys
from typing import Dict, Optional, Tuple

import pytest
from erp_logging.formatters.json_lines_formatter import JsonLinesFormatter


def make_record(
    message: str = "hello",
    args: Optional[Tuple[object, ...]] = None,
    level: int = logging.INFO,
    exc_info: Optional[Tuple[type, BaseException, object]] = None,
    extras: Optional[Dict[str, str]] = None,
) -> logging.LogRecord:
    record = logging.LogRecord("erp.test", level, __file__, 1, message, args, exc_info)
    for name, value in (extras or {}).items():
        setattr(record, name, value)
    return record


class TestJsonLinesFormatter:
    def test_the_output_is_a_json_object_with_exactly_the_fields(self) -> None:
        line = JsonLinesFormatter().format(make_record())
        assert list(json.loads(line).keys()) == list(JsonLinesFormatter.FIELDS)

    def test_the_time_is_utc_iso_8601_with_milliseconds_and_a_z(self) -> None:
        record = make_record()
        record.created = 1700000000.123456
        data = json.loads(JsonLinesFormatter().format(record))
        assert data["time"] == "2023-11-14T22:13:20.123Z"
        assert re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z", data["time"])

    @pytest.mark.parametrize(
        ("level", "name"),
        [(logging.DEBUG, "DEBUG"), (logging.INFO, "INFO"), (logging.WARNING, "WARNING"), (logging.ERROR, "ERROR")],
    )
    def test_the_level_is_its_name(self, level: int, name: str) -> None:
        data = json.loads(JsonLinesFormatter().format(make_record(level=level)))
        assert data["level"] == name

    def test_the_logger_is_its_name(self) -> None:
        data = json.loads(JsonLinesFormatter().format(make_record()))
        assert data["logger"] == "erp.test"

    def test_the_message_is_formatted_with_its_arguments(self) -> None:
        record = make_record("Created %s in %d ms.", ("customer", 12))
        data = json.loads(JsonLinesFormatter().format(record))
        assert data["message"] == "Created customer in 12 ms."

    def test_the_tag_attributes_are_written(self) -> None:
        record = make_record(extras={"service": "customers", "company": "c-123", "request": "r-456"})
        data = json.loads(JsonLinesFormatter().format(record))
        assert (data["service"], data["company"], data["request"]) == ("customers", "c-123", "r-456")

    @pytest.mark.parametrize("name", ["service", "company", "request"])
    def test_a_missing_tag_attribute_is_a_dash(self, name: str) -> None:
        data = json.loads(JsonLinesFormatter().format(make_record()))
        assert data[name] == "-"

    @pytest.mark.parametrize("message", ["first\nsecond", "first\r\nsecond\nthird"])
    def test_a_message_with_a_newline_stays_on_one_line(self, message: str) -> None:
        line = JsonLinesFormatter().format(make_record(message))
        assert "\n" not in line
        assert "\r" not in line
        assert json.loads(line)["message"] == message

    def test_an_extra_attribute_ending_in_key_is_not_written(self) -> None:
        line = JsonLinesFormatter().format(make_record(extras={"password_key": "s3cret"}))
        assert "password_key" not in json.loads(line)
        assert "s3cret" not in line

    def test_an_exception_adds_the_formatted_traceback(self) -> None:
        try:
            raise ValueError("boom")
        except ValueError:
            exc_info = sys.exc_info()
        record = make_record(level=logging.ERROR, exc_info=exc_info)  # type: ignore[arg-type]
        line = JsonLinesFormatter().format(record)
        data = json.loads(line)
        assert "\n" not in line
        assert "ValueError: boom" in data["exception"]
        assert set(data.keys()) == set(JsonLinesFormatter.FIELDS) | {"exception"}

    def test_there_is_no_exception_key_without_exc_info(self) -> None:
        data = json.loads(JsonLinesFormatter().format(make_record()))
        assert "exception" not in data
