🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Onboarding and module activation menu](README.md) › 🗂️ S-F21-L16 Language settings

# 🗂️ S-F21-L16 Language settings

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U01 Employee](../../../../01-users/personas/u01-employee.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

**Not embedded for:** U07: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-F21-16 Language setting](../../data/e-f21-16-language-setting.md) the user may see: to
find, filter, total and act on many language settings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Language settings, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "language settings" offers this view.
- **AI assistant:** "show the language settings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Language settings    Administration › Language settings   [+ New]                                            |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] SCOPE   STATE   LANGUAGE                                                             |
| scope             | [ ] ...                                                  Open >                          |
| language          | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Scope | scope | text | yes |
| State | state | badge: Set, Changed | yes |
| Language | language | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Set, Changed | the visible rows (D488) |
| Scope | each value | the visible rows (D488) |
| Language | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: language settings link to no other record type in their fields.

## KPI strip

- Count of the visible rows.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New language setting | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- language: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F21-24 Languages](../01-first-run/s-f21-24-languages.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 language settings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no language setting the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f21-l16-language-settings-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f21-l16-language-settings-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f21-l16-language-settings-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f21-l16-language-settings-u13-owner-phone-dark.png) |
| Listed, U01, view All | desktop | ![Listed, U01, view All, light](../../images/lists/s-f21-l16-language-settings-u01-employee-desktop-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f21-l16-language-settings-u01-employee-desktop-dark.png) |
| Listed, U01, view All | phone | ![Listed, U01, view All, light](../../images/lists/s-f21-l16-language-settings-u01-employee-phone-light.png) | ![Listed, U01, view All, dark](../../images/lists/s-f21-l16-language-settings-u01-employee-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Language settings](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U01](../../../../04-ux/views/u01-employee/workspace.md) |
| Flows | [FL-F20-07](../../../f20-hosted-support-assistant/flows/fl-f20-07-employees-help.md), [FL-F21-01](../../flows/fl-f21-01-first-run.md) |

## Open questions

None.

---

⬅️ [S-F21-L15 Opening balance checks](s-f21-l15-opening-balance-checks.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-L17 Migration guides](s-f21-l17-migration-guides.md)
