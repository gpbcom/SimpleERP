# T0.01: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

## What changed

- `backend/models` (package `erp_models`, built with `uv_build`) and `sdk` (a virtual member with no build system) are now real members of the uv workspace, recorded in the `[manifest]` of the one `uv.lock`. The other declared globs (`backend/shared/*`, `backend/services/*`, `plugins/*`) stay empty.
- New pnpm workspace: a private root `package.json` with `engines.node` `^22` and `packageManager` `pnpm@10.34.9`, read by `pnpm/action-setup` in CI. `pnpm-workspace.yaml` lists the back office, mobile, `portals/*` and `packages/*`. `pnpm-lock.yaml` is a single YAML document with three importers.
- Every D438 folder named by the ticket has a README that says what it holds and links D438 and the layout page.
- The README quick start now installs from both locks (`uv sync --locked`, `pnpm install --frozen-lockfile`). The configuration page gains a Workspaces table and per-service `conf/` paths, and the layout page's Today section lists what exists on disk.
- Static pytest suites in `tests/layout/` and `tests/ci/detect_changes/test_repository_layout.py` pin all of this. The detector test runs against the real repository root, not a fixture.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. A clean clone passes `uv sync --locked` with the members pinned in one `uv.lock` | `tests/layout/test_uv_workspace.py` (`test_a_member_is_pinned_in_the_one_lock`), tests-evidences/pytest.txt, tests-evidences/mypy.txt. No `uv sync --locked` run is recorded (follow-up) | ✅ Pass (the lock looks consistent, and CI runs `uv sync --locked` in every Python job) |
| 2. A clean clone passes `pnpm install --frozen-lockfile` with `pnpm-lock.yaml` pinned | tests-evidences/pnpm-install.txt, `tests/layout/test_pnpm_workspace.py` | ✅ Pass |
| 3. CI's change detection lists the new folders | `tests/ci/detect_changes/test_repository_layout.py` (packages `backend/models` and `sdk`, TypeScript projects `frontend/backoffice` and `frontend/mobile`, README-only folders select nothing) | ✅ Pass |
| 4. Every D438 folder has a README saying what it holds | `tests/layout/test_folder_readmes.py` (17 folders: has a README, starts with a title, has prose, links D438) | ✅ Pass |
| 5. The README's quick start works | `tests/layout/test_readme_quick_start.py`, tests-evidences/pnpm-install.txt, tests-evidences/pytest.txt (928 passed) | ✅ Pass |

## Look at first

- **CI impact of the new members.** This pull request changes `uv.lock` and `pnpm-lock.yaml`, so CI selects every package. Check that `check_python_project.sh` skips mypy for `sdk` (no `src/`) and pytest for both members (no tests). Check that `typescript.yml` installs with `--frozen-lockfile` and runs `--if-present` scripts on the two script-less apps. Files: `/home/guillaume/Documents/Projects/Others/simple-erp/.github/workflows/python.yml`, `/home/guillaume/Documents/Projects/Others/simple-erp/.github/workflows/typescript.yml`, `/home/guillaume/Documents/Projects/Others/simple-erp/.github/scripts/check_python_project.sh`.
- **The pnpm pin.** `pnpm@10.34.9` is not the local pnpm 12. The 12.x lock carries a second YAML document that the layout test cannot parse. Developers on pnpm 12 will be switched to 10.34.9 by `packageManager`. File: `/home/guillaume/Documents/Projects/Others/simple-erp/package.json`.
- **The lock and the build backend.** Read the `[manifest]` and the two new `[[package]]` entries of `/home/guillaume/Documents/Projects/Others/simple-erp/uv.lock`, and the build-system range of `/home/guillaume/Documents/Projects/Others/simple-erp/backend/models/pyproject.toml`.
- **The detector test's departure from the brief.** A change to `frontend/packages/README.md` selects every front end, as AGENT.md CI/CD step 1 says. File: `/home/guillaume/Documents/Projects/Others/simple-erp/tests/ci/detect_changes/test_repository_layout.py`.
- **Identity, permissions and company data isolation:** not touched. The ticket adds no runtime code, only an empty `__init__.py`, manifests and documents.

## Assumptions accepted

- K01 (how a README is parsed, fragments ignored on the D438 link): accepted. It does not weaken criterion 4.
- K02 and K06 (the root members were already declared, and only the comment changed): accepted. The root `pyproject.toml` confirms it.
- K03 and K10 (`^22` for Node 22 only): accepted. `^22` means the same as `>=22 <23`.
- K04 and FIX (a change to `frontend/packages/` selects every front end, and the README files stayed unchanged): accepted, as AGENT.md CI/CD step 1 says.
- K05 (README section and table matching): accepted.
- K08 and K09 (plain-text citations where the layout page has no link, and links to the pack specification pages): accepted. Every link resolves.
- K10 (pnpm@10.34.9 instead of the local 12.21.0, and the install run with CI=true): accepted. No specification pins a pnpm version, and CI reads the field.
- K12 (no pnpm number in the README): accepted. The `packageManager` pin is the one source of truth.
- K13 and K14 (Planned wording kept, and the pages describe what is on disk): accepted.
- TICKET.md assumptions (no use case or budget, only parent folders for the shared libraries and front-end packages): accepted.

## Follow-ups

- Record a `uv sync --locked` run in `tests-evidences/` for criterion 1, and consider adding it to `checks.py` (verifier, K06).
- Pin the `uv_build` backend exactly, since `uv.lock` does not lock build requirements (D415, K06).
- README Project structure: 'every folder of the tree exists' overstates it, because `frontend/portals/` and `compose.e2e.yaml` are still missing (K12).
- Configuration page: mention that the tracked root `conf/logger.yaml` is still the one in use until services exist (K13).
- `test_the_engines_allow_node_22_only` rejects valid ranges such as `^22.11` (K03).
- The first line of the root `pyproject.toml` comment is about 122 characters long (K06).
- Three of the five new test files use import group comments, which AGENT.md leaves out of tests (K02, K04, K05).
