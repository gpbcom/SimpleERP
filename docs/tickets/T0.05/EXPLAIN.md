# T0.05: Lifecycle and factories library

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- Adds the first shared library of the repository, `erp-lifecycle`, with no dependency and no business rule.
- Gives every future service and job two base classes, `Runnable` and `AsyncRunnable`, whose `execute()` always closes what it opened, even when `initialize()` or `run()` fails.
- Gives an abstract `RunnableFactory`, so that runnables are built by a factory and not by a direct constructor call.
- Extends the convention scanner tests so that the async form and the new base classes are accepted.

## ⚙️ How it works

1. **The library is a workspace member:** its own project declares the package `erp_lifecycle` and no dependency, in [`backend/shared/lifecycle/pyproject.toml`](../../../backend/shared/lifecycle/pyproject.toml#L1-L14). The root workspace already includes `backend/shared/*`, and the root now depends on it through a workspace source, in [`pyproject.toml`](../../../pyproject.toml#L8) and [`pyproject.toml`](../../../pyproject.toml#L14-L15).
2. **A runnable is built:** the base constructor keeps the given logger or makes one named after the module, in [`runnable.py:21-27`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L21-L27) and [`async_runnable.py:23-29`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L23-L29).
3. **A subclass must define the three steps:** `initialize`, `run` and `close` are abstract, in [`runnable.py:33-43`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L33-L43) (coroutines in [`async_runnable.py:35-45`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L35-L45)). Without one of them the class cannot be instantiated.
4. **`execute()` runs the steps:** `initialize()` then `run()` inside a `try`, in [`runnable.py:53-56`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L53-L56). The async version awaits them, in [`async_runnable.py:53-57`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L53-L57).
5. **A failure is logged and re-raised unchanged:** the `except` logs at `ERROR` only the exception type, never its message, then `raise`, in [`runnable.py:58-60`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L58-L60) and [`async_runnable.py:58-60`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L58-L60).
6. **`close()` always runs:** the `finally` block calls it (awaits it, for the async form), whether the steps passed or failed, in [`runnable.py:61-63`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L61-L63) and [`async_runnable.py:61-63`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L61-L63). Making `close()` safe after a failed `initialize()` is the subclass's duty, stated in the class notes at [`runnable.py:15-18`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L15-L18).
7. **A factory builds the runnable:** `RunnableFactory` is generic over `Runnable` or `AsyncRunnable`, in [`runnable_factory.py:13`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L13). Its one abstract `create()` takes no argument, in [`runnable_factory.py:37-43`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L37-L43): a concrete factory receives the inputs at its own constructor.
8. **The convention scanner accepts both forms:** the new cases in [`test_convention_scanner.py:91`](../../../tests/conventions/scanner/test_convention_scanner.py#L91) and [`test_convention_scanner.py:146-156`](../../../tests/conventions/scanner/test_convention_scanner.py#L146-L156) show that an `async def run` without a lifecycle base is refused and that subclasses of both bases are accepted.

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`backend/shared/lifecycle/pyproject.toml`](../../../backend/shared/lifecycle/pyproject.toml) | Added | [1-14](../../../backend/shared/lifecycle/pyproject.toml#L1) | +14 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/factories/__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py) | Added | [1-43](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L1) | +43 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/py.typed`](../../../backend/shared/lifecycle/src/erp_lifecycle/py.typed) | Added | ➖ | +0 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/runnables/__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py) | Added | [1-63](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L1) | +63 | −0 |
| [`backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py) | Added | [1-63](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L1) | +63 | −0 |
| [`backend/shared/lifecycle/tests/factories/stand_in_runnable.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable.py) | Added | [1-41](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable.py#L1) | +41 | −0 |
| [`backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py) | Added | [1-33](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py#L1) | +33 | −0 |
| [`backend/shared/lifecycle/tests/factories/test_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py) | Added | [1-50](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py#L1) | +50 | −0 |
| [`backend/shared/lifecycle/tests/runnables/recording_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/recording_async_runnable.py) | Added | [1-38](../../../backend/shared/lifecycle/tests/runnables/recording_async_runnable.py#L1) | +38 | −0 |
| [`backend/shared/lifecycle/tests/runnables/recording_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/recording_runnable.py) | Added | [1-44](../../../backend/shared/lifecycle/tests/runnables/recording_runnable.py#L1) | +44 | −0 |
| [`backend/shared/lifecycle/tests/runnables/test_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_async_runnable.py) | Added | [1-67](../../../backend/shared/lifecycle/tests/runnables/test_async_runnable.py#L1) | +67 | −0 |
| [`backend/shared/lifecycle/tests/runnables/test_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py) | Added | [1-57](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py#L1) | +57 | −0 |
| [`docs/technical/architecture/backend.md`](../../../docs/technical/architecture/backend.md) | Modified | [10-11](../../../docs/technical/architecture/backend.md#L10), [39](../../../docs/technical/architecture/backend.md#L39) | +3 | −1 |
| [`pyproject.toml`](../../../pyproject.toml) | Modified | [8](../../../pyproject.toml#L8), [15-17](../../../pyproject.toml#L15) | +4 | −1 |
| [`tests/conventions/scanner/test_convention_scanner.py`](../../../tests/conventions/scanner/test_convention_scanner.py) | Modified | [91](../../../tests/conventions/scanner/test_convention_scanner.py#L91), [146-156](../../../tests/conventions/scanner/test_convention_scanner.py#L146) | +12 | −0 |
| [`uv.lock`](../../../uv.lock) | Modified | [7](../../../uv.lock#L7), [75-79](../../../uv.lock#L75), [346-348](../../../uv.lock#L346), [364](../../../uv.lock#L364) | +10 | −0 |
| **19 files** | | | **+542** | **−2** |
<!-- /changes -->

- [`backend/shared/lifecycle/pyproject.toml`](../../../backend/shared/lifecycle/pyproject.toml), lines [`1-14`](../../../backend/shared/lifecycle/pyproject.toml#L1-L14): the new uv project `erp-lifecycle`, Python 3.13, no dependency, built with `uv_build` as module `erp_lifecycle`.
- [`backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py) and [`async_runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py): the two abstract bases and their `execute()`, lines 9-63 and 11-63.
- [`backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py), lines [`13-43`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L13-L43): the abstract generic factory.
- [`backend/shared/lifecycle/src/erp_lifecycle/py.typed`](../../../backend/shared/lifecycle/src/erp_lifecycle/py.typed) and the empty package files [`__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/__init__.py), [`runnables/__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/__init__.py), [`factories/__init__.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/__init__.py): the typed package. Callers import by full path, as AGENT.md requires.
- [`backend/shared/lifecycle/tests/runnables/`](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py): [`test_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py) and [`test_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_async_runnable.py), with the helper classes [`recording_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/recording_runnable.py) and [`recording_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/recording_async_runnable.py). The failing-initialize cases are at [`test_runnable.py:21`](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py#L21) and [`test_async_runnable.py:53`](../../../backend/shared/lifecycle/tests/runnables/test_async_runnable.py#L53).
- [`backend/shared/lifecycle/tests/factories/`](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py): [`test_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py) with the stand-ins [`stand_in_runnable.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable.py) and [`stand_in_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py), proving that a concrete factory builds the runnable with its inputs and a new instance each time.
- [`tests/conventions/scanner/test_convention_scanner.py`](../../../tests/conventions/scanner/test_convention_scanner.py), lines [`91`](../../../tests/conventions/scanner/test_convention_scanner.py#L91) and [`146-156`](../../../tests/conventions/scanner/test_convention_scanner.py#L146-L156): the async cases. The scanner itself is unchanged.
- [`pyproject.toml`](../../../pyproject.toml), lines [`8`](../../../pyproject.toml#L8) and [`14-15`](../../../pyproject.toml#L14-L15), and [`uv.lock`](../../../uv.lock): the root depends on `erp-lifecycle` through a workspace source, and the lock gains that member.
- [`docs/technical/architecture/backend.md`](../../../docs/technical/architecture/backend.md), lines [`10`](../../../docs/technical/architecture/backend.md#L10) and [`39`](../../../docs/technical/architecture/backend.md#L39): a paragraph on the library and the new review date.

## 🧪 How to test it

```bash
uv run --package erp-lifecycle pytest backend/shared/lifecycle/tests -n 2
uv run pytest tests/conventions/scanner -n 2
uv run ruff check backend/shared/lifecycle tests/conventions
uv run mypy backend/shared/lifecycle/src
```

The first shows the 28 tests of the library, including the two failing-`initialize()` cases. The second shows the scanner accepting both bases. The last two show the lint and type checks.

## 🔗 Evidence

- [Library tests](tests-evidences/pytest-backend-shared-lifecycle.txt): 28 passed.
- [Repository tests](tests-evidences/pytest.txt): 1156 passed.
- [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt) and [mypy](tests-evidences/mypy.txt): pass.
- [Plan view](tests-evidences/plan-view.txt) and [specification links](tests-evidences/ticket-refs.txt): up to date and empty (no unresolved link).

## 📝 Assumptions accepted

- The roadmap gives no use case, business rule or requirement for T0.05, so the criteria come from D406, D438, the design pages and AGENT.md "Lifecycle and factories".
- Criteria 2 and 4 come from AGENT.md word for word.
- The links use the sprint anchor `#s01` and the epic anchor `#epics`, because the roadmap rows have no ticket anchor.
- The folder is `backend/shared/lifecycle` (D572), which matches D438's `backend/shared/<lib>` layout.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L45-L63), [`async_runnable.py`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L47-L63) | The two `execute()` methods log differently: `Runnable` logs "Ran %s." and "Failed to execute %s: %s."; `AsyncRunnable` logs no INFO line on success and "Failed %s with %s.". Use the same messages in both. A `close()` that raises in `finally` replaces the original error, so either say so in `Raises` (`Runnable` says "unchanged") or log the close failure and keep the first error. |
| [`test_runnable_factory.py:49`](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py#L49) | The assertion on `RunnableFactory.__init__(...) is None` is always true (the review note cites line 360, the file has 50 lines). Replace it with an `isinstance(..., Logger)` check on a factory built without a logger, or split the test in two. |
| [`stand_in_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py), [`stand_in_runnable.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable.py), [`recording_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/recording_async_runnable.py) | The import group comments are wrong (`# First-party imports` above the `backend.shared...` import, `erp_lifecycle` unlabelled). Test files need none: remove them. In `recording_async_runnable.py`, annotate `INITIALIZE_MESSAGE` and `RUN_MESSAGE` as `ClassVar[str]`. |
| [`test_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/test_runnable_factory.py), [`test_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_runnable.py), [`test_async_runnable.py`](../../../backend/shared/lifecycle/tests/runnables/test_async_runnable.py), [`stand_in_runnable_factory.py`](../../../backend/shared/lifecycle/tests/factories/stand_in_runnable_factory.py) | They import helpers as `backend.shared.lifecycle.tests...`, while `backend/models` (T0.03) uses `tests...`. Pick one style for the shared packages once both have landed. |
| [`convention_scanner.py`](../../../tests/conventions/convention_scanner.py), [`test_convention_scanner.py`](../../../tests/conventions/scanner/test_convention_scanner.py) | Criterion 4 is proven only by the factory's own tests. Add a convention test that refuses a runnable constructor called in `src/` outside a `factories/` package, when the first service lands (T0.14). |
| [`pyproject.toml`](../../../pyproject.toml#L8), [`uv.lock`](../../../uv.lock) | The root has a runtime dependency on `erp-lifecycle`, although CI installs every member with `uv sync --locked --all-packages`. No agent reported it as a decision: it is recorded in [IMPLEMENTATION.md](IMPLEMENTATION.md#d3) as an open point. Drop it or explain it. |
| [`tests-evidences/`](tests-evidences/pytest.txt) | Save the output of `uv lock --check` and `uv sync --locked --all-packages` from the clean ticket tree. |
| [`backend.md:10`](../../../docs/technical/architecture/backend.md#L10) | Wrap the T0.05 paragraph (one line of about 380 characters) at 120 like the text around it. |
