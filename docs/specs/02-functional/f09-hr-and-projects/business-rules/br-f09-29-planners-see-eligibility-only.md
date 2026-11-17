🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-29 Planners see eligibility, never sensitive details

# 📏 BR-F9-29 Planners see eligibility, never sensitive details

**Status:** 🔄 draft (GH-2 step S4b, from VD-24, VD-29 / D506, D511)

## Statement

A planner, a proposal and the scheduling board show only whether a person is eligible and, when not, a short reason
("not eligible: medical restriction", "not eligible: under 18", "not eligible: licence expired"); the birth date, the
medical fitness details, the proofs and the AI's readings stay with HR and the person.

## Why

- Private data is visible only to HR and the person; managers see work data (
  [BR-F9-02 HR data stays with HR and the person](br-f09-02-hr-data-stays-with-hr-and-the-person.md)).
- The birth date is kept only for the age checks, and medical fitness is a status with its restrictions, never a
  diagnosis [D506](../../../06-decisions/f09-hr-and-projects/d506-employees-degrees-optional-and-structured.md),
  [D511](../../../06-decisions/f09-hr-and-projects/d511-required-or-preferred-attributes-legal-ones-always-required.md).
- Legal values from the France country pack:
  [CR-FR-050](../../../10-country-packs/france/data-protection/cr-fr-050-privacy-by-design.md).

## Examples

| Case | Result |
|---|---|
| A planner opens the excluded people of a proposal | "Paul Martin: not eligible: medical restriction" |
| A planner opens Paul Martin's record | Work data only: no birth date, no fitness details (BR-F9-02) |
| A planner asks the AI assistant why Paul is excluded | The same short reason, nothing more (D12) |
| HR opens the reading of Paul's licence | Everything, with the source document |
| Paul opens his own profile | Everything about himself |
| A planner exports the excluded list | The names and the short reasons only |

## Applies to

- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)
- [E-F9-01 Employee record](../data/e-f09-01-employee-record.md)
- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-38](../use-cases/13-keep-qualifications/uc-f09-38-record-degrees-and-qualifications.md)

## Exceptions

None.

## Configurable

No. (Proposed) The wording of the short reasons comes from the qualification type catalogue and is translated (T10).

## Open questions

None.

---

⬅️ [BR-F9-28 HR confirms every AI reading](br-f09-28-hr-confirms-every-ai-reading.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-30](br-f09-30-live-position-team-option-working-hours.md)
