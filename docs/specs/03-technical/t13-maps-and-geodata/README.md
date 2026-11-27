🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🗺️ T13 Maps and geodata

# 🗺️ T13 Maps and geodata

**Status:** ✅ specified

## Summary

Maps, plans and places for the whole suite, served from the company's own servers: map tiles, geocoding of every
address, routing and travel times, areas and outlines, live positions within the law, floor and venue plans, and the
scheduling engine that turns work requests into assignments. Maps appear on planning screens, as a layout of list views,
as mini-maps on record pages and as area maps on dashboards, in four domains, for planners and managers only (decided
by the owner on 2026-11-13, VD-18 to VD-20). Every part runs on open data and open-source software (D517), which
fits the sovereign objective of the [vision](../../00-vision/product/objectives.md).

## Scope

- Self-hosted map tiles (REQ-T13-01).
- Geocoding of every address, and routing with travel times (REQ-T13-02, REQ-T13-03).
- Areas and outlines: plots, zones, territories (REQ-T13-04).
- Live positions: ingest, pause, retention (REQ-T13-05).
- Map queries within the user's permissions and the map right (REQ-T13-06).
- The scheduling engine: eligibility, ranking, proposals, automatic mode (REQ-T13-07).
- Floor and venue plans (REQ-T13-08).

## Functional capabilities served

F9 HR and projects first (scheduling board, planning map, rounds, positions); also F16 (work requests, arrival time),
F6 (territories, visit planning), F7 (warehouse plans), F10 (restaurant floor), F11 (store locator), F12 (shop floor),
and the sectors SC01, SC02, SC04, SC05, SC06, SC07, SC10, SC13, SC15, SC16 (VD-19).

## Out of scope

- The map and plan components themselves: [C-17 Map](../../04-ux/design-system/components/c-17-map.md) and
  [C-18 Plan](../../04-ux/design-system/components/c-18-plan.md).
- The rights model: T2 (T13 asks it, REQ-T13-06).
- Reading documents for employees' attributes: T7 and F3.
- Vehicles' telematics feeds: connectors of T12.

## Contents

| | ID | Page | Status |
|---|---|---|---|
| 📌 |  | [Requirements](requirements/README.md) | ✅ |
| 🗃️ |  | [Data](data/README.md) | ✅ |
| 🖥️ |  | [Screens](screens/README.md) | ✅ |
| 🖼️ |  | [Images](images/README.md) | ✅ |

Architecture, interfaces, security, operations, errors, tests and open questions are written when the owner
has reviewed the requirements.

---

⬅️ [Connectors and scrapers](../t12-connectors-and-scrapers/README.md) · ⬆️ [Up](../README.md)

