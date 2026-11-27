# T0.02: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `ConventionScanner` has three new import rules: `shared_models_imports` (`erp_models` imports no other first-party package), `shared_library_imports` (a library of `backend/shared/` imports only `erp_models` and other libraries) and `plugin_and_sdk_imports` (`plugins/` and `sdk/` import only `erp_models` and their own package). `tests/conventions/test_layers.py` runs all three on the real repository.
- First-party packages are found from the folders on disk (`_first_party_packages`), never from a list. A new library, plugin or front-end package needs no change to the tests.
- The new package `@simpleerp/config` in `frontend/packages/config` exports a shared ESLint flat config (`./eslint`: JS, typescript-eslint and Vue recommended rules) and strict TypeScript options (`./tsconfig`).
- Broken fixture front ends under `frontend/packages/config/tests/fixtures/` show that the shared settings apply when a front end extends them. Vitest runs them, and the package's own lint and typecheck leave them out.
- The repository-layout and front-end design pages describe the new rules and the package.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. A broken fixture in `erp_models` that imports a library or a service fails the rule once | `TestSharedModelsImports::test_an_import_of_a_first_party_package_is_reported` (asserts exactly one offender), `tests-evidences/pytest.txt` | ✅ Pass |
| 2. A broken fixture in `backend/shared` that imports a service fails the rule once | `TestSharedLibraryImports::test_a_library_importing_a_service_plugin_or_sdk_is_reported`, `tests-evidences/pytest.txt` | ✅ Pass |
| 3. A broken fixture in `plugins/` or `sdk/` that imports anything but `erp_models` fails the rule once | `TestPluginAndSdkImports::test_an_import_of_another_first_party_package_is_reported`, `tests-evidences/pytest.txt` | ✅ Pass |
| 4. Adding an empty library or front-end package needs no change to the tests | `TestNewPackages::test_an_empty_new_package_passes_every_rule` (library, plugin and front-end package across every rule), plus the two "caught without any list of names" tests | ✅ Pass |
| 5. The shared ESLint and strict TypeScript settings apply to a front end that uses them | `frontend/packages/config/tests/eslint-settings.test.ts`, `strict-typescript.test.ts`, `tests-evidences/test.txt` (7 passed), `lint.txt`, `typecheck.txt` | ✅ Pass |

## Look at first

- How offenders are worked out in `_foreign_imports`: the file's own package is always allowed (the `own` override exists only for `erp_models`), relative imports are ignored, and only top-level names that are first-party packages count. Files: `tests/conventions/convention_scanner.py` (`_first_party_packages`, `_foreign_imports`, the three public rules).
- Two places where the rules are stricter than the wording of the ticket. A shared library may not import a plugin or the SDK, as well as a service. A plugin may not import `erp_sdk`. Both match `docs/technical/architecture/repository-layout.md` ("plugins, built on backend/models") and AGENT.md. If plugins come to need the SDK later, this rule must change. Files: `tests/conventions/convention_scanner.py`, `tests/conventions/helpers.py`.
- The ESLint and tsconfig exports, and the fixtures kept out of the package's own lint and typecheck: `frontend/packages/config/package.json`, `eslint.base.js`, `eslint.config.js`, `tsconfig.base.json`, `tsconfig.json`.
- The ticket touches no identity, permissions or company data isolation: it is test and configuration code only.

## Assumptions accepted

- The ticket links to the sprint anchor `#s01` because the row has no anchor of its own: accepted, S01 lists T0.02.
- The criteria come from the roadmap row because no use case or business rule applies: accepted, D438 defers the convention tests to this ticket.

## Follow-ups

- Move the `write()` helper and the clean service tree, now copied into four test files of `tests/conventions/scanner/`, into one shared helpers module. Add the missing module docstring to `test_shared_models_imports.py`.
- `eslint.base.js`: remove the first entry, which holds only a file pattern, and line up `globals.es2021` with `ecmaVersion` 2022.
- Wire `frontend/backoffice` and `frontend/mobile` to `@simpleerp/config` when they get their first sources.
- `pnpm-lock.yaml` is shared with the open ticket that adds `frontend/packages/tokens`, and the root lockfile is in no area lock. Whichever ticket finishes second regenerates the lockfile. Consider making the root lockfiles an area in the harness.
