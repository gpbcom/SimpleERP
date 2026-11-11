"""The ``pr-watch-hook`` console script: the prompt hook's light entry point."""

from __future__ import annotations

# First-party imports
from harness_core.logs.harness_logging import HarnessLogging
from pr_watch.api.factories.hook.default_hook_factory import DefaultHookFactory
from pr_watch.models.configuration.watch_settings import WatchSettings


def main() -> int:
    """Answer the ``UserPromptSubmit`` hook.

    Returns:
        int: Always 0, so that the hook never blocks a prompt.

    Notes:
        - This entry point imports the inbox service only: no GitHub client, no YAML catalogue, no other command.
          ``bin/pr-watch hook-inbox`` runs it directly when the skills' environment is installed.
        - **It exits 0 whatever happens**, even when the settings cannot be read, and prints nothing then.
    """
    try:
        settings = WatchSettings()
        logger = HarnessLogging("pr-watch", settings.state_dir).logger("pr_watch")
        DefaultHookFactory(settings.state_dir, logger).hook().execute()
    except Exception:  # noqa: BLE001
        return 0
    return 0
