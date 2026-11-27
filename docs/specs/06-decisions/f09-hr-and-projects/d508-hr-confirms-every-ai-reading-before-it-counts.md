🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D508 HR confirms every AI reading before it counts

# 📜 D508 HR confirms every AI reading before it counts

**Status:** 🔄 draft (GH-2 step S4b, from VD-26 / D508)

## Context

Whether an attribute read by the AI counts at once
([D507](d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md)).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

HR confirms each reading, with the source document beside it; until then the attribute is "to verify" and scheduling
ignores it.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-26).

## Consequences

- [BR-F9-28 HR confirms every AI
  reading](../../02-functional/f09-hr-and-projects/business-rules/br-f09-28-hr-confirms-every-ai-reading.md); [BR-F9-27
  Unverified or expired attributes do not
  count](../../02-functional/f09-hr-and-projects/business-rules/br-f09-27-unverified-attributes-do-not-count.md).
- [S-F9-36 Readings to
  verify](../../02-functional/f09-hr-and-projects/screens/13-keep-qualifications/s-f09-36-readings-to-verify.md).

## Related

- [BR-F9-28 HR confirms every AI
  reading](../../02-functional/f09-hr-and-projects/business-rules/br-f09-28-hr-confirms-every-ai-reading.md)
- [BR-F9-27 Unverified or expired attributes do not
  count](../../02-functional/f09-hr-and-projects/business-rules/br-f09-27-unverified-attributes-do-not-count.md)
- [S-F9-36 Readings to
  verify](../../02-functional/f09-hr-and-projects/screens/13-keep-qualifications/s-f09-36-readings-to-verify.md)
- [D507 Attributes entered by hand or read by the AI from
  documents](d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D507](d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md) · ⬆️ [Up](README.md) ·
➡️ [D509 Four attribute families for scheduling](d509-four-attribute-families-for-scheduling.md)
