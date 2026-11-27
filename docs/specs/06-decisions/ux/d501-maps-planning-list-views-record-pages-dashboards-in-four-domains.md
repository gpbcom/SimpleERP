🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D501 Maps: planning, list views, record pages, dashboards, in four domains

# 📜 D501 Maps: planning, list views, record pages, dashboards, in four domains

**Status:** ✅ decided

## Context

The owner asked on 2026-11-13 where maps should be and who can see them. The specs had no geographic map: 83 entities
held a place field, about 40 of them real places, and [D101](../f02-no-code-configuration/d101-custom-field-types.md)
already offers a location field type; the aggregated views had no map layout
([D486](d486-plain-words-filter-facets-with-counts-related-record-filters.md)). The findings are in maps and
eligibility (the owner's interview notes of 2026-11 for the specifications, not kept in the repository).

## Options

The first proposal of 2026-11-13 (maps and
eligibility (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)):
- geographic maps for the sectors and capabilities of high or very high value, plus F6;
- a map layout on the list views of place-bearing entities;
- one plan component for floors and venues.

- The interview record keeps the owner's answer, not every option the question offered.

## Choice

Maps appear on planning and dispatch screens, as a map layout on the list views of record types that hold a place, as a
mini-map on record pages and as area maps on dashboards, in four domains:
- **field and mobility:** SC07, SC04, SC01, F9 field work, F16 interventions;
- **land and property:** SC13 plots, SC10 properties;
- **sales and retail:** F6 territories, SC02 stores, F11 store locator, SC15 zones;
- **floor and venue plans:** F7 and SC15 warehouses, SC06 rooms, F10 floor, SC16 venues, F12 and SC05 shop floor.

## Decided by

The owner, on 2026-11-13, in the interview on maps, degrees and scheduling (interview
record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository), VD-18 and VD-19).

## Consequences

- [D486](d486-plain-words-filter-facets-with-counts-related-record-filters.md) is amended: the views of place-bearing
  record types offer a map layout, to the roles of [D502](d502-records-on-a-map-for-planners-and-managers-only.md) only.
- New components [C-17 Map](../../04-ux/design-system/components/c-17-map.md) and [C-18
  Plan](../../04-ux/design-system/components/c-18-plan.md).
- New technical capability [T13 Maps and geodata](../../03-technical/t13-maps-and-geodata/README.md): self-hosted tiles,
  geocoding, routing, areas and outlines, floor and venue plans.
- [E-F2-04 List view](../../02-functional/f02-no-code-configuration/data/e-f02-04-list-view.md) saves a map layout
  (change note).
- About 15 to 20 map and planning screens, such as [S-F9-33 Planning
  map](../../02-functional/f09-hr-and-projects/screens/12-schedule-customer-requests/s-f09-33-planning-map.md), and the
  map layout of about 40 list views.

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [C-17 Map](../../04-ux/design-system/components/c-17-map.md)
- [C-18 Plan](../../04-ux/design-system/components/c-18-plan.md)
- [T13 Maps and geodata](../../03-technical/t13-maps-and-geodata/README.md)
- [E-F2-04 List view](../../02-functional/f02-no-code-configuration/data/e-f02-04-list-view.md)
- [D486 Plain-words filter, facets with counts, related-record
  filters](d486-plain-words-filter-facets-with-counts-related-record-filters.md)
- [D502 Records on a map for planners and managers only](d502-records-on-a-map-for-planners-and-managers-only.md)
- Interview record (the owner's interview notes of 2026-11 for the specifications, not kept in the repository)

---

⬅️ [D500 Images live in the specs folders](d500-images-live-in-the-specs-folders.md) · ⬆️ [Up](README.md) ·
➡️ [D502 Records on a map for planners and managers only](d502-records-on-a-map-for-planners-and-managers-only.md)
