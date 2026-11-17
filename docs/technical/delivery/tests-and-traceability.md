# Tests and traceability

How simple-erp is tested, and how every test result stays provable.

## Levels

| Level | Tool | Where | Proves |
|---|---|---|---|
| Unit | pytest, two workers | local, CI, stages | Each class does what its tests say |
| Conventions | `tests/conventions/` | local, CI | The house rules of `AGENT.md` that a test can enforce |
| Static | ruff, mypy | local, CI | Style and types |
| GUI | Playwright in `frontends/<frontend>/e2e/` | local, dev, QA | Screens and flows, against the real images |
| API | Bruno collection in `bruno/` | dev, QA | The HTTP APIs, headless |
| Upgrade | `scripts/stage/upgrade-test.sh` (to come) | QA | The previous release's data under the new images |

Tests mirror `src/`, use real stand-ins rather than mocks (a local server, a git sandbox, a fake executable), and are
named as sentences (`AGENT.md`, "Tests"). How to run each level: `.claude/rules/TESTS-NOTICE.md`.

## Tests first (TEST-7)

Every code step of a ticket goes: the tests, committed alone; a red run, recorded; the code; a green run, recorded. A
`PreToolUse` hook refuses a production-code commit that skips it, and `ticket-docs check` verifies the order in the
history (saved in a bundle before each squash).

## Evidence (TEST-8) and kept reports (TEST-9)

```mermaid
flowchart LR
    run["a run: local, CI or stage"] -->|ticket-docs record-run| folder["docs/tickets/GH-n/tests-evidences/where-date-check/"]
    folder --> index["docs/tickets/README.md (generated index)"]
    folder -->|ticket-docs archive| asset["pre-release evidence-GH-n: GH-n-date.zip"]
    stage["stage.yml artifacts (90 days)"] -->|gh run download| folder
    qa["QA run of a release"] -->|release.yml| release["GitHub Release assets"]
```

- A result counts only with its evidence folder: the command, the commit, the raw output and the verdict.
- Every report is kept, failed and invalid runs included: unit (`report.xml`, `report.html`), GUI and E2E (Playwright
  report and `results.json`, Bruno reports, failure traces), CI and stage runs (their artifacts and log).
- `docs/tickets/` is local. Each ticket folder is archived to its GitHub pre-release at every hand-over, and each
  release carries its QA reports.

## Target design (specified in GH-2, not built yet)

**Levels (D426).** Unit tests first (TEST-7); contract tests generated from each OpenAPI; the Bruno collection on the
API (TEST-1); Playwright against the real images (TEST-6) with one seeded company per sector (16); country-pack rules
tested per date in force; AI evaluation sets (D417); acceptance tests generated from the use cases' Given/When/Then. QA
runs the whole suite.

**Coverage.** 100 % coverage, errors and edge cases included (the owner's requirement): every error flow of the use
cases and every error case of the D122 pattern has its test.

**Load and resilience.** k6 load tests per release against the targets of D408 on the three reference sizes, the laptop
profile included; failure tests in staging (a pod, a node, the bus, a database failover); an upgrade test from the
previous release and the last LTS.

**Test data.** Only synthetic data: one generated company per sector and size, with history; never production data in
tests; anonymised copies only for the hosted support assistant's reproductions, inside the customer's namespace.

Decided in [D426](../../specs/06-decisions/technical/d426-testing-strategy.md).

Last reviewed: 2026-11-12 (GH-2)
