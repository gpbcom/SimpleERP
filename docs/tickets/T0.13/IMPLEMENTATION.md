# T0.13: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The library is `backend/shared/testing`, with no business rules, and each of its tests uses its own helpers ([TICKET.md](TICKET.md), acceptance criteria 1 and 5; [D438](../../specs/06-decisions/technical/d438-repository-layout.md)).
- A stand-in with no configured answer returns a valid empty value of the real model (TEST-2, acceptance criterion 2).
- Only synthetic data, and no mock library ([D426](../../specs/06-decisions/technical/d426-testing-strategy.md), [Tests and traceability](../../technical/delivery/tests-and-traceability.md)).
- AGENT.md forbids module-level functions and constants, a runnable built outside a factory, a nested function and `unittest.mock`; `tests/conventions/` must pass unchanged ([AGENT.md](../../../AGENT.md)).
- `close()` must be safe after a failed `initialize` (AGENT.md, "Lifecycle and factories").

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How the fixtures are exposed | One `TestingPlugin` class, registered by a conftest | A `pytest11` entry point with a module of hooks | Each consumer writes three lines of registration |
| [D2](#d2) | Where the company of `company_context` comes from | `user_builder.company` | A second company from `company_builder` | The fixture depends on the user builder only |
| [D3](#d3) | Form of the session-scoped fixtures | Instance methods of the plugin | `@classmethod` fixtures | A pytest 10 deprecation warning |
| [D4](#d4) | Missing PostgreSQL binaries | Skip inside a nested `try`, close in `finally` | Catch the error in the factory | A nested `try` in the fixture |
| [D5](#d5) | How a PostgreSQL server is provided | Local binaries, trust authentication, no driver | Docker or testcontainers | Tests are skipped where binaries are missing |
| [D6](#d6) | The default answer of a stand-in route | Valid empty value of the model, refused at registration if none | Answer an empty JSON object whatever the model | Models need defaults, or `many` |
| [D7](#d7) | `logs` package under `src/` | Un-ignore `src/**/logs/` and `tests/**/logs/` in the ignore rules | Rename the package | One more ignore rule and a test |

## <a id="d1"></a>D1: How the fixtures are exposed

**Chosen:** a `TestingPlugin` class · **Where:** [`testing_plugin.py:24`](../../../backend/shared/testing/src/erp_testing/plugin/testing_plugin.py#L24) · **Source:** plan assumption

| Option | For | Against |
| --- | --- | --- |
| ✅ Plugin class registered in `pytest_configure` | Fits AGENT.md: only classes at module level in `src/`; the library's own tests register it in [`conftest.py:8`](../../../backend/shared/testing/tests/plugin/conftest.py#L8), so other test folders could run before it existed | Each consumer must register it |
| `pytest11` entry point | No registration by the consumer | Needs a module of hooks, which AGENT.md forbids at module level |

**Trade-off:** three lines of registration per consumer, documented in [`tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md).

**Revisit when:** the conventions allow a hooks module, or many services repeat the registration.

## <a id="d2"></a>D2: Where the company of `company_context` comes from

**Chosen:** `user_builder.company` and `user_builder.build()` · **Where:** [`testing_plugin.py:134`](../../../backend/shared/testing/src/erp_testing/plugin/testing_plugin.py#L134) · **Source:** K19, then the review fix

| Option | For | Against |
| --- | --- | --- |
| ✅ Company of the user builder | Context company, user `company_id` and `RequestContext` user company are one id by construction; the equality test is [`test_testing_plugin.py:74-78`](../../../backend/shared/testing/tests/plugin/test_testing_plugin.py#L74-L78) | The fixture no longer asks for `company_builder` directly |
| Build the company and user separately (the first version) | Followed the brief literally | Produced two different company ids: data seeded with `user.company_id` fell outside the context (blocking finding, D426) |
| Keep `company_builder` and pass its first build to both | Explicit | Needs the user builder to take an external company, more wiring |

**Trade-off:** a caller building `SyntheticCompanyContext` by hand can still pair mismatched objects (follow-up).

**Revisit when:** `SyntheticCompanyContext` refuses mismatched pairs.

## <a id="d3"></a>D3: Form of the session-scoped fixtures

**Chosen:** instance methods · **Where:** [`testing_plugin.py:64-65`](../../../backend/shared/testing/src/erp_testing/plugin/testing_plugin.py#L64-L65) · **Source:** K19

| Option | For | Against |
| --- | --- | --- |
| ✅ Instance method | Keeps a plugin instance that holds the logger (AGENT.md logging) | `PytestRemovedIn10Warning`, not recommended by pytest |
| `@classmethod` fixtures | What pytest recommends for non-function scopes | The logger would have to live on the class |
| Module-level function | None here | AGENT.md forbids it |

**Trade-off:** a deprecation warning now ([evidence](tests-evidences/pytest-backend-shared-testing.txt)); nothing is read from instance attributes across tests.

**Revisit when:** before pytest 10 (follow-up).

## <a id="d4"></a>D4: Missing PostgreSQL binaries

**Chosen:** nested `try`, skip on `SEPostgresBinariesNotFoundError`, `close()` in the outer `finally` · **Where:** [`testing_plugin.py:75-85`](../../../backend/shared/testing/src/erp_testing/plugin/testing_plugin.py#L75-L85) · **Source:** K19

| Option | For | Against |
| --- | --- | --- |
| ✅ Nested `try` in the fixture | `close()` is safe after a failed `initialize`, so nothing leaks | Two levels of `try` |
| Catch in the factory | Fixture is flatter | The factory would carry a pytest decision |
| Skip inside `finally` | None given | A skip there would hide the close |

**Trade-off:** readability for no leaked server. **Revisit when:** a second fixture needs the same skip.

## <a id="d5"></a>D5: How a PostgreSQL server is provided

**Chosen:** local binaries found by [`postgres_binaries.py:120`](../../../backend/shared/testing/src/erp_testing/postgres/postgres_binaries.py#L120), trust authentication, no Python driver · **Source:** the assumptions of [PLAN.md](PLAN.md)

| Option | For | Against |
| --- | --- | --- |
| ✅ Local binaries | No driver to choose (no decision picks one); fast per-session start | Skipped where binaries are missing, so CI must have them |
| Docker or testcontainers | Same server everywhere | Not used in this plan; needs a container runtime |

**Trade-off:** the 4 skipped tests in the evidence. **Revisit when:** a decision chooses a driver or CI lacks binaries (follow-up on `python.yml`).

## <a id="d6"></a>D6: The default answer of a stand-in route

**Chosen:** the empty value of the route's model, `[]` for a list, refused at registration when the model has none · **Where:** [`stand_in_server.py:83-101`](../../../backend/shared/testing/src/erp_testing/stand_in/stand_in_server.py#L83-L101), [`stand_in_handler.py:104`](../../../backend/shared/testing/src/erp_testing/stand_in/stand_in_handler.py#L104) · **Source:** plan

| Option | For | Against |
| --- | --- | --- |
| ✅ Validate at registration | Meets acceptance criterion 2: the answer is valid for the real model; fails early | A model with required fields needs `many` or an explicit answer |
| Fail at request time | Simpler registration | The error shows in the code under test, far from the cause |

**Trade-off:** TEST-2 is defined by no spec page, only the roadmap row (assumption in [PLAN.md](PLAN.md)). **Revisit when:** a spec defines TEST-2.

## <a id="d7"></a>D7: A `logs` package under `src/`

**Chosen:** un-ignore it in [`.gitignore:35-39`](../../../.gitignore#L35-L39), with [`test_logs_folders.py`](../../../tests/ci/gitignore/test_logs_folders.py) · **Source:** read from the diff

| Option | For | Against |
| --- | --- | --- |
| ✅ Un-ignore `src/**/logs/` and `tests/**/logs/` | Keeps the name `erp_testing.logs` | A rule outside the ticket's own area |
| Rename the package | No ignore-rule change | Open point: no worker recorded why it was not chosen |

**Trade-off:** one extra rule. **Revisit when:** the logging configuration writes logs elsewhere.

## 📝 Assumptions behind the choices

None accepted by the reviewer. The plan's own assumptions (TEST-2 wording, local PostgreSQL binaries) are listed in [PLAN.md](PLAN.md): they support [D5](#d5) and [D6](#d6).
