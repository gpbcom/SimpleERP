🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💼 [SC03 Services](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Services menu](README.md) › 🗂️ S-SC03-L01 Engagements

# 🗂️ S-SC03-L01 Engagements

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U24 Engagement manager](../../../../01-users/personas/u24-engagement-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U36: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC03-01 Engagement](../../data/e-sc03-01-engagement.md) the user may see: to find,
filter, total and act on many engagements at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Services › Engagements, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "engagements" offers this view.
- **AI assistant:** "show the engagements that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Engagements    Services › Engagements   [+ New]                                                              |
| [count] [total budget] [new this month]   [chart: count by state, budget stacked]                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] REFERENCE   STATE   BUDGET   MODEL                                                   |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Reference | reference | label | yes |
| State | state | badge: PreSales, Running, Closed | yes |
| Budget | budget | amount, right-aligned | yes |
| Model | model | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | PreSales, Running, Closed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: engagements link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of budget.
- New this month, by model.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, budget stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: PreSales, Running.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New engagement | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- model: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC03-10 Engagement margin](../04-bill-and-recognise/s-sc03-10-engagement-margin.md).

The records also show on: [S-SC03-15 Engagement assistant](../03-deliver-and-record/s-sc03-15-engagement-assistant.md),
[S-SC03-01 Statement of work](../01-win-and-price/s-sc03-01-statement-of-work.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 engagements of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no engagement the user may see yet, with the create action when allowed.
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
| Listed, U24, view Open: PreSales, Running | desktop | ![Listed, U24, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u24-engagement-manager-desktop-light.png) | ![Listed, U24, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u24-engagement-manager-desktop-dark.png) |
| Listed, U24, view Open: PreSales, Running | phone | ![Listed, U24, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u24-engagement-manager-phone-light.png) | ![Listed, U24, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u24-engagement-manager-phone-dark.png) |
| Listed, U03, view Open: PreSales, Running | desktop | ![Listed, U03, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u03-sales-desktop-light.png) | ![Listed, U03, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u03-sales-desktop-dark.png) |
| Listed, U03, view Open: PreSales, Running | phone | ![Listed, U03, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u03-sales-phone-light.png) | ![Listed, U03, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u03-sales-phone-dark.png) |
| Listed, U09, view Open: PreSales, Running | desktop | ![Listed, U09, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u09-customer-desktop-light.png) | ![Listed, U09, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: PreSales, Running | phone | ![Listed, U09, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u09-customer-phone-light.png) | ![Listed, U09, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u09-customer-phone-dark.png) |
| Listed, U13, view Open: PreSales, Running | desktop | ![Listed, U13, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u13-owner-desktop-light.png) | ![Listed, U13, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u13-owner-desktop-dark.png) |
| Listed, U13, view Open: PreSales, Running | phone | ![Listed, U13, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u13-owner-phone-light.png) | ![Listed, U13, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u13-owner-phone-dark.png) |
| Listed, U16, view Open: PreSales, Running | desktop | ![Listed, U16, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: PreSales, Running | phone | ![Listed, U16, view Open: PreSales, Running, light](../../images/lists/s-sc03-l01-engagements-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: PreSales, Running, dark](../../images/lists/s-sc03-l01-engagements-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Services › Engagements](README.md) |
| Workspaces | [U24](../../../../04-ux/views/u24-engagement-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-SC03-01](../../flows/fl-sc03-01-win-and-price.md), [FL-SC03-03](../../flows/fl-sc03-03-deliver-and-record.md), [FL-SC03-04](../../flows/fl-sc03-04-bill-and-recognise.md) |

## Open questions

None.

---

⬅️ [S-SC03-19 Answer library](../06-staffing-agencies-and-certification/s-sc03-19-answer-library.md) ·
⬆️ [Up](README.md) · ➡️ [S-SC03-L02 Statement of works](s-sc03-l02-statement-of-works.md)
