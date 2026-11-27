🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💶 [F13 Payroll (plugin)](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Payroll (plugin) menu](README.md) ›
🗂️ S-F13-L09 Social declarations

# 🗂️ S-F13-L09 Social declarations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U45 Payroll officer](../../../../01-users/personas/u45-payroll-officer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U43 Event producer](../../../../01-users/personas/u43-event-producer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F13-09 Social declaration](../../data/e-f13-09-social-declaration.md) the user may see:
to find, filter, total and act on many social declarations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Payroll (plugin) › Social declarations, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "social declarations" offers this view.
- **AI assistant:** "show the social declarations that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Social declarations    Payroll (plugin) › Social declarations   [+ New]                                      |
| [count] [Late] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| kind              | [ ] PERIOD   STATE   DUE   KIND                                                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Period | period | link to the record | yes |
| State | state | badge: Accepted, Filed, Returned, Late, Rejected | yes |
| Due | due | link to the record | yes |
| Kind | kind | link to the record | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Kind | each linked kind | the visible rows (D488) |
| State | Accepted, Filed, Returned, Late, Rejected | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: social declarations link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Late.
- New this month, by period.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Accepted, Filed, Returned.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New social declaration | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- due: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F13-10 Social declaration](../03-declarations-and-payments/s-f13-10-social-declaration.md).

The records also show on: [S-F13-23 Special regimes](../07-schemes-and-special-contracts/s-f13-23-special-regimes.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 social declarations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no social declaration the user may see yet, with the create action when allowed.
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
| Listed, U45, view Open: Accepted, Filed, Returned | desktop | ![Listed, U45, view Open: Accepted, Filed, Returned, light](../../images/lists/s-f13-l09-social-declarations-u45-payroll-officer-desktop-light.png) | ![Listed, U45, view Open: Accepted, Filed, Returned, dark](../../images/lists/s-f13-l09-social-declarations-u45-payroll-officer-desktop-dark.png) |
| Listed, U45, view Open: Accepted, Filed, Returned | phone | ![Listed, U45, view Open: Accepted, Filed, Returned, light](../../images/lists/s-f13-l09-social-declarations-u45-payroll-officer-phone-light.png) | ![Listed, U45, view Open: Accepted, Filed, Returned, dark](../../images/lists/s-f13-l09-social-declarations-u45-payroll-officer-phone-dark.png) |
| Listed, U43, view Needs attention | desktop | ![Listed, U43, view Needs attention, light](../../images/lists/s-f13-l09-social-declarations-u43-event-producer-desktop-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f13-l09-social-declarations-u43-event-producer-desktop-dark.png) |
| Listed, U43, view Needs attention | phone | ![Listed, U43, view Needs attention, light](../../images/lists/s-f13-l09-social-declarations-u43-event-producer-phone-light.png) | ![Listed, U43, view Needs attention, dark](../../images/lists/s-f13-l09-social-declarations-u43-event-producer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Payroll (plugin) › Social declarations](README.md) |
| Workspaces | [U45](../../../../04-ux/views/u45-payroll-officer/workspace.md), [U43](../../../../04-ux/views/u43-event-producer/workspace.md) |
| Flows | [FL-F13-03](../../flows/fl-f13-03-declarations-and-payments.md), [FL-F13-07](../../flows/fl-f13-07-schemes-and-special-contracts.md), [FL-F9-08](../../../f09-hr-and-projects/flows/fl-f09-08-hr-duties.md) |

## Open questions

None.

---

⬅️ [S-F13-L08 Pay transfers](s-f13-l08-pay-transfers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F13-L10 Corrections](s-f13-l10-corrections.md)
