🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-06 Map queries respect permissions

# 📌 REQ-T13-06 Map queries respect permissions

**Status:** 🔄 draft (GH-2 step S4b, from VD-05, VD-20, VD-21 / D488, D502, D503)

## Statement

Every map, plan, cluster, area total and route must show only the records and fields the user may see, and only to a
user whose role holds the map right; people's positions only to the people allowed to see them.

## Why

Records on a map are for planners and managers only (VD-20,
[BR-F1-32](../../../02-functional/f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md));
people's positions for their planner or dispatcher, their manager and, as an arrival time, the customer (VD-21,
[BR-F9-32](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-32-who-sees-a-position.md)); counts and
charts use visible rows only (VD-05).

Decided by the owner on 2026-11-12 (VD-05) and 2026-11-13 (VD-20, VD-21).

## Acceptance criteria

1. A user without the map right gets no map layout, mini-map or area map; the same records show as lists and
   addresses.
2. A cluster's count, an area's total and a heat map use only the rows the user may see; nothing hints that other
   records exist.
3. A hidden field never shows in a map's label, tooltip or filter.
4. A live position shows only to the people BR-F9-32 names.
5. The tile server holds no business records; records reach the map only through the API, filtered by T2.
6. The public store locator (F11) and the arrival time are the only maps without the map right.

## Measure

Leaks found by the permission test suite: 0.

## Priority

Must

## Capabilities served

F1, F9, F16 and every capability with a map; T2.

## Tests

The permission test suite run on every map endpoint with each role of the examples; a test per hidden field; API
tests of the position endpoints with every role.

## Open questions

None.

---

⬅️ [REQ-T13-05 Live positions: ingest, pause, retention](req-t13-05-live-positions.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-07 Scheduling engine](req-t13-07-scheduling-engine.md)
