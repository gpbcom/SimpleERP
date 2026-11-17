🏠 [Specs](../../../README.md) › ⚙️ [Technical capabilities](../../README.md) ›
🗺️ [T13 Maps and geodata](../README.md) › 📌 [Requirements](README.md) ›
📌 REQ-T13-02 Geocoding of every address

# 📌 REQ-T13-02 Geocoding of every address

**Status:** 🔄 draft (GH-2 step S4b, from VD-18, VD-19 / D501)

## Statement

Every address saved on a record must be geocoded on the company's own servers into a position with its precision; a
person may place or move the pin by hand; a changed address is geocoded again.

Decided (D517): The national address base (BAN) for France, Nominatim on OpenStreetMap data elsewhere, both self-hosted.

## Why

A map, a travel time or an area search needs a position, and about 40 entities hold a place
([E-T13-01 Geocoded place](../data/e-t13-01-geocoded-place.md)). Sending addresses to an outside service would send
customers' and care recipients' homes outside the company.

Decided by the owner on 2026-11-13 (VD-18, VD-19). The sources named are decided (D517).

## Acceptance criteria

1. An address saved on any place-bearing record gets a geocoded place with its precision (house, street, town).
2. An address not found is marked "Not found" and listed for a person to place the pin.
3. A pin moved by hand keeps its position until the address changes.
4. An import of 10,000 addresses is geocoded in bulk without blocking the import.
5. No address leaves the company's servers unless an administrator chose an outside service.

## Measure

Decided (D517): Share of French addresses found at house precision: 95 % at least. One address within 300 ms; 10,000
addresses within 10 minutes.

## Priority

Must (Proposed)

## Capabilities served

F9, F16, F6, F11; every sector with places.

## Tests

Unit tests of the geocoder's contract; a reference set of 1,000 French addresses with known positions; a bulk import
test; a network capture.

## Open questions

None.

---

⬅️ [REQ-T13-01 Self-hosted map tiles](req-t13-01-self-hosted-tiles.md) · ⬆️ [Up](README.md) ·
➡️ [REQ-T13-03 Routing and travel times](req-t13-03-routing.md)
