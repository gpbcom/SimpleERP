---
name: exception-and-log-messages
description: How this project lays out the text of exception and log messages, with one sentence per source line. Use this whenever you write or edit a `raise`, a `self.logger.*` call, or a Pydantic `field_validator` in this repository, even for a one-line fix or when the message would fit on one line.
---

# Exception and log messages

A message with two or more sentences has one sentence per source line, joined by implicit string concatenation. The first line ends with `# noqa: E501`.

```python
if isinstance(value, bool) or not isinstance(value, int):
    raise SEDatabaseConfigInvalidPort(
        f"Invalid port: {value!r}. "  # noqa: E501
        "Must be an integer."
    )
if not cls.PORT_MIN <= value <= cls.PORT_MAX:
    raise SEDatabaseConfigInvalidPort(
        f"Invalid port: {value}. "  # noqa: E501
        f"Must be in [{cls.PORT_MIN}, {cls.PORT_MAX}]."
    )
```

Log calls follow the same layout, with the lazy `%s` arguments after the message:

```python
self.logger.info(
    "simple-erp is ready. "  # noqa: E501
    "Clients connect to %s.",
    server.url(),
)
```

## Details that matter

- **No comma between the sentences.** A comma makes them two arguments, so `str(error)` prints a tuple: `('Invalid enabled: 1. ', 'Must be a boolean.')`. With a log call, the second sentence would be taken as a `%s` argument.
- **Keep the marker, even when the line is short.** Without a comment, `ruff format` joins the sentences back onto one line. `RUF100` is ignored in `pyproject.toml` so that `ruff check --fix` does not delete the marker.
- **The trailing space stays on the earlier sentence**, inside its quotes, so the text reads the same once joined.
- **Use the `f` prefix only on lines with a placeholder.** `"Must be an integer."` stays a plain string.
- **A sentence ends at `. `, `! `, `? ` or `\n`**, and only outside `{...}`. A colon does not end one, so `Invalid port: {value}.` is a single sentence.
- **Leave single-sentence messages as they are.** `self.logger.warning("The customer could not be saved: %s.", name)` has nothing to split.
- **Keep what follows the call**, such as `from error`, after the closing parenthesis.

## Checking your change

Format only the files you edited, then lint them:

```bash
.venv/bin/ruff format <edited files>
.venv/bin/ruff check <edited files>
```
