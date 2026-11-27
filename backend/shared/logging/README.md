# erp_logging

`erp_logging` is the logging library every SimpleERP back-end service uses. It configures the logs once at start-up
and tags every line with the service, the company and the request it belongs to.

## What it holds

- `LoggingSetup`: applies a service's `conf/logger.yaml`. Calling `LoggingSetup(config_path, service, logs_dir).configure()`
  writes three outputs:
  - a coloured console;
  - a coloured rotating file, `logs/simpleerp.log`;
  - the JSON lines of `logs/simpleerp.jsonl`, for machines.
- `ContextFilter`: adds `service`, `company` (an opaque identifier) and `request` to every log record. A field that is
  not set shows `-`.
- `LogContext.bind(company, request)`: sets the company and the request for the current call. The request middleware
  of T0.09 calls it for every HTTP request.

The library holds no business rules. It follows [D406](../../../docs/specs/06-decisions/technical/d406-back-end.md) and
sits in the shared libraries of the layout fixed by
[D438](../../../docs/specs/06-decisions/technical/d438-repository-layout.md).

## How a service uses it

Each service keeps its own `conf/logger.yaml`, copied from the default in this library, and configures logging when it
starts:

```python
LoggingSetup(Path("conf/logger.yaml"), "customers", Path("logs")).configure()
```

The design is in [D416](../../../docs/specs/06-decisions/technical/d416-observability-design.md), and the operating
view is in [observability](../../../docs/technical/operations/observability.md). The requirements are in
[observability](../../../docs/specs/05-non-functional/observability.md).

## Reading the logs

- `tail -f logs/simpleerp.log` follows the coloured file. Use `less -R` to keep the colours.
- `logs/simpleerp.jsonl` holds one JSON object per line, for tools that parse the logs.

## Tests

```bash
uv run pytest backend/shared/logging/tests -n 2
```
