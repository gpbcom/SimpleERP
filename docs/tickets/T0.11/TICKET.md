# T0.11: Metering client

**Status:** ✅ Done

## Roadmap

- **Ticket:** [T0.11](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) in [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Phase:** [🛣️ P0: Foundations](../../specs/00-vision/roadmap/phases/01-p0-foundations.md)
- **Sprint:** [S02](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02), 4 to 15 January 2027: the service kit and the first service
- **Epic:** [E0.3 Service kit](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#epics): the libraries of Back end: lifecycle, logging, configuration, company context and rights, outbox, metering client, country-pack rules, test helpers

## What it delivers

- The client every paid call goes through, in `backend/shared/metering`: budget check, reservation, call, settlement, as [Architecture, Metering (TC-21)](../../technical/architecture/architecture.md).
- A usage event written through the outbox of [T0.10](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02) for each settled call.
- A legal-duty flag that bypasses the stop at the budget, as [BR-F22-06](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md).

## Features, use cases and business rules

- [📏 BR-F22-06: Stop at the budget, legal duties kept](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md): at 100 % new paid calls stop, except calls a legal duty needs.
- [📜 D398: Budgets warn, then stop](../../specs/06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md): the choice the stop and its exception follow.
- [📜 D405: Architecture and scalability](../../specs/06-decisions/technical/d405-architecture-and-scalability.md): the outbox through which the usage event goes.
- [🧗 TC-21: Metering every paid call, and stopping on a budget](../../specs/03-technical/challenges/tc-21-metering-every-paid-call.md): one library every paid call goes through, with reservation before and settlement after.

## Technical pages it builds on

- [🏗️ Architecture](../../technical/architecture/architecture.md): "Every paid call goes through one metering gateway or shared library: budget check, reservation, call, settlement, usage event; a legal-duty flag bypasses the stop (F22)."
- [🏗️ Back end](../../technical/architecture/backend.md): the shared code is a service kit with no business rules, and the metering client is one of its libraries.

## Screens touched

- ➖ No screen: a shared back-end library in `backend/shared/metering`, with no front end.

## Budgets touched

- The ticket touches no budget: neither the roadmap row nor the specifications give it a measure.

## Acceptance criteria

1. **Given** a stand-in metering server and a budget already spent, **when** a paid call is made, **then** it is refused before the call is made. ([📏 BR-F22-06](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md))
2. **Given** a call within budget, **when** it is reserved, made and settled, **then** exactly one usage event is emitted through the outbox. ([📜 D398](../../specs/06-decisions/f22-unified-cost-management/d398-budgets-warn-then-stop.md))
3. **Given** an exhausted budget, **when** a call carries the legal-duty flag, **then** it passes. ([📏 BR-F22-06](../../specs/02-functional/f22-unified-cost-management/business-rules/br-f22-06-stop-at-budget-legal-duties-kept.md))

## Out of scope

- The event outbox it writes through, see [T0.10](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The test helpers and the stand-in server kit, see [T0.13](../../specs/00-vision/roadmap/phases/01-p0-foundations.md#s02).
- The F22 budgets, thresholds and screens themselves, which the roadmap row does not give this ticket.

## Assumptions

- The roadmap names no use case or screen for this ticket: BR-F22-06 and D398 are linked because they settle the stop and the legal-duty bypass.
- The list of legal duties comes from the country pack (BR-F22-06); this ticket only carries the flag and does not read a pack.
- TC-21 asks whether the check must be exact under parallel calls; it is an open question, so reservation before the call is taken as the conservative option.
- The roadmap anchors rows by sprint, so the ticket and its epic link to the sprint and epics sections.
