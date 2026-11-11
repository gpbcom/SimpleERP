from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_github_config_exception import SEInvalidGithubConfigException


class SEGithubConfigInvalidStageWorkflow(SEInvalidGithubConfigException):
    """Exception raised when an invalid ``stage_workflow`` is provided."""
