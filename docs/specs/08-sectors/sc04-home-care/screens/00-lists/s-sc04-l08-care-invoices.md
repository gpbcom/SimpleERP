🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Home care menu](README.md) › 🗂️ S-SC04-L08 Care invoices

# 🗂️ S-SC04-L08 Care invoices

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC04-08 Care invoice](../../data/e-sc04-08-care-invoice.md) the user may see: to find,
filter, total and act on many care invoices at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Home care › Care invoices, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "care invoices" offers this view.
- **AI assistant:** "show the care invoices that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Care invoices    Home care › Care invoices   [+ New]                                                         |
| [count] [total amount]   [chart: count by state, amount stacked]                                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PAYER   STATE   AMOUNT                                                               |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Payer | payer | link to the record | yes |
| State | state | badge: Sent, Issued | yes |
| Amount | amount | amount, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sent, Issued | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: care invoices link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Total of amount.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, amount stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to their
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
| New care invoice | header | the personas whose roles may create it | the record's own page (Row opens) |
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

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC04-08 Billing](../04-bill-and-fund/s-sc04-08-billing.md).

The records also show on: [S-SC04-10 Immediate advance](../04-bill-and-fund/s-sc04-10-immediate-advance.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 care invoices of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no care invoice the user may see yet, with the create action when allowed.
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
| Listed, U05, view All | desktop | ![Listed, U05, view All, light](../../images/lists/s-sc04-l08-care-invoices-u05-accounting-desktop-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u05-accounting-desktop-dark.png) |
| Listed, U05, view All | phone | ![Listed, U05, view All, light](../../images/lists/s-sc04-l08-care-invoices-u05-accounting-phone-light.png) | ![Listed, U05, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u05-accounting-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-sc04-l08-care-invoices-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-sc04-l08-care-invoices-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u25-care-coordinator-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc04-l08-care-invoices-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u09-customer-desktop-dark.png) |
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc04-l08-care-invoices-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc04-l08-care-invoices-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Home care › Care invoices](README.md) |
| Workspaces | [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F6-07](../../../../02-functional/f06-customers-and-sales/flows/fl-f06-07-special-invoicing.md), [FL-SC04-04](../../flows/fl-sc04-04-bill-and-fund.md) |

## Open questions

None.

---

⬅️ [S-SC04-L07 Care incidents](s-sc04-l07-care-incidents.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-L09 Tax-credit certificates](s-sc04-l09-tax-credit-certificates.md)
