🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L06 Roles

# 🗂️ S-F1-L06 Roles

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | as the permissions row "Roles and record rules (UC-F1-06)": yes | actions as [permissions](../../permissions.md) gives them |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | as the permissions row "Roles and record rules (UC-F1-06)": no | actions as [permissions](../../permissions.md) gives them |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Roles and record rules (UC-F1-06)": as administrator | actions as [permissions](../../permissions.md) gives them |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | as the permissions row "Roles and record rules (UC-F1-06)": yes | actions as [permissions](../../permissions.md) gives them |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F1-06 Role](../../data/e-f01-06-role.md) the user may see: to find, filter, total and
act on many roles at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Roles, in the capability's menu (D495).
- **Workspaces:** 10 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "roles" offers this view.
- **AI assistant:** "show the roles that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Roles    Administration › Roles   [+ New]                                                                    |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   COPIED FROM   READY-MADE   MAP RIGHT   PLANNER                        |
| ready-made        | [ ] ...                                                  Open >                          |
| copied from       | [ ] ...                                                  Open >                          |
| map right         | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| State | state | badge: Active | yes |
| Copied from | copied from | text | yes |
| Ready-made | ready-made | yes or no | yes |
| Map right | map right | yes or no | yes |
| Planner | planner | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Ready-made | each value | the visible rows (D488) |
| Copied from | each value | the visible rows (D488) |
| Map right | each value | the visible rows (D488) |
| Planner | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: roles link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: copied from.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New role | header | the personas whose roles may create it | the record's own page (Row opens) |
| Assign | bulk bar | the personas whose roles may assign | sets the copied from; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- ready-made: editable in its cell unless the record's state locks it.
- copied from: editable in its cell unless the record's state locks it.
- map right: editable in its cell unless the record's state locks it.
- planner: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F1-06 Role editor](../04-edit-a-role/s-f01-06-role-editor.md).

The records also show on: [S-F1-05 Offboarding](../03-user-lifecycle/s-f01-05-offboarding.md),
[S-F1-15 My site's users](../10-bring-users-in-at-scale/s-f01-15-my-sites-users.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 roles of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no role the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f01-l06-roles-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l06-roles-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f01-l06-roles-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l06-roles-u07-administrator-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f01-l06-roles-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f01-l06-roles-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f01-l06-roles-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f01-l06-roles-u02-manager-phone-dark.png) |
| Listed, U25, view All | desktop | ![Listed, U25, view All, light](../../images/lists/s-f01-l06-roles-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f01-l06-roles-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view All | phone | ![Listed, U25, view All, light](../../images/lists/s-f01-l06-roles-u25-care-coordinator-phone-light.png) | ![Listed, U25, view All, dark](../../images/lists/s-f01-l06-roles-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view All | desktop | ![Listed, U29, view All, light](../../images/lists/s-f01-l06-roles-u29-dispatcher-desktop-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f01-l06-roles-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view All | phone | ![Listed, U29, view All, light](../../images/lists/s-f01-l06-roles-u29-dispatcher-phone-light.png) | ![Listed, U29, view All, dark](../../images/lists/s-f01-l06-roles-u29-dispatcher-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f01-l06-roles-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f01-l06-roles-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f01-l06-roles-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f01-l06-roles-u23-store-manager-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f01-l06-roles-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l06-roles-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f01-l06-roles-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l06-roles-u13-owner-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f01-l06-roles-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l06-roles-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f01-l06-roles-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l06-roles-u11-provider-admin-phone-dark.png) |
| Listed, U26, view Mine: copied from | desktop | ![Listed, U26, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: copied from | phone | ![Listed, U26, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u26-carer-phone-light.png) | ![Listed, U26, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: copied from | desktop | ![Listed, U30, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: copied from | phone | ![Listed, U30, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u30-driver-phone-light.png) | ![Listed, U30, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u30-driver-phone-dark.png) |
| Listed, U14, view Mine: copied from | desktop | ![Listed, U14, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: copied from | phone | ![Listed, U14, view Mine: copied from, light](../../images/lists/s-f01-l06-roles-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: copied from, dark](../../images/lists/s-f01-l06-roles-u14-field-worker-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Roles](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md) |
| Flows | [FL-F1-03](../../flows/fl-f01-03-user-lifecycle.md), [FL-F1-04](../../flows/fl-f01-04-edit-a-role.md), [FL-F1-05](../../flows/fl-f01-05-connect-an-external-tool.md), [FL-F1-07](../../flows/fl-f01-07-set-up-single-sign-on.md), [FL-F1-09](../../flows/fl-f01-09-administration-reports.md), [FL-F1-10](../../flows/fl-f01-10-bring-users-in-at-scale.md), [FL-F1-11](../../flows/fl-f01-11-team-delegation-and-access-review.md), [FL-F1-12](../../flows/fl-f01-12-portal-accounts-and-integrations.md), [FL-F2-05](../../../f02-no-code-configuration/flows/fl-f02-05-publish-and-roll-back.md), [FL-F2-08](../../../f02-no-code-configuration/flows/fl-f02-08-views-and-bookings.md), [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F24-04](../../../f24-integrations-hub/flows/fl-f24-04-run-and-control.md), [FL-F3-02](../../../f03-assistant/flows/fl-f03-02-ask-about-the-screen.md), [FL-F9-12](../../../f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md), [FL-SC01-03](../../../../08-sectors/sc01-construction/flows/fl-sc01-03-run-the-site.md), [FL-SC02-05](../../../../08-sectors/sc02-retail/flows/fl-sc02-05-unsold-goods-and-performance.md), [FL-SC03-01](../../../../08-sectors/sc03-services/flows/fl-sc03-01-win-and-price.md), [FL-SC03-02](../../../../08-sectors/sc03-services/flows/fl-sc03-02-staff-and-plan.md), [FL-SC03-03](../../../../08-sectors/sc03-services/flows/fl-sc03-03-deliver-and-record.md), [FL-SC04-03](../../../../08-sectors/sc04-home-care/flows/fl-sc04-03-visit.md), [FL-SC05-04](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-04-quality-system.md), [FL-SC06-03](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC08-02](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-02-donations-and-receipts.md), [FL-SC10-06](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-06-portal-and-assistant.md), [FL-SC12-03](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-03-deliver-and-assess.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md), [FL-SC14-06](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-06-portal-and-metrics.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md), [FL-SC16-05](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-05-declarations-and-reports.md) |

## Open questions

None.

---

⬅️ [S-F1-L05 Former-employee accesses](s-f01-l05-former-employee-accesses.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L07 Record rules](s-f01-l07-record-rules.md)
