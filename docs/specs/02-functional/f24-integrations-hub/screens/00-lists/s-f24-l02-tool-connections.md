🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Integrations hub menu](README.md) ›
🗂️ S-F24-L02 Tool connections

# 🗂️ S-F24-L02 Tool connections

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F24-02 Tool connection](../../data/e-f24-02-tool-connection.md) the user may see: to
find, filter, total and act on many tool connections at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Integrations hub › Tool connections, in the capability's menu (D495).
- **Workspaces:** 5 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "tool connections" offers this view.
- **AI assistant:** "show the tool connections that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Tool connections    Integrations hub › Tool connections   [+ New]                                            |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| company           | [ ] COMPANY   STATE   LINKED USER   CONNECTOR   ACCOUNT   KIND   DAILY AND WEEKLY CAPS   |
| connector         | [ ] ...                                                  Open >                          |
| account           | [ ] ...                                                  Open >                          |
| state             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Company | company | link to the record | yes |
| State | state | badge: Proposed, Active, Revoked | yes |
| Linked user | linked user | text | yes |
| Connector | connector | link to the record | yes |
| Account | account | link to the record | yes |
| Kind | kind | text | yes |
| Daily and weekly caps | daily and weekly caps | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Company | each linked company | the visible rows (D488) |
| Connector | each linked connector | the visible rows (D488) |
| Account | each linked account | the visible rows (D488) |
| State | Proposed, Active, Revoked | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Account | each linked account | the visible rows (D488) |
| State | Proposed, Active, Revoked | the visible rows (D488) |
| Linked user | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Tool connections of a chosen account, or of the accounts that match a filter.
- From the other side: the accounts that have tool connections, or none.
- Tool connections of a chosen company, or of the companies that match a filter.
- From the other side: the companies that have tool connections, or none.
- Tool connections of a chosen connector, or of the connectors that match a filter.
- From the other side: the connectors that have tool connections, or none.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: linked user.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New tool connection | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the linked user; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- kind: editable in its cell unless the record's state locks it.
- daily and weekly caps: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| linked user | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F24-01 Catalogue](../01-find-and-connect/s-f24-01-catalogue.md).

The records also show on: [S-F24-02 Connect](../01-find-and-connect/s-f24-02-connect.md),
[S-F21-10 Connections](../../../f21-onboarding-and-modules/screens/03-team-and-data/s-f21-10-connections.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 tool connections of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no tool connection the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f24-l02-tool-connections-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f24-l02-tool-connections-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f24-l02-tool-connections-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f24-l02-tool-connections-u07-administrator-phone-dark.png) |
| Listed, U06, view All | desktop | ![Listed, U06, view All, light](../../images/lists/s-f24-l02-tool-connections-u06-hr-desktop-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f24-l02-tool-connections-u06-hr-desktop-dark.png) |
| Listed, U06, view All | phone | ![Listed, U06, view All, light](../../images/lists/s-f24-l02-tool-connections-u06-hr-phone-light.png) | ![Listed, U06, view All, dark](../../images/lists/s-f24-l02-tool-connections-u06-hr-phone-dark.png) |
| Listed, U01, view Mine: linked user | desktop | ![Listed, U01, view Mine: linked user, light](../../images/lists/s-f24-l02-tool-connections-u01-employee-desktop-light.png) | ![Listed, U01, view Mine: linked user, dark](../../images/lists/s-f24-l02-tool-connections-u01-employee-desktop-dark.png) |
| Listed, U01, view Mine: linked user | phone | ![Listed, U01, view Mine: linked user, light](../../images/lists/s-f24-l02-tool-connections-u01-employee-phone-light.png) | ![Listed, U01, view Mine: linked user, dark](../../images/lists/s-f24-l02-tool-connections-u01-employee-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f24-l02-tool-connections-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f24-l02-tool-connections-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f24-l02-tool-connections-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f24-l02-tool-connections-u13-owner-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f24-l02-tool-connections-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f24-l02-tool-connections-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f24-l02-tool-connections-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f24-l02-tool-connections-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Integrations hub › Tool connections](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U06](../../../../04-ux/views/u06-hr/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F11-06](../../../f11-online-shop/flows/fl-f11-06-channels-and-legal.md), [FL-F21-03](../../../f21-onboarding-and-modules/flows/fl-f21-03-team-and-data.md), [FL-F24-01](../../flows/fl-f24-01-find-and-connect.md), [FL-F24-02](../../flows/fl-f24-02-office-suites.md), [FL-F24-04](../../flows/fl-f24-04-run-and-control.md), [FL-F24-06](../../flows/fl-f24-06-business-tools.md), [FL-F24-07](../../flows/fl-f24-07-employees-and-their-tools.md), [FL-F4-01](../../../f04-meetings/flows/fl-f04-01-record-an-online-meeting.md), [FL-F4-06](../../../f04-meetings/flows/fl-f04-06-set-up-meetings-and-calendars.md), [FL-F4-08](../../../f04-meetings/flows/fl-f04-08-share-and-reuse-outside.md), [FL-F8-03](../../../f08-accounting/flows/fl-f08-03-bank-and-collect.md), [FL-F9-02](../../../f09-hr-and-projects/flows/fl-f09-02-recruit.md), [FL-F9-14](../../../f09-hr-and-projects/flows/fl-f09-14-source-candidates-on-linkedin.md), [FL-SC14-04](../../../../08-sectors/sc14-it-and-software/flows/fl-sc14-04-product-delivery.md), [FL-SC15-02](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-02-orders.md) |

## Open questions

None.

---

⬅️ [S-F24-L01 Connectors](s-f24-l01-connectors.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-L03 Suite components](s-f24-l03-suite-components.md)
