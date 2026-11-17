🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Competitive analysis menu](README.md) › 🗂️ S-F17-L18 Price suggestions

# 🗂️ S-F17-L18 Price suggestions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F17-18 Price suggestion](../../data/e-f17-18-price-suggestion.md) the user may see: to
find, filter, total and act on many price suggestions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Competitive analysis › Price suggestions, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "price suggestions" offers this view.
- **AI assistant:** "show the price suggestions that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Price suggestions    Competitive analysis › Price suggestions   [+ New]                                      |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PRODUCT   STATUS   FROM   EVIDENCE                                                   |
| product           | [ ] ...                                                  Open >                          |
| evidence          | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Product | product | link to the record | yes |
| Status | status | badge | yes |
| From | from | date | yes |
| Evidence | evidence | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Proposed, Approved, Refused, Applied | the visible rows (D488) |
| Product | each linked product | the visible rows (D488) |
| Evidence | each value | the visible rows (D488) |
| Status | Proposed, Approved, Refused, Applied | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Price suggestions of a chosen product, or of the products that match a filter.
- From the other side: the products that have price suggestions, or none.

## KPI strip

- Count of the visible rows.
- New this month, by from.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New price suggestion | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- from: editable in its cell unless the record's state locks it.
- evidence: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F17-23 Price suggestions](../06-price-intelligence/s-f17-23-price-suggestions.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 price suggestions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no price suggestion the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Drawn in step S8 (36k) from this page: one row per persona and device for each state of the view, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f17-l18-price-suggestions-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l18-price-suggestions-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f17-l18-price-suggestions-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l18-price-suggestions-u13-owner-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f17-l18-price-suggestions-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l18-price-suggestions-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f17-l18-price-suggestions-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l18-price-suggestions-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Competitive analysis › Price suggestions](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F17-06](../../flows/fl-f17-06-price-intelligence.md) |

## Open questions

None.

---

⬅️ [S-F17-L17 Price indexes](s-f17-l17-price-indexes.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-L19 Data cost lines](s-f17-l19-data-cost-lines.md)
