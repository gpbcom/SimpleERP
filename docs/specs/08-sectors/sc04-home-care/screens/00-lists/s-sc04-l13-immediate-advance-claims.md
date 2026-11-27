🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Home care menu](README.md) › 🗂️ S-SC04-L13 Immediate advance claims

# 🗂️ S-SC04-L13 Immediate advance claims

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC04-13 Immediate advance claim](../../data/e-sc04-13-immediate-advance-claim.md) the
user may see: to find, filter, total and act on many immediate advance claims at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Home care › Immediate advance claims, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "immediate advance claims" offers this view.
- **AI assistant:** "show the immediate advance claims that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Immediate advance claims    Home care › Immediate advance claims   [+ New]                                   |
| [count] [total amount] [Refused] [new this month]   [chart: count by state, amount stacked]                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] IMMEDIATE AD   CLIENT   AMOUNT   SENT ON   VALIDATED ON   PAID ON   STATE            |
| client            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Immediate advance claim | title | text | yes |
| Client | client | person's name | yes |
| Amount | amount | amount, right-aligned | yes |
| Sent on | sent on | date | yes |
| Validated on | validated on | date | yes |
| Paid on | paid on | date | yes |
| State | state | badge: Sent, Refused, Validated, Cancelled, Paid | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sent, Refused, Validated, Cancelled, Paid | the visible rows (D488) |
| Client | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Immediate advance claims of a chosen care invoice, or of the care invoices that match a filter.
- From the other side: the care invoices that have immediate advance claims, or none.
- Immediate advance claims of a chosen care recipient, or of the care recipients that match a filter.
- From the other side: the care recipients that have immediate advance claims, or none.

## KPI strip

- Count of the visible rows.
- Total of amount.
- Needs attention: count in the state Refused.
- New this month, by sent on.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
home screen (C-09).

## Saved views

- All.
- Open: Sent, Refused, Validated.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New immediate advance claim | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
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

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| client | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC04-10 Immediate advance](../04-bill-and-fund/s-sc04-10-immediate-advance.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 immediate advance claims of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no immediate advance claim the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc04-l13-immediate-advance-claims-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc04-l13-immediate-advance-claims-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc04-l13-immediate-advance-claims-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc04-l13-immediate-advance-claims-u05-accounting-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc04-l13-immediate-advance-claims-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc04-l13-immediate-advance-claims-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc04-l13-immediate-advance-claims-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc04-l13-immediate-advance-claims-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Home care › Immediate advance claims](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-SC04-04](../../flows/fl-sc04-04-bill-and-fund.md) |

## Open questions

None.

---

⬅️ [S-SC04-L12 Activity reports](s-sc04-l12-activity-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-L14 Residents](s-sc04-l14-residents.md)
