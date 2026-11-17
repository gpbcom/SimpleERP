🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Onboarding and module activation menu](README.md) › 🗂️ S-F21-L14 Migration sources

# 🗂️ S-F21-L14 Migration sources

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md) | only their own records, through the portal or the AI assistant | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U05, U45: their use cases only read these records, inside a screen of the use case, so they open
them from there (D493).

## Purpose

The aggregated list of every [E-F21-14 Migration source](../../data/e-f21-14-migration-source.md) the user may see: to
find, filter, total and act on many migration sources at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Onboarding and module activation › Migration sources, in the capability's menu (D495).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "migration sources" offers this view.
- **AI assistant:** "show the migration sources that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Migration sources    Onboarding and module activation › Migration sources   [+ New]                          |
| [count] [Errors]   [chart: count by state]                                                                   |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TOOL   STATE   FILES   MAPPING   ROWS   ERRORS                                       |
| tool              | [ ] ...                                                  Open >                          |
| files             | [ ] ...                                                  Open >                          |
| mapping           | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Tool | tool | text | yes |
| State | state | badge: Uploaded, Mapped, Imported, Errors | yes |
| Files | files | text | yes |
| Mapping | mapping | text | yes |
| Rows | rows | number, right-aligned | yes |
| Errors | errors | number, right-aligned | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Uploaded, Mapped, Imported, Errors | the visible rows (D488) |
| Tool | each value | the visible rows (D488) |
| Files | each value | the visible rows (D488) |
| Mapping | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Migration sources of a chosen tool, or of the tools that match a filter.
- From the other side: the tools that have migration sources, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Errors.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Needs attention.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New migration source | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- files: editable in its cell unless the record's state locks it.
- mapping: editable in its cell unless the record's state locks it.
- rows: editable in its cell unless the record's state locks it.
- errors: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F21-21 Migration](../05-migration-from-another-tool/s-f21-21-migration.md).

The records also show on: [S-F21-09 Import](../03-team-and-data/s-f21-09-import.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 migration sources of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no migration source the user may see yet, with the create action when allowed.
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
| Listed, U07, view Needs attention | desktop | ![Listed, U07, view Needs attention, light](../../images/lists/s-f21-l14-migration-sources-u07-administrator-desktop-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f21-l14-migration-sources-u07-administrator-desktop-dark.png) |
| Listed, U07, view Needs attention | phone | ![Listed, U07, view Needs attention, light](../../images/lists/s-f21-l14-migration-sources-u07-administrator-phone-light.png) | ![Listed, U07, view Needs attention, dark](../../images/lists/s-f21-l14-migration-sources-u07-administrator-phone-dark.png) |
| Listed, U08, view Needs attention | desktop | ![Listed, U08, view Needs attention, light](../../images/lists/s-f21-l14-migration-sources-u08-external-accountant-desktop-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f21-l14-migration-sources-u08-external-accountant-desktop-dark.png) |
| Listed, U08, view Needs attention | phone | ![Listed, U08, view Needs attention, light](../../images/lists/s-f21-l14-migration-sources-u08-external-accountant-phone-light.png) | ![Listed, U08, view Needs attention, dark](../../images/lists/s-f21-l14-migration-sources-u08-external-accountant-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Onboarding and module activation › Migration sources](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U08](../../../../04-ux/views/u08-external-accountant/workspace.md) |
| Flows | [FL-F21-03](../../flows/fl-f21-03-team-and-data.md), [FL-F21-05](../../flows/fl-f21-05-migration-from-another-tool.md) |

## Open questions

None.

---

⬅️ [S-F21-L13 Onboarding figures](s-f21-l13-onboarding-figures.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-L15 Opening balance checks](s-f21-l15-opening-balance-checks.md)
