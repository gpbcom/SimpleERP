🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-26 Legal requirements are never relaxed

# 📏 BR-F9-26 Legal requirements are never relaxed

**Status:** 🔄 draft (GH-2 step S4b, from VD-29 / D511)

## Statement

An attribute the law ties to a task (a minimum age for regulated work, medical fitness for a post under reinforced
follow-up, a qualification or a licence the law requires) is always required: a configurator cannot make it preferred,
a planner cannot relax it, and the automatic mode stops when it cannot be met.

## Why

- The owner's decision VD-29
  [D511](../../../06-decisions/f09-hr-and-projects/d511-required-or-preferred-attributes-legal-ones-always-required.md):
  legal requirements are always required and cannot be relaxed.
- Which requirement is legal comes from the country pack, through the qualification types (
  [E-F9-30 Qualification type](../data/e-f09-30-qualification-type.md)), never from a person's choice.
- Legal values from the France country pack:
  - [CR-FR-208](../../../10-country-packs/france/labour/cr-fr-208-young-workers-regulated-work.md);
  - [CR-FR-209](../../../10-country-packs/france/labour/cr-fr-209-reinforced-medical-follow-up.md);
  - [CR-FR-210](../../../10-country-packs/france/labour/cr-fr-210-qualifications-tied-to-tasks.md);
  - [CR-FR-119](../../../10-country-packs/france/transport/cr-fr-119-driver-training.md);
  - [CR-FR-121 Dangerous goods (ADR)](../../../10-country-packs/france/transport/cr-fr-121-dangerous-goods.md).

## Examples

| Case | Result |
|---|---|
| Night work; a candidate aged 17 | Excluded: "not eligible: under 18"; the planner cannot relax it |
| A configurator sets the dangerous-goods training to "preferred" | Refused: it is a legal requirement |
| A planner tries to relax the driver card on one trip | Refused; the planner may pick another driver, move the window or subcontract |
| Automatic mode; the only candidate's licence has expired | The automatic mode stops and notifies the planner (BR-F9-33) |
| A post under reinforced follow-up; the person's fitness is out of date | Excluded: "not eligible: medical fitness to renew" |

## Applies to

- [UC-F2-30](../../f02-no-code-configuration/use-cases/12-set-up-request-types/uc-f02-30-set-up-a-request-type.md)
- [UC-F9-33 Schedule a work request](../use-cases/12-schedule-customer-requests/uc-f09-33-schedule-a-work-request.md)
- [UC-F9-34](../use-cases/12-schedule-customer-requests/uc-f09-34-run-the-automatic-scheduling.md)
- [E-F2-25 Request type](../../f02-no-code-configuration/data/e-f02-25-request-type.md)
- [E-F9-30 Qualification type](../data/e-f09-30-qualification-type.md)
- [E-F9-28 Assignment proposal](../data/e-f09-28-assignment-proposal.md)

## Exceptions

None. (Proposed) An exemption the law itself allows, such as a young worker's exemption on file, is part of the
requirement written in the country pack (CR-FR-208), not an override.

## Configurable

No. The legal requirements change only with a country pack update (D294).

## Open questions

None.

---

⬅️ [BR-F9-25 Required attributes exclude a candidate](br-f09-25-required-attributes-exclude.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-27 Unverified or expired attributes do not count](br-f09-27-unverified-attributes-do-not-count.md)
