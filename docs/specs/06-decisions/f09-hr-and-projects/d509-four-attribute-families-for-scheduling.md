🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D509 Four attribute families for scheduling

# 📜 D509 Four attribute families for scheduling

**Status:** ✅ decided

## Context

Which employees' attributes scheduling may take into account. The law and common practice tie some tasks to an age, a
medical fitness, a licence, an operator certificate, an authorisation or a professional registration (maps and
eligibility (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), part 2).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Four families: degrees and qualifications; skills and languages; place and travel; person and contract.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-27).

## Consequences

- [E-F9-01 Employee record](../../02-functional/f09-hr-and-projects/data/e-f09-01-employee-record.md) gains a birth date
  (used only
  for age checks), a medical fitness status (fit, fit with restrictions, unfit, with dates, never a diagnosis),
  languages and skills with their level, a home base, zones, a maximum travel, a vehicle and a cost rate (change note).
- [E-F9-12 Certification](../../02-functional/f09-hr-and-projects/data/e-f09-12-certification.md) becomes
  "Qualification", typed from the catalogue of [E-F9-30 Qualification
  type](../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md), kept in YAML catalogues of the
  country and sector packs.
- A planner sees only "eligible" or "not eligible" with its reason, never the birth date or the fitness details
  [BR-F9-29](../../02-functional/f09-hr-and-projects/business-rules/br-f09-29-planners-see-eligibility-only.md).
- France: [CR-FR-208](../../10-country-packs/france/labour/cr-fr-208-young-workers-regulated-work.md),
  [CR-FR-209](../../10-country-packs/france/labour/cr-fr-209-reinforced-medical-follow-up.md),
  [CR-FR-210](../../10-country-packs/france/labour/cr-fr-210-qualifications-tied-to-tasks.md).

## Related

- [E-F9-01 Employee record](../../02-functional/f09-hr-and-projects/data/e-f09-01-employee-record.md)
- [E-F9-30 Qualification type](../../02-functional/f09-hr-and-projects/data/e-f09-30-qualification-type.md)
- [BR-F9-29 Planners see eligibility, never sensitive details](../../02-functional/f09-hr-and-projects/business-rules/br-f09-29-planners-see-eligibility-only.md)
- [CR-FR-210 Qualifications the law ties to tasks](../../10-country-packs/france/labour/cr-fr-210-qualifications-tied-to-tasks.md)
- [D510 Attributes chosen per request type, adjustable per request](d510-attributes-chosen-per-request-type-adjustable-per-request.md)
- [D511 Required or preferred attributes; legal ones always required](d511-required-or-preferred-attributes-legal-ones-always-required.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D508 HR confirms every AI reading before it counts](d508-hr-confirms-every-ai-reading-before-it-counts.md) ·
⬆️ [Up](README.md) · ➡️ [D510](d510-attributes-chosen-per-request-type-adjustable-per-request.md)
