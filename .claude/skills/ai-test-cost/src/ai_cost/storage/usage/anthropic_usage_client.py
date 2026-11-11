from __future__ import annotations

# Standard library imports
import os
from datetime import UTC, datetime, timedelta
from logging import Logger, getLogger
from typing import ClassVar, Dict, List, Optional, Tuple

# Third-party imports
import httpx
from pydantic import JsonValue, SecretStr

# First-party imports
from ai_cost.models.ledger.exceptions import SEInvalidModelUsageException
from ai_cost.models.ledger.model_usage import ModelUsage
from ai_cost.storage.usage.exceptions import SEAnthropicUsageRequestFailedError, SEAnthropicUsageUnavailableError


class AnthropicUsageClient:
    """Reads the tokens each model used from the Anthropic Admin API usage report.

    Attributes:
        URL (str): The usage report endpoint, ``GET /v1/organizations/usage_report/messages``.
        API_VERSION (str): The ``anthropic-version`` header sent.
        ADMIN_KEY_VARIABLE (str): The environment variable that holds the admin key.
        BUCKET_WIDTH (str): The time bucket asked for: one minute, the finest the report gives.
        PAGE_LIMIT (int): The most one-minute buckets one page holds.
        MAX_PAGES (int): The most pages read for one measure.
        TIMEOUT_S (float): Seconds a request may take.
        UNKNOWN_MODEL (str): The name given to usage whose model the report leaves out.
        api_key_id (Optional[str]): The API key whose usage is read, ``None`` for the whole organisation.
        transport (Optional[httpx.BaseTransport]): The HTTP transport, the network by default.
        admin_secret (Optional[SecretStr]): The admin key, held in memory only.
        logger (Logger): Logger instance.

    Notes:
        - **The admin key is never logged nor put in an error**: it is a ``SecretStr`` read from
          ``ANTHROPIC_ADMIN_KEY`` and sent only as the ``x-api-key`` header.
        - Buckets are snapped to the minute in UTC: ``starting_at`` is floored and ``ending_at`` rounded up, so the
          window covers the whole run, and usage of the same key in the same minutes counts too.
        - The report lags a few minutes behind the requests, which is why a run is settled later.
        - Each call makes one request per page and never retries: the guard counts failed measures itself.
    """

    URL: ClassVar[str] = "https://api.anthropic.com/v1/organizations/usage_report/messages"
    API_VERSION: ClassVar[str] = "2023-06-01"
    ADMIN_KEY_VARIABLE: ClassVar[str] = "ANTHROPIC_ADMIN_KEY"
    BUCKET_WIDTH: ClassVar[str] = "1m"
    PAGE_LIMIT: ClassVar[int] = 1440
    MAX_PAGES: ClassVar[int] = 50
    TIMEOUT_S: ClassVar[float] = 30.0
    UNKNOWN_MODEL: ClassVar[str] = "unknown"

    def __init__(
        self,
        api_key_id: Optional[str],
        logger: Optional[Logger] = None,
        transport: Optional[httpx.BaseTransport] = None,
    ) -> None:
        """Read the admin key and set the key whose usage is read.

        Args:
            api_key_id (Optional[str]): The API key whose usage is read, ``None`` for the whole organisation.
            logger (Optional[Logger]): Logger instance.
            transport (Optional[httpx.BaseTransport]): The HTTP transport, the network by default.
        """
        self.api_key_id = api_key_id
        self.transport = transport
        secret = os.environ.get(self.ADMIN_KEY_VARIABLE, "").strip()
        self.admin_secret = SecretStr(secret) if secret else None
        self.logger = logger if logger else getLogger(__name__)

    ############################
    # Internal Helpers Methods #
    ############################

    def _minute(self, moment: datetime, up: bool) -> str:
        """Snap a moment to the minute, in UTC.

        Args:
            moment (datetime): The moment.
            up (bool): Whether to round up rather than down.

        Returns:
            str: The minute in RFC 3339, such as ``2026-11-10T09:01:00Z``.
        """
        utc = moment.astimezone(UTC)
        floor = utc.replace(second=0, microsecond=0)
        snapped = floor + timedelta(minutes=1) if up and floor != utc else floor
        return snapped.strftime("%Y-%m-%dT%H:%M:%SZ")

    def _params(self, start: datetime, end: datetime, page: Optional[str]) -> httpx.QueryParams:
        """Build the query of one page.

        Args:
            start (datetime): The start of the window.
            end (datetime): The end of the window.
            page (Optional[str]): The page cursor, ``None`` for the first page.

        Returns:
            httpx.QueryParams: The query parameters, repeated keys included.
        """
        params: List[Tuple[str, str]] = [
            ("starting_at", self._minute(start, False)),
            ("ending_at", self._minute(end, True)),
            ("bucket_width", self.BUCKET_WIDTH),
            ("group_by[]", "model"),
            ("limit", str(self.PAGE_LIMIT)),
        ]
        if self.api_key_id:
            params.append(("api_key_ids[]", self.api_key_id))
        if page:
            params.append(("page", page))
        return httpx.QueryParams(tuple(params))

    def _tokens(self, result: JsonValue, name: str) -> int:
        """Read one token count of a result.

        Args:
            result (JsonValue): The result.
            name (str): The field, such as ``output_tokens``.

        Returns:
            int: The count, 0 when the field is missing.

        Raises:
            SEAnthropicUsageRequestFailedError: When the count is not a whole number.
        """
        value = result.get(name, 0) if isinstance(result, dict) else None
        if value is None:
            return 0
        if isinstance(value, bool) or not isinstance(value, int):
            self.logger.error("The usage report gave %s as %s.", name, type(value).__name__)
            raise SEAnthropicUsageRequestFailedError(
                f"The usage report gave {name} as {value!r}. "  # noqa: E501
                "A token count must be a whole number."
            )
        return value

    def _add(self, usage: Dict[str, ModelUsage], result: JsonValue) -> None:
        """Add the tokens of one result to its model's.

        Args:
            usage (Dict[str, ModelUsage]): The tokens of each model so far, updated in place.
            result (JsonValue): One result of a bucket.

        Raises:
            SEAnthropicUsageRequestFailedError: When the result is not an object of token counts.
        """
        if not isinstance(result, dict):
            self.logger.error("The usage report gave a result of type %s.", type(result).__name__)
            raise SEAnthropicUsageRequestFailedError("The usage report gave a result that is not an object.")
        model = result.get("model")
        name = model if isinstance(model, str) and model else self.UNKNOWN_MODEL
        creation = result.get("cache_creation") or {}
        known = usage.get(name, ModelUsage())
        try:
            usage[name] = ModelUsage(
                input_tokens=known.input_tokens + self._tokens(result, "uncached_input_tokens"),
                output_tokens=known.output_tokens + self._tokens(result, "output_tokens"),
                cache_read_tokens=known.cache_read_tokens + self._tokens(result, "cache_read_input_tokens"),
                cache_write_5m_tokens=known.cache_write_5m_tokens + self._tokens(creation, "ephemeral_5m_input_tokens"),
                cache_write_1h_tokens=known.cache_write_1h_tokens + self._tokens(creation, "ephemeral_1h_input_tokens"),
            )
        except SEInvalidModelUsageException as error:
            self.logger.error("The usage report gave a negative token count for %s.", name)
            raise SEAnthropicUsageRequestFailedError(
                f"The usage report gave an invalid token count for {name}. "  # noqa: E501
                f"The error was {type(error).__name__}."
            ) from error

    def _page(self, client: httpx.Client, params: httpx.QueryParams) -> JsonValue:
        """Fetch one page of the report.

        Args:
            client (httpx.Client): The HTTP client.
            params (httpx.QueryParams): The query.

        Returns:
            JsonValue: The page's JSON body.

        Raises:
            SEAnthropicUsageRequestFailedError: When the request fails, is refused, or its body is not JSON.
        """
        secret = self.admin_secret.get_secret_value() if self.admin_secret else ""
        headers = {"x-api-key": secret, "anthropic-version": self.API_VERSION}
        try:
            response = client.get(self.URL, params=params, headers=headers)
        except httpx.HTTPError as error:
            self.logger.error("The usage report request failed: %s.", type(error).__name__)
            raise SEAnthropicUsageRequestFailedError(
                "The usage report request failed. "  # noqa: E501
                f"The error was {type(error).__name__}."
            ) from error
        if response.status_code != httpx.codes.OK:
            self.logger.error("The usage report answered HTTP %d.", response.status_code)
            raise SEAnthropicUsageRequestFailedError(
                f"The usage report answered HTTP {response.status_code}. "  # noqa: E501
                "Check that ANTHROPIC_ADMIN_KEY holds an Admin API key of the organisation."
            )
        try:
            body: JsonValue = response.json()
        except ValueError as error:
            self.logger.error("The usage report answered a body that is not JSON.")
            raise SEAnthropicUsageRequestFailedError("The usage report answered a body that is not JSON.") from error
        return body

    ############################
    # Publicly Exposed Methods #
    ############################

    @property
    def configured(self) -> bool:
        """Whether an admin key is set, so that the report can be read."""
        return self.admin_secret is not None

    def usage(self, start: datetime, end: datetime) -> Dict[str, ModelUsage]:
        """Read the tokens each model used between two moments.

        Args:
            start (datetime): The start of the window.
            end (datetime): The end of the window.

        Returns:
            Dict[str, ModelUsage]: The tokens of each model, not priced yet.

        Raises:
            SEAnthropicUsageUnavailableError: When no admin key is set.
            SEAnthropicUsageRequestFailedError: When a request fails or a page cannot be read.
        """
        if not self.configured:
            self.logger.error("No admin key in %s: the usage report cannot be read.", self.ADMIN_KEY_VARIABLE)
            raise SEAnthropicUsageUnavailableError(
                f"{self.ADMIN_KEY_VARIABLE} is not set. "  # noqa: E501
                "The usage report needs an Anthropic Admin API key."
            )
        usage: Dict[str, ModelUsage] = {}
        page: Optional[str] = None
        with httpx.Client(transport=self.transport, timeout=self.TIMEOUT_S) as client:
            for number in range(1, self.MAX_PAGES + 1):
                body = self._page(client, self._params(start, end, page))
                buckets = body.get("data") if isinstance(body, dict) else None
                if not isinstance(body, dict) or not isinstance(buckets, list):
                    self.logger.error("The usage report page %d has no list of buckets.", number)
                    raise SEAnthropicUsageRequestFailedError("The usage report answered a page without buckets.")
                for bucket in buckets:
                    results = bucket.get("results") if isinstance(bucket, dict) else None
                    for result in results if isinstance(results, list) else []:
                        self._add(usage, result)
                next_page = body.get("next_page")
                if not body.get("has_more") or not isinstance(next_page, str):
                    break
                page = next_page
            else:
                self.logger.error("The usage report had more than %d pages.", self.MAX_PAGES)
                raise SEAnthropicUsageRequestFailedError(
                    f"The usage report had more than {self.MAX_PAGES} pages. "  # noqa: E501
                    "A partial count would price the run too low."
                )
        self.logger.info("Read the usage of %d models from %s to %s.", len(usage), start, end)
        return usage
