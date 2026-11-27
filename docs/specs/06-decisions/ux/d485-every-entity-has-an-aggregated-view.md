🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎨 [Decisions: Users and UX](README.md) ›
📜 D485 Every entity has an aggregated view

# 📜 D485 Every entity has an aggregated view

**Status:** 🔄 draft (GH-2 step S4, from VD-02 / D485)

## Context

Which entities get an aggregated list view. On 2026-11-12 at about 22:30 the specs held 747 entities: 662 business
records and 85 settings or technical records ([view
cards](../../../tickets/GH-2/resources/flowcharts-screens/view-cards/README.md)).

## Options

- Business records only.
- Business records, and the technical records as admin lists.
- Every entity.

## Choice

Every entity has an aggregated list view, settings and technical records included.

## Decided by

The owner, on 2026-11-12, in the interview on aggregated views, wording and state screens ([interview
record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md), answer 2).

## Consequences

- About 747 list pages (the count moves; step S0 of the
  [plan](../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md) measures it again).
- Settings and technical records are admin lists ([D494](d494-settings-and-technical-records-as-admin-lists.md)); 35
  technical entities had no screen at all ([screenless
  entities](../../../tickets/GH-2/resources/flowcharts-screens/screenless/README.md)).
- (Proposed) A check fails on an entity without its list page (`check_views.py`, step S5 of the plan).

## Related

- [Aggregated list view pattern](../../04-ux/design-system/patterns/aggregated-list-view.md)
- [View cards](../../../tickets/GH-2/resources/flowcharts-screens/view-cards/README.md)
- [D484 Aggregated list view per record type and persona
  workspaces](d484-aggregated-list-view-per-record-type-and-persona-workspaces.md)
- [D494 Settings and technical records as admin lists](d494-settings-and-technical-records-as-admin-lists.md)
- [Interview record](../../../tickets/GH-2/resources/flowcharts-screens/INTERVIEW.md)

---

⬅️ [D484](d484-aggregated-list-view-per-record-type-and-persona-workspaces.md) · ⬆️ [Up](README.md) ·
➡️ [D486](d486-plain-words-filter-facets-with-counts-related-record-filters.md)
