# T0.02: Conventions for the shared libraries and the front ends

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- The convention tests now fail when `erp_models` imports another first-party package, when a shared library imports a service, a plugin or the SDK, or when a plugin or the SDK imports anything but `erp_models` and itself.
- The packages are found from the folders on disk, so a new library, plugin or front-end package needs no change to the tests.
- A new package `@simpleerp/config` gives every front end one shared ESLint flat config and one strict TypeScript base.
- Vitest tests run deliberately broken fixture front ends, which shows the shared settings apply when a front end extends them.

## ⚙️ How it works

1. **Constants name the source folders:** the globs of the shared models, the libraries, the plugins and the SDK are in [`tests/conventions/helpers.py:20-27`](../../../tests/conventions/helpers.py#L20-L27).
2. **The first-party packages are found on disk:** [`tests/conventions/convention_scanner.py:89-91`](../../../tests/conventions/convention_scanner.py#L89-L91) lists the package names under every source folder, never from a list.
3. **One helper reports the offenders:** [`tests/conventions/convention_scanner.py:93-111`](../../../tests/conventions/convention_scanner.py#L93-L111) walks the files of the given source folders and reports each top-level import that is a first-party package, not allowed, and not the file's own package. Relative, standard library and third-party imports are ignored.
4. **Three public rules call it:** `shared_models_imports` allows only `erp_models` ([`convention_scanner.py:336-339`](../../../tests/conventions/convention_scanner.py#L336-L339)); `shared_library_imports` allows `erp_models` and every library found under `backend/shared` ([`convention_scanner.py:341-345`](../../../tests/conventions/convention_scanner.py#L341-L345)); `plugin_and_sdk_imports` allows `erp_models` only ([`convention_scanner.py:347-350`](../../../tests/conventions/convention_scanner.py#L347-L350)).
5. **The real repository is checked:** three tests run the rules in [`tests/conventions/test_layers.py:21-29`](../../../tests/conventions/test_layers.py#L21-L29).
6. **Fixtures prove each rule fails once:** the scanner tests build a small tree in `tmp_path` with one broken import and assert one offender, for example [`test_shared_models_imports.py:48`](../../../tests/conventions/scanner/test_shared_models_imports.py#L48), [`test_shared_library_imports.py:51`](../../../tests/conventions/scanner/test_shared_library_imports.py#L51) and [`test_plugin_and_sdk_imports.py:53`](../../../tests/conventions/scanner/test_plugin_and_sdk_imports.py#L53). [`test_new_packages.py:59`](../../../tests/conventions/scanner/test_new_packages.py#L59) adds an empty library, plugin and front-end package and expects every rule to pass.
7. **The shared ESLint config:** [`frontend/packages/config/eslint.base.js:7-31`](../../../frontend/packages/config/eslint.base.js#L7-L31) combines `@eslint/js`, `typescript-eslint` and Vue 3 recommended rules, with the Vue parser for `.vue` files.
8. **The shared TypeScript base:** [`frontend/packages/config/tsconfig.base.json:3-12`](../../../frontend/packages/config/tsconfig.base.json#L3-L12) sets `strict: true` and the ES2022, bundler and DOM options.
9. **The package exports them:** `./eslint` and `./tsconfig` in [`frontend/packages/config/package.json:6-9`](../../../frontend/packages/config/package.json#L6-L9).
10. **Fixtures show the settings apply:** [`eslint-settings.test.ts:21-27`](../../../frontend/packages/config/tests/eslint-settings.test.ts#L21-L27) lints a fixture front end that extends the base and expects `no-explicit-any` and `vue/no-use-v-if-with-v-for`; [`strict-typescript.test.ts:21-33`](../../../frontend/packages/config/tests/strict-typescript.test.ts#L21-L33) compiles a fixture whose [`tsconfig.json`](../../../frontend/packages/config/tests/fixtures/strict-front-end/tsconfig.json) extends the base and expects the strict errors.
11. **The package's own checks leave the fixtures out:** [`eslint.config.js:5`](../../../frontend/packages/config/eslint.config.js#L5) ignores them for lint and [`tsconfig.json:7`](../../../frontend/packages/config/tsconfig.json#L7) excludes them from the typecheck.

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md) | Modified | [8-10](../../../docs/technical/architecture/frontend.md#L8) | +3 | −1 |
| [`docs/technical/architecture/repository-layout.md`](../../../docs/technical/architecture/repository-layout.md) | Modified | [28-33](../../../docs/technical/architecture/repository-layout.md#L28) | +6 | −0 |
| [`frontend/packages/config/README.md`](../../../frontend/packages/config/README.md) | Added | [1-71](../../../frontend/packages/config/README.md#L1) | +71 | −0 |
| [`frontend/packages/config/eslint.base.js`](../../../frontend/packages/config/eslint.base.js) | Added | [1-31](../../../frontend/packages/config/eslint.base.js#L1) | +31 | −0 |
| [`frontend/packages/config/eslint.config.js`](../../../frontend/packages/config/eslint.config.js) | Added | [1-11](../../../frontend/packages/config/eslint.config.js#L1) | +11 | −0 |
| [`frontend/packages/config/package.json`](../../../frontend/packages/config/package.json) | Added | [1-36](../../../frontend/packages/config/package.json#L1) | +36 | −0 |
| [`frontend/packages/config/tests/eslint-settings.test.ts`](../../../frontend/packages/config/tests/eslint-settings.test.ts) | Added | [1-28](../../../frontend/packages/config/tests/eslint-settings.test.ts#L1) | +28 | −0 |
| [`frontend/packages/config/tests/fixtures/eslint-front-end/eslint.config.js`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/eslint.config.js) | Added | [1-3](../../../frontend/packages/config/tests/fixtures/eslint-front-end/eslint.config.js#L1) | +3 | −0 |
| [`frontend/packages/config/tests/fixtures/eslint-front-end/src/Broken.vue`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/Broken.vue) | Added | [1-9](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/Broken.vue#L1) | +9 | −0 |
| [`frontend/packages/config/tests/fixtures/eslint-front-end/src/Clean.vue`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/Clean.vue) | Added | [1-7](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/Clean.vue#L1) | +7 | −0 |
| [`frontend/packages/config/tests/fixtures/eslint-front-end/src/broken.ts`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/broken.ts) | Added | [1](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/broken.ts#L1) | +1 | −0 |
| [`frontend/packages/config/tests/fixtures/eslint-front-end/src/clean.ts`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/clean.ts) | Added | [1](../../../frontend/packages/config/tests/fixtures/eslint-front-end/src/clean.ts#L1) | +1 | −0 |
| [`frontend/packages/config/tests/fixtures/strict-front-end/src/broken.ts`](../../../frontend/packages/config/tests/fixtures/strict-front-end/src/broken.ts) | Added | [1-5](../../../frontend/packages/config/tests/fixtures/strict-front-end/src/broken.ts#L1) | +5 | −0 |
| [`frontend/packages/config/tests/fixtures/strict-front-end/src/clean.ts`](../../../frontend/packages/config/tests/fixtures/strict-front-end/src/clean.ts) | Added | [1-5](../../../frontend/packages/config/tests/fixtures/strict-front-end/src/clean.ts#L1) | +5 | −0 |
| [`frontend/packages/config/tests/fixtures/strict-front-end/tsconfig.json`](../../../frontend/packages/config/tests/fixtures/strict-front-end/tsconfig.json) | Added | [1-5](../../../frontend/packages/config/tests/fixtures/strict-front-end/tsconfig.json#L1) | +5 | −0 |
| [`frontend/packages/config/tests/strict-typescript.test.ts`](../../../frontend/packages/config/tests/strict-typescript.test.ts) | Added | [1-34](../../../frontend/packages/config/tests/strict-typescript.test.ts#L1) | +34 | −0 |
| [`frontend/packages/config/tsconfig.base.json`](../../../frontend/packages/config/tsconfig.base.json) | Added | [1-14](../../../frontend/packages/config/tsconfig.base.json#L1) | +14 | −0 |
| [`frontend/packages/config/tsconfig.json`](../../../frontend/packages/config/tsconfig.json) | Added | [1-9](../../../frontend/packages/config/tsconfig.json#L1) | +9 | −0 |
| [`frontend/packages/config/vitest.config.ts`](../../../frontend/packages/config/vitest.config.ts) | Added | [1-8](../../../frontend/packages/config/vitest.config.ts#L1) | +8 | −0 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Modified | [14-1601](../../../pnpm-lock.yaml#L14) | +1588 | −0 |
| [`tests/conventions/convention_scanner.py`](../../../tests/conventions/convention_scanner.py) | Modified | [16](../../../tests/conventions/convention_scanner.py#L16), [19-20](../../../tests/conventions/convention_scanner.py#L19), [89-112](../../../tests/conventions/convention_scanner.py#L89), [335-350](../../../tests/conventions/convention_scanner.py#L335) | +43 | −0 |
| [`tests/conventions/helpers.py`](../../../tests/conventions/helpers.py) | Modified | [20-25](../../../tests/conventions/helpers.py#L20) | +6 | −0 |
| [`tests/conventions/scanner/test_new_packages.py`](../../../tests/conventions/scanner/test_new_packages.py) | Added | [1-92](../../../tests/conventions/scanner/test_new_packages.py#L1) | +92 | −0 |
| [`tests/conventions/scanner/test_plugin_and_sdk_imports.py`](../../../tests/conventions/scanner/test_plugin_and_sdk_imports.py) | Added | [1-61](../../../tests/conventions/scanner/test_plugin_and_sdk_imports.py#L1) | +61 | −0 |
| [`tests/conventions/scanner/test_shared_library_imports.py`](../../../tests/conventions/scanner/test_shared_library_imports.py) | Added | [1-66](../../../tests/conventions/scanner/test_shared_library_imports.py#L1) | +66 | −0 |
| [`tests/conventions/scanner/test_shared_models_imports.py`](../../../tests/conventions/scanner/test_shared_models_imports.py) | Added | [1-64](../../../tests/conventions/scanner/test_shared_models_imports.py#L1) | +64 | −0 |
| [`tests/conventions/test_layers.py`](../../../tests/conventions/test_layers.py) | Modified | [21-29](../../../tests/conventions/test_layers.py#L21) | +9 | −0 |
| **27 files** | | | **+2216** | **−1** |
<!-- /changes -->

- [`tests/conventions/convention_scanner.py`](../../../tests/conventions/convention_scanner.py), lines [`89-111`](../../../tests/conventions/convention_scanner.py#L89-L111) and [`336-350`](../../../tests/conventions/convention_scanner.py#L336-L350): the package finder, the shared offender helper and the three rules.
- [`tests/conventions/helpers.py`](../../../tests/conventions/helpers.py), lines [`20-27`](../../../tests/conventions/helpers.py#L20-L27): the source globs and the `erp_models` name.
- [`tests/conventions/test_layers.py`](../../../tests/conventions/test_layers.py), lines [`21-29`](../../../tests/conventions/test_layers.py#L21-L29): the three repository-wide assertions.
- [`tests/conventions/scanner/test_shared_models_imports.py`](../../../tests/conventions/scanner/test_shared_models_imports.py), [`test_shared_library_imports.py`](../../../tests/conventions/scanner/test_shared_library_imports.py), [`test_plugin_and_sdk_imports.py`](../../../tests/conventions/scanner/test_plugin_and_sdk_imports.py), [`test_new_packages.py`](../../../tests/conventions/scanner/test_new_packages.py): fixture tests for each rule and for new packages.
- [`frontend/packages/config`](../../../frontend/packages/config/): the new package: [`eslint.base.js`](../../../frontend/packages/config/eslint.base.js), [`tsconfig.base.json`](../../../frontend/packages/config/tsconfig.base.json), [`package.json`](../../../frontend/packages/config/package.json), its own [`eslint.config.js`](../../../frontend/packages/config/eslint.config.js), [`tsconfig.json`](../../../frontend/packages/config/tsconfig.json) and [`vitest.config.ts`](../../../frontend/packages/config/vitest.config.ts), the [README](../../../frontend/packages/config/README.md), the two Vitest files and the fixture front ends under [`tests/fixtures/`](../../../frontend/packages/config/tests/fixtures/eslint-front-end/eslint.config.js).
- [`pnpm-lock.yaml`](../../../pnpm-lock.yaml): the lockfile gains the package and its dependencies.
- [`docs/technical/architecture/repository-layout.md`](../../../docs/technical/architecture/repository-layout.md), lines [`28-33`](../../../docs/technical/architecture/repository-layout.md#L28-L33), and [`docs/technical/architecture/frontend.md`](../../../docs/technical/architecture/frontend.md), lines [`8-10`](../../../docs/technical/architecture/frontend.md#L8-L10): describe the rules and the package.

## 🧪 How to test it

```bash
uv run pytest tests/conventions -n 2
uv run ruff check tests/conventions
pnpm install
pnpm --filter ./frontend/packages/config run lint
pnpm --filter ./frontend/packages/config run typecheck
pnpm --filter ./frontend/packages/config run test
```

The first command runs the three rules on the real repository and on the broken fixtures. The last runs the ESLint and TypeScript fixtures.

## 🔗 Evidence

- [Python tests](tests-evidences/pytest.txt): 1107 passed.
- [Ruff check](tests-evidences/ruff-check.txt) and [format](tests-evidences/ruff-format.txt): clean, 7 files formatted.
- [Mypy](tests-evidences/mypy.txt): no issues.
- [pnpm install](tests-evidences/pnpm-install.txt), [lint](tests-evidences/lint.txt), [typecheck](tests-evidences/typecheck.txt) and [Vitest](tests-evidences/test.txt): all done, 7 Vitest tests passed.
- [Plan view](tests-evidences/plan-view.txt) and [ticket references](tests-evidences/ticket-refs.txt): no problem printed.

## 📝 Assumptions accepted

- The roadmap row has no anchor of its own, so the ticket links to the sprint anchor `#s01`: accepted, the S01 section of the P0 phase page lists the ticket.
- The acceptance criteria come from the roadmap row's "Done when" and "Delivers" text, because no use case or business rule applies: accepted, D438 says the convention tests follow in a ticket of their own.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`tests/conventions/scanner/test_new_packages.py`](../../../tests/conventions/scanner/test_new_packages.py), [`test_plugin_and_sdk_imports.py`](../../../tests/conventions/scanner/test_plugin_and_sdk_imports.py), [`test_shared_library_imports.py`](../../../tests/conventions/scanner/test_shared_library_imports.py), [`test_shared_models_imports.py`](../../../tests/conventions/scanner/test_shared_models_imports.py) | The same `write()` helper and almost the same clean service tree are copied into four test files. Move them to one shared helpers module, for example `tests/conventions/scanner/helpers.py`, and import it by its full path. Add the missing module docstring to `test_shared_models_imports.py`. Owner: the test-writer task of the convention tests. |
| [`frontend/packages/config/eslint.base.js`](../../../frontend/packages/config/eslint.base.js) | The first entry, `{ files: [...] }`, holds only a file pattern and repeats the pattern of the next entry. `globals.es2021` also sits beside `ecmaVersion` 2022. Remove the redundant entry and line up the globals with the ECMAScript version. |
| [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json), [`frontend/mobile/package.json`](../../../frontend/mobile/package.json) | They do not yet depend on `@simpleerp/config` or extend it. When they get their first sources, add the workspace devDependency, an `eslint.config.js` and a `tsconfig.json` that extend the shared settings, as the package README describes. |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Another open ticket adds `frontend/packages/tokens` to the same pnpm workspace, and the root lockfile belongs to no area lock. Whichever ticket finishes second must regenerate the lockfile. Consider making the root lockfiles an area in the harness. |
