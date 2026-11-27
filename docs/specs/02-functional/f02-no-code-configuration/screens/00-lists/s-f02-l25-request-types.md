🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L25 Request types

# 🗂️ S-F2-L25 Request types

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Request types (UC-F2-30)": on record types their roles see | actions as [permissions](../../permissions.md) gives them |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | as the permissions row "Request types (UC-F2-30)": yes | actions as [permissions](../../permissions.md) gives them |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U16 Office worker](../../../../01-users/personas/u16-office-worker.md) | as the permissions row "Request types (UC-F2-30)": on record types their roles see | actions as [permissions](../../permissions.md) gives them |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F2-25 Request type](../../data/e-f02-25-request-type.md) the user may see: to find,
filter, total and act on many request types at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** No-code configuration › Request types, in the capability's menu (D495).
- **Workspaces:** 9 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "request types" offers this view.
- **AI assistant:** "show the request types that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Request types    No-code configuration › Request types   [+ New]                                             |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATUS   KIND   AUTOMATIC MODE ALLOWED   PLACE NEEDED                         |
| kind              | [ ] ...                                                  Open >                          |
| automatic mode al | [ ] ...                                                  Open >                          |
| place needed      | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Status | status | badge | yes |
| Kind | kind | text | yes |
| Automatic mode allowed | automatic mode allowed | yes or no | yes |
| Place needed | place needed | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Retired | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Automatic mode allowed | each value | the visible rows (D488) |
| Place needed | each value | the visible rows (D488) |
| Status | Draft, Published, Retired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: request types link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Draft, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New request type | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- automatic mode allowed: editable in its cell unless the record's state locks it.
- place needed: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F2-10 Publish and versions](../05-publish-and-roll-back/s-f02-10-publish-and-versions.md).

The records also show on:
[S-F16-11 My requests](../../../f16-customer-support-agents/screens/05-customer-side/s-f16-11-my-requests.md),
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 request types of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no request type the user may see yet, with the create action when allowed.
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
| Listed, U29, view Needs attention | desktop | ![Listed, U29, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Needs attention | phone | ![Listed, U29, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u29-dispatcher-phone-light.png) | ![Listed, U29, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u29-dispatcher-phone-dark.png) |
| Listed, U25, view Needs attention | desktop | ![Listed, U25, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Needs attention | phone | ![Listed, U25, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u25-care-coordinator-phone-dark.png) |
| Listed, U02, view Needs attention | desktop | ![Listed, U02, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u02-manager-desktop-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u02-manager-desktop-dark.png) |
| Listed, U02, view Needs attention | phone | ![Listed, U02, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u02-manager-phone-light.png) | ![Listed, U02, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u02-manager-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l25-request-types-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l25-request-types-u07-administrator-phone-dark.png) |
| Listed, U09, view Open: Draft, Published | desktop | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Draft, Published | phone | ![Listed, U09, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u09-customer-phone-light.png) | ![Listed, U09, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u09-customer-phone-dark.png) |
| Listed, U16, view Open: Draft, Published | desktop | ![Listed, U16, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u16-office-worker-desktop-light.png) | ![Listed, U16, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u16-office-worker-desktop-dark.png) |
| Listed, U16, view Open: Draft, Published | phone | ![Listed, U16, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u16-office-worker-phone-light.png) | ![Listed, U16, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u16-office-worker-phone-dark.png) |
| Listed, U26, view Open: Draft, Published | desktop | ![Listed, U26, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u26-carer-desktop-light.png) | ![Listed, U26, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u26-carer-desktop-dark.png) |
| Listed, U26, view Open: Draft, Published | phone | ![Listed, U26, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u26-carer-phone-light.png) | ![Listed, U26, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u26-carer-phone-dark.png) |
| Listed, U30, view Open: Draft, Published | desktop | ![Listed, U30, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u30-driver-desktop-light.png) | ![Listed, U30, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u30-driver-desktop-dark.png) |
| Listed, U30, view Open: Draft, Published | phone | ![Listed, U30, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u30-driver-phone-light.png) | ![Listed, U30, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u30-driver-phone-dark.png) |
| Listed, U14, view Open: Draft, Published | desktop | ![Listed, U14, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: Draft, Published | phone | ![Listed, U14, view Open: Draft, Published, light](../../images/lists/s-f02-l25-request-types-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: Draft, Published, dark](../../images/lists/s-f02-l25-request-types-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [No-code configuration › Request types](README.md) |
| Workspaces | [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md), [U16](../../../../04-ux/views/u16-office-worker/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-F16-06](../../../f16-customer-support-agents/flows/fl-f16-06-take-in-every-request.md), [FL-F2-12](../../flows/fl-f02-12-set-up-request-types.md), [FL-F9-12](../../../f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md) |

## Open questions

None.

---

⬅️ [S-F2-L24 Approval chains](s-f02-l24-approval-chains.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L26 Configuration drafts](s-f02-l26-configuration-drafts.md)
