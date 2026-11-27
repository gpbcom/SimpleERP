🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Accounting menu](README.md) ›
🗂️ S-F8-L10 Fiscal periods

# 🗂️ S-F8-L10 Fiscal periods

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U04, U31: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F8-10 Fiscal period](../../data/e-f08-10-fiscal-period.md) the user may see: to find,
filter, total and act on many fiscal periods at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Accounting › Fiscal periods, in the capability's menu (D495).
- **Workspaces:** 4 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "fiscal periods" offers this view.
- **AI assistant:** "show the fiscal periods that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Fiscal periods    Accounting › Fiscal periods   [+ New]                                                      |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] YEAR   STATE                                                                         |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Year | year | date | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: fiscal periods link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by year.

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
| New fiscal period | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F8-01 Books setup](../01-set-up-and-post/s-f08-01-books-setup.md).

The records also show on: [S-F8-10 Closing](../05-close-report-and-consolidate/s-f08-10-closing.md),
[S-F8-25 Annual accounts](../08-year-end-duties/s-f08-25-annual-accounts.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 fiscal periods of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no fiscal period the user may see yet, with the create action when allowed.
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
| Listed, U08, view All | desktop | ![Listed, U08, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u08-external-accountant-desktop-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view All | phone | ![Listed, U08, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u08-external-accountant-phone-light.png) | ![Listed, U08, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u08-external-accountant-phone-dark.png) |
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u05-accounting-phone-dark.png) |
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u07-administrator-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f08-l10-fiscal-periods-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f08-l10-fiscal-periods-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Accounting › Fiscal periods](README.md) |
| Workspaces | [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F12-05](../../../f12-manufacturing/flows/fl-f12-05-subcontracting-and-costs.md), [FL-F12-13](../../../f12-manufacturing/flows/fl-f12-13-energy-passport-and-work-in-progress.md), [FL-F15-05](../../../f15-legal-assistant/flows/fl-f15-05-duties-and-records.md), [FL-F23-07](../../../f23-what-if-simulation/flows/fl-f23-07-accuracy-and-drivers.md), [FL-F8-01](../../flows/fl-f08-01-set-up-and-post.md), [FL-F8-04](../../flows/fl-f08-04-tax-assets-and-analytics.md), [FL-F8-05](../../flows/fl-f08-05-close-report-and-consolidate.md), [FL-F8-08](../../flows/fl-f08-08-year-end-duties.md), [FL-F8-09](../../flows/fl-f08-09-pay-analyse-and-report.md), [FL-F9-08](../../../f09-hr-and-projects/flows/fl-f09-08-hr-duties.md), [FL-SC08-06](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-06-accounts-and-data.md) |

## Open questions

None.

---

⬅️ [S-F8-L09 Expense claims](s-f08-l09-expense-claims.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L11 Consolidation groups](s-f08-l11-consolidation-groups.md)
