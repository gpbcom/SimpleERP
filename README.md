# simple-erp

simple-erp is a small ERP for start-ups and small companies. It is built as a mono-repo of Python back-end services and
front ends, each shipped as its own Docker image. Today the repository holds the project's skeleton: the layered
package layout, the house rules and the tests that enforce them, the command line entry point, the CI/CD pipeline and
the development harness. No business capability is built yet.

## Quick start

```bash
uv sync                      # install Python 3.13 dependencies into .venv
uv run simple-erp            # the command line entry point
uv run pytest                # every test, two workers
```

## Commands

| Command | Does |
|---|---|
| `uv run simple-erp` | Runs the command line entry point |
| `uv run ruff check src tests` | Lints the code |
| `uv run ruff format <files>` | Formats the files you edited (never a whole folder) |
| `uv run mypy src` | Type-checks the code |
| `uv run pytest tests/<layer>/<package>` | Runs one folder of tests |
| `uv run pytest tests/conventions` | Checks the house rules a test enforces (`AGENT.md`) |

## Layout

| Path | Holds |
|---|---|
| `src/api/` | The entry points: the command line today, HTTP routes later |
| `src/service/` | The business rules, one package per concern |
| `src/storage/` | Reading and writing data |
| `src/models/` | Pydantic models, enums and their exceptions |
| `conf/` | Configuration: `logger.yaml` today |
| `tests/` | Mirrors `src/`; `tests/conventions/` enforces the house rules |
| `docs/` | `specs/` (input), `functional/` and `technical/` documentation |
| `.github/` | The CI/CD workflows and the issue and pull request templates |
| `.claude/` | The Claude Code harness: rules, skills, hooks and their documentation |
| `CHANGELOG.md`, `changelog.d/` | The changelog and the fragments waiting for the next release |

The target layout (`services/`, `frontends/`, `packages/`) is described in `AGENT.md`, "Mono-repo".

## Services and front ends

None yet. Each one will get its folder under `services/` or `frontends/`, its Dockerfile, and its chapter in
[docs/technical/](docs/technical/README.md).

## Documentation

- [Functional documentation](docs/functional/README.md): what users can do and see.
- [Technical documentation](docs/technical/README.md): how it is built, tested and released.
- [Changelog](CHANGELOG.md).
- [How code is written](AGENT.md) and [how work is done with Claude Code](.claude/harness-docs/README.md).

Last reviewed: 2026-11-10 (GH-1)
