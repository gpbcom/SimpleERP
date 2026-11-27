🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Administration menu](README.md) ›
🗂️ S-F1-L03 Users

# 🗂️ S-F1-L03 Users

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F1-03 User](../../data/e-f01-03-user.md) the user may see: to find, filter, total and
act on many users at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Users, in the capability's menu (D495).
- **Workspaces:** 6 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "users" offers this view.
- **AI assistant:** "show the users that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Users    Administration › Users   [+ New]                                                                    |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATUS   MANAGER   SITE   LANGUAGE   DENSITY                                  |
| site              | [ ] ...                                                  Open >                          |
| manager           | [ ] ...                                                  Open >                          |
| language          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Status | status | badge | yes |
| Manager | manager | person's name | yes |
| Site | site | text | yes |
| Language | language | text | yes |
| Density | density | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Invited, Active, Deactivated | the visible rows (D488) |
| Site | each value | the visible rows (D488) |
| Manager | each person, the user first | the visible rows (D488) |
| Language | each value | the visible rows (D488) |
| Status | Invited, Active, Deactivated | the visible rows (D488) |
| Density | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Users of a chosen site, or of the sites that match a filter.
- From the other side: the sites that have users, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: manager.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New user | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change status | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the manager; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- language: editable in its cell unless the record's state locks it.
- density: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| name | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| email | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| manager | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| hr record | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F1-03 Users](../03-user-lifecycle/s-f01-03-users.md).

The records also show on: [S-F1-04 User page](../03-user-lifecycle/s-f01-04-user-page.md),
[S-F1-05 Offboarding](../03-user-lifecycle/s-f01-05-offboarding.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 users of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no user the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f01-l03-users-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l03-users-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f01-l03-users-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f01-l03-users-u07-administrator-phone-dark.png) |
| Listed, U02, view All | desktop | ![Listed, U02, view All, light](../../images/lists/s-f01-l03-users-u02-manager-desktop-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f01-l03-users-u02-manager-desktop-dark.png) |
| Listed, U02, view All | phone | ![Listed, U02, view All, light](../../images/lists/s-f01-l03-users-u02-manager-phone-light.png) | ![Listed, U02, view All, dark](../../images/lists/s-f01-l03-users-u02-manager-phone-dark.png) |
| Listed, U01, view Mine: manager | desktop | ![Listed, U01, view Mine: manager, light](../../images/lists/s-f01-l03-users-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: manager, dark](../../images/lists/s-f01-l03-users-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: manager | phone | ![Listed, U01, view Mine: manager, light](../../images/lists/s-f01-l03-users-u01-employee-phone-light.png) | ![Listed, U01, view Mine: manager, dark](../../images/lists/s-f01-l03-users-u01-employee-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f01-l03-users-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l03-users-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f01-l03-users-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f01-l03-users-u11-provider-admin-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f01-l03-users-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l03-users-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f01-l03-users-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f01-l03-users-u13-owner-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-f01-l03-users-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f01-l03-users-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-f01-l03-users-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-f01-l03-users-u23-store-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Users](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md) |
| Flows | [FL-F1-01](../../flows/fl-f01-01-guided-setup.md), [FL-F1-02](../../flows/fl-f01-02-manage-sites.md), [FL-F1-03](../../flows/fl-f01-03-user-lifecycle.md), [FL-F1-04](../../flows/fl-f01-04-edit-a-role.md), [FL-F1-07](../../flows/fl-f01-07-set-up-single-sign-on.md), [FL-F1-09](../../flows/fl-f01-09-administration-reports.md), [FL-F1-10](../../flows/fl-f01-10-bring-users-in-at-scale.md), [FL-F1-11](../../flows/fl-f01-11-team-delegation-and-access-review.md), [FL-F1-13](../../flows/fl-f01-13-security-and-audit.md), [FL-F12-08](../../../f12-manufacturing/flows/fl-f12-08-report-and-assist.md), [FL-F15-01](../../../f15-legal-assistant/flows/fl-f15-01-ask-a-legal-question.md), [FL-F15-02](../../../f15-legal-assistant/flows/fl-f15-02-receive-a-legal-warning.md), [FL-F15-05](../../../f15-legal-assistant/flows/fl-f15-05-duties-and-records.md), [FL-F17-04](../../../f17-competitive-analysis/flows/fl-f17-04-alerts-and-sharing.md), [FL-F2-06](../../../f02-no-code-configuration/flows/fl-f02-06-share-a-configuration.md), [FL-F3-01](../../../f03-assistant/flows/fl-f03-01-ask-the-assistant.md), [FL-F3-02](../../../f03-assistant/flows/fl-f03-02-ask-about-the-screen.md), [FL-F3-03](../../../f03-assistant/flows/fl-f03-03-act-through-the-assistant.md), [FL-F3-04](../../../f03-assistant/flows/fl-f03-04-summarise-or-draft.md), [FL-F3-05](../../../f03-assistant/flows/fl-f03-05-find-and-get-guided.md), [FL-F3-06](../../../f03-assistant/flows/fl-f03-06-use-an-outside-tool.md), [FL-F3-07](../../../f03-assistant/flows/fl-f03-07-manage-knowledge.md), [FL-F3-08](../../../f03-assistant/flows/fl-f03-08-manage-and-share-conversations.md), [FL-F3-11](../../../f03-assistant/flows/fl-f03-11-trust-the-answers.md), [FL-F3-12](../../../f03-assistant/flows/fl-f03-12-personal-cost-aware-and-learning.md), [FL-SC01-03](../../../../08-sectors/sc01-construction/flows/fl-sc01-03-run-the-site.md), [FL-SC02-05](../../../../08-sectors/sc02-retail/flows/fl-sc02-05-unsold-goods-and-performance.md), [FL-SC03-03](../../../../08-sectors/sc03-services/flows/fl-sc03-03-deliver-and-record.md), [FL-SC04-03](../../../../08-sectors/sc04-home-care/flows/fl-sc04-03-visit.md), [FL-SC05-04](../../../../08-sectors/sc05-manufacturing/flows/fl-sc05-04-quality-system.md), [FL-SC06-03](../../../../08-sectors/sc06-hospitality/flows/fl-sc06-03-rooms-and-bookings.md), [FL-SC07-01](../../../../08-sectors/sc07-transport/flows/fl-sc07-01-orders-and-planning.md), [FL-SC08-02](../../../../08-sectors/sc08-non-profit/flows/fl-sc08-02-donations-and-receipts.md), [FL-SC10-06](../../../../08-sectors/sc10-real-estate/flows/fl-sc10-06-portal-and-assistant.md), [FL-SC12-03](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-03-deliver-and-assess.md), [FL-SC13-03](../../../../08-sectors/sc13-agriculture-and-food/flows/fl-sc13-03-farm-business.md), [FL-SC14-06](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-06-portal-and-metrics.md), [FL-SC15-05](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-05-sales-force-and-performance.md), [FL-SC16-05](../../../../08-sectors/sc16-events-and-culture/flows/fl-sc16-05-declarations-and-reports.md) |

## Open questions

None.

---

⬅️ [S-F1-L02 Company sites](s-f01-l02-company-sites.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-L04 Invitations](s-f01-l04-invitations.md)
