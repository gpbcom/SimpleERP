🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-15 Facet panel

# 🧩 C-15 Facet panel

**Status:** 🔄 draft (GH-2 step S4, from VD-03 / D486)

## Purpose

Lets users narrow an [aggregated list view](../patterns/aggregated-list-view.md) by ticking values, each with the number
of visible records that have it, and by related-record filters
[D486](../../../06-decisions/ux/d486-plain-words-filter-facets-with-counts-related-record-filters.md).

## Anatomy

```text
+---------------------------+
| FACETS            [Clear] |
| Stage                     |
| [x] Proposal          17  |
| [x] Negotiation       11  |
| [ ] Won                6  |
| Show 4 more               |
| Owner                     |
| [ ] Marie Dupont      15  |
| Eligible for              |
| [ ] Home visit: care   9  |
| Related records           |
| [ ] Customer has an       |
|     overdue invoice    4  |
+---------------------------+
```

1. **Header:** "Facets" and **Clear**, shown when a value is ticked.
2. **Facet groups:** one per facet field of the view card, 8 at most (rule VR-5 of the
   [plan](../../../../tickets/GH-2/resources/flowcharts-screens/PLAN.md#view-rules)): state, category, people and link
   fields. Each value has a box, its label and its count, counted on the visible rows only
   [D488](../../../06-decisions/ux/d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md).
3. **Show more:** (Proposed) a group shows 5 values, the rest behind "Show n more".
4. **Eligible for:** on the views where scheduling attributes apply, one value per request type or operation with
   required attributes; see the [pattern](../patterns/aggregated-list-view.md)
   [D511](../../../06-decisions/f09-hr-and-projects/d511-required-or-preferred-attributes-legal-ones-always-required.md).
5. **Related records:** filters on linked records, both ways ("customers with an overdue invoice", "invoices of a
   customer in Lyon"), rule VR-6.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-15-facet-panel-desktop-light.png) | ![Variants and states, dark](../images/c-15-facet-panel-desktop-dark.png) |

## Variants

- **Sidebar:** on a desktop and a tablet, at the left of the table.
- **Drawer:** on a phone, opened by "Facets" in the toolbar, with the result count and "Show n results" at the bottom
  ([D491](../../../06-decisions/ux/d491-on-a-phone-the-list-keeps-its-table-and-scrolls-sideways.md)).
- **Range facet:** (Proposed) for an amount or a date: preset ranges with counts ("Due in 7 days 9"), and "Custom".
- **Searchable facet:** (Proposed) a search field in a group with more than 20 values, such as people or customers.

## States

| State | Look |
|---|---|
| Loading | (Proposed) The groups with skeleton counts; boxes disabled until the counts arrive |
| Default | Values with their counts, none ticked |
| Value ticked | Box ticked, the value in `color-primary`; its chip appears in the toolbar |
| Zero count | (Proposed) Values with no visible record are hidden, unless ticked |
| Recounting | (Proposed) The counts dim while the server recounts; boxes stay usable |
| No facet | No facet field the user may read: the panel is not shown |
| Error | The counts are replaced by a dash and a retry link ([error message pattern](../patterns/error-messages.md)) |

## Tokens

`color-surface` panel on `color-surface-alt` page, `color-border` between groups, `color-primary` for a ticked value,
`color-text-muted` for counts ([Colours](../../visual-identity/colours.md)); group titles in `font-label`, values in
`font-body` or `font-body-compact` with the density of the role
([D42](../../../06-decisions/ux/d42-density-per-role.md)), counts in tabular figures
([Typography](../../visual-identity/typography.md)); `field-height` for the boxes' touch targets
([Tokens](../tokens.md)).

## Accessibility

- Each group is a set of checkboxes with its legend ("Stage"); each box reads its value and count ("Proposal, 17
  records").
- The new result count is announced politely after a box changes; the focus stays on the box.
- The drawer is a dialog: the focus moves into it, Escape closes it, and the focus returns to "Facets".
- A ticked value is shown by its box and its chip, never by colour alone.

## Do and don't

- Do count on the server, on the visible rows only
  [D488](../../../06-decisions/ux/d488-totals-facets-charts-ai-answers-and-exports-on-visible-rows-only.md),
  [Performance](../../../05-non-functional/performance.md).
- Do keep the facets the user ticked in their saved view
  ([D109](../../../06-decisions/f02-no-code-configuration/d109-list-views.md)).
- Don't offer a facet on a field the user may not read, and never show a count of hidden records.
- Don't show a planner the reason details of "Eligible for" that belong to HR: a category only
  [BR-F9-29](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-29-planners-see-eligibility-only.md).

## Used in

The [aggregated list view pattern](../patterns/aggregated-list-view.md), and so every list page; for example
[S-F16-14](../../../02-functional/f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## Open questions

None.

---

⬅️ [Timeline](c-14-timeline.md) · ⬆️ [Up](README.md) · ➡️ [KPI strip](c-16-kpi-strip.md)

