🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-05 Live positions: ingest, pause, retention

# 📌 REQ-T13-05 Live positions: ingest, pause, retention

**Status:** 🔄 draft (GH-2 step S4b, from VD-21, VD-22, VD-23 / D503, D504, D505)

## Statement

The platform must take in an employee's live position only during working hours, only for a team whose live-position
option is on, stop at once when the employee pauses, record nothing outside working hours, compute no speed or
performance from it, show it only to the people allowed, and erase each position at its erase date.

## Why

Live positions are an option for drivers (SC07) and carers (SC04) only, with a stated purpose and an impact
assessment, off outside working hours, never for speed or performance; the employee sees what is shared and may pause
(VD-21 to VD-23;
[CR-FR-211](../../../10-country-packs/france/data-protection/cr-fr-211-live-geolocation-of-employees.md)).

Decided by the owner on 2026-11-13 (VD-21 to VD-23). The retention of 2 months at most is decided (D517).

## Acceptance criteria

1. A position sent outside working hours, while paused, or for a team without the option is refused and not stored.
2. A pause on the phone stops the sending within 5 seconds and the planning map shows "paused", not the last place.
3. No field, report or API returns a speed, a heading or a score computed from positions.
4. Each position is erased at its erase date; a nightly check finds none older.
5. The customer receives an arrival time during the visit's window only; no position of the employee reaches them.
6. Every view of a person's positions by someone other than the employee is logged (T3).

## Measure

Decided (D517): Positions older than the retention found by the nightly check: 0. Positions stored outside working
hours:
0. Battery use of the phone app under 5 % an hour while sharing.

## Priority

Must (Proposed)

## Capabilities served

F9, F16; sectors SC04, SC07.

## Tests

API tests sending positions at every boundary (hours, pause, option off); a retention test with a moved clock; a
search of the API schema and reports for any speed field; phone tests on Android and iOS.

## Open questions

None. The CNIL guidance is read with the France country pack (CR-FR-211).

---

⬅️ [REQ-T13-04 Areas and outlines (plots, zones)](req-t13-04-areas-and-outlines.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-06 Map queries respect permissions](req-t13-06-map-queries-respect-permissions.md)
