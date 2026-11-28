# T0.22: Playwright scaffold against the real images

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) in [🛣️ P0 Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0 Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04), 1 to 12 February 2027: Foundations ready
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- The Playwright configuration in `frontend/backoffice/e2e/`, with trace, video and screenshot kept on failure, as [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md#levels) (GUI level: Playwright in `frontend/<app>/e2e/`, against the real images of `compose.e2e.yaml`).
- The first `@smoke` tests of the shell, in light and dark and in French and English, and an accessibility check, run against `compose.e2e.yaml`, as [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#stages-dev-and-qa) (the dev stage runs Playwright `@smoke`).
- `.github/scripts/playwright.sh`, which runs them in CI and in `stage.yml`; a failure uploads the HTML report ([🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md#workflows), `images.yml`).
- A test for each screen of the shell that T0.17 lists (TKT-21).

## Features, use cases and business rules

- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md): specs-driven tests on the real images.
- [📜 D47 App shell](../../specs/06-decisions/ux/d47-app-shell.md): the shell the smoke tests cover.
- [📜 D43 Light and dark modes](../../specs/06-decisions/ux/d43-light-and-dark.md): both themes are tested.
- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md): French and English are tested.
- [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md): the accessibility check.

## Technical pages it builds on

- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md): GUI tests are Playwright in `frontend/<app>/e2e/`, against the real images of `compose.e2e.yaml`; a front-end ticket plans a Playwright test for every screen it builds (TKT-21).
- [🏗️ CI/CD and stages](../../technical/delivery/ci-cd-and-stages.md): `images.yml` runs Playwright against the real images; the dev stage runs Playwright `@smoke`, QA the full suite.
- [🏗️ Front end](../../technical/architecture/frontend.md): the front ends have Playwright tests.

## Screens touched

- ➖ No screen: the ticket builds no screen. It tests the shell that T0.17 builds, and the roadmap's T0.17 row says its screens are listed for these Playwright tests.

## Budgets touched

- The ticket touches no budget: the roadmap row and the specifications give it no measure (the [♿ Accessibility](../../specs/05-non-functional/accessibility.md) measures are still to be specified).

## Acceptance criteria

1. **Given** the real images started by `compose.e2e.yaml`, **when** `.github/scripts/playwright.sh` runs in CI and in `stage.yml`, **then** the `@smoke` tests of the shell pass. ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))
2. **Given** a Playwright test that fails, **when** the run ends, **then** the trace, video and screenshot are kept and the HTML report is uploaded. ([📜 D426](../../specs/06-decisions/technical/d426-testing-strategy.md))
3. **Given** the shell of T0.17, **when** the smoke tests run, **then** they cover light and dark, French and English, and an accessibility check. ([📜 D43](../../specs/06-decisions/ux/d43-light-and-dark.md), [📜 D21](../../specs/06-decisions/foundations/d21-languages.md), [📜 D46](../../specs/06-decisions/ux/d46-accessibility-standard.md))
4. **Given** the screens of the shell listed by T0.17, **when** the suite runs, **then** each of them has a test. ([📜 D47](../../specs/06-decisions/ux/d47-app-shell.md))

## Out of scope

- The compose stack `compose.e2e.yaml` itself, see [T0.21](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).
- The shell, see [T0.17](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The error messages on screen and their Playwright test, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap names no screen page for the shell, and the specifications have no `S-F` page for it, so "Screens touched" says no screen. The shell's screens are those T0.17 lists, which is not yet written.
- The roadmap names no business rule or use case, so the acceptance criteria cite the decisions that settle them.
- The roadmap rows carry no ticket anchor, so the ticket links point to the sprint anchors.
- The exact set of `@smoke` tests beyond "the shell in light and dark, French and English, and an accessibility check" is not specified; the plan settles it from T0.17's list.
