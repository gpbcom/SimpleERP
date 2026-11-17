from __future__ import annotations

from progress_updates.models.hooks.tool_call import ToolCall
from progress_updates.service.hooks.background_reminder import BackgroundReminder


class TestBackgroundReminder:
    def test_a_command_moved_to_the_background_gives_a_reminder(self) -> None:
        reminder = BackgroundReminder().reminder(ToolCall(tool_name="Bash", background=True))
        assert reminder is not None
        assert "progress-updates watch --every 120" in reminder

    def test_a_subagent_in_the_background_gives_a_reminder(self) -> None:
        reminder = BackgroundReminder().reminder(ToolCall(tool_name="Agent", background=True))
        assert reminder is not None
        assert "--task" in reminder

    def test_a_workflow_always_gives_a_reminder(self) -> None:
        assert BackgroundReminder().reminder(ToolCall(tool_name="Workflow", background=False)) is not None

    def test_a_foreground_command_or_another_tool_gives_nothing(self) -> None:
        assert BackgroundReminder().reminder(ToolCall(tool_name="Bash", background=False)) is None
        assert BackgroundReminder().reminder(ToolCall(tool_name="Read", background=False)) is None
