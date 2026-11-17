🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D506 Employees' degrees, optional and structured

# 📜 D506 Employees' degrees, optional and structured

**Status:** 🔄 draft (GH-2 step S4b, from VD-24 / D506)

## Context

The owner asked for an optional degree field on the employee, to be used by scheduling.
[E-F9-01 Employee record](../../02-functional/f09-hr-and-projects/data/e-f09-01-employee-record.md) held a free list of
skills and [E-F9-12 Certification](../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md) only a name
and a "valid until" date.

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

An optional, structured field: an employee has none, one or several degrees, each with its title, level (EQF 1 to 8 and
the national level, RNCP in France), field of study, institution, country, year, proof, and whether it is verified.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-24).

## Consequences

- New entity [E-F9-29 Degree](../../02-functional/f09-hr-and-projects/data/e-f09-29-degree.md); E-F9-01 relates to it
  (change note).
-
  [S-F9-35](../../02-functional/f09-hr-and-projects/screens/13-keep-qualifications/s-f09-35-employee-qualifications.md),
  [UC-F9-38](../../02-functional/f09-hr-and-projects/use-cases/13-keep-qualifications/uc-f09-38-record-degrees-and-qualifications.md).

## Related

- [E-F9-29 Degree](../../02-functional/f09-hr-and-projects/data/e-f09-29-degree.md)
- [E-F9-01 Employee record](../../02-functional/f09-hr-and-projects/data/e-f09-01-employee-record.md)
-
  [S-F9-35](../../02-functional/f09-hr-and-projects/screens/13-keep-qualifications/s-f09-35-employee-qualifications.md)
- [D507 Attributes entered by hand or read by the AI from documents](d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md)
- [D509 Four attribute families for scheduling](d509-four-attribute-families-for-scheduling.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D505 The employee sees their own position live](d505-the-employee-sees-their-own-position-live.md) ·
⬆️ [Up](README.md) · ➡️ [D507](d507-attributes-entered-by-hand-or-read-by-the-ai-from-documents.md)
