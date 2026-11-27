🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🔧 [Decisions: F2 No-code configuration](README.md) ›
📜 D109 Shared and personal list views

# 📜 D109 Shared and personal list views

**Status:** ✅ decided

## Context

Whether list views are part of F2.

## Options

- Shared views by configurators and personal views.
- Personal views only.
- Shared views only.

## Choice

Configurators publish shared list views (columns, filters, sort, grouping) per role; every user can save personal views
on top.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Every list offers its shared views and the user's own. Amended by:
- [D486](../ux/d486-plain-words-filter-facets-with-counts-related-record-filters.md): every view has the
  plain-words filter, the facets with counts and the related-record filters, within the user's permissions;
- [D501](../ux/d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md): on a record type that has a
  place, a view can use the map layout;
- [D502](../ux/d502-records-on-a-map-for-planners-and-managers-only.md): only roles holding the map right see that
  layout
  [BR-F1-32](../../02-functional/f01-administration/business-rules/br-f01-32-map-right-for-planners-and-managers.md).

## Related

- [UC-F2-03](../../02-functional/f02-no-code-configuration/use-cases/01-configure-a-record-type/uc-f02-03-arrange-a-form.md)
- [E-F2-04 List view](../../02-functional/f02-no-code-configuration/data/e-f02-04-list-view.md)
- [Aggregated list view](../../04-ux/design-system/patterns/aggregated-list-view.md)

---

⬅️ [D108 Form layout options](d108-form-layout-options.md) · ⬆️ [Up](README.md) ·
➡️ [D110 Phone forms](d110-phone-forms.md)
