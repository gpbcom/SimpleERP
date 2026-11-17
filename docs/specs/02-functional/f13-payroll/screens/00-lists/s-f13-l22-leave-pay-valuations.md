🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L22 Leave pay valuations

# 🗂️ S-F13-L22 Leave pay valuations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-22 Leave pay valuation](../../data/e-f13-22-leave-pay-valuation.md) the user may
see: to find, filter, total and act on many leave pay valuations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Leave pay valuations, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "leave pay valuations" offers this view.
- **AI assistant:** "show the leave pay valuations that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Leave pay valuations    Payroll (plugin) › Leave pay valuations   [+ New]                                    |
| [count] [total maintained pay]   [chart: count by state, maintained pay stacked]                             |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMPLOYEE   STATE   LEAVE TAKEN   MAINTAINED PAY   ONE TENTH   KEPT   PAID BY         |
| employee          | [ ] ...                                                  Open >                          |
| leave taken       | [ ] ...                                                  Open >                          |
| paid by           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Employee | employee | link to the record | yes |
| State | state | badge: Computed, Paid, Adjusted | yes |
| Leave taken | leave taken | link to the record | yes |
| Maintained pay | maintained pay | amount, right-aligned | yes |
| One tenth | one tenth | amount, right-aligned | yes |
| Kept | kept | amount, right-aligned | yes |
| Paid by | paid by | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Computed, Paid, Adjusted | the visible rows (D488) |
| Employee | each linked employee | the visible rows (D488) |
| Leave taken | each linked leave taken | the visible rows (D488) |
| Paid by | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Leave pay valuations of a chosen leave taken, or of the leave takens that match a filter.
- From the other side: the leave takens that have leave pay valuations, or none.

## KPI strip

- Count of the visible rows.
- Total of maintained pay.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state, maintained pay stacked (VR-8); the Chart button turns the filtered list into a chart the user can pin to
their home screen (C-09).

## Saved views

- All.
- Mine: employee.
- Open: Computed, Adjusted.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New leave pay valuation | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the employee; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- paid by: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| employee | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| leave taken | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| maintained pay | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| one tenth | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| kept | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F13-26 Leave pay valuation](../08-deductions-savings-and-leave-pay/s-f13-26-leave-pay-valuation.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 leave pay valuations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no leave pay valuation the user may see yet, with the create action when allowed.
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
| Listed, U45, view Mine: employee | desktop | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l22-leave-pay-valuations-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l22-leave-pay-valuations-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Mine: employee | phone | ![Listed, U45, view Mine: employee, light](../../images/lists/s-f13-l22-leave-pay-valuations-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Mine: employee, dark](../../images/lists/s-f13-l22-leave-pay-valuations-u45-payroll-officer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Leave pay valuations](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md) |
| Flows | [FL-F13-08](../../flows/fl-f13-08-deductions-savings-and-leave-pay.md) |

## Open questions

None.

---

⬅️ [S-F13-L21 Profit-sharing years](s-f13-l21-profit-sharing-years.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L23 Agreement families](s-f13-l23-agreement-families.md)
