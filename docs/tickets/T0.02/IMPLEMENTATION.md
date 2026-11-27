# T0.02: Implementation choices

**Ticket:** [TICKET.md](TICKET.md) · **How it works:** [EXPLAIN.md](EXPLAIN.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🎯 Constraints

- The import boundaries of the layout are those of [D438](../../specs/06-decisions/technical/d438-repository-layout.md) and of [AGENT.md](../../../AGENT.md) (Layout and Mono-repo): `erp_models` imports no service or library, libraries import models and libraries, plugins and the SDK import `erp_models`.
- Adding a library or a service must not need a change to `tests/conventions/` ([AGENT.md](../../../AGENT.md), Mono-repo; acceptance criterion 4 of [TICKET.md](TICKET.md)).
- A folder holds at most five Python files, and a file one class ([AGENT.md](../../../AGENT.md), File shape): [`tests/conventions/`](../../../tests/conventions/convention_scanner.py) was already full.
- A front end uses the shared ESLint and strict TypeScript settings ([D407](../../specs/06-decisions/technical/d407-front-end.md)); no front-end app exists yet.
- Broken fixtures must not be committed as source trees, because the repository-wide rules would scan them.

## ⚖️ Choices at a glance

| # | Decision | Chosen | Main alternative | Trade-off accepted |
| --- | --- | --- | --- | --- |
| [D1](#d1) | How packages are known to the rules | Found from the folders on disk | A list of names in the helpers | Each rule reads the disk on each call |
| [D2](#d2) | How strict the rules are | Literal: only `erp_models` for plugins, SDK and models | Allow a library for plugins, or the SDK for plugins | A plugin cannot use the SDK until the rule changes |
| [D3](#d3) | Where the broken fixtures live | Written to `tmp_path` by the tests | Committed broken source trees | Each test file builds its own tree |
| [D4](#d4) | Where the new tests live | `tests/conventions/scanner/` | `tests/conventions/` itself | Helper code copied into four files |
| [D5](#d5) | How the front-end settings are proven | Vitest on fixture front ends inside the config package | Wait for the first real app | The apps are not wired yet |
| [D6](#d6) | The ESLint rule set | Recommended sets, not type-aware | Type-aware strict sets | Fewer checks, faster lint |

## <a id="d1"></a>D1: How packages are known to the rules

**Chosen:** the package names are read from the source folders · **Where:** [`tests/conventions/convention_scanner.py:89-91`](../../../tests/conventions/convention_scanner.py#L89-L91) · **Source:** PLAN.md, K08

| Option | For | Against |
| --- | --- | --- |
| ✅ Found on disk | A new library or plugin is covered at once, as AGENT.md requires; [`test_new_packages.py:59`](../../../tests/conventions/scanner/test_new_packages.py#L59) proves it | The folder tree is walked on every rule call |
| A list of names | Simple to read | Every new package would need a test change, against AGENT.md |

**Trade-off:** a little disk reading in the tests, for no maintenance.

**Revisit when:** the scan time of `tests/conventions/` becomes a problem. No measure was taken.

## <a id="d2"></a>D2: How strict the rules are

**Chosen:** the literal reading of D438 and the layout page · **Where:** [`tests/conventions/convention_scanner.py:336-350`](../../../tests/conventions/convention_scanner.py#L336-L350) · **Source:** PLAN.md assumptions, review note

| Option | For | Against |
| --- | --- | --- |
| ✅ Models import nothing else, libraries may not import a plugin or the SDK, plugins and the SDK import only `erp_models` | Matches the layout page ("plugins, built on backend/models") and AGENT.md ("`plugins/` and `sdk/` import `erp_models`, never a service") | A plugin may not import `erp_sdk` |
| Allow plugins to import the SDK | Might suit a future SDK | No page says so; it would loosen the rule without a source |

**Trade-off:** a stricter rule than the ticket wording. The reviewer noted it.

**Revisit when:** a plugin needs the SDK. Whether D425's SDK is meant to be imported by plugins is an open point.

## <a id="d3"></a>D3: Where the broken fixtures live

**Chosen:** the tests write them to `tmp_path` · **Where:** [`tests/conventions/scanner/test_shared_models_imports.py:48`](../../../tests/conventions/scanner/test_shared_models_imports.py#L48) · **Source:** PLAN.md assumptions

| Option | For | Against |
| --- | --- | --- |
| ✅ `tmp_path` trees | Repository-wide rules never see them; same approach as the existing scanner tests | Each file builds its tree |
| Committed broken trees | Easy to read | The rules would scan them and fail |

**Trade-off:** some repeated set-up code (see D4).

**Revisit when:** a shared fixture builder exists (the first follow-up).

## <a id="d4"></a>D4: Where the new tests live

**Chosen:** four self-contained files in `tests/conventions/scanner/` · **Where:** [`tests/conventions/scanner/test_new_packages.py`](../../../tests/conventions/scanner/test_new_packages.py) · **Source:** PLAN.md assumptions

| Option | For | Against |
| --- | --- | --- |
| ✅ The `scanner/` folder, self-contained files | `tests/conventions/` already holds five files, the AGENT.md limit; the wave-1 tasks owned one file each | `write()` and the clean tree are copied four times |
| `tests/conventions/` itself | Next to the scanner | Breaks the five-file limit |
| A shared helpers module | No copies | It would be a file shared between parallel tasks, against TKT-4 |

**Trade-off:** duplication, recorded as a follow-up.

**Revisit when:** the helpers module is added.

## <a id="d5"></a>D5: How the front-end settings are proven

**Chosen:** Vitest tests that lint and compile fixture front ends extending the shared files · **Where:** [`frontend/packages/config/tests/eslint-settings.test.ts:21`](../../../frontend/packages/config/tests/eslint-settings.test.ts#L21), [`strict-typescript.test.ts:21`](../../../frontend/packages/config/tests/strict-typescript.test.ts#L21) · **Source:** PLAN.md assumptions

| Option | For | Against |
| --- | --- | --- |
| ✅ Fixture front ends in the package | Works now, with no app; shows that extending the files has an effect | The real apps are not wired |
| Wire `frontend/backoffice` and `frontend/mobile` | Tests the real apps | They have no sources yet; later tickets create them |

**Trade-off:** a package-level proof now, wiring later (third follow-up).

**Revisit when:** the apps get their first sources.

## <a id="d6"></a>D6: The ESLint rule set

**Chosen:** `@eslint/js`, `typescript-eslint` and `eslint-plugin-vue` recommended sets · **Where:** [`frontend/packages/config/eslint.base.js:9-11`](../../../frontend/packages/config/eslint.base.js#L9-L11) · **Source:** PLAN.md assumptions

| Option | For | Against |
| --- | --- | --- |
| ✅ Recommended, not type-aware | D407 names Vue 3 and TypeScript; needs no project file per app | Fewer checks |
| Type-aware strict sets | Stricter | Each app would need type information to lint; no reason is given in the ticket |

**Trade-off:** a modest rule set that can be tightened later.

**Revisit when:** a front end shows defects the recommended set misses. Open point: no one measured this.

## 📝 Assumptions behind the choices

- The roadmap row has no anchor of its own, so the sprint anchor `#s01` is used: supports [D1](#d1).
- The criteria come from the roadmap row, since D438 defers the convention tests to this ticket: supports [D2](#d2) and [D5](#d5).
