🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L31 Delegation hours

# 🗂️ S-F13-L31 Delegation hours

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-31 Delegation hours](../../data/e-f13-31-delegation-hours.md) the user may see: to
find, filter, total and act on many delegation hours at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Delegation hours, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "delegation hours" offers this view.
- **AI assistant:** "show the delegation hours that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Delegation hours    Payroll (plugin) > Delegation hours   [+ New]                                            |
| [count] [Held] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| mandate           | [ ] PERSON   MANDATE   MONTH   MONTHLY CRED   HOURS USED   STATE                         |
| month             | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Person | person | text | yes |
| Mandate | mandate | text | yes |
| Month | month | text | yes |
| Monthly credit | monthly credit | text | yes |
| Hours used | hours used | text | yes |
| State | state | badge: Recorded, Confirmed, Held, Refused, Paid | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Mandate | each value | the visible rows (D488) |
| Month | each value | the visible rows (D488) |
| State | Recorded, Confirmed, Held, Refused, Paid | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Hours whose person has a pay input of the month.
- From the other side: the pay inputs fed by delegation hours, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Held.
- New this month, by month.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New delegation hours | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| person | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| held reason | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F13-31](../10-special-contracts-and-outsourcing/s-f13-31-staff-representatives.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 delegation hours of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no delegation hours the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Not drawn yet: step S8 draws them from this page, one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f13-l31-delegation-hours-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f13-l31-delegation-hours-u06-hr-desktop-dark.png) |
| Listed, U45, view All | desktop | ![Listed, U45, view All, light](../../images/lists/s-f13-l31-delegation-hours-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l31-delegation-hours-u45-payroll-officer-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f13-l31-delegation-hours-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f13-l31-delegation-hours-u06-hr-phone-dark.png) |
| Listed, U45, view All | phone | ![Listed, U45, view All, light](../../images/lists/s-f13-l31-delegation-hours-u45-payroll-officer-phone-light.png) | ![Listed, U45, view All, dark](../../images/lists/s-f13-l31-delegation-hours-u45-payroll-officer-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Delegation hours](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md) |
| Flows | [FL-F13-10](../../flows/fl-f13-10-special-contracts-and-outsourcing.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-F13-L30 Payroll handovers](s-f13-l30-payroll-handovers.md) · ⬆️ [Up](README.md)
