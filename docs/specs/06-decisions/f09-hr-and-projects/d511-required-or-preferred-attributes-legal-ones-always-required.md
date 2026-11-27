🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D511 Required or preferred attributes; legal ones always required

# 📜 D511 Required or preferred attributes; legal ones always required

**Status:** ✅ decided

## Context

How a selected attribute weighs in scheduling
([D510](d510-attributes-chosen-per-request-type-adjustable-per-request.md)).

## Options

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Each selected attribute is required or preferred, with a weight; legal requirements are always required and cannot be
relaxed.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-29).

## Consequences

- [BR-F9-25 Required attributes exclude a
  candidate](../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md); [BR-F9-26
  Legal requirements are never
  relaxed](../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md).
- Nine domain rules become requirements of a request type or an operation on this one mechanism (change note):
  [BR-F12-17](../../02-functional/f12-manufacturing/business-rules/br-f12-17-operators-sign-in-only-where-qualified.md),
  [BR-SC05-13](../../08-sectors/sc05-manufacturing/business-rules/br-sc05-13-operators-qualified-for-the-operation.md),
  [BR-F9-17](../../02-functional/f09-hr-and-projects/business-rules/br-f09-17-mandatory-trainings-must-be-current-for-the-work-that-needs-them.md),
  [BR-F9-22](../../02-functional/f09-hr-and-projects/business-rules/br-f09-22-rounds-respect-travel-skills-continuity-and-working-time.md),
  [BR-SC03-13](../../08-sectors/sc03-services/business-rules/br-sc03-13-skills-kept-current.md),
  [BR-SC04-06](../../08-sectors/sc04-home-care/business-rules/br-sc04-06-carers-match-the-needs.md),
  [BR-SC07-05](../../08-sectors/sc07-transport/business-rules/br-sc07-05-drivers-qualified-and-current.md),
  [BR-SC07-09](../../08-sectors/sc07-transport/business-rules/br-sc07-09-dangerous-goods-checked.md),
  [BR-SC12-07](../../08-sectors/sc12-education-and-training/business-rules/br-sc12-07-quality-evidence-kept.md).
- The [aggregated list view](../../04-ux/design-system/patterns/aggregated-list-view.md) gains an "Eligible for" facet
  where these attributes apply.

## Related

- [BR-F9-25 Required attributes exclude a
  candidate](../../02-functional/f09-hr-and-projects/business-rules/br-f09-25-required-attributes-exclude.md)
- [BR-F9-26 Legal requirements are never
  relaxed](../../02-functional/f09-hr-and-projects/business-rules/br-f09-26-legal-requirements-never-relaxed.md)
- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [D510 Attributes chosen per request type, adjustable per
  request](d510-attributes-chosen-per-request-type-adjustable-per-request.md)
- [D514 Scheduling objectives](d514-scheduling-objectives.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D510](d510-attributes-chosen-per-request-type-adjustable-per-request.md) · ⬆️ [Up](README.md) ·
➡️ [D512](../f16-customer-support-agents/d512-every-customer-request-feeds-scheduling.md)
