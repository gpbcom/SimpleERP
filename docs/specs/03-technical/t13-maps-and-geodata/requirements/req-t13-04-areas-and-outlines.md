🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-04 Areas and outlines (plots, zones)

# 📌 REQ-T13-04 Areas and outlines (plots, zones)

**Status:** 🔄 draft (GH-2 step S4b, from VD-18, VD-19 / D501)

## Statement

The platform must store areas as outlines (plots, delivery zones, territories, store zones), draw them, and answer
spatial questions: which records are within an area, which area holds a place, the nearest records to a place, and
totals by area for dashboards.

Decided (D517): A spatial extension of the company's database; IGN's cadastre parcels imported for plots in France.

## Why

The land and property domain needs plot outlines (SC13, SC10), sales and retail need territories and zones (F6, SC02,
SC15), and dashboards need area maps (VD-18, VD-19).

Decided by the owner on 2026-11-13 (VD-18, VD-19). The software and data named are decided (D517).

## Acceptance criteria

1. An outline drawn or imported is checked (closed, not crossing itself) and its surface is computed.
2. A list view filtered "within this area" returns only the records inside it.
3. An area map on a dashboard shows totals per area, computed on visible records only (REQ-T13-06).
4. (Proposed) A plot is created from a cadastre parcel by picking it on the map.

## Measure

Decided (D517): An "within area" filter on 100,000 records within 1 second. Surfaces within 1 % of the cadastre's.

## Priority

Should (Proposed)

## Capabilities served

F6, F23; sectors SC02, SC10, SC13, SC15.

## Tests

Unit tests of the geometry checks; filter tests on a seeded set of records with known areas; a dashboard test with two
roles.

## Open questions

None.

---

⬅️ [REQ-T13-03 Routing and travel times](req-t13-03-routing.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-05 Live positions: ingest, pause, retention](req-t13-05-live-positions.md)
