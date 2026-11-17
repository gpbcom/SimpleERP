🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L04 Invitations

# 🗂️ S-F1-L04 Invitations

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F1-04 Invitation](../../data/e-f01-04-invitation.md) the user may see: to find, filter,
total and act on many invitations at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Invitations, in the capability's menu (D495).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "invitations" offers this view.
- **AI assistant:** "show the invitations that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Invitations    Administration › Invitations   [+ New]                                                        |
| [count] [Expired] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] EMAIL   STATUS   SENT AT   EXPIRES AT                                                |
| status            | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Email | email | text | yes |
| Status | status | badge | yes |
| Sent at | sent at | date and time | yes |
| Expires at | expires at | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Sent, Accepted, Expired, Cancelled, NotDelivered | the visible rows (D488) |
| Status | Sent, Accepted, Expired, Cancelled, NotDelivered | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: invitations link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.
- New this month, by sent at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Sent, Accepted, NotDelivered.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New invitation | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- sent at: editable in its cell unless the record's state locks it.
- expires at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| email | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| settings | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F1-03 Users](../03-user-lifecycle/s-f01-03-users.md).

The records also show on: [S-F1-14 Bulk invite](../10-bring-users-in-at-scale/s-f01-14-bulk-invite.md),
[S-F21-08 Team](../../../f21-onboarding-and-modules/screens/03-team-and-data/s-f21-08-team.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 invitations of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no invitation the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u07-administrator-phone-dark.png) |
| Listed, U01, view Open: Sent, Accepted, NotDelivered | desktop | ![Listed, U01, view Open: Sent, Accepted, NotDelivered, light](../../images/lists/s-f01-l04-invitations-u01-employee-desktop-light.png) | ![Listed, U01, view Open: Sent, Accepted, NotDelivered, dark](../../images/lists/s-f01-l04-invitations-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: Sent, Accepted, NotDelivered | phone | ![Listed, U01, view Open: Sent, Accepted, NotDelivered, light](../../images/lists/s-f01-l04-invitations-u01-employee-phone-light.png) | ![Listed, U01, view Open: Sent, Accepted, NotDelivered, dark](../../images/lists/s-f01-l04-invitations-u01-employee-phone-dark.png) |
| Listed, U11, view Needs attention | desktop | ![Listed, U11, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Needs attention | phone | ![Listed, U11, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u11-provider-admin-phone-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u11-provider-admin-phone-dark.png) |
| Listed, U13, view Needs attention | desktop | ![Listed, U13, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u13-owner-desktop-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u13-owner-desktop-dark.png) |
| Listed, U13, view Needs attention | phone | ![Listed, U13, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u13-owner-phone-light.png) | ![Listed, U13, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u13-owner-phone-dark.png) |
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u08-external-accountant-phone-dark.png) |
| Listed, U38, view Needs attention | desktop | ![Listed, U38, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u38-training-coordinator-desktop-dark.png) |
| Listed, U38, view Needs attention | phone | ![Listed, U38, view Needs attention, light](../../images/lists/s-f01-l04-invitations-u38-training-coordinator-phone-light.png) | ![Listed, U38, view Needs attention, dark](../../images/lists/s-f01-l04-invitations-u38-training-coordinator-phone-dark.png) |
| Listed, U09, view Open: Sent, Accepted, NotDelivered | desktop | ![Listed, U09, view Open: Sent, Accepted, NotDelivered, light](../../images/lists/s-f01-l04-invitations-u09-customer-desktop-light.png) | ![Listed, U09, view Open: Sent, Accepted, NotDelivered, dark](../../images/lists/s-f01-l04-invitations-u09-customer-desktop-dark.png) |
| Listed, U09, view Open: Sent, Accepted, NotDelivered | phone | ![Listed, U09, view Open: Sent, Accepted, NotDelivered, light](../../images/lists/s-f01-l04-invitations-u09-customer-phone-light.png) | ![Listed, U09, view Open: Sent, Accepted, NotDelivered, dark](../../images/lists/s-f01-l04-invitations-u09-customer-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Invitations](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md), [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U09](../../../../04-ux/views/u09-customer/workspace.md) |
| Flows | [FL-F1-01](../../flows/fl-f01-01-guided-setup.md), [FL-F1-03](../../flows/fl-f01-03-user-lifecycle.md), [FL-F1-08](../../flows/fl-f01-08-provider-and-client-companies.md), [FL-F1-10](../../flows/fl-f01-10-bring-users-in-at-scale.md), [FL-F21-03](../../../f21-onboarding-and-modules/flows/fl-f21-03-team-and-data.md), [FL-F21-04](../../../f21-onboarding-and-modules/flows/fl-f21-04-learn-and-improve.md), [FL-SC12-02](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-02-enrol-and-fund.md) |

## Open questions

None.

---

⬅️ [S-F1-L03 Users](s-f01-l03-users.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L05 Former-employee accesses](s-f01-l05-former-employee-accesses.md)
