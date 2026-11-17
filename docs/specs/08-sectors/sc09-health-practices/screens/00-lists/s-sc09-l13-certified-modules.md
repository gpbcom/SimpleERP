🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🩺 [SC09 Health practices](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Health practices menu](README.md) › 🗂️ S-SC09-L13 Certified modules

# 🗂️ S-SC09-L13 Certified modules

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U33, U36: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-SC09-13 Certified module](../../data/e-sc09-13-certified-module.md) the user may see: to
find, filter, total and act on many certified modules at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Health practices › Certified modules, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "certified modules" offers this view.
- **AI assistant:** "show the certified modules that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Certified modules    Health practices › Certified modules   [+ New]                                          |
| [count] [Expired] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] MODULE   STATE   APPROVAL   VALID TO                                                 |
| module            | [ ] ...                                                  Open >                          |
| approval          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Module | module | link to the record | yes |
| State | state | badge: Approved, Certified, Expired | yes |
| Approval | approval | link to the record | yes |
| Valid to | valid to | date | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Approved, Certified, Expired | the visible rows (D488) |
| Module | each linked module | the visible rows (D488) |
| Approval | each linked approval | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Certified modules of a chosen approval, or of the approvals that match a filter.
- From the other side: the approvals that have certified modules, or none.
- Certified modules of a chosen module, or of the modules that match a filter.
- From the other side: the modules that have certified modules, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Expired.
- New this month, by valid to.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Open: Approved, Certified.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New certified module | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- valid to: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-SC09-19 Certifications](../06-compliance-and-certification/s-sc09-19-certifications.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 certified modules of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no certified module the user may see yet, with the create action when allowed.
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
| Listed, U11, view Needs attention | desktop | ![Listed, U11, view Needs attention, light](../../images/lists/s-sc09-l13-certified-modules-u11-provider-admin-desktop-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-sc09-l13-certified-modules-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view Needs attention | phone | ![Listed, U11, view Needs attention, light](../../images/lists/s-sc09-l13-certified-modules-u11-provider-admin-phone-light.png) | ![Listed, U11, view Needs attention, dark](../../images/lists/s-sc09-l13-certified-modules-u11-provider-admin-phone-dark.png) |
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-sc09-l13-certified-modules-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-sc09-l13-certified-modules-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-sc09-l13-certified-modules-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-sc09-l13-certified-modules-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Health practices › Certified modules](README.md) |
| Workspaces | [U11](../../../../04-ux/views/u11-provider-admin/workspace.md), [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-SC09-03](../../flows/fl-sc09-03-insurance-billing.md), [FL-SC09-06](../../flows/fl-sc09-06-compliance-and-certification.md) |

## Open questions

None.

---

⬅️ [S-SC09-L12 Locum agreements](s-sc09-l12-locum-agreements.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC09-L14 Dispensations](s-sc09-l14-dispensations.md)
