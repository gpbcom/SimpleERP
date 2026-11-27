# T0.09: Company context and rights middleware

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.09](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 Jan 2027: the service kit and the first service. Sprint done when `platform` answers in its container, a request without a company is refused, and an outbox event survives a restart.
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of Back end (lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers), one library per agent, in `backend/shared/<lib>`.

## What it delivers

In `backend/shared/context`, with no business rules:

- The middleware that reads the company and the user of each request and carries them to the service and storage layers, as [REQ-T01-02](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) asks.
- The rights interface `allowed(user, action, record)` with a deny-by-default policy, as [I-T02-02](../../specs/03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md) and [REQ-T02-02](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md) ask.
- Refusals returned as problem+json with their code ([REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md)) and logged for the audit ([REQ-T02-06](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md)).

## Features, use cases and business rules

- [📌 REQ-T01-02](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md): the company context is checked at the gateway, in each service and in storage.
- [📌 REQ-T02-02](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md): rights are policies evaluated by one library in every service.
- [📌 REQ-T02-06](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md): every refused action is recorded in the audit trail.
- [📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md): errors are problem+json with the error codes.
- [🔌 I-T02-02](../../specs/03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md): `allowed(user, action, record)` evaluated in every service.
- [📜 D405](../../specs/06-decisions/technical/d405-architecture-and-scalability.md), [📜 D406](../../specs/06-decisions/technical/d406-back-end.md), [📜 D414](../../specs/06-decisions/technical/d414-security-design.md), [📜 D410](../../specs/06-decisions/technical/d410-api-style-and-auth.md) and [📜 D122](../../specs/06-decisions/ux/d122-error-message-standard.md): the decisions the requirements cite.
- [📜 D438](../../specs/06-decisions/technical/d438-repository-layout.md): the library lives in `backend/shared/<lib>`, with no business rules.

## Technical pages it builds on

- [🏗️ Back end](../../technical/architecture/backend.md): the company-context and rights middleware is one of the libraries of the service kit under `backend/shared/`.

## Screens touched

- ➖ No screen: a back-end library with no user interface.

## Budgets touched

- The ticket touches no budget: the roadmap row gives none, and [🧱 Data isolation](../../specs/05-non-functional/data-isolation.md) still says "To be specified" for its measures.

## Acceptance criteria

1. **Given** a request without a company, **when** it reaches the middleware, **then** it is refused. ([📌 REQ-T01-02](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) criterion 1)
2. **Given** the same user, action and record, **when** the decision is asked from HTTP and from a direct call, **then** both give the same decision. ([📌 REQ-T02-02](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-02-policies-one-library.md) criterion 1)
3. **Given** no policy allows an action, **when** `allowed(user, action, record)` is called, **then** it denies by default. ([🔌 I-T02-02](../../specs/03-technical/t02-identity-and-access/interfaces/i-t02-02-policy-decision-library.md))
4. **Given** a refused call, **when** the answer is built, **then** it is a problem+json body with its code and no secret. ([📌 REQ-T05-03](../../specs/03-technical/t05-api-and-webhooks/requirements/req-t05-03-problem-json.md) criteria 1 and 2)
5. **Given** a refusal, **when** it happens, **then** it is logged with its code, and the log holds who, what and why. ([📌 REQ-T02-06](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md) criterion 1)

## Out of scope

- The row-level security guard of storage and the gateway itself, see [📌 REQ-T01-02](../../specs/03-technical/t01-companies-and-data-isolation/requirements/req-t01-02-company-context-everywhere.md) criterion 2, built where the services own their storage.
- The audit writer that stores refusals in the audit trail, see [T0.10](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The alert on many refusals from one token ([📌 REQ-T02-06](../../specs/03-technical/t02-identity-and-access/requirements/req-t02-06-refusals-audited.md) criterion 2).
- The first service that uses the middleware, see [T0.14](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).

## Assumptions

- The roadmap row has no anchor of its own, so the ticket links the sprint anchor `#s02` and the epic links the `#epics` section.
- "Logged for the audit" is taken as a log line with the code, because the audit writer comes with T0.10 and later tickets.
- Out-of-scope items above are conservative readings: the roadmap row names only the middleware, the rights interface, problem+json refusals and their logging.
