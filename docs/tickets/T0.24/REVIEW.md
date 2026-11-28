# T0.24: Review note

**Verdict:** ✅ Approved · **Branch:** `feature/tickets`

Round 2, confirm fixes. The one blocking finding from round 1 is resolved. The fix only adds evidence files and changes no code, so it brings in no new defect.

## What changed

- `bruno/platform/` is generated from the OpenAPI of `platform`, and CI fails when the collection drifts from it.
- Two hand-written tests: the health call, and a refused call that must answer problem+json with its code and no secret.
- The `stage.yml` step runs every collection under `bruno/` headless with CLI 4.2.1 and keeps a JUnit and a JSON report for each.
- A credential scan keeps secrets out of `bruno/`, and change detection runs the Bruno checks when `bruno/` or the OpenAPI changes.
- Round 2 fix: the collection was run against a live `platform` and its reports were saved as evidence.

## Acceptance criteria

| Criterion | Evidence | Result |
| --- | --- | --- |
| 1. Given the OpenAPI of `platform`, when the generator runs, then `bruno/platform/` holds the collection | tests/ci/bruno_collection/test_generate.py, tests-evidences/pytest.txt | ✅ Pass |
| 2. Given the collection, when it runs headless against `platform`, then its health test passes | tests-evidences/bruno-platform.xml and bruno-platform.json (tests/health.bru, 2 of 2) | ✅ Pass |
| 3. Given a refused call, when its test runs, then the body is problem+json with its code and no secret | tests-evidences/bruno-platform.xml and bruno-platform.json (tests/refused-call.bru, 4 of 4) | ✅ Pass |
| 4. Given the files of `bruno/`, when they are searched, then no credential is committed | tests/ci/bruno_credentials/test_bruno_credentials.py, tests-evidences/pytest.txt | ✅ Pass |
| 5. Given a run of `stage.yml` on dev, when it reaches the Bruno step, then it runs headless and keeps JUnit and JSON reports | tests/ci/workflows/test_stage_workflow.py; a local run of the same command (bruno-platform.*) | ✅ Pass |
| 6. Given a collection that no longer matches the OpenAPI, when CI runs, then it fails | tests/ci/bruno_collection/test_check.py, tests/ci/workflows/checks/test_python_workflow.py, tests/ci/detect_changes/bruno/test_bruno_changes.py | ✅ Pass |

## Look at first

- The Bruno step of the stage workflow (the loop over `bruno/*/`, the `--env stage` flag, the report paths): /home/guillaume/Documents/Projects/Others/simple-erp/.github/workflows/stage.yml lines 124-134.
- The refused-call assertions, which guard against leaking secrets or stack traces in problem+json: /home/guillaume/Documents/Projects/Others/simple-erp/bruno/platform/tests/refused-call.bru.
- The credential scan, which enforces TEST-1 and D426: /home/guillaume/Documents/Projects/Others/simple-erp/tests/ci/bruno_credentials/.
- The ticket touches no identity, permissions or company data. The refused call only checks that a request without a company context is turned away with a 400.

## Assumptions accepted

- Bruno CLI 4.2.1 goes into subfolders when run from the collection root: accepted. The saved run shows both tests/*.bru files ran.

## Follow-ups

- The Bruno reports hold the absolute local worktree path and the machine's hostname. Strip them or use relative paths before committing (K14).
- Save the command and the stack the Bruno evidence was run against, as the other evidence files do (K14).
- Make the stage step fail when a collection runs zero tests, so a later CLI upgrade cannot pass while testing nothing (K12, K06).
