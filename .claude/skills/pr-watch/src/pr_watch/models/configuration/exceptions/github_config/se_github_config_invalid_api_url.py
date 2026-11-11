from __future__ import annotations

from pr_watch.models.configuration.exceptions.se_invalid_github_config_exception import SEInvalidGithubConfigException


class SEGithubConfigInvalidApiUrl(SEInvalidGithubConfigException):
    """Exception raised when an invalid ``api_url`` is provided."""
