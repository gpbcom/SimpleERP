# T0.23: Error messages on screen

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04), 1 to 12 Feb 2027: Foundations ready
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- The error message pattern as a component in `frontend/packages/ui`: title, why, the action button, the faulty field highlighted and the small support reference, as [🧵 Error messages](../../specs/04-ux/design-system/patterns/error-messages.md).
- The wiring in `frontend/backoffice`: from the problem+json code of a refused call, through the API client and the catalogues of T0.16, to the message, as [📜 D122 Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md).
- The title, why and action texts in French and English, in `frontend/packages/i18n`.
- A Playwright test proving a refused call of `platform` shows its message against the real images.

## Features, use cases and business rules

- [📜 D122 Error message standard](../../specs/06-decisions/ux/d122-error-message-standard.md): "Every error message has a short title in plain words saying what happened, one sentence saying why, and the action that fixes it as a button; the faulty field is highlighted; no code or jargon, except a small support reference at the bottom."
- [📌 REQ-T05-03 problem+json errors](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md): "Errors are problem+json with the error codes of the error pattern."
- [🧵 Error messages](../../specs/04-ux/design-system/patterns/error-messages.md): the anatomy, behaviour and accessibility of the pattern.
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md): the front-end stack the component is built on.
- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md): French and English at launch.
- [📜 D46 Accessibility standard](../../specs/06-decisions/ux/d46-accessibility-standard.md): the error colour always comes with the icon and the words.

## Technical pages it builds on

- [🏗️ Front end](../../technical/architecture/frontend.md): Vue 3, TypeScript and Vite, the component library on the design system's tokens, and Playwright tests against the real images.
- [🏗️ API](../../technical/interfaces/api.md): `application/problem+json` errors carrying the error codes of the error message pattern (D122).
## Screens touched

- ➖ No screen: the ticket builds a component and its wiring in the app, not a screen page of `docs/specs/02-functional/`; the Playwright test shows it on the refused call of `platform`, and the roadmap lists no screen page for it.

## Budgets touched

- The ticket touches no budget: the roadmap row gives none, and [♿ Accessibility](../../specs/05-non-functional/accessibility.md) has no measure specified yet.

## Acceptance criteria

1. **Given** a call to `platform` that is refused with a problem+json code, **when** the back office shows the error, **then** it shows the title, the why and the action button of that code in French and in English, with its support reference. ([📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md), [📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md))
2. **Given** an error about a field, **when** it is shown, **then** the faulty field is highlighted with the message next to it. ([🧵 Error messages](../../specs/04-ux/design-system/patterns/error-messages.md))
3. **Given** an error shown, **when** a screen reader user reaches it, **then** it is announced, the message is linked to its field and the colour comes with the icon and the words. ([📜 D46](../../specs/06-decisions/ux/d46-accessibility-standard.md))
4. **Given** the real images started by `compose.e2e.yaml`, **when** the Playwright test refuses a call of `platform`, **then** the message appears as above. (roadmap "Done when")

## Out of scope

- The error code catalogue and its message keys, see [T0.04](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s01).
- The catalogues and their languages, see [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The typed API client and its mapping of problem+json, see [T0.20](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The Playwright scaffold, see [T0.22](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap gives no screen page for this ticket, so it says "No screen" and relies on the Playwright test against the shell.
- The accessibility budget has no measure yet, so none is listed.
- The ticket anchor is the sprint anchor `#s04`, as the phase page has no per-ticket anchor.
