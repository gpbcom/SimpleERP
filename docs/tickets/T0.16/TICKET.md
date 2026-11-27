# T0.16: Internationalisation base

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S03](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03), 18 to 29 January 2027: The contracts and the shell
- **Epic:** [E0.6 Back-office foundation](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): tokens, base components, i18n, the app shell, the error pattern on screen and the Playwright scaffold

## What it delivers

- `frontend/packages/i18n`: message catalogues per language, French and English at launch, as [D21](../../specs/06-decisions/foundations/d21-languages.md) and [Localisation](../../specs/05-non-functional/localisation.md).
- Dates, numbers and money formatted per locale, the money keeping its exact decimals, as [REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md).
- The user's language applied without reloading.
- A check that fails when a key misses in one language, as [REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md).

## Features, use cases and business rules

- [📜 D21 Languages](../../specs/06-decisions/foundations/d21-languages.md): "French and English at launch, every text in translation files, documents in the customer's language."
- [📌 REQ-T10-01 Translation catalogues reviewed](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md): translations live in catalogues; the review workflow comes in P2.
- [📌 REQ-T10-03 Money as exact decimals](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md): "Given a sum of lines, no float error."
- [📜 D407 Front end](../../specs/06-decisions/technical/d407-front-end.md): Vue 3 with TypeScript, the front end the package serves.

## Technical pages it builds on

- [🏗️ Front end](../../technical/architecture/frontend.md): Vue 3 with TypeScript and Vite, the shared packages of the front ends.

## Screens touched

- ➖ No screen: the ticket builds the `frontend/packages/i18n` package (catalogues, formatting, language switch, key check) and no screen.

## Budgets touched

- [🌐 Localisation](../../specs/05-non-functional/localisation.md#measures): French and English when the first version ships, every text in translation files. Its measures are not yet specified.

## Acceptance criteria

1. **Given** a key added in English only, **when** CI runs the catalogue check, **then** it fails. ([REQ-T10-01](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-01-translation-catalogues.md))
2. **Given** a component showing a translated text, **when** the user switches language, **then** it re-renders in the new language without reloading. ([D21](../../specs/06-decisions/foundations/d21-languages.md))
3. **Given** a money amount, **when** it is formatted for a locale, **then** it keeps its exact decimals. ([REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md))
4. **Given** dates and numbers, **when** they are formatted, **then** they follow the locale. ([Localisation](../../specs/05-non-functional/localisation.md))
5. **Given** the catalogues, **when** the package loads, **then** French and English are both present. ([D21](../../specs/06-decisions/foundations/d21-languages.md))

## Out of scope

- The review workflow of the catalogues, which comes in P2, see [T0.16](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The app shell using the catalogues, see [T0.17](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s03).
- The error messages on screen, see [T0.23](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s04).

## Assumptions

- The roadmap row has no anchor of its own, so the ticket links to the sprint anchor `#s03`, and the epic to `#epics`.
- No use case or business rule applies, so the criteria come from the roadmap row's "Delivers" and "Done when" text.
- The measures of the Localisation page are still "To be specified", so no budget figure is set.
- The package has no design page of its own in `docs/technical/`; the Front end page and D407 settle its framework.
