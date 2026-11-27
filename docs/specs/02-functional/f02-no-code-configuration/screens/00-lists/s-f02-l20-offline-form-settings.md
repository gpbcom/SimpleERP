🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L20 Offline form settings

# 🗂️ S-F2-L20 Offline form settings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U22 Site manager](../../../../01-users/personas/u22-site-manager.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F2-20 Offline form setting](../../data/e-f02-20-offline-form-setting.md) the user may
see: to find, filter, total and act on many offline form settings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Offline form settings, in the Administration menu (D494).
- **Workspaces:** 7 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "offline form settings" offers this view.
- **AI assistant:** "show the offline form settings that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Offline form settings    Administration › Offline form settings   [+ New]                                    |
| [count] [Draft]   [chart: count by state]                                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] RECORD TYPE   STATE   ROLES   CONFLICT RULE                                          |
| record type       | [ ] ...                                                  Open >                          |
| conflict rule     | [ ] ...                                                  Open >                          |
| roles             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Record type | record type | text | yes |
| State | state | badge: Draft, Published, Archived | yes |
| Roles | roles | text | yes |
| Conflict rule | conflict rule | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Draft, Published, Archived | the visible rows (D488) |
| Record type | each value | the visible rows (D488) |
| Conflict rule | each value | the visible rows (D488) |
| Roles | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Offline form settings of a chosen record type, or of the record types that match a filter.
- From the other side: the record types that have offline form settings, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Draft.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: roles.
- Open: Draft, Published.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New offline form setting | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the roles; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- conflict rule: editable in its cell unless the record's state locks it.
- roles: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F2-21 Offline form](../09-portals-and-offline-forms/s-f02-21-offline-form.md).

The records also show on:
[S-F6-18 Phone order](../../../f06-customers-and-sales/screens/09-sell-on-the-road-and-steer-sales/s-f06-18-phone-order.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 offline form settings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no offline form setting the user may see yet, with the create action when allowed.
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
| Listed, U22, view Needs attention | desktop | ![Listed, U22, view Needs attention, light](../../images/lists/s-f02-l20-offline-form-settings-u22-site-manager-desktop-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-f02-l20-offline-form-settings-u22-site-manager-desktop-dark.png) |
| Listed, U22, view Needs attention | phone | ![Listed, U22, view Needs attention, light](../../images/lists/s-f02-l20-offline-form-settings-u22-site-manager-phone-light.png) | ![Listed, U22, view Needs attention, dark](../../images/lists/s-f02-l20-offline-form-settings-u22-site-manager-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l20-offline-form-settings-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l20-offline-form-settings-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f02-l20-offline-form-settings-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f02-l20-offline-form-settings-u07-administrator-phone-dark.png) |
| Listed, U14, view Mine: roles | desktop | ![Listed, U14, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u14-field-worker-desktop-light.png) | ![Listed, U14, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Mine: roles | phone | ![Listed, U14, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u14-field-worker-phone-light.png) | ![Listed, U14, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u14-field-worker-phone-dark.png) |
| Listed, U26, view Mine: roles | desktop | ![Listed, U26, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u26-carer-desktop-light.png) | ![Listed, U26, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u26-carer-desktop-dark.png) |
| Listed, U26, view Mine: roles | phone | ![Listed, U26, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u26-carer-phone-light.png) | ![Listed, U26, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u26-carer-phone-dark.png) |
| Listed, U30, view Mine: roles | desktop | ![Listed, U30, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u30-driver-desktop-light.png) | ![Listed, U30, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u30-driver-desktop-dark.png) |
| Listed, U30, view Mine: roles | phone | ![Listed, U30, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u30-driver-phone-light.png) | ![Listed, U30, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u30-driver-phone-dark.png) |
| Listed, U42, view Mine: roles | desktop | ![Listed, U42, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u42-sales-representative-desktop-light.png) | ![Listed, U42, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u42-sales-representative-desktop-dark.png) |
| Listed, U42, view Mine: roles | phone | ![Listed, U42, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u42-sales-representative-phone-light.png) | ![Listed, U42, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u42-sales-representative-phone-dark.png) |
| Listed, U03, view Mine: roles | desktop | ![Listed, U03, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u03-sales-desktop-light.png) | ![Listed, U03, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u03-sales-desktop-dark.png) |
| Listed, U03, view Mine: roles | phone | ![Listed, U03, view Mine: roles, light](../../images/lists/s-f02-l20-offline-form-settings-u03-sales-phone-light.png) | ![Listed, U03, view Mine: roles, dark](../../images/lists/s-f02-l20-offline-form-settings-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Offline form settings](README.md) |
| Workspaces | [U22](../../../../04-ux/views/u22-site-manager/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U42](../../../../04-ux/views/u42-sales-representative/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F2-09](../../flows/fl-f02-09-portals-and-offline-forms.md), [FL-F6-09](../../../f06-customers-and-sales/flows/fl-f06-09-sell-on-the-road-and-steer-sales.md), [FL-SC12-03](../../../../08-sectors/sc12-education-and-training/flows/fl-sc12-03-deliver-and-assess.md), [FL-SC15-03](../../../../08-sectors/sc15-wholesale-and-distribution/flows/fl-sc15-03-warehouse.md) |

## Open questions

None.

---

⬅️ [S-F2-L19 Portal exposures](s-f02-l19-portal-exposures.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L21 Test cases](s-f02-l21-test-cases.md)
