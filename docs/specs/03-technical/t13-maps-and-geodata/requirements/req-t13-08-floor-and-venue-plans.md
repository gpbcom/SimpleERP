🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-08 Floor and venue plans

# 📌 REQ-T13-08 Floor and venue plans

**Status:** ✅ specified

## Statement

The platform must store plans of the inside of buildings (floors, rooms, warehouse bins, restaurant tables, seats,
venues, work centres), place records on them, and draw them with their records' states, within the same rights as
maps.

## Why

The fourth domain of maps is floor and venue plans: F7 and SC15 warehouses, SC06 rooms, F10 floor, SC16 venues, F12
and SC05 shop floor (VD-19). The seat map of E-F5-11 becomes one of their uses.

Decided by the owner on 2026-11-13 (VD-18, VD-19).

## Acceptance criteria

1. A plan is drawn or imported, and each of its places is linked to one record (a bin, a room, a table, a seat).
2. The plan shows each place's state from its record (free, taken, to clean, blocked).
3. A user without the map right sees the same records as lists.
4. A plan imported from an SVG or DXF drawing keeps its scale.

## Measure

Decided (D517): A plan of 5,000 places drawn within 1 second.

## Priority

Should

## Capabilities served

F5, F7, F10, F12; sectors SC05, SC06, SC15, SC16.

## Tests

Unit tests of the place-to-record links; a drawing test on a plan of 5,000 places; a permission test with two
roles.

## Open questions

None.

---

⬅️ [REQ-T13-07 Scheduling engine](req-t13-07-scheduling-engine.md) · ⬆️ [Up](README.md)
