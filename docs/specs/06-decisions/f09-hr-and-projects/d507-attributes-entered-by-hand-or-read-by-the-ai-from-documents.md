🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D507 Attributes entered by hand or read by the AI from documents

# 📜 D507 Attributes entered by hand or read by the AI from documents

**Status:** 🔄 draft (GH-2 step S4b, from VD-25 / D507)

## Context

How employees' degrees and qualifications are fed.

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

By hand, or by the AI reading the employee's documents: CVs and résumés, diploma scans or photos, licences and
certificates, training records.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md), VD-25).

## Consequences

- New entity [E-F9-31 Attribute reading](../../02-functional/f09-hr-and-projects/data/e-f09-31-attribute-reading.md):
  the source document, the fields read, their confidence, the status and the reviewer.
-
  [UC-F9-39](../../02-functional/f09-hr-and-projects/use-cases/13-keep-qualifications/uc-f09-39-read-documents-and-verify.md);
  the reading uses the AI of [F3](../../02-functional/f03-assistant/README.md) and the document reading of
  [T7](../../03-technical/t07-ai-providers-and-models/README.md).
- The readings and the proof documents are HR documents, with their retention; the employee is told what was read.

## Related

- [E-F9-31 Attribute reading](../../02-functional/f09-hr-and-projects/data/e-f09-31-attribute-reading.md)
-
  [UC-F9-39](../../02-functional/f09-hr-and-projects/use-cases/13-keep-qualifications/uc-f09-39-read-documents-and-verify.md)
- [F3 Assistant](../../02-functional/f03-assistant/README.md)
- [D506 Employees' degrees, optional and structured](d506-employees-degrees-optional-and-structured.md)
- [D508 HR confirms every AI reading before it counts](d508-hr-confirms-every-ai-reading-before-it-counts.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/scheduling-maps-attributes.md)

---

⬅️ [D506 Employees' degrees, optional and structured](d506-employees-degrees-optional-and-structured.md) ·
⬆️ [Up](README.md) ·
➡️ [D508 HR confirms every AI reading before it counts](d508-hr-confirms-every-ai-reading-before-it-counts.md)
