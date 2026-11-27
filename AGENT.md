# AGENT.md

How code is written in SimpleERP. See `README.md` for what it does and how to use it.

When you edit a file, follow these rules even where a neighbouring file does not.

## Commands

```bash
uv sync
uv run ruff check backend plugins sdk tests
uv run ruff format <the files you edited>
uv run mypy backend/models/src backend/shared/*/src backend/services/*/src plugins/*/src sdk/src
uv run --package <service> pytest backend/services/<service>/tests -n 2
uv run pytest tests/<folder> -n 2
pnpm install
pnpm --filter ./frontend/<app> run lint
pnpm --filter ./frontend/<app> run typecheck
```

- `.github/workflows/ci.yml` runs on every push and pull request, for what the change touches: `ruff check`,
  `ruff format --check`, `mypy` and `pytest` for each Python package (`python.yml`), and lint, type check and tests for
  each front end (`typescript.yml`). All of them must pass.
- Run a service's tests with `--package <service>`, from its own `tests/` folder.
- Serve a service on a laptop from its folder, `backend/services/<service>/`, with
  `uv run --package <service> uvicorn --factory <service_pkg>.api.app_factory:AppFactory.create --port 8000`.
- Run tests one file or one folder at a time.
- Format only the files you edited, never a whole folder.

## Layout

Each back-end service holds these layers, under its own package, in `backend/services/<service>/`:

| Path | Holds |
| --- | --- |
| `src/<service_pkg>/api/` | The FastAPI application: its routers, their dependencies, middlewares and exception handlers, and its application factory. They call `service` and hold no business rules |
| `src/<service_pkg>/service/` | The business rules, one package per concern |
| `src/<service_pkg>/storage/` | Reading and writing data, and nothing else: the repositories |
| `src/<service_pkg>/models/` | The service's own Pydantic models, enums and their exceptions. They only load and validate, and never log |
| `conf/app.yaml` | The configuration, with every default written out |
| `conf/logger.yaml` | The logging: coloured console and coloured rotating file, written to `logs/` |
| `conf/catalogs/` | Data that would otherwise be hard-coded |
| `tests/` | Mirrors `src/<service_pkg>/` folder by folder |
| `Dockerfile`, `pyproject.toml` | The service's image and its uv package |

The public contracts several packages use (API resources, events, plugin and connector contracts, enums and their
`SE` exceptions) are not in a service: they are the shared models of `backend/models/src/erp_models/`, defined once,
with the same rules as a `models` layer.

Each layer only calls the one below it: `api` imports `service`, and `service` imports `storage`. All three import
`models`, and `models` imports none of them. `api` never imports `storage`, and no layer imports one above it. Any
layer may import `erp_models`, which imports no service and no library of `backend/shared/`.

**Every service is a regular FastAPI application, and no package has a command line.**

- A service's `api/` layer is its FastAPI application: the versioned routers (`/v1`) of `api/http/`, their `Depends`
  providers, the middlewares and the exception handlers, and `api/app_factory.py`. `AppFactory.create()`, a
  `@classmethod` that takes no argument, reads `conf/app.yaml` in the working folder, configures logging from
  `conf/logger.yaml` and returns the `FastAPI` application.
- uvicorn serves it, in the image and on a laptop:
  `uvicorn --factory <service_pkg>.api.app_factory:AppFactory.create --host <host> --port <port>`. The address and the
  port are uvicorn's options, never the service's configuration.
- **NEVER a `cli` module or package** (`cli.py`, `cli/`, `<name>_cli.py`, `cli_<name>.py`), a `__main__.py`, a console
  script (`[project.scripts]` or any other) in a `pyproject.toml`, an argument parser (`argparse`, `click`, `typer`) or
  a read of `sys.argv`, in any package of `backend/`, `plugins/` or `sdk/`. Only the harness (`.claude/`) and CI
  (`.github/`) keep command lines.
- What a command would have done is done the FastAPI way:

  | Instead of a command that | Do |
  | --- | --- |
  | Serves the service | uvicorn serves the application factory |
  | Exports the OpenAPI document | The application serves it at `/openapi.json`, and a script of `.github/scripts/` writes the committed copy from `app.openapi()` |
  | Checks a contract or a generated file | A test in the service's `tests/`, which CI runs with the others |
  | Runs a job beside the service (a consumer, a scheduler, the outbox relay) | An `AsyncRunnable` that the application's lifespan initialises at startup and closes at shutdown |
  | Runs an operation a person starts (an import, a re-index) | An endpoint, behind the rights it needs, that starts the job's runnable |
  | Runs a CI or release step | A script of `.github/scripts/` |

Elsewhere in this file:

- `src/` means every Python source folder: `backend/services/<service>/src/<service_pkg>/`,
  `backend/shared/<lib>/src/<lib_pkg>/`, `backend/models/src/erp_models/`, `plugins/<plugin>/src/` and `sdk/src/`.
- `src/models/` means a service's own `models/` package, or `erp_models`.
- `from service.customers...` reads `from <service_pkg>.service.customers...`.
- `tests/` means the tests folder of the package concerned, or the repository's `tests/`.

## Mono-repo

SimpleERP is a mono-repo with the back end and the front end apart
([D438](docs/specs/06-decisions/technical/d438-repository-layout.md)): Python back-end micro-services and Vue front
ends, each with its own Docker image. The first tickets of phase P0 create this layout, and the tests of
`tests/conventions/` that enforce it.

| Path | Holds |
| --- | --- |
| `pyproject.toml`, `uv.lock` | The uv workspace root (Python 3.13), with one lock for every Python package |
| `package.json`, `pnpm-workspace.yaml`, `pnpm-lock.yaml` | The pnpm workspace of the front ends, with one lock |
| `backend/models/` | `erp_models`: the shared Pydantic models of every public contract, imported by the services, `plugins/` and `sdk/` |
| `backend/shared/<lib>/` | The libraries the services share, with no business rules: lifecycle, logging, configuration, company context and rights, event outbox, metering client, country-pack rules, test helpers |
| `backend/services/<service>/` | One back-end service: its `Dockerfile`, `pyproject.toml`, `conf/`, `src/<service_pkg>/`, `tests/` |
| `frontend/backoffice/` | The back-office web app |
| `frontend/portals/<portal>/` | The customer and supplier portals |
| `frontend/mobile/` | The offline-first mobile app, a progressive web app |
| `frontend/packages/<pkg>/` | The shared TypeScript packages: design tokens, components, API client |
| `plugins/<plugin>/` | The first-party plugins, built on `backend/models/` |
| `sdk/` | The plugin SDK ([D425](docs/specs/06-decisions/technical/d425-plugin-sdk-and-cli.md)), built on `backend/models/` |
| `infra/compose/`, `infra/helm/`, `infra/terraform/` | The laptop and one-server Compose profiles, the Helm charts, the Terraform modules and cloud deployments |
| `packs/countries/`, `packs/sectors/` | The country and sector packs, as data |
| `tests/` | The repository-level tests: `tests/harness/`, `tests/ci/`, and `tests/conventions/`, the [rules a test enforces](#rules-a-test-enforces), run against every Python package |
| `compose.e2e.yaml` | Starts the real images for Playwright |
| `.github/workflows/` | The CI/CD pipeline |

The Python rules in this file apply to `backend/`, `plugins/` and `sdk/`. They do not apply to front-end code.

**Services**

- The layers in [Layout](#layout) sit inside each service, under its own package:
  `backend/services/<service>/src/<service_pkg>/{api,service,storage,models}/`.
- NEVER add a top-level `api`, `service`, `storage` or `models` package to a service. Services share one uv environment,
  so they would overwrite each other.
- A service never imports another service. Code they share goes in `backend/shared/`, which holds no business rules,
  and the contracts they share go in `backend/models/`.
- Services call each other through their HTTP API for reads and commands, and publish what happened as events through
  their outbox.
- `plugins/` and `sdk/` import `erp_models`, never a service: a plugin reaches SimpleERP only through the public API.
- Adding a service must not need a change to `tests/conventions/`, so that its rules cover new code automatically.

**Docker images**

- Each service and front end has exactly one image, built by a multi-stage `Dockerfile` in its own folder.
- The build context is the repository root, because the shared `uv.lock` and `pnpm-lock.yaml` are there.
- A service's image runs uvicorn on its application factory, listening on `0.0.0.0` inside the container. It has no
  console script of its own.

**Front ends**

- Vue 3 with TypeScript and Vite, Pinia for state, and the components of `frontend/packages/` built on the design
  system's tokens ([D407](docs/specs/06-decisions/technical/d407-front-end.md)).
- **Every npm package uses the `@simpleerp` scope**, apps and shared packages alike: `@simpleerp/backoffice`,
  `@simpleerp/config`, `@simpleerp/tokens`, `@simpleerp/ui`, `@simpleerp/api-client`. Never `@simple-erp` or another
  scope.
- Each screen follows its screen page and its HTML mock-ups in `docs/specs/`.
- Front-end tests use Playwright, and live in the app's `e2e/` folder: `frontend/backoffice/e2e/`,
  `frontend/portals/<portal>/e2e/`, `frontend/mobile/e2e/`.
- They run against the real images started by `compose.e2e.yaml`, never a development server, so that they test what
  ships.

**CI/CD**

Each step must pass before the next one starts:

1. Detect what changed, and run jobs only for those services, packages and front ends. A change in `backend/models/`,
   `backend/shared/`, `frontend/packages/`, `uv.lock` or `pnpm-lock.yaml` runs all of them.
2. Run `ruff check`, `ruff format --check`, `mypy` and `pytest` for each changed Python package, and lint, type check
   and tests for each changed front end.
3. Build each changed image.
4. Run Playwright against those images, and upload the HTML report if a test fails.
5. Publish the images tagged with the commit SHA, from `develop` or `master` only.

## Rules a test enforces

`tests/conventions/` fails on any of these, in `src/` and `tests/` unless stated:

- More than one top-level class in a file, whatever the kind of class.
- More than five Python files in a folder, not counting `__init__.py` and `conftest.py`.
- A nested function.
- `@staticmethod`. Use an instance method or a `@classmethod`.
- `Any`. See [Typing](#typing).
- A command line, in the packages of `backend/`, `plugins/` and `sdk/`: a `cli` module or package, a `__main__.py`, a
  console script in a `pyproject.toml`, and, in `src/`, an argument parser or a read of `sys.argv`. See
  [Layout](#layout).
- An attribute starting with an underscore: `self.process`, never `self._process`. Methods may start with one. The only
  exception is a name a third-party protocol owns, listed in `tests/conventions/helpers.py`.
- An import that [Layout](#layout) does not allow.
- A Pydantic model outside `src/models/`.
- A class outside `src/models/` with `start` or `stop`, or with `run` but no lifecycle base class.
- A node without `__call__`, or with `run`.
- A sync method declared after an async method of the same banner section of its class. See
  [File shape](#file-shape).
- A `package.json` under `frontend/` whose package name is not in the `@simpleerp` scope, outside `node_modules`.

## File shape

**NEVER more than one class in one file, whatever the kind of class.** This has no exceptions: it covers Pydantic
models, `Enum`, `TypedDict`, exceptions, helpers and test classes, in `src/` and in `tests/`. Each class has its own
file, named after the class: `CustomerService` in `customer_service.py`, `CustomerStatus` in `customer_status.py`.

**Classes that share a method name share a base class.** `TaskNode` has `__call__`, and `YamlCatalog` has `load`. If two
methods only happen to share a name and mean different things, rename one instead.

**NEVER more than five Python files in one folder.** When a folder would go past five, create sub-folders and dispatch
its files by entity type: `storage/customers/repositories/` for the repositories, `models/customers/enums/` for the
enums. This applies to `src/` and `tests/`, including `exceptions/` folders. `__init__.py` and `conftest.py` do not
count towards the five.

An `enums/` or `exceptions/` package's `__init__.py` re-exports everything under it, so callers keep importing from the
package. Other code is imported by its full path: `from service.customers.customer_service import CustomerService`.

Nothing else sits at module level, so there are no module constants, helper functions, module-level loggers or
module-level applications. The only exception is `__all__`. Constants become `ClassVar` attributes in `UPPER_CASE`,
above the constructor.

Inside a class, the order is: constants and fields, `__init__`, validators, then these two banners. Leave out a banner
whose section would be empty.

```python
    ############################
    # Internal Helpers Methods #
    ############################

    def _active_customers(self, customers: List[Customer]) -> List[Customer]: ...

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self, customer: Customer) -> Customer: ...
```

`@property` and `@classmethod` constructors such as `load` are public, so they go under the second banner.

**Async methods MUST always be declared after the sync methods**, within each banner section: the sync helpers, then
the async helpers under "Internal Helpers Methods"; the sync public methods, then the async public methods under
"Publicly Exposed Methods". A class with no banner, such as a test class, is one section.

```python
    ############################
    # Internal Helpers Methods #
    ############################

    def _active_customers(self, customers: List[Customer]) -> List[Customer]: ...

    async def _fetch_customers(self) -> List[Customer]: ...

    ############################
    # Publicly Exposed Methods #
    ############################

    def create(self, customer: Customer) -> Customer: ...

    async def refresh(self) -> None: ...
```

A task graph node subclasses `TaskNode`, and its work is in `async def __call__(self, state)`, never a `run` method. The
graph adds the instance itself: `graph.add_node(NodeName.CHECK.value, self.check)`. `__call__` goes under the second
banner.

## Lifecycle and factories

Every runnable class except the nodes subclasses `Runnable` or `AsyncRunnable`, and has exactly these methods:

| Method | Does |
| --- | --- |
| `initialize()` | Acquires what the work needs. A service is already serving when it returns |
| `run()` | Does the work. A service blocks here until it is closed, and a job returns when it is done |
| `close()` | Releases everything, and must be safe after a failed or partial `initialize` |

- `execute()` on the base class calls all three, and closes whatever happens. Use it unless something runs alongside.
- They take no arguments. Inputs go to the constructor, and results are read from attributes afterwards, such as
  `ImportJob.imported_count`.
- Runnables are created by an abstract factory in their layer's `factories/` package, with concrete ones in its
  sub-folders: `JobFactory` in `service/factories/`, and `ImportJobFactory` in `service/factories/imports/`. Do not
  call a runnable's constructor in `src/` outside a factory.
- The FastAPI application is not a runnable: `AppFactory` builds it and uvicorn runs it. A job that runs beside it is
  initialised in the application's lifespan and closed when the lifespan ends.

## Imports

`from __future__ import annotations` comes first in every non-empty file, after the module docstring if there is one.
Then come up to three groups, each under its own comment:

```python
from __future__ import annotations

# Standard library imports
from logging import Logger, getLogger
from typing import List, Optional

# Third-party imports
import yaml

# First-party imports
from models.customers.exceptions import SECustomerCatalogUnreadable
```

- Imports are absolute, at the top of the file, never inside a function.
- Import exceptions from their package (`models.customers.exceptions`), not from the file that defines them.
- Test files, `__init__.py` files and most exception files have no group comments.

## Typing

- Annotate every signature, including `-> None`.
- Use `Optional`, `List`, `Dict`, `Tuple`, `Set` and `Union` from `typing`, not `X | None` or `list[str]`.
- Use `JsonValue` for raw input in validators.
- Use `object` only for something truly opaque, or a parameter a third-party signature forces on you.

## Naming

- Exceptions start with `SE` (see [Exceptions](#exceptions)). Other classes write acronyms in title case: `HttpClient`,
  `SqlConfig`.
- Durations and sizes carry their unit: `start_timeout_s`, `poll_interval_ms`, `page_width_px`.
- Bounds on a field are `ClassVar`s named `<FIELD>_MIN` and `<FIELD>_MAX`.
- A field ending in `_key` names a secret store entry and never holds a secret.
- Use `error` for a caught exception and `value` for a validator's input.

## Docstrings and comments

Every class and method in `src/` has a Google-style docstring, private ones included. Types go in parentheses.

```python
class CustomerService:
    """Everything the application does with a customer.

    Attributes:
        repository (CustomerRepository): Where customers are stored.
        logger (Logger): Logger instance.

    Notes:
        Callers go through this class rather than the repository, so that each rule about a customer lives in one
        place.
    """
```

- A class summary says what the class is. A method summary starts with a verb: `Create one customer.`
- List every attribute under `Attributes:`, constants included.
- Use `Args:`, `Returns:` and `Raises:` wherever they apply.
- Put the reasoning in `Notes:`, after the other sections. Use bullets for several points, and bold the ones that would
  cause harm if missed.
- Write ``` ``double_backticks`` ``` around code.
- Avoid inline comments: `src/` has almost none. A reason belongs in `Notes:`.

## Exceptions

Each exception has its own file, and the package's `exceptions/__init__.py` re-exports it through a sorted `__all__`.

| Kind | Name | Docstring |
| --- | --- | --- |
| Layer base | `SE<Domain>Error` | `Base class for every error raised while storing a customer.` |
| Layer | `SE<Domain><Problem>Error` | `Raised when a customer cannot be found.` |
| Model base | `SEInvalid<Model>Exception` | `Exception raised when an invalid DatabaseConfig is provided.` |
| Model field | `SE<Model>Invalid<Field>` | `Exception raised when an invalid ``port`` is provided.` |
| Model, other | `SE<Model><Problem>` | `SECustomerCatalogUnreadable`, `SEDatabaseConfigNoHost` |

- Each file is the class name in snake case: `se_database_config_invalid_port.py`.
- Keep the cause: `raise SECustomerCatalogUnreadable(...) from error`.
- Outside `models`, log at `ERROR` just before raising.
- Catch specific types. A broad `except Exception` exists only where any failure must be reported rather than end the
  process.

## Messages

**Use the `exception-and-log-messages` skill whenever you write a `raise` or a log call.** A message with two or more
sentences has one sentence per source line, with no comma between them, and the first line ends with `# noqa: E501`:

```python
raise SEDatabaseConfigInvalidPort(
    f"Invalid port: {value}. "  # noqa: E501
    f"Must be in [{cls.PORT_MIN}, {cls.PORT_MAX}]."
)
```

- A field error reads `Invalid <field>: {value!r}.` then `Must be ...`
- Write full sentences that end with a full stop, and no semicolons.

## Logging

Classes outside `models` that log take the logger as their last constructor argument:

```python
def __init__(self, config: DatabaseConfig, logger: Optional[Logger] = None) -> None:
    self.config = config
    self.logger = logger if logger else getLogger(__name__)
```

- Use lazy arguments, never an f-string: `self.logger.info("Created customer %s in %d ms.", name, duration_ms)`.
- Use the levels this way:

  | Level | For |
  | --- | --- |
  | `DEBUG` | Decisions and small steps |
  | `INFO` | What was actually done |
  | `WARNING` | A degraded result the code recovers from |
  | `ERROR` | A failure, just before raising |

- **Every method logs, at each level that applies to it, except in `tests/` and `src/models/`.** Not every method has a
  failure to report, so do not invent one, but every failure path has its `WARNING` or `ERROR`.
- These stay silent, because they have nothing to report: one-line getters and predicates, data holders, and code that
  runs for every event. Log the outcome one level up instead.
- The log file holds colour codes. Read it with `tail -f` or `less -R`.
- `DEBUG` lines are written by default, because the root level in `conf/logger.yaml` is `DEBUG`. Keep them short.
- **Never log a secret or a typed value.** If an error might quote one, log `type(error).__name__`.
- `models` never logs. It raises.
- Nothing in `src/` uses `print`: a service answers through its HTTP API and reports through its logs.

## Pydantic models

Every field has a `Field(description=...)` and a `@field_validator` that raises its own exception. Fields with the same
rule may share a validator.

```python
class DatabaseConfig(BaseModel):
    model_config = ConfigDict(extra="forbid", validate_default=True)

    port: int = Field(default=5432, description="The port the database listens on.")

    @field_validator("port", mode="before")
    def validate_port(cls, value: JsonValue) -> JsonValue:
        """Validate ``port``. ..."""
        if value is None:
            return cls.model_fields["port"].get_default(call_default_factory=True)
        if isinstance(value, bool) or not isinstance(value, int):
            raise SEDatabaseConfigInvalidPort(...)
        return value
```

- Validators are named `validate_<field>` and use `mode="before"`. Do not add `@classmethod`: ruff is configured for
  `field_validator`.
- `None` becomes the default, if the field has one.
- Reject `bool` where a number is expected, because Python treats it as an `int`.
- Strip strings, and reject empty ones.
- Check rules across fields in `@model_validator(mode="after")`.
- Use `extra="forbid"`. Configuration sections add `validate_default=True`. Models that must not change use
  `frozen=True`.

## Data and enums

- Do not hard-code data in Python. It goes in `conf/catalogs/*.yaml`, loaded by a model that subclasses `YamlCatalog`,
  which provides `load(path)` and raises the model's `UNREADABLE` exception.
- A string that selects behaviour is a `StrEnum` with `@unique`, in its own file named after it, with its members
  listed under `Attributes:`.
- Use `match`/`case` to branch on an enum.
- Open files with `encoding="utf-8"`.
- Secrets live in a secret store. They never appear in configuration or logs.

## Tests

- Name files `test_<subject>.py`, in the folder that mirrors the source. There are no `__init__.py` files.
- Put each file's tests in one `Test<Subject>` class. A helper class, such as a stand-in server, gets its own file.
- When a source file needs several test classes, give it a folder of its name:
  `tests/service/customers/customer_service/`.
- In that folder, `helpers.py` holds the functions and constants several classes share, and `conftest.py` the fixtures.
  Import them by their full path: `from tests.service.customers.customer_service.helpers import a_customer`.
- Scripts that tests run as child processes load their helpers by path, so keep them in place.
- Name tests as sentences: `test_a_customer_without_a_name_is_refused`.
- Tests need no docstrings, banners or import comments. Add a docstring only if the purpose is not obvious.
- Assert the specific exception: `pytest.raises(SEDatabaseConfigInvalidPort)`.
- Use `pytest.mark.parametrize` for cases of the same behaviour.
- Async tests need no marker, because `asyncio_mode` is `auto`.
- Prefer real things to mocks. `unittest.mock` is not used: tests use real services, such as a local test server.

Every model gets this set of tests:

```python
class TestDatabaseConfig:
    def test_defaults(self) -> None: ...
    def test_full_valid_construction(self) -> None: ...
    def test_none_becomes_the_default(self, name: str) -> None: ...
    def test_rejects_bad_values(self, name: str, value: JsonValue, error: type[Exception]) -> None: ...
    def test_rejects_unknown_keys(self) -> None: ...
    def test_round_trip(self) -> None: ...
```

## Formatting and prose

- Ruff handles formatting, with lines up to 120 characters and double quotes.
- Write docstrings, messages and documentation in plain British English: `Initialise`, `normalised`, `colour`,
  `catalogue`. Identifiers use `catalog`.
- Do not use em dashes.
