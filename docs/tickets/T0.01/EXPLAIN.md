# T0.01: Mono-repo folders and workspaces

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- The repository now has the folders of the D438 layout, each with a README that says what it holds and links D438.
- The uv workspace has two real members, the shared models (`erp_models`) and the SDK, pinned in the one lock.
- A pnpm workspace exists (root manifest, workspace file, lock) with the back office and the mobile app as members.
- The README quick start installs from both locks, and the configuration and layout pages describe what is on disk.
- Static tests pin all of this, and CI's change detection lists the new packages and front ends.

## ⚙️ How it works

1. **uv workspace root:** the root file declares the members `backend/models`, `backend/shared/*`, `backend/services/*`, `plugins/*` and `sdk`; only its comment changed, in [`pyproject.toml:11-16`](../../../pyproject.toml#L11-L16).
2. **Shared models member:** `erp-models` is built with `uv_build` and exposes the module `erp_models`, in [`backend/models/pyproject.toml:10-15`](../../../backend/models/pyproject.toml#L10-L15). The package itself is an empty [`__init__.py`](../../../backend/models/src/erp_models/__init__.py).
3. **SDK member:** `erp-sdk` has no `[build-system]` and no source, so it is a virtual member, in [`sdk/pyproject.toml:1-8`](../../../sdk/pyproject.toml#L1-L8).
4. **One lock:** the two members are recorded in the `[manifest]` and as `[[package]]` entries of [`uv.lock:5-11`](../../../uv.lock#L5-L11) and [`uv.lock:74-83`](../../../uv.lock#L74-L83), so `uv sync --locked` resolves them from one file.
5. **pnpm root:** the private root manifest sets `engines.node` to `^22` and `packageManager` to `pnpm@10.34.9` ([`package.json:5-8`](../../../package.json#L5-L8)); `pnpm/action-setup` in CI reads that field.
6. **pnpm members:** [`pnpm-workspace.yaml:1-5`](../../../pnpm-workspace.yaml#L1-L5) lists the two apps by path and `portals/*` and `packages/*` by glob. The apps are private named packages ([`frontend/backoffice/package.json:1-5`](../../../frontend/backoffice/package.json#L1-L5), [`frontend/mobile/package.json:1-5`](../../../frontend/mobile/package.json#L1-L5)), and [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) pins three importers in one YAML document.
7. **Folder READMEs:** each folder of the layout has a README, for example [`backend/README.md`](../../../backend/README.md), [`frontend/README.md`](../../../frontend/README.md), [`infra/README.md`](../../../infra/README.md) and [`packs/README.md`](../../../packs/README.md).
8. **Quick start:** the README installs with `uv sync --locked` and `pnpm install --frozen-lockfile` ([`README.md:220-221`](../../../README.md#L220-L221)) and points to the `packageManager` pin for the pnpm version ([`README.md:194`](../../../README.md#L194)).
9. **Tests, in the order the checks run them:**
   - [`tests/layout/test_uv_workspace.py`](../../../tests/layout/test_uv_workspace.py) parses the TOML files and checks that each member is named, needs Python 3.13 and is listed in the lock ([lines 47-52](../../../tests/layout/test_uv_workspace.py#L47-L52)).
   - [`tests/layout/test_pnpm_workspace.py`](../../../tests/layout/test_pnpm_workspace.py) parses the JSON and YAML files: private root, exact pnpm version ([line 37](../../../tests/layout/test_pnpm_workspace.py#L37)), Node 22 only ([line 42](../../../tests/layout/test_pnpm_workspace.py#L42)), importers in the lock ([line 56](../../../tests/layout/test_pnpm_workspace.py#L56)).
   - [`tests/layout/test_folder_readmes.py`](../../../tests/layout/test_folder_readmes.py) checks the 17 folders ([lines 12-30](../../../tests/layout/test_folder_readmes.py#L12-L30)): a README, a title, a line of prose and a link that resolves to D438 ([lines 54-63](../../../tests/layout/test_folder_readmes.py#L54-L63)).
   - [`tests/layout/test_readme_quick_start.py`](../../../tests/layout/test_readme_quick_start.py) reads the README's setup section and its first `bash` block.
   - [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py) runs the real detector on the real repository root: packages `backend/models` and `sdk`, front ends `frontend/backoffice` and `frontend/mobile`, README-only folders select nothing ([lines 55-70](../../../tests/ci/detect_changes/test_repository_layout.py#L55-L70)).

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`README.md`](../../../README.md) | Modified | [194](../../../README.md#L194), [220-221](../../../README.md#L220), [303-304](../../../README.md#L303) | +5 | −4 |
| [`backend/README.md`](../../../backend/README.md) | Added | [1-7](../../../backend/README.md#L1) | +7 | −0 |
| [`backend/models/README.md`](../../../backend/models/README.md) | Added | [1-8](../../../backend/models/README.md#L1) | +8 | −0 |
| [`backend/models/pyproject.toml`](../../../backend/models/pyproject.toml) | Added | [1-15](../../../backend/models/pyproject.toml#L1) | +15 | −0 |
| [`backend/models/src/erp_models/__init__.py`](../../../backend/models/src/erp_models/__init__.py) | Added | ➖ | +0 | −0 |
| [`backend/services/README.md`](../../../backend/services/README.md) | Added | [1-8](../../../backend/services/README.md#L1) | +8 | −0 |
| [`backend/shared/README.md`](../../../backend/shared/README.md) | Added | [1-9](../../../backend/shared/README.md#L1) | +9 | −0 |
| [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md) | Modified | [7-11](../../../docs/technical/architecture/configuration.md#L7), [16-28](../../../docs/technical/architecture/configuration.md#L16) | +18 | −3 |
| [`docs/technical/architecture/repository-layout.md`](../../../docs/technical/architecture/repository-layout.md) | Modified | [8-26](../../../docs/technical/architecture/repository-layout.md#L8) | +19 | −1 |
| [`frontend/README.md`](../../../frontend/README.md) | Added | [1-15](../../../frontend/README.md#L1) | +15 | −0 |
| [`frontend/backoffice/README.md`](../../../frontend/backoffice/README.md) | Added | [1-7](../../../frontend/backoffice/README.md#L1) | +7 | −0 |
| [`frontend/backoffice/package.json`](../../../frontend/backoffice/package.json) | Added | [1-5](../../../frontend/backoffice/package.json#L1) | +5 | −0 |
| [`frontend/mobile/README.md`](../../../frontend/mobile/README.md) | Added | [1-7](../../../frontend/mobile/README.md#L1) | +7 | −0 |
| [`frontend/mobile/package.json`](../../../frontend/mobile/package.json) | Added | [1-5](../../../frontend/mobile/package.json#L1) | +5 | −0 |
| [`frontend/packages/README.md`](../../../frontend/packages/README.md) | Added | [1-9](../../../frontend/packages/README.md#L1) | +9 | −0 |
| [`infra/README.md`](../../../infra/README.md) | Added | [1-7](../../../infra/README.md#L1) | +7 | −0 |
| [`infra/compose/README.md`](../../../infra/compose/README.md) | Added | [1-7](../../../infra/compose/README.md#L1) | +7 | −0 |
| [`infra/helm/README.md`](../../../infra/helm/README.md) | Added | [1-7](../../../infra/helm/README.md#L1) | +7 | −0 |
| [`infra/terraform/README.md`](../../../infra/terraform/README.md) | Added | [1-7](../../../infra/terraform/README.md#L1) | +7 | −0 |
| [`package.json`](../../../package.json) | Added | [1-9](../../../package.json#L1) | +9 | −0 |
| [`packs/README.md`](../../../packs/README.md) | Added | [1-9](../../../packs/README.md#L1) | +9 | −0 |
| [`packs/countries/README.md`](../../../packs/countries/README.md) | Added | [1-7](../../../packs/countries/README.md#L1) | +7 | −0 |
| [`packs/sectors/README.md`](../../../packs/sectors/README.md) | Added | [1-7](../../../packs/sectors/README.md#L1) | +7 | −0 |
| [`plugins/README.md`](../../../plugins/README.md) | Added | [1-7](../../../plugins/README.md#L1) | +7 | −0 |
| [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) | Added | [1-13](../../../pnpm-lock.yaml#L1) | +13 | −0 |
| [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml) | Added | [1-5](../../../pnpm-workspace.yaml#L1) | +5 | −0 |
| [`pyproject.toml`](../../../pyproject.toml) | Modified | [11-12](../../../pyproject.toml#L11) | +2 | −2 |
| [`sdk/README.md`](../../../sdk/README.md) | Added | [1-6](../../../sdk/README.md#L1) | +6 | −0 |
| [`sdk/pyproject.toml`](../../../sdk/pyproject.toml) | Added | [1-8](../../../sdk/pyproject.toml#L1) | +8 | −0 |
| [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py) | Added | [1-70](../../../tests/ci/detect_changes/test_repository_layout.py#L1) | +70 | −0 |
| [`tests/layout/test_folder_readmes.py`](../../../tests/layout/test_folder_readmes.py) | Added | [1-63](../../../tests/layout/test_folder_readmes.py#L1) | +63 | −0 |
| [`tests/layout/test_pnpm_workspace.py`](../../../tests/layout/test_pnpm_workspace.py) | Added | [1-70](../../../tests/layout/test_pnpm_workspace.py#L1) | +70 | −0 |
| [`tests/layout/test_readme_quick_start.py`](../../../tests/layout/test_readme_quick_start.py) | Added | [1-44](../../../tests/layout/test_readme_quick_start.py#L1) | +44 | −0 |
| [`tests/layout/test_uv_workspace.py`](../../../tests/layout/test_uv_workspace.py) | Added | [1-55](../../../tests/layout/test_uv_workspace.py#L1) | +55 | −0 |
| [`uv.lock`](../../../uv.lock) | Modified | [5-11](../../../uv.lock#L5), [74-83](../../../uv.lock#L74) | +17 | −0 |
| **35 files** | | | **+557** | **−10** |
<!-- /changes -->

- [`pyproject.toml`](../../../pyproject.toml), lines [11-12](../../../pyproject.toml#L11-L12): the comment now says which members exist. No setting changed.
- [`backend/models/`](../../../backend/models/pyproject.toml) (pyproject, [README](../../../backend/models/README.md), empty package) and [`sdk/`](../../../sdk/pyproject.toml) ([README](../../../sdk/README.md)): the two uv members, so the lock has something to pin.
- [`uv.lock`](../../../uv.lock), lines [5-11](../../../uv.lock#L5-L11) and [74-83](../../../uv.lock#L74-L83): the manifest and the two package entries.
- [`package.json`](../../../package.json), [`pnpm-workspace.yaml`](../../../pnpm-workspace.yaml), [`pnpm-lock.yaml`](../../../pnpm-lock.yaml) and the two app manifests: the pnpm workspace and its lock.
- The folder READMEs ([`backend/shared`](../../../backend/shared/README.md), [`backend/services`](../../../backend/services/README.md), [`frontend/packages`](../../../frontend/packages/README.md), [`plugins`](../../../plugins/README.md), [`infra/compose`](../../../infra/compose/README.md), [`infra/helm`](../../../infra/helm/README.md), [`infra/terraform`](../../../infra/terraform/README.md), [`packs/countries`](../../../packs/countries/README.md), [`packs/sectors`](../../../packs/sectors/README.md), the app READMEs [`backoffice`](../../../frontend/backoffice/README.md) and [`mobile`](../../../frontend/mobile/README.md)): acceptance criterion 4.
- [`README.md`](../../../README.md), lines [194](../../../README.md#L194), [220-221](../../../README.md#L220-L221) and [303-304](../../../README.md#L303-L304): Node 22 prerequisite, install commands, the structure paragraph.
- [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md), lines [7-11](../../../docs/technical/architecture/configuration.md#L7-L11) and [16-28](../../../docs/technical/architecture/configuration.md#L16-L28): per-service `conf/` paths and a Workspaces table of the root files.
- [`docs/technical/architecture/repository-layout.md`](../../../docs/technical/architecture/repository-layout.md), lines [8-26](../../../docs/technical/architecture/repository-layout.md#L8-L26): the Today section lists what exists, as links.
- The five test files named in step 9: the static checks of every criterion.

## 🧪 How to test it

```bash
uv run pytest tests/layout -n 2
uv run pytest tests/ci/detect_changes/test_repository_layout.py -n 2
uv run mypy backend/models/src
uv sync --locked
pnpm install --frozen-lockfile
python3 .claude/scripts/tickets/ticket_tree.py docs --ticket T0.01
```

The first two run the static layout tests, the next two install from the locks (the `uv sync --locked` run has no recorded evidence, see the follow-ups), and the last checks these documents.

## 🔗 Evidence

- [Tests](tests-evidences/pytest.txt): the repository suite passes (928 passed).
- [Type check](tests-evidences/mypy.txt): no issue in the one source file of `erp_models`.
- [pnpm install](tests-evidences/pnpm-install.txt): `--frozen-lockfile` passes on 3 workspace projects with pnpm 10.34.9.
- [Ruff check](tests-evidences/ruff-check.txt) and [format](tests-evidences/ruff-format.txt): Python style.
- [Lint](tests-evidences/lint.txt), [type check](tests-evidences/typecheck.txt) and [test](tests-evidences/test.txt) of the front ends: no script to run in the two apps.
- [Ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt): the ticket and plan checks.

## 📝 Assumptions accepted

- K01: blank lines are ignored when finding a README's title and prose, prose is any non-blank line after the heading that does not start with `#`, and a fragment on the D438 link is ignored.
- K02: the root pyproject already listed the members and `requires-python`, so only some tests failed first.
- K03: `engines.node` must name only major 22, the strictest reading of D407's "Node 22". The tests/layout folder holds four files and no `__init__.py`.
- K04: "images holds neither" means that no image has those folders. A change under `frontend/packages/` selects every front end, as AGENT.md says.
- K05: the README section is found by its "Development setup" heading and its first bash block, and table rows by tool name.
- K06: the READMEs titled "Shared models" and "Plugin SDK" use only the layout page and the AGENT.md table. Only the comment of the root pyproject changed.
- K08 and K09: the infra READMEs cite D408, D421 and REQ-T09-08 as plain text, and the pack READMEs link the country-pack and sector pages. Every link resolves.
- K10: `packageManager` is `pnpm@10.34.9`, not the local 12.21.0, because pnpm 12 writes a two-document lock. `engines.node` is `^22`, the same as `>=22 <23`. The frozen-lockfile check ran with `CI=true` and pnpm 10.
- K12: the README names Node 22 and points to the `packageManager` pin, with no pnpm number.
- K13 and K14: the `app.yaml` and `catalogs/` rows keep their Planned wording, and the Today section describes only what is on disk.
- The README files did not change in the fix round, because README content cannot change what the detector selects.
- TICKET.md: the roadmap row names no use case or budget, so D438, D406, D407, D415 and the design pages settle the scope, and only the parent folders of `backend/shared` and `frontend/packages` are created.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`tests-evidences/`](tests-evidences/) | Criterion 1 has no evidence file: `checks.py` runs `pnpm install --frozen-lockfile` but not `uv sync --locked`. Record a `uv sync --locked` run and consider adding it to `checks.py` (verifier). |
| [`backend/models/pyproject.toml`](../../../backend/models/pyproject.toml) | `uv_build>=0.12.21,<0.13` is a range and the lock does not lock build requirements. Pin it exactly (`uv_build==0.12.21`) or record why a range is accepted. |
| [`README.md`](../../../README.md) | The structure paragraph says every folder of the tree exists, but `frontend/portals/` and `compose.e2e.yaml` do not yet. Reword it. |
| [`docs/technical/architecture/configuration.md`](../../../docs/technical/architecture/configuration.md) | Say that the tracked root [`conf/logger.yaml`](../../../conf/logger.yaml) moves into each service when services arrive (T0.06), or mark the per-service logger row as planned. |
| [`tests/layout/test_pnpm_workspace.py`](../../../tests/layout/test_pnpm_workspace.py) | `test_the_engines_allow_node_22_only` reads every digit run, so a valid `^22.11` would fail. Compare only the major numbers. |
| [`pyproject.toml`](../../../pyproject.toml) | The first line of the comment of `[tool.uv]` is about 122 characters. Wrap it at 120. |
| [`tests/ci/detect_changes/test_repository_layout.py`](../../../tests/ci/detect_changes/test_repository_layout.py), [`tests/layout/test_uv_workspace.py`](../../../tests/layout/test_uv_workspace.py), [`tests/layout/test_readme_quick_start.py`](../../../tests/layout/test_readme_quick_start.py) | Drop the import group comments, which AGENT.md leaves out of tests. |
