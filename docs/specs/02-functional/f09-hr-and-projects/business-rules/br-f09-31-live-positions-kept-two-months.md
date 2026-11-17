🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 👥 [F9 HR and projects](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F9-31 Live positions kept two months at most

# 📏 BR-F9-31 Live positions kept two months at most

**Status:** 🔄 draft (GH-2 step S4b, from VD-22 / D504; retention proposed)

## Statement

Live positions are deleted 2 months at most after they were recorded (D517); positions at check-in and check-out
keep their own period of 1 year (D290, BR-F9-06).

## Why

- (Proposed) The CNIL's guidance on the geolocation of employees, to confirm in the France country pack:
  [CR-FR-211](../../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md).
- Personal data is kept no longer than needed:
  [CR-FR-052](../../../10-country-packs/france/data-protection/cr-fr-052-storage-limitation.md).

## Examples

| Case | Result |
|---|---|
| A live position of 2026-09-10; today is 2026-11-11 | Deleted |
| A check-in position of 2026-02-01 | Kept until 2027-02-01 (BR-F9-06) |
| The employee opens their position history | The last 2 months at most |
| An arrival time shown to a customer | Nothing kept (BR-F9-32) |

## Applies to

- [E-F9-32 Live position](../data/e-f09-32-live-position.md)
- [UC-F9-37](../use-cases/12-schedule-customer-requests/uc-f09-37-share-my-position-during-work.md)
- [REQ-T13-05](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-05-live-positions.md)

## Exceptions

None.

## Configurable

(Proposed) A company may set a shorter period, never a longer one.

## Open questions

None. The CNIL's guidance stays to read with the France country pack (above).

---

⬅️ [BR-F9-30](br-f09-30-live-position-team-option-working-hours.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F9-32 Who sees a person's position](br-f09-32-who-sees-a-position.md)
