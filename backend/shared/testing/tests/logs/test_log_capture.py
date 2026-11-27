from __future__ import annotations

import logging

import pytest
from erp_testing.logs.log_capture import LogCapture


class TestLogCapture:
    def test_records_of_the_named_logger_are_captured(self) -> None:
        with LogCapture("erp.test.capture.named") as capture:
            logging.getLogger("erp.test.capture.named").info("hello")
        assert capture.messages() == ["hello"]

    def test_records_of_a_child_logger_are_captured(self) -> None:
        with LogCapture("erp.test.capture.parent") as capture:
            logging.getLogger("erp.test.capture.parent.child").warning("from child")
        assert capture.messages() == ["from child"]

    def test_records_of_another_logger_are_not_captured(self) -> None:
        with LogCapture("erp.test.capture.mine") as capture:
            logging.getLogger("erp.test.capture.other").error("not mine")
        assert capture.records == []

    def test_the_root_logger_is_captured_when_no_name_is_given(self) -> None:
        with LogCapture() as capture:
            logging.getLogger("erp.test.capture.anywhere").info("to root")
        assert capture.contains("to root")

    def test_lazy_arguments_are_formatted(self) -> None:
        with LogCapture("erp.test.capture.lazy") as capture:
            logging.getLogger("erp.test.capture.lazy").info("Created %s in %d ms.", "Acme", 12)
        assert capture.messages() == ["Created Acme in 12 ms."]

    @pytest.mark.parametrize("level", [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR])
    def test_messages_can_be_filtered_by_level(self, level: int) -> None:
        logger = logging.getLogger("erp.test.capture.levels")
        with LogCapture("erp.test.capture.levels") as capture:
            logger.debug("debug")
            logger.info("info")
            logger.warning("warning")
            logger.error("error")
        expected = logging.getLevelName(level).lower()
        assert capture.messages(level) == [expected]
        assert capture.contains(expected, level)
        assert len(capture.messages()) == 4

    def test_the_logger_level_is_lowered_while_attached_and_restored_after(self) -> None:
        logger = logging.getLogger("erp.test.capture.level")
        logger.setLevel(logging.ERROR)
        with LogCapture("erp.test.capture.level"):
            assert logger.level == logging.DEBUG
        assert logger.level == logging.ERROR

    def test_the_handlers_and_level_are_restored_after_an_exception(self) -> None:
        logger = logging.getLogger("erp.test.capture.failure")
        logger.setLevel(logging.WARNING)
        before = list(logger.handlers)
        with pytest.raises(RuntimeError), LogCapture("erp.test.capture.failure"):
            raise RuntimeError("boom")
        assert logger.handlers == before
        assert logger.level == logging.WARNING

    def test_nothing_is_captured_after_detach(self) -> None:
        capture = LogCapture("erp.test.capture.detach")
        capture.attach()
        logging.getLogger("erp.test.capture.detach").info("before")
        capture.detach()
        logging.getLogger("erp.test.capture.detach").info("after")
        assert capture.messages() == ["before"]

    def test_contains_is_false_for_absent_text(self) -> None:
        with LogCapture("erp.test.capture.secret") as capture:
            logging.getLogger("erp.test.capture.secret").info("Connected to the database.")
        assert not capture.contains("s3cr3t-password")

    def test_contains_can_be_limited_to_a_level(self) -> None:
        with LogCapture("erp.test.capture.contains") as capture:
            logging.getLogger("erp.test.capture.contains").info("only info")
        assert capture.contains("only info", logging.INFO)
        assert not capture.contains("only info", logging.ERROR)

    def test_clear_empties_the_records(self) -> None:
        with LogCapture("erp.test.capture.clear") as capture:
            logging.getLogger("erp.test.capture.clear").info("one")
            capture.clear()
        assert capture.records == []

    def test_a_higher_capture_level_drops_lower_records(self) -> None:
        with LogCapture("erp.test.capture.threshold", level=logging.WARNING) as capture:
            logging.getLogger("erp.test.capture.threshold").info("quiet")
            logging.getLogger("erp.test.capture.threshold").error("loud")
        assert capture.messages() == ["loud"]
