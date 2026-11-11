from __future__ import annotations

from pr_watch.models.exceptions import SEPrWatchError


class SEInvalidLiveSessionException(SEPrWatchError):
    """Exception raised when an invalid LiveSession is provided."""
