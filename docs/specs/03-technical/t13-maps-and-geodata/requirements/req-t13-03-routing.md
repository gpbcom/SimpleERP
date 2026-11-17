🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-03 Routing and travel times

# 📌 REQ-T13-03 Routing and travel times

**Status:** 🔄 draft (GH-2 step S4b, from VD-18, VD-32 / D501, D514)

## Statement

The platform must compute, on its own servers, the distance and travel time between places for a profile of travel
(car, van, truck, bicycle, foot), as single routes drawn on the map and as matrices for the scheduling engine.

Decided (D517): OSRM or Valhalla on the OpenStreetMap road graph.

## Why

Travel and lateness are objectives of scheduling (VD-32), the route optimiser already places visits by travel time
[BR-F9-22](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-22-rounds-respect-travel-skills-continuity-and-working-time.md),
and the planning map draws routes (VD-18).

Decided by the owner on 2026-11-13 (VD-18, VD-32). The software named is decided (D517).

## Acceptance criteria

1. A route between two to 50 stops returns its distance, time, legs and line.
2. A travel-time matrix of 200 places by 200 places returns for the engine.
3. A truck profile avoids roads closed to trucks when the road data says so.
4. A route whose stop or road data changed is marked "Outdated" and computed again when next read.

## Measure

Decided (D517): A route within 200 ms; a 200 by 200 matrix within 2 seconds. Travel times within 15 % of the times
driven,
measured on a sample of rounds.

## Priority

Must (Proposed)

## Capabilities served

F9, F6, F16; sectors SC01, SC04, SC07, SC09, SC10, SC15.

## Tests

Unit tests on a small road graph with known answers; load tests of the matrix; a comparison with the check-in times of
past rounds.

## Open questions

None.

---

⬅️ [REQ-T13-02 Geocoding of every address](req-t13-02-geocoding.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-04 Areas and outlines (plots, zones)](req-t13-04-areas-and-outlines.md)
