🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L26 Rounds

# 🗂️ S-F9-L26 Rounds

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U05 Accounting](../../../../01-users/personas/u05-accounting.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-26 Round](../../data/e-f09-26-round.md) the user may see: to find, filter, total and
act on many rounds at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Rounds, in the capability's menu (D495).
- **Workspaces:** 11 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "rounds" offers this view.
- **AI assistant:** "show the rounds that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Rounds    HR and projects › Rounds   [+ New]                                                                 |
| [count] [Draft] [new this month]   [chart: count by state]                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] PERSON   STATUS   CARER   DAY   STOPS   DATE                                         |
| person            | [ ] ...                                                  Open >                          |
| status            | [ ] ...                                                  Open >                          |
| carer             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Person | person | person's name | yes |
| Status | status | badge | yes |
| Carer | carer | text | yes |
| Day | day | date | yes |
| Stops | stops | date and time | yes |
| Date | date | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Changed | the visible rows (D488) |
| Person | each person, the user first | the visible rows (D488) |
| Status | Draft, Published, Changed | the visible rows (D488) |
| Carer | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: rounds link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.
- New this month, by day.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: person.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New round | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the person; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- day: editable in its cell unless the record's state locks it.
- carer: editable in its cell unless the record's state locks it.
- date: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| person | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| stops | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to
[S-F16-11 My requests](../../../f16-customer-support-agents/screens/05-customer-side/s-f16-11-my-requests.md).

The records also show on:
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md),
[S-F16-15 Arrival of your visit](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-15-arrival-of-your-visit.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 rounds of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no round the user may see yet, with the create action when allowed.
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
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Mine: person | desktop | ![Listed, U26, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: person | phone | ![Listed, U26, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u26-carer-phone-light.png) | ![Listed, U26, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: person | desktop | ![Listed, U30, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: person | phone | ![Listed, U30, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u30-driver-phone-light.png) | ![Listed, U30, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u30-driver-phone-dark.png) |
| Listed, U09, view Mine: person | desktop | ![Listed, U09, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u09-customer-desktop-light.png) | ![Listed, U09, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u09-customer-desktop-dark.png) |
| Listed, U09, view Mine: person | phone | ![Listed, U09, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u09-customer-phone-light.png) | ![Listed, U09, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u09-customer-phone-dark.png) |
| Listed, U42, view Mine: person | desktop | ![Listed, U42, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Mine: person | phone | ![Listed, U42, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u42-sales-representative-phone-light.png) | ![Listed, U42, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u42-sales-representative-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u02-manager-phone-dark.png) |
| Listed, U14, view Mine: person | desktop | ![Listed, U14, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: person | phone | ![Listed, U14, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u14-field-worker-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f09-l26-rounds-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f09-l26-rounds-u07-administrator-phone-dark.png) |
| Listed, U05, view Mine: person | desktop | ![Listed, U05, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u05-accounting-desktop-light.png) | ![Listed, U05, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u05-accounting-desktop-dark.png) |
| Listed, U05, view Mine: person | phone | ![Listed, U05, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u05-accounting-phone-light.png) | ![Listed, U05, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u05-accounting-phone-dark.png) |
| Listed, U03, view Mine: person | desktop | ![Listed, U03, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: person | phone | ![Listed, U03, view Mine: person, light](../../images/lists/s-f09-l26-rounds-u03-sales-phone-light.png) | ![Listed, U03, view Mine: person, dark](../../images/lists/s-f09-l26-rounds-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Rounds](README.md) |
| Workspaces | [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U05](../../../../04-ux/views/u05-accounting/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F16-06](../../../f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md), [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-11](../../flows/fl-f09-11-capacity-rounds-and-partners.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md), [FL-SC04-02](../../../../08-sectors/sc04-home-care/flows/fl-sc04-02-plan-the-rounds.md), [FL-SC04-03](../../../../08-sectors/sc04-home-care/flows/fl-sc04-03-visit.md), [FL-SC04-04](../../../../08-sectors/sc04-home-care/flows/fl-sc04-04-bill-and-fund.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md) |

## Open questions

None.

---

⬅️ [S-F9-L25 Resource allocations](s-f09-l25-resource-allocations.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L27 Subcontractor assignments](s-f09-l27-subcontractor-assignments.md)
