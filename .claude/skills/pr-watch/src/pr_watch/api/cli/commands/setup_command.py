from __future__ import annotations

# Standard library imports
from pathlib import Path

# First-party imports
from pr_watch.api.cli.command import Command


class SetupCommand(Command):
    """``pr-watch install-units``: copy the systemd user units of the timer.

    Notes:
        The units are only copied: enabling the timer stays the person's decision, so the command prints the two
        commands that do it.
    """

    ############################
    # Internal Helpers Methods #
    ############################

    def _perform(self) -> None:
        """Copy the units and print how to start the timer."""
        target = Path(self.options.target) if self.options.target else Path.home() / ".config" / "systemd" / "user"
        for unit in self.services.installer().install(target):
            print(f"Wrote {unit}.")
        print(
            "Then, once per login: systemctl --user import-environment DISPLAY WAYLAND_DISPLAY DBUS_SESSION_BUS_ADDRESS"
        )
        print("Then start it: systemctl --user daemon-reload && systemctl --user enable --now claude-pr-watch.timer")
