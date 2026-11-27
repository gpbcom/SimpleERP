🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-06 Location only at check-in

# 📏 BR-F9-06 Location only at check-in

**Status:** ✅ specified

## Statement

When the team's setting is on, the phone's position is recorded at check-in and check-out only, shown to the employee on
screen; it is never tracked in between, never used for anything else, and kept 1 year (D290). This is the default; a
live position during working hours is only an option for drivers' and carers' teams, under
[BR-F9-30](br-f09-30-live-position-team-option-working-hours.md).

## Why

See [D286](../../../06-decisions/f09-hr-and-projects/d286-location-at-check-in.md).

Legal values from the France country pack:
[CR-FR-047 HR records retention](../../../10-country-packs/france/labour/cr-fr-047-hr-records-retention.md),
[CR-FR-054 Location only when needed and announced](../../../10-country-packs/france/data-protection/cr-fr-054-location-with-consent.md).

Kept as the default by
[D504](../../../06-decisions/f09-hr-and-projects/d504-positions-at-check-in-by-default-live-as-a-team-option-for-drivers-and-carers.md),
which adds the live option of BR-F9-30.

## Examples

| Case | Result |
|---|---|
| Field worker checks in on site | Position recorded and shown |
| Between check-in and check-out | Nothing recorded |
| Drivers' team with the live option on | Live position during working hours, under BR-F9-30; check-in and check-out as here |

## Applies to

Every F9 use case concerned, among them:
- [UC-F9-36 See work and places on a map](../use-cases/12-schedule-customer-requests/uc-f09-36-see-work-and-places-on-a-map.md)
- [UC-F9-37 Share my position during work](../use-cases/12-schedule-customer-requests/uc-f09-37-share-my-position-during-work.md)
- [E-F9-10 Attendance](../data/e-f09-10-attendance.md)

## Exceptions

None.

## Configurable

Yes: per team, off by default. The live position is a separate option (BR-F9-30).

## Open questions

None.

---

⬅️ [BR-F9-05 Time off follows its type](br-f09-05-time-off-follows-its-type.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-07 Activity drafts stay private](br-f09-07-activity-drafts-stay-private.md)
