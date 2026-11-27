# T0.05: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- `execute()` closes whatever happens, for both the sync and the async form, and runnables are created by factories ([AGENT.md "Lifecycle and factories"](../../../AGENT.md)).
- A shared library has no business rules and lives in `backend/shared/<lib>` ([D438](../../specs/06-decisions/technical/d438-repository-layout.md), [D406](../../specs/06-decisions/technical/d406-back-end.md)).
- Inputs go to the constructor, so the base classes and `create()` take no argument beyond the optional logger ([AGENT.md](../../../AGENT.md)).
- Nothing logs a typed value or a secret: an error is logged by its type only ([AGENT.md "Logging"](../../../AGENT.md)).
- Classes that share a method name share a base class, and one class per file ([AGENT.md "File shape"](../../../AGENT.md)).
- The package name `erp_lifecycle` is the one the harness tests already use, for example [`test_check_touched_layout.py`](../../../tests/harness/check_touched/test_check_touched_layout.py).

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How `execute()` guarantees the close | `try`/`except`/`finally`, error re-raised unchanged | Wrap the error in an `SE` exception | A `close()` that raises replaces the first error |
| [D2](#d2) | Shape of the factory base | One generic `RunnableFactory` with `create()` and no argument | Arguments on `create()`, or one factory base per runnable kind | Inputs only through the factory constructor |
| [D3](#d3) | How the root sees the library | Root `dependencies = ["erp-lifecycle"]` with a workspace source | Leave the root with no dependency | Open point: reason not recorded |
| [D4](#d4) | Sync and async bases | Two separate classes without a common base | One shared base class | Two near-copies of `execute()` that already drift |
| [D5](#d5) | Closing after a failed `initialize()` | `close()` abstract, safe by the subclass's duty | A default `close()` in the base | Each subclass must handle partial state |
| [D6](#d6) | Criterion 3 | New cases in the scanner tests, scanner unchanged | Change the scanner | Criterion 4 has no convention test yet |

## <a id="d1"></a>D1: How `execute()` guarantees the close

**Chosen:** `try`/`except Exception`/`finally`, with `raise` and no wrapping · **Where:** [`runnable.py:53-63`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L53-L63), [`async_runnable.py:53-63`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L53-L63) · **Source:** plan assumption, read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ `finally` and bare `raise` | `close()` runs on every path, including a failed `initialize()`. The caller sees the original exception type. Only `type(error).__name__` is logged, as AGENT.md asks. | A `close()` that raises inside `finally` replaces the original error (plain `try`/`finally` behaviour). |
| Wrap the error in an `SE` exception | Fits the "SE" naming of AGENT.md for layer errors. | The plan states the specifications only say "closes whatever happens"; a wrapper would hide the caller's own exception types. |

**Trade-off:** the failure of `close()` can mask the first error. The two `execute()` methods also log differently (see the follow-up in [EXPLAIN.md](EXPLAIN.md)).

**Revisit when:** the first service shows a real `close()` that fails after a failed `run()`: then log it and keep the first error.

## <a id="d2"></a>D2: Shape of the factory base

**Chosen:** one `RunnableFactory[RunnableT: Union[Runnable, AsyncRunnable]]` with an abstract `create()` that takes no argument · **Where:** [`runnable_factory.py:13`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L13), [`runnable_factory.py:37-43`](../../../backend/shared/lifecycle/src/erp_lifecycle/factories/runnable_factory.py#L37-L43) · **Source:** plan assumption (K08), reviewer note on typing

| Option | For | Against |
| --- | --- | --- |
| ✅ One generic base, `create()` without arguments | AGENT.md says inputs go to the constructor. One base serves sync and async runnables, and `mypy` knows the type built. | AGENT.md names `ServiceFactory` and `CommandFactory` but not the base nor its method: the name and the method are the plan's assumption. |
| Arguments on `create()` | A single factory could build many differently configured runnables. | Contradicts "They take no arguments. Inputs go to the constructor". |

**Trade-off:** a factory is built per set of inputs, not shared across them.

**Revisit when:** a service needs one factory to build many runnables with different inputs (T0.14 and later).

## <a id="d3"></a>D3: How the root sees the library

**Chosen:** the root depends on `erp-lifecycle` · **Where:** [`pyproject.toml:8`](../../../pyproject.toml#L8), [`pyproject.toml:14-15`](../../../pyproject.toml#L14-L15) · **Source:** plan assumption (K05)

| Option | For | Against |
| --- | --- | --- |
| ✅ Root dependency plus workspace source | The plan says the verifier runs `uv run pytest <folder>` from the root and installs only the root project, so the library is importable that way. | The reviewer notes that CI runs `uv sync --locked --all-packages` and `erp-models` is not a root dependency. It touches a root file other tickets may change. |
| No root dependency | The root stays a dependency-free virtual workspace. | The plan's reason says imports would fail from the root. |

**Trade-off:** a root file is shared between running tickets.

**Revisit when:** open point. The review asks to either explain or drop it; no worker or reviewer measured whether `--all-packages` makes it redundant.

## <a id="d4"></a>D4: Sync and async bases

**Chosen:** `Runnable` and `AsyncRunnable` as two unrelated classes · **Where:** [`runnable.py:9`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L9), [`async_runnable.py:11`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/async_runnable.py#L11) · **Source:** plan assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Two classes | AGENT.md names both. Their methods differ in being coroutines, so the rule on shared method names is taken not to apply. | The `execute()` bodies are duplicated and have already drifted. |
| A common base class | Follows "classes that share a method name share a base class" literally. | The signatures cannot be shared: one set is `async`. |

**Trade-off:** duplicated logic and a drift to fix.

**Revisit when:** a third lifecycle form appears, or the drift causes a bug.

## <a id="d5"></a>D5: Closing after a failed `initialize()`

**Chosen:** `close()` is abstract and the subclass makes it safe · **Where:** [`runnable.py:41-43`](../../../backend/shared/lifecycle/src/erp_lifecycle/runnables/runnable.py#L41-L43) · **Source:** plan assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Abstract `close()` | AGENT.md says `close()` "must be safe after a failed or partial `initialize`"; only the subclass knows what it acquired. | Nothing in the base enforces it. |
| Default `close()` in the base | No subclass forgets it. | The base cannot know what to release. |

**Trade-off:** safety rests on the subclass and its tests.

**Revisit when:** a service shows the same release pattern in several subclasses.

## <a id="d6"></a>D6: Criterion 3 and the scanner

**Chosen:** add cases to the scanner's tests and leave the scanner alone · **Where:** [`test_convention_scanner.py:91`](../../../tests/conventions/scanner/test_convention_scanner.py#L91), [`test_convention_scanner.py:146-156`](../../../tests/conventions/scanner/test_convention_scanner.py#L146-L156) · **Source:** plan assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Tests only | The scanner already exempts bases named `Runnable` and `AsyncRunnable`, as the plan notes. | No convention test refuses a runnable constructor called outside `factories/`, so criterion 4 rests on the factory's own tests. |
| Change the scanner | Would also enforce criterion 4. | Not needed by criterion 3. Open point: nobody weighed its cost. |

**Trade-off:** criterion 4 is tested, not enforced.

**Revisit when:** the first service lands (T0.14).

## 📝 Assumptions behind the choices

- The roadmap gives no use case, so the criteria come from D406, D438 and AGENT.md: supports [D1](#d1), [D2](#d2), [D5](#d5).
- The folder is `backend/shared/lifecycle` (D572), matching D438: supports [D3](#d3).
