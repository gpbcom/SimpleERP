# T0.05: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

The round-3 blocker is fixed. `uv.lock` now holds only T0.05's hunks and `reports/lifecycle.xml` is gone. No finding is blocking. Eight follow-ups are listed below.

## What changed

- A new workspace library, `erp-lifecycle` (`backend/shared/lifecycle`, package `erp_lifecycle`), with no dependencies and no business rules (D406, D438).
- `Runnable` and `AsyncRunnable` are abstract bases. Each has `initialize`, `run` and `close`, plus an `execute()` that always calls (or awaits) `close()` in `finally` and passes the original error on unchanged.
- `RunnableFactory[RunnableT]` is an abstract generic factory with one `create()` method that takes no arguments. A concrete factory receives the runnable's inputs at its own constructor.
- The convention scanner tests now also cover the async form: an `async def run` with no lifecycle base is refused, and subclasses of `Runnable` and `AsyncRunnable` imported from `erp_lifecycle` are accepted. The scanner itself already exempts the base classes through `RUNNABLE_BASES`.
- The root `pyproject.toml` depends on `erp-lifecycle` through a workspace source, and `uv.lock` gains only that member.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. A `Runnable` whose `initialize()` fails still calls `close()` from `execute()` | `test_runnable.py::test_a_failed_initialize_still_closes_and_skips_run`, `tests-evidences/pytest-backend-shared-lifecycle.txt` (28 passed) | ✅ Pass |
| 2. An `AsyncRunnable` whose `initialize()` fails still awaits `close()` from `execute()` | `test_async_runnable.py::test_close_is_awaited_and_run_skipped_when_initialize_fails`, same evidence | ✅ Pass |
| 3. The lifecycle convention test accepts subclasses of `Runnable` and `AsyncRunnable` | `tests/conventions/scanner/test_convention_scanner.py::test_what_the_layout_allows_passes` (new cases), `tests-evidences/pytest.txt` (1156 passed) | ✅ Pass |
| 4. A concrete factory builds the runnable, not a direct constructor call | `test_runnable_factory.py::test_the_concrete_factory_builds_a_runnable_carrying_its_inputs`, `test_each_create_returns_a_new_instance` | ✅ Pass (no convention test enforces it yet: follow-up) |
| 5. The library's tests, ruff and mypy pass | `tests-evidences/pytest-backend-shared-lifecycle.txt`, `ruff-check.txt`, `ruff-format.txt`, `mypy.txt` | ✅ Pass |

## Look at first

- **How `execute()` handles errors:** `backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py` and `backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py`. The ERROR log records only the exception type, never its message, so no value leaks into the logs. Note that a `close()` that raises replaces the original error.
- **Workspace wiring:** `pyproject.toml` (the root now depends on `erp-lifecycle`) and `uv.lock` (only T0.05's hunks). T0.03's `erp-models` lock hunk must be regenerated when T0.03 lands. CI runs `uv sync --locked --all-packages`.
- **Factory typing:** `backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py` uses PEP 695 generics bound to `Union[Runnable, AsyncRunnable]`.
- Identity, permissions and company data isolation: not affected. This is a pure lifecycle library with no data access, no secrets and no hot path.

## Assumptions accepted

- The criteria come from D406, D438, the design pages and AGENT.md, because the roadmap gives no use case: accepted, AGENT.md is the binding rule for this foundation library.
- Criteria 2 and 4 come from AGENT.md "Lifecycle and factories": accepted, they quote it word for word.
- The links use the sprint and epic anchors: accepted, they resolve (`ticket-refs.txt` is empty).
- The folder is `backend/shared/lifecycle` (D572): accepted, it matches D438.
- The workers reported no assumptions or decisions.

## Follow-ups

- Make the two `execute()` methods log the same way, and document (or handle) a `close()` that raises and replaces the original error.
- In `test_runnable_factory.py`, the assertion on line 360 is always true. Replace it with a real logger check.
- Remove the wrong import group comments in the test helpers, and mark the async helper's constants as `ClassVar`.
- Settle one import style for test helpers across shared packages (`backend.shared...` here, `tests....` in T0.03).
- Add a convention test that refuses a runnable constructor called outside `factories/` (with T0.14).
- Explain or drop the root `pyproject.toml` dependency on `erp-lifecycle`. No agent reported it as a decision.
- Save the output of `uv lock --check` and `uv sync --locked --all-packages` in `tests-evidences/`.
- Wrap the long T0.05 paragraph in `docs/technical/architecture/backend.md`.
