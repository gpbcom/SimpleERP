# T0.12: Country-pack rules library

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.12](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: The service kit and the first service
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of the back end: lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers, in `backend/shared/<lib>`

## What it delivers

- The rules library `value(rule, country, date)`, in `backend/shared/country-rules`, as [📝 I-T11-01 Rules library](../../specs/03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md) specifies it.
- A pack catalogue of values with validity dates, which the library reads by the date of the fact, as [📌 REQ-T11-02 One rules library by date](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md).
- Money values read as exact decimals with their currency, as [📌 REQ-T10-03 Money as exact decimals](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md).
- Tests per date in force, as [📌 REQ-T11-06 Rules tested per date](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-06-tests-per-date.md) asks.

## Features, use cases and business rules

- [📌 REQ-T11-02 One rules library by date](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md)
- [📌 REQ-T11-06 Rules tested per date](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-06-tests-per-date.md)
- [📌 REQ-T10-03 Money as exact decimals](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md)
- [🔌 I-T11-01 Rules library](../../specs/03-technical/t11-legal-corpora/interfaces/i-t11-01-rules-library.md)
- [📜 D438 Repository layout](../../specs/06-decisions/technical/d438-repository-layout.md)
- [📜 D405 Architecture and scalability](../../specs/06-decisions/technical/d405-architecture-and-scalability.md)
- [📜 D426 Testing strategy](../../specs/06-decisions/technical/d426-testing-strategy.md)

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md#target-design-specified-in-gh-2-not-built-yet): the shared code is a service kit with no business rules, and the country-pack rules library is one of its libraries.
- [🏗️ Repository layout](../../technical/architecture/repository-layout.md): where `backend/shared/<lib>` sits.
- [🏗️ Tests and traceability](../../technical/delivery/tests-and-traceability.md#target-design-specified-in-gh-2-not-built-yet): country-pack rules are tested per date in force.

## Screens touched

- ➖ No screen: a back-end shared library in `backend/shared/country-rules`, with no front end.

## Budgets touched

- The ticket touches no budget: neither the roadmap row nor the specifications give it a measure.

## Acceptance criteria

1. **Given** a test pack and an invoice of last year, **when** the library is asked for a rule's value at that date, **then** it returns last year's value. ([📌 REQ-T11-02](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md) criterion 1)
2. **Given** a test pack with a future-dated value, **when** the library is asked at a date on or after it, **then** the value applies from its date, and before it the earlier value applies. ([📌 REQ-T11-02](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-02-rules-library.md) criterion 2)
3. **Given** a rate change in the test pack, **when** the tests run, **then** there are tests before and after its date. ([📌 REQ-T11-06](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-06-tests-per-date.md) criterion 1)
4. **Given** a money value in the pack, **when** it is read and lines are summed, **then** it is an exact decimal with its currency and the sum has no float error. ([📌 REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md) criterion 2)
5. **Given** the new library, **when** the conventions and the library's own tests run, **then** they pass (the roadmap's "done when").

## Out of scope

- Signed, versioned packs and the pack registry, see [📌 REQ-T11-01](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-01-signed-packs.md).
- The release block on a missing per-date test, see [📌 REQ-T11-06](../../specs/03-technical/t11-legal-corpora/requirements/req-t11-06-tests-per-date.md) criterion 2.
- Conversions rounded as the pack says, which need real pack data, see [📌 REQ-T10-03](../../specs/03-technical/t10-translations-and-notifications/requirements/req-t10-03-money-decimals.md) criterion 1.
- The test helpers library, see [T0.13](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- The roadmap row gives no budget and no screen, so none is listed.
- Criteria 3 and 5 restate the roadmap's "done when" ("tests per date as REQ-T11-06 asks"); criterion 2 of REQ-T11-06 (release blocked) is taken as out of scope because it concerns the release, not the library.
- The ticket graph names T0.04 and T0.06 as prerequisites; the pack catalogue format is not specified beyond "values with validity dates", so its fields are left to the plan.
- The ticket anchor links to the sprint section `#s02` because the roadmap rows carry no anchor of their own.
