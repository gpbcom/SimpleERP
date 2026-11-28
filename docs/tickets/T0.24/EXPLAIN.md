# T0.24: Bruno collection scaffold

**Status:** ✅ Done · **Ticket:** [TICKET.md](TICKET.md) · **Choices and trade-offs:** [IMPLEMENTATION.md](IMPLEMENTATION.md) · **Review:** [REVIEW.md](REVIEW.md)

## 🔭 What it does

- A Bruno collection for `platform` is generated from its committed OpenAPI document, and CI fails when it goes stale.
- Two hand-written tests run on it: the health call, and a refused call that must answer problem+json with a code and no secret.
- The dev stage runs every collection under `bruno/` headless and keeps a JUnit and a JSON report for each.
- A scan keeps credentials out of `bruno/`, and change detection runs the Bruno checks when `bruno/` changes.

## ⚙️ How it works

1. **Generate:** [`main`](../../../.github/scripts/bruno_collection.py#L250) reads the service's `openapi.json`, then [`render`](../../../.github/scripts/bruno_collection.py#L155) builds `bruno.json`, `collection.bru` and one `.bru` request per operation, in memory. [`generate`](../../../.github/scripts/bruno_collection.py#L199) writes them and removes request files no longer generated. The result is [`bruno/platform/requests/default/get_health_v1_health_get.bru`](../../../bruno/platform/requests/default/get_health_v1_health_get.bru), [`bruno/platform/bruno.json`](../../../bruno/platform/bruno.json) and [`bruno/platform/collection.bru`](../../../bruno/platform/collection.bru).
2. **Freshness in CI:** the `services` job of `python.yml` runs `check` in the step at [`.github/workflows/python.yml:61-62`](../../../.github/workflows/python.yml#L61-L62). [`check`](../../../.github/scripts/bruno_collection.py#L214) compares bytes in memory and lists missing, changed and unexpected files. It leaves `tests/`, `environments/` and the collection's own ignore file alone, and a service with no collection passes. Bad arguments exit 2 through [`parse_args`](../../../.github/scripts/bruno_collection.py#L235).
3. **Change detection:** a path under `bruno/<name>/` sets `repository` and selects `backend/services/<name>` when that service exists, with no image, in [`.github/scripts/detect_changes.py:212-216`](../../../.github/scripts/detect_changes.py#L212-L216).
4. **Hand-written tests:** [`bruno/platform/tests/health.bru`](../../../bruno/platform/tests/health.bru) asserts 200 and `{status: "ok"}`. [`bruno/platform/tests/refused-call.bru`](../../../bruno/platform/tests/refused-call.bru) calls `GET /v1/anything` with no company header and asserts 400, problem+json, a title and code, and no secret word or `Traceback` ([lines 29-33](../../../bruno/platform/tests/refused-call.bru#L29-L33)).
5. **Environment:** [`bruno/platform/environments/stage.bru:2`](../../../bruno/platform/environments/stage.bru#L2) sets `baseUrl` to `http://localhost:8000`, and [`bruno/platform/.gitignore:1`](../../../bruno/platform/.gitignore#L1) ignores `.env`.
6. **Run on dev:** `stage.yml` sets up Node 22 ([`.github/workflows/stage.yml:123-126`](../../../.github/workflows/stage.yml#L123-L126)), then loops over `bruno/*/` and runs the pinned CLI with `--env stage`, a JSON and a JUnit report, and headers and bodies skipped ([`.github/workflows/stage.yml:127-137`](../../../.github/workflows/stage.yml#L127-L137)). Any failing collection fails the step.
7. **Credential scan:** [`scan_file`](../../../tests/ci/bruno_credentials/helpers.py#L110) walks each file by line and block, flags any literal in an auth block that is not a structural key ([`AUTH_STRUCTURAL_KEYS`](../../../tests/ci/bruno_credentials/helpers.py#L14)), and checks that each collection ignores `.env`. [`list_files`](../../../tests/ci/bruno_credentials/helpers.py#L66) uses git's file list inside the repository.

## 🧱 Files and lines changed

<!-- changes -->
| File | Change | Lines in the new version | Added | Removed |
| --- | --- | --- | --- | --- |
| [`.github/scripts/bruno_collection.py`](../../../.github/scripts/bruno_collection.py) | Added | [1-275](../../../.github/scripts/bruno_collection.py#L1) | +275 | −0 |
| [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py) | Modified | [28-31](../../../.github/scripts/detect_changes.py#L28), [50](../../../.github/scripts/detect_changes.py#L50), [212-216](../../../.github/scripts/detect_changes.py#L212) | +10 | −0 |
| [`.github/workflows/python.yml`](../../../.github/workflows/python.yml) | Modified | [7](../../../.github/workflows/python.yml#L7), [61-62](../../../.github/workflows/python.yml#L61) | +3 | −1 |
| [`.github/workflows/stage.yml`](../../../.github/workflows/stage.yml) | Modified | [123-126](../../../.github/workflows/stage.yml#L123) | +4 | −0 |
| [`bruno/platform/.gitignore`](../../../bruno/platform/.gitignore) | Added | [1](../../../bruno/platform/.gitignore#L1) | +1 | −0 |
| [`bruno/platform/bruno.json`](../../../bruno/platform/bruno.json) | Added | [1-9](../../../bruno/platform/bruno.json#L1) | +9 | −0 |
| [`bruno/platform/collection.bru`](../../../bruno/platform/collection.bru) | Added | [1-4](../../../bruno/platform/collection.bru#L1) | +4 | −0 |
| [`bruno/platform/environments/stage.bru`](../../../bruno/platform/environments/stage.bru) | Added | [1-3](../../../bruno/platform/environments/stage.bru#L1) | +3 | −0 |
| [`bruno/platform/requests/default/get_health_v1_health_get.bru`](../../../bruno/platform/requests/default/get_health_v1_health_get.bru) | Added | [1-11](../../../bruno/platform/requests/default/get_health_v1_health_get.bru#L1) | +11 | −0 |
| [`bruno/platform/tests/health.bru`](../../../bruno/platform/tests/health.bru) | Added | [1-21](../../../bruno/platform/tests/health.bru#L1) | +21 | −0 |
| [`bruno/platform/tests/refused-call.bru`](../../../bruno/platform/tests/refused-call.bru) | Added | [1-34](../../../bruno/platform/tests/refused-call.bru#L1) | +34 | −0 |
| [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md) | Modified | [50](../../../docs/technical/delivery/ci-cd-and-stages.md#L50), [60](../../../docs/technical/delivery/ci-cd-and-stages.md#L60), [70-71](../../../docs/technical/delivery/ci-cd-and-stages.md#L70), [130](../../../docs/technical/delivery/ci-cd-and-stages.md#L130) | +5 | −3 |
| [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md) | Modified | [14](../../../docs/technical/delivery/tests-and-traceability.md#L14), [51-68](../../../docs/technical/delivery/tests-and-traceability.md#L51), [157](../../../docs/technical/delivery/tests-and-traceability.md#L157) | +20 | −2 |
| [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) | Modified | [44-62](../../../docs/technical/interfaces/api.md#L44), [91](../../../docs/technical/interfaces/api.md#L91) | +20 | −1 |
| [`tests/ci/bruno_collection/helpers.py`](../../../tests/ci/bruno_collection/helpers.py) | Added | [1-128](../../../tests/ci/bruno_collection/helpers.py#L1) | +128 | −0 |
| [`tests/ci/bruno_collection/test_check.py`](../../../tests/ci/bruno_collection/test_check.py) | Added | [1-145](../../../tests/ci/bruno_collection/test_check.py#L1) | +145 | −0 |
| [`tests/ci/bruno_collection/test_generate.py`](../../../tests/ci/bruno_collection/test_generate.py) | Added | [1-160](../../../tests/ci/bruno_collection/test_generate.py#L1) | +160 | −0 |
| [`tests/ci/bruno_credentials/helpers.py`](../../../tests/ci/bruno_credentials/helpers.py) | Added | [1-162](../../../tests/ci/bruno_credentials/helpers.py#L1) | +162 | −0 |
| [`tests/ci/bruno_credentials/test_bruno_credentials.py`](../../../tests/ci/bruno_credentials/test_bruno_credentials.py) | Added | [1-90](../../../tests/ci/bruno_credentials/test_bruno_credentials.py#L1) | +90 | −0 |
| [`tests/ci/detect_changes/bruno/test_bruno_changes.py`](../../../tests/ci/detect_changes/bruno/test_bruno_changes.py) | Added | [1-47](../../../tests/ci/detect_changes/bruno/test_bruno_changes.py#L1) | +47 | −0 |
| [`tests/ci/workflows/checks/test_python_workflow.py`](../../../tests/ci/workflows/checks/test_python_workflow.py) | Modified | [12](../../../tests/ci/workflows/checks/test_python_workflow.py#L12), [20-25](../../../tests/ci/workflows/checks/test_python_workflow.py#L20), [84-101](../../../tests/ci/workflows/checks/test_python_workflow.py#L84) | +25 | −1 |
| [`tests/ci/workflows/test_stage_workflow.py`](../../../tests/ci/workflows/test_stage_workflow.py) | Modified | [4](../../../tests/ci/workflows/test_stage_workflow.py#L4), [52](../../../tests/ci/workflows/test_stage_workflow.py#L52), [67-105](../../../tests/ci/workflows/test_stage_workflow.py#L67) | +41 | −1 |
| **22 files** | | | **+1218** | **−9** |
<!-- /changes -->

- [`.github/scripts/bruno_collection.py`](../../../.github/scripts/bruno_collection.py): new, standard-library generator and checker (steps 1 and 2).
- [`.github/scripts/detect_changes.py`](../../../.github/scripts/detect_changes.py), lines [`28-31`](../../../.github/scripts/detect_changes.py#L28-L31), [`50`](../../../.github/scripts/detect_changes.py#L50), [`212-216`](../../../.github/scripts/detect_changes.py#L212-L216): the `BRUNO` constant, its docstring and the selection.
- [`.github/workflows/python.yml`](../../../.github/workflows/python.yml), lines [`61-62`](../../../.github/workflows/python.yml#L61-L62): the freshness step after the contract check.
- [`.github/workflows/stage.yml`](../../../.github/workflows/stage.yml), lines [`123-137`](../../../.github/workflows/stage.yml#L123-L137): the Node 22 setup and the Bruno step.
- [`bruno/platform/`](../../../bruno/platform/bruno.json): the generated files, the two tests, the `stage` environment and the ignore file.
- [`tests/ci/bruno_collection/`](../../../tests/ci/bruno_collection/helpers.py): tests of the generator and of `check` (the three files [`helpers.py`](../../../tests/ci/bruno_collection/helpers.py), [`test_generate.py`](../../../tests/ci/bruno_collection/test_generate.py) and [`test_check.py`](../../../tests/ci/bruno_collection/test_check.py)), run as a subprocess on a fake service.
- [`tests/ci/bruno_credentials/`](../../../tests/ci/bruno_credentials/helpers.py): the scan and its tests ([`test_bruno_credentials.py`](../../../tests/ci/bruno_credentials/test_bruno_credentials.py)).
- [`tests/ci/detect_changes/bruno/test_bruno_changes.py`](../../../tests/ci/detect_changes/bruno/test_bruno_changes.py): three parametrised behaviours of the selection.
- [`tests/ci/workflows/checks/test_python_workflow.py`](../../../tests/ci/workflows/checks/test_python_workflow.py), lines [`17-24`](../../../tests/ci/workflows/checks/test_python_workflow.py#L17-L24) and [`85-93`](../../../tests/ci/workflows/checks/test_python_workflow.py#L85-L93): the step exists, runs the script and follows the workspace install.
- [`tests/ci/workflows/test_stage_workflow.py`](../../../tests/ci/workflows/test_stage_workflow.py), lines [`73-108`](../../../tests/ci/workflows/test_stage_workflow.py#L73-L108): the Bruno flags, and Node 22 set up before the step.
- [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md), lines [`44-62`](../../../docs/technical/interfaces/api.md#L44-L62); [`docs/technical/delivery/tests-and-traceability.md`](../../../docs/technical/delivery/tests-and-traceability.md), lines [`51-63`](../../../docs/technical/delivery/tests-and-traceability.md#L51-L63); [`docs/technical/delivery/ci-cd-and-stages.md`](../../../docs/technical/delivery/ci-cd-and-stages.md), lines [`50`](../../../docs/technical/delivery/ci-cd-and-stages.md#L50), [`60`](../../../docs/technical/delivery/ci-cd-and-stages.md#L60) and [`70`](../../../docs/technical/delivery/ci-cd-and-stages.md#L70): the collection, its commands, the freshness check, the detection and the report files.

## 🧪 How to test it

```bash
uv run pytest tests/ci/bruno_collection tests/ci/bruno_credentials tests/ci/detect_changes/bruno -n 2
uv run pytest tests/ci/workflows/checks/test_python_workflow.py tests/ci/workflows/test_stage_workflow.py -n 2
python3 .github/scripts/bruno_collection.py check --service backend/services/platform
docker compose -f compose.e2e.yaml up -d --wait
cd bruno/platform && npx --yes @usebruno/cli@4.2.1 run --env stage
```

The first three show the generator, the scan, the detection and the workflows. The last two run the collection against the real image.

## 🔗 Evidence

- [pytest](tests-evidences/pytest.txt): 1514 passed, 3 skipped.
- [ruff check](tests-evidences/ruff-check.txt), [ruff format](tests-evidences/ruff-format.txt) and [mypy](tests-evidences/mypy.txt): the checks on the ticket's files.
- [Bruno JUnit report](tests-evidences/bruno-platform.xml) and [Bruno JSON report](tests-evidences/bruno-platform.json): a run against a live `platform`, `tests/health.bru` 2 of 2 and `tests/refused-call.bru` 4 of 4.
- [ticket references](tests-evidences/ticket-refs.txt) and [plan view](tests-evidences/plan-view.txt): the specification links and the plan view are in order.

## 📝 Assumptions accepted

- Bruno CLI 4.2.1 goes into the collection's subfolders when `bru run` starts at the collection root, so `stage.yml` needs no recursive flag. The saved run shows both `tests/*.bru` files ran.

## 🔜 Follow-ups

| File | What to change |
| --- | --- |
| [`.github/scripts/detect_changes.py:28-31`](../../../.github/scripts/detect_changes.py#L28-L31) | The docstring says the freshness check runs with the repository tests. It runs in the `services` job of `python.yml`. Only the credential scan runs with the repository tests. |
| [`docs/technical/interfaces/api.md`](../../../docs/technical/interfaces/api.md) | The footer reads "(GH-2)". Name this ticket, "(T0.24)", as the other two pages do. |
| [`tests/ci/bruno_credentials/test_bruno_credentials.py`](../../../tests/ci/bruno_credentials/test_bruno_credentials.py) and [`tests/ci/bruno_credentials/helpers.py`](../../../tests/ci/bruno_credentials/helpers.py) | Move the module-level `plant` function of the test file into `helpers.py`, or make it a method of `TestBrunoCredentials`. |
| [`.github/scripts/bruno_collection.py`](../../../.github/scripts/bruno_collection.py) and [`tests/ci/bruno_collection/test_generate.py`](../../../tests/ci/bruno_collection/test_generate.py) | Path parameters become collection variables written with double braces in the URL and also get a `params:path` block, while Bruno's own form is `:customer_id`. `platform` has none. Settle one form before the first service with path parameters, and count `seq` within each folder as the brief said. |
| [`tests-evidences/bruno-platform.json`](tests-evidences/bruno-platform.json) and [`tests-evidences/bruno-platform.xml`](tests-evidences/bruno-platform.xml) | The JSON holds the absolute local worktree path and the JUnit holds the machine's hostname. Strip them before the commit. |
| [`tests-evidences/`](tests-evidences/pytest.txt) | Add a short file with the compose and Bruno commands the reports ran against, to show they match [`.github/workflows/stage.yml:127-137`](../../../.github/workflows/stage.yml#L127-L137). |
| [`.github/workflows/stage.yml`](../../../.github/workflows/stage.yml) and [`tests/ci/workflows/test_stage_workflow.py`](../../../tests/ci/workflows/test_stage_workflow.py) | Make the step fail when a collection runs zero tests, so a later CLI upgrade cannot pass while testing nothing. |
