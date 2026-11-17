🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L07 Personal connections

# 🗂️ S-F3-L07 Personal connections

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U04 Purchasing and stock](../../../../01-users/personas/u04-purchasing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

- The owner's review (VC-3, D519): "Create persona(s) related to this enitity."
- Every AI assistant user sees their own records.

## Purpose

The aggregated list of every [E-F3-07 Personal connection](../../data/e-f03-07-personal-connection.md) the user may see:
to find, filter, total and act on many personal connections at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Assistant › Personal connections, in the capability's menu (D495).
- **Workspaces:** 12 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "personal connections" offers this view.
- **AI assistant:** "show the personal connections that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Personal connections    Assistant › Personal connections   [+ New]                                           |
| [count] [Expired]   [chart: count by state]                                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] USER   STATUS   ACCOUNT                                                              |
| user              | [ ] ...                                                  Open >                          |
| account           | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| User | user | person's name | yes |
| Status | status | badge | yes |
| Account | account | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Connected, Expired | the visible rows (D488) |
| User | each person, the user first | the visible rows (D488) |
| Account | each value | the visible rows (D488) |
| Status | Connected, Expired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Personal connections of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have personal connections, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: user.
- Open: Connected.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New personal connection | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the user; audited |
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
| user | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| account | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| tokens | secret | nobody | everyone (VR-4) |

## Row opens

Open › goes to [S-F3-06 My connections](../06-use-an-outside-tool/s-f03-06-my-connections.md).

The records also show on: [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md),
[S-F1-07 Connections](../../../f01-administration/screens/05-connect-an-external-tool/s-f01-07-connections.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 personal connections of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no personal connection the user may see yet, with the create action when allowed.
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
| Listed, U01, view Mine: user | desktop | ![Listed, U01, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: user | phone | ![Listed, U01, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u01-employee-phone-light.png) | ![Listed, U01, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u01-employee-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u02-manager-phone-dark.png) |
| Listed, U03, view Mine: user | desktop | ![Listed, U03, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: user | phone | ![Listed, U03, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u03-sales-phone-light.png) | ![Listed, U03, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u03-sales-phone-dark.png) |
| Listed, U04, view Mine: user | desktop | ![Listed, U04, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u04-purchasing-desktop-light.png) | ![Listed, U04, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u04-purchasing-desktop-dark.png) |
| Listed, U04, view Mine: user | phone | ![Listed, U04, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u04-purchasing-phone-light.png) | ![Listed, U04, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u04-purchasing-phone-dark.png) |
| Listed, U05, view Mine: user | desktop | ![Listed, U05, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: user | phone | ![Listed, U05, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u05-accounting-phone-dark.png) |
| Listed, U06, view Needs attention | desktop | ![Listed, U06, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u06-hr-desktop-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u06-hr-desktop-dark.png) |
| Listed, U06, view Needs attention | phone | ![Listed, U06, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u06-hr-phone-light.png) | ![Listed, U06, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u06-hr-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u07-administrator-phone-dark.png) |
| Listed, U12, view Mine: user | desktop | ![Listed, U12, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u12-marketing-desktop-light.png) | ![Listed, U12, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u12-marketing-desktop-dark.png) |
| Listed, U12, view Mine: user | phone | ![Listed, U12, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u12-marketing-phone-light.png) | ![Listed, U12, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u12-marketing-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f03-l07-personal-connections-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f03-l07-personal-connections-u13-owner-phone-dark.png) |
| Listed, U14, view Mine: user | desktop | ![Listed, U14, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: user | phone | ![Listed, U14, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u14-field-worker-phone-dark.png) |
| Listed, U15, view Mine: user | desktop | ![Listed, U15, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u15-warehouse-operator-desktop-light.png) | ![Listed, U15, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u15-warehouse-operator-desktop-dark.png) |
| Listed, U15, view Mine: user | phone | ![Listed, U15, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u15-warehouse-operator-phone-light.png) | ![Listed, U15, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u15-warehouse-operator-phone-dark.png) |
| Listed, U16, view Mine: user | desktop | ![Listed, U16, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u16-office-worker-desktop-light.png) | ![Listed, U16, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Mine: user | phone | ![Listed, U16, view Mine: user, light](../../images/lists/s-f03-l07-personal-connections-u16-office-worker-phone-light.png) | ![Listed, U16, view Mine: user, dark](../../images/lists/s-f03-l07-personal-connections-u16-office-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Assistant › Personal connections](README.md) |
| Workspaces | [U01](../../../../04-ux/views/u01-employee/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md), [U04](../../../../04-ux/views/u04-purchasing/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U15](../../../../04-ux/views/u15-warehouse-operator/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md) |
| Flows | [FL-F3-06](../../flows/fl-f03-06-use-an-outside-tool.md), [FL-F4-06](../../../f04-meetings/flows/fl-f04-06-set-up-meetings-and-calendars.md) |

## Open questions

None.

---

⬅️ [S-F3-L06 Configuration requests](s-f03-l06-configuration-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L08 Outside calls](s-f03-l08-outside-calls.md)
