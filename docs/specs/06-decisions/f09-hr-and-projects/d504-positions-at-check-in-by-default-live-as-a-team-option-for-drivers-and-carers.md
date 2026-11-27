🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 👥 [Decisions: F9 HR and projects](README.md) ›
📜 D504 Positions at check-in by default, live as a team option for drivers and carers

# 📜 D504 Positions at check-in by default, live as a team option for drivers and carers

**Status:** ✅ decided

## Context

How a person's position is recorded. Today: at check-in and check-out only, per team, off by default, kept one year
[BR-F9-06](../../02-functional/f09-hr-and-projects/business-rules/br-f09-06-location-only-at-check-in.md),
[D286](d286-location-at-check-in.md), [D290](d290-f9-use-cases.md),
[CR-FR-054](../../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md).

## Options

The first proposal of 2026-11-13 (maps and
eligibility (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)):
- A. position at check-in and check-out only;
- B. live position during working hours, for a stated purpose;
- C. vehicles' positions, not people's.

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Check-in and check-out by default; a live position during working hours as a per-team option for drivers (SC07) and
carers (SC04), with its stated purpose and its data protection impact assessment, off outside working hours, and never
used to control speed or measure performance.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-22).

## Consequences

- [BR-F9-06](../../02-functional/f09-hr-and-projects/business-rules/br-f09-06-location-only-at-check-in.md) keeps its
  default; the live position becomes an option under
  [BR-F9-30](../../02-functional/f09-hr-and-projects/business-rules/br-f09-30-live-position-team-option-working-hours.md)
  (change note).
- New entity [E-F9-32 Live position](../../02-functional/f09-hr-and-projects/data/e-f09-32-live-position.md);
  [REQ-T13-05 Live positions](../../03-technical/t13-maps-and-geodata/requirements/req-t13-05-live-positions.md).
- Live positions are kept two months at most (D517), the CNIL guidance to read in the France country pack
  [BR-F9-31](../../02-functional/f09-hr-and-projects/business-rules/br-f09-31-live-positions-kept-two-months.md),
  [CR-FR-211](../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md).

## Related

- [BR-F9-06 Location only at
  check-in](../../02-functional/f09-hr-and-projects/business-rules/br-f09-06-location-only-at-check-in.md)
- [BR-F9-30 Live position only as a team option, during working
  hours](../../02-functional/f09-hr-and-projects/business-rules/br-f09-30-live-position-team-option-working-hours.md)
- [BR-F9-31 Live positions kept two months at
  most](../../02-functional/f09-hr-and-projects/business-rules/br-f09-31-live-positions-kept-two-months.md)
- [E-F9-32 Live position](../../02-functional/f09-hr-and-projects/data/e-f09-32-live-position.md)
- [CR-FR-211 Live geolocation of
  employees](../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md)
- [D503 Who sees people's positions](d503-who-sees-peoples-positions.md)
- [D505 The employee sees their own position live](d505-the-employee-sees-their-own-position-live.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D503 Who sees people's positions](d503-who-sees-peoples-positions.md) · ⬆️ [Up](README.md) ·
➡️ [D505 The employee sees their own position live](d505-the-employee-sees-their-own-position-live.md)
