🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
👥 [F9 HR and projects](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: HR and projects menu](README.md) ›
🗂️ S-F9-L30 Qualification types

# 🗂️ S-F9-L30 Qualification types

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U06 Human resources](../../../../01-users/personas/u06-hr.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U26 Carer](../../../../01-users/personas/u26-carer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U30 Driver](../../../../01-users/personas/u30-driver.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U14 Field worker](../../../../01-users/personas/u14-field-worker.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U02 Manager](../../../../01-users/personas/u02-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F9-30 Qualification type](../../data/e-f09-30-qualification-type.md) the user may see:
to find, filter, total and act on many qualification types at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** HR and projects › Qualification types, in the capability's menu (D495).
- **Workspaces:** 9 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "qualification types" offers this view.
- **AI assistant:** "show the qualification types that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Qualification types    HR and projects › Qualification types   [+ New]                                       |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] CODE   STATUS   COUNTRY RULE   VALIDITY   KIND   LEVELS OR CATEGORIES   LEGAL        |
| kind              | [ ] ...                                                  Open >                          |
| levels or categor | [ ] ...                                                  Open >                          |
| legal             | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Code | code | text | yes |
| Status | status | badge | yes |
| Country rule | country rule | text | yes |
| Validity | validity | label | yes |
| Kind | kind | text | yes |
| Levels or categories | levels or categories | text | yes |
| Legal | legal | yes or no | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active, Retired | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Levels or categories | each value | the visible rows (D488) |
| Legal | each value | the visible rows (D488) |
| Country rule | each value | the visible rows (D488) |
| Status | Active, Retired | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Qualification types of a chosen country rule, or of the country rules that match a filter.
- From the other side: the country rules that have qualification types, or none.

## KPI strip

- Count of the visible rows.
- New this month, by validity.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Active.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New qualification type | header | the personas whose roles may create it | the record's own page (Row opens) |
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
- levels or categories: editable in its cell unless the record's state locks it.
- validity: editable in its cell unless the record's state locks it.
- legal: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F2-29 Request type settings](../../../f02-no-code-configuration/screens/12-set-up-request-types/s-f02-29-request-type-settings.md).

The records also show on:
[S-F16-14 Work requests](../../../f16-customer-support-agents/screens/06-take-in-every-request/s-f16-14-work-requests.md),
[S-F2-10 Publish and versions](../../../f02-no-code-configuration/screens/05-publish-and-roll-back/s-f02-10-publish-and-versions.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 qualification types of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no qualification type the user may see yet, with the create action when allowed.
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
| Listed, U06, view Open: Active | desktop | ![Listed, U06, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u06-hr-desktop-light.png) | ![Listed, U06, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u06-hr-desktop-dark.png) |
| Listed, U06, view Open: Active | phone | ![Listed, U06, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u06-hr-phone-light.png) | ![Listed, U06, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u06-hr-phone-dark.png) |
| Listed, U01, view Open: Active | desktop | ![Listed, U01, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u01-employee-desktop-light.png) | ![Listed, U01, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u01-employee-desktop-dark.png) |
| Listed, U01, view Open: Active | phone | ![Listed, U01, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u01-employee-phone-light.png) | ![Listed, U01, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u01-employee-phone-dark.png) |
| Listed, U07, view Open: Active | desktop | ![Listed, U07, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u07-administrator-desktop-light.png) | ![Listed, U07, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u07-administrator-desktop-dark.png) |
| Listed, U07, view Open: Active | phone | ![Listed, U07, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u07-administrator-phone-light.png) | ![Listed, U07, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u07-administrator-phone-dark.png) |
| Listed, U25, view Open: Active | desktop | ![Listed, U25, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u25-care-coordinator-desktop-light.png) | ![Listed, U25, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u25-care-coordinator-desktop-dark.png) |
| Listed, U25, view Open: Active | phone | ![Listed, U25, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u25-care-coordinator-phone-light.png) | ![Listed, U25, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u25-care-coordinator-phone-dark.png) |
| Listed, U29, view Open: Active | desktop | ![Listed, U29, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u29-dispatcher-desktop-light.png) | ![Listed, U29, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u29-dispatcher-desktop-dark.png) |
| Listed, U29, view Open: Active | phone | ![Listed, U29, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u29-dispatcher-phone-light.png) | ![Listed, U29, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u29-dispatcher-phone-dark.png) |
| Listed, U26, view Open: Active | desktop | ![Listed, U26, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u26-carer-desktop-light.png) | ![Listed, U26, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u26-carer-desktop-dark.png) |
| Listed, U26, view Open: Active | phone | ![Listed, U26, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u26-carer-phone-light.png) | ![Listed, U26, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u26-carer-phone-dark.png) |
| Listed, U30, view Open: Active | desktop | ![Listed, U30, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u30-driver-desktop-light.png) | ![Listed, U30, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u30-driver-desktop-dark.png) |
| Listed, U30, view Open: Active | phone | ![Listed, U30, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u30-driver-phone-light.png) | ![Listed, U30, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u30-driver-phone-dark.png) |
| Listed, U14, view Open: Active | desktop | ![Listed, U14, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u14-field-worker-desktop-light.png) | ![Listed, U14, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u14-field-worker-desktop-dark.png) |
| Listed, U14, view Open: Active | phone | ![Listed, U14, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u14-field-worker-phone-light.png) | ![Listed, U14, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u14-field-worker-phone-dark.png) |
| Listed, U02, view Open: Active | desktop | ![Listed, U02, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u02-manager-desktop-light.png) | ![Listed, U02, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u02-manager-desktop-dark.png) |
| Listed, U02, view Open: Active | phone | ![Listed, U02, view Open: Active, light](../../images/lists/s-f09-l30-qualification-types-u02-manager-phone-light.png) | ![Listed, U02, view Open: Active, dark](../../images/lists/s-f09-l30-qualification-types-u02-manager-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [HR and projects › Qualification types](README.md) |
| Workspaces | [U06](../../../../04-ux/views/u06-hr/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U25](../../../../04-ux/views/u25-care-coordinator/workspace.md), [U29](../../../../04-ux/views/u29-dispatcher/workspace.md), [U26](../../../../04-ux/views/u26-carer/workspace.md), [U30](../../../../04-ux/views/u30-driver/workspace.md), [U14](../../../../04-ux/views/u14-field-worker/workspace.md), [U02](../../../../04-ux/views/u02-manager/workspace.md) |
| Flows | [FL-F2-12](../../../f02-no-code-configuration/flows/fl-f02-12-set-up-request-types.md), [FL-F9-12](../../flows/fl-f09-12-schedule-customer-requests.md), [FL-F9-13](../../flows/fl-f09-13-keep-qualifications.md) |

## Open questions

None.

---

⬅️ [S-F9-L29 Degrees](s-f09-l29-degrees.md) · ⬆️ [Up](README.md) ·
➡️ [S-F9-L31 Attribute readings](s-f09-l31-attribute-readings.md)
