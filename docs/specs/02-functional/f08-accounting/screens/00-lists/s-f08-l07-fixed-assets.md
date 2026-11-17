🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L07 Fixed assets

# 🗂️ S-F8-L07 Fixed assets

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U40 Farmer](../../../../01-users/personas/u40-farmer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U54: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F8-07 Fixed asset](../../data/e-f08-07-fixed-asset.md) the user may see: to find,
filter, total and act on many fixed assets at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Fixed assets, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "fixed assets" offers this view.
- **AI assistant:** "show the fixed assets that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Fixed assets    Accounting › Fixed assets   [+ New]                                                          |
| [count] [total value] [new this month]   [chart: count by state, value stacked]                              |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   VALUE   DURATION                                                      |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Running, Disposed, Sold | yes |
| Value | value | amount, right-aligned | yes |
| Duration | duration | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Running, Disposed, Sold | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: fixed assets link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of value.
- New this month, by duration.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, value stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New fixed asset | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- duration: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-08 Fixed assets](../04-tax-assets-and-analytics/s-f08-08-fixed-assets.md).

The records also show on: [S-F8-22 Grants](../07-client-money-grants-and-non-profits/s-f08-22-grants.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 fixed assets of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no fixed asset the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f08-l07-fixed-assets-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f08-l07-fixed-assets-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u05-accounting-phone-dark.png) |
| Listed, U31, view All | desktop | ![Listed, U31, view All, light](../../images/lists/s-f08-l07-fixed-assets-u31-treasurer-desktop-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u31-treasurer-desktop-dark.png) |
| Listed, U31, view All | phone | ![Listed, U31, view All, light](../../images/lists/s-f08-l07-fixed-assets-u31-treasurer-phone-light.png) | ![Listed, U31, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u31-treasurer-phone-dark.png) |
| Listed, U40, view All | desktop | ![Listed, U40, view All, light](../../images/lists/s-f08-l07-fixed-assets-u40-farmer-desktop-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u40-farmer-desktop-dark.png) |
| Listed, U40, view All | phone | ![Listed, U40, view All, light](../../images/lists/s-f08-l07-fixed-assets-u40-farmer-phone-light.png) | ![Listed, U40, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u40-farmer-phone-dark.png) |
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f08-l07-fixed-assets-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f08-l07-fixed-assets-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f08-l07-fixed-assets-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Fixed assets](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U31](../../../../04-ux/views/u31-treasurer/workspace.md), [U40](../../../../04-ux/views/u40-farmer/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F8-04](../../flows/fl-f08-04-tax-assets-and-analytics.md), [FL-F8-07](../../flows/fl-f08-07-client-money-grants-and-non-profits.md) |

## Open questions

None.

---

⬅️ [S-F8-L06 Tax returns](s-f08-l06-tax-returns.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L08 Accounting budgets](s-f08-l08-accounting-budgets.md)
