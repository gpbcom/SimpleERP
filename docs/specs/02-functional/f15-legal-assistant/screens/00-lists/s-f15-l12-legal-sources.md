🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Legal assistant menu](README.md) ›
🗂️ S-F15-L12 Legal sources

# 🗂️ S-F15-L12 Legal sources

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F15-12 Legal source](../../data/e-f15-12-legal-source.md) the user may see: to find,
filter, total and act on many legal sources at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Legal assistant › Legal sources, in the capability's menu (D495).
- **Workspaces:** 1 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "legal sources" offers this view.
- **AI assistant:** "show the legal sources that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Legal sources    Legal assistant › Legal sources                                                           |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   LAW PACK   KIND   PULL SCHEDUL   LAST PULL   PULL RESULT   STATE              |
| law pack          | [ ] ...                                                  Open >                          |
| kind              | [ ] ...                                                  Open >                          |
| pull schedule     | [ ] ...                                                  Open >                          |
| pull result       | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | text | yes |
| Law pack | law pack | link to the record | yes |
| Kind | kind | label | yes |
| Pull schedule | pull schedule | label | yes |
| Last pull | last pull | date and time | yes |
| Pull result | pull result | label | yes |
| State | state | badge: Active | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Law pack | each linked law pack | the visible rows (D488) |
| Kind | each value | the visible rows (D488) |
| Pull schedule | each value | the visible rows (D488) |
| Pull result | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Legal sources of a chosen law pack, or of the law packs that match a filter.
- From the other side: the law packs that have legal sources, or none.

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
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

No legal source is created or deleted here: the T11 legal corpora own the sources, their licences and their schedule
(REQ-T11-03), and a technical capability prevails over a feature page
([D573](../../../../06-decisions/foundations/d573-precedence-between-spec-pages.md)).

## Inline edit

None: the pull schedule belongs to the T11 legal corpora (REQ-T11-03), and pulls run with no human validation
(BR-F15-09).

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to
[S-F15-04 Legal assistant settings](../04-set-up-the-legal-assistant/s-f15-04-legal-assistant-settings.md).

The records also show on: [S-F15-05 Law packs refresh](../04-set-up-the-legal-assistant/s-f15-05-law-packs-refresh.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 legal sources of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no legal source the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f15-l12-legal-sources-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f15-l12-legal-sources-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f15-l12-legal-sources-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f15-l12-legal-sources-u07-administrator-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Legal assistant › Legal sources](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md) |
| Flows | [FL-F15-04](../../flows/fl-f15-04-set-up-the-legal-assistant.md) |

## Open questions

None.

---

⬅️ [S-F15-L11 Warning triggers](s-f15-l11-warning-triggers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-L13 Data protection impact assessments](s-f15-l13-data-protection-impact-assessments.md)
