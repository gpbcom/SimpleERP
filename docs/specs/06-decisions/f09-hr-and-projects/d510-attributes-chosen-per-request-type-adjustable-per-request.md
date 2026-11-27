🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D510 Attributes chosen per request type, adjustable per request

# 📜 D510 Attributes chosen per request type, adjustable per request

**Status:** 🔄 draft (GH-2 step S4b, from VD-28 / D510)

## Context

Who selects the attributes scheduling takes into account ([D509](d509-four-attribute-families-for-scheduling.md)).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

A configurator sets them per request type; the planner may add or relax one on a single request, and that change is
logged.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-28).

## Consequences

- New entity [E-F2-25 Request type](../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md), set on
  [S-F2-29](../../02-functional/f02-no-code-configuration/screens/12-set-up-request-types/s-f02-29-request-type-settings.md)
  [UC-F2-30](../../02-functional/f02-no-code-configuration/use-cases/12-set-up-request-types/uc-f02-30-set-up-a-request-type.md),
  [FL-F2-12](../../02-functional/f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md) by the configurator
  ([D96](../f02-no-code-configuration/d96-configurator-role.md)).
- [BR-F9-34 Every override is logged with its
  reason](../../02-functional/f09-hr-and-projects/business-rules/br-f09-34-overrides-logged-with-a-reason.md).
- A legal requirement cannot be relaxed ([D511](d511-required-or-preferred-attributes-legal-ones-always-required.md)).

## Related

- [E-F2-25 Request type](../../02-functional/f02-no-code-configuration/data/e-f02-25-request-type.md)
-
  [S-F2-29](../../02-functional/f02-no-code-configuration/screens/12-set-up-request-types/s-f02-29-request-type-settings.md)
- [BR-F9-34 Every override is logged with its
  reason](../../02-functional/f09-hr-and-projects/business-rules/br-f09-34-overrides-logged-with-a-reason.md)
- [D509 Four attribute families for scheduling](d509-four-attribute-families-for-scheduling.md)
- [D511 Required or preferred attributes; legal ones always
  required](d511-required-or-preferred-attributes-legal-ones-always-required.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D509 Four attribute families for scheduling](d509-four-attribute-families-for-scheduling.md) · ⬆️ [Up](README.md) ·
➡️ [D511](d511-required-or-preferred-attributes-legal-ones-always-required.md)
