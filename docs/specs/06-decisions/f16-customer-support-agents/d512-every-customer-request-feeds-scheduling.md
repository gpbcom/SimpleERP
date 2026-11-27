🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D512 Every customer request feeds scheduling

# 📜 D512 Every customer request feeds scheduling

**Status:** 🔄 draft (GH-2 step S4b, from VD-30 / D512)

## Context

The owner set the input of scheduling: "customer's request whatever there types".

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Every customer request, whatever its type: service and interventions, orders to fulfil and deliver, projects and
engagements, bookings and appointments.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-30).

## Consequences

- New entity [E-F16-12 Work request](../../02-functional/f16-customer-support-agents/data/e-f16-12-work-request.md),
  shared by every capability that schedules work.
- [FL-F9-12 Schedule customer
  requests](../../02-functional/f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md),
  [UC-F9-33](../../02-functional/f09-hr-and-projects/use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md).
- F6 and F7 orders are turned into work requests.

## Related

- [E-F16-12 Work request](../../02-functional/f16-customer-support-agents/data/e-f16-12-work-request.md)
- [FL-F9-12 Schedule customer
  requests](../../02-functional/f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md)
- [D513 One work request whatever the channel](d513-one-work-request-whatever-the-channel.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D511](../f09-hr-and-projects/d511-required-or-preferred-attributes-legal-ones-always-required.md) ·
⬆️ [Up](README.md) · ➡️ [D513 One work request whatever the channel](d513-one-work-request-whatever-the-channel.md)
