🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-01 Self-hosted map tiles

# 📌 REQ-T13-01 Self-hosted map tiles

**Status:** ✅ specified

## Statement

Every map and plan must be drawn from tiles served by the company's own servers, built from open data, with the data's
attribution shown; no outside tile service is called unless an administrator chooses one.

Decided (D517): Vector tiles built from OpenStreetMap, served by an open-source tile server next to the platform.

## Why

Maps appear on planning screens, list views, record pages and dashboards in four domains (VD-18, VD-19). Calling an
outside tile service would send every viewed area, and so the places of customers and staff, outside the company; the
vision asks for every part to run on the operator's servers ([objectives](../../../00-vision/product/objectives.md)).

Decided by the owner on 2026-11-13 (VD-18, VD-19). The technology named is decided (D517).

## Acceptance criteria

1. With outgoing traffic blocked, every map of the suite draws its base layer.
2. No request from a browser showing a map leaves for a domain other than the platform's, unless an administrator chose
   an outside tile service.
3. The attribution of each source (E-T13-04) shows on every map.
4. A tile update replaces the previous version without a break in service.

## Measure

Decided (D517): Share of map views drawn with no outside call: 100 %. Tiles of a city zoom level served within 200 ms at
the 95th percentile.

## Priority

Must

## Capabilities served

F9, F16, F6, F7, F10, F11, F12; sectors SC01, SC02, SC04, SC05, SC06, SC07, SC10, SC13, SC15, SC16.

## Tests

A browser test with outgoing traffic blocked; a network capture listing every domain a map page calls; a load test of
the tile server.

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [REQ-T13-02 Geocoding of every address](req-t13-02-geocoding.md)
