🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Professional firms menu](README.md) › 🗂️ S-SC11-L19 Audit engagements

# 🗂️ S-SC11-L19 Audit engagements

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U49 Statutory auditor](../../../../01-users/personas/u49-statutory-auditor.md) | only the records shared with them | columns, facets and actions as their roles' field rules allow (D488) |
| [U36 Professional](../../../../01-users/personas/u36-professional.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

**Not embedded for:** U37: their use cases only read these records, inside a screen of the use case, so they open them
from there (D493).

## Purpose

The aggregated list of every [E-SC11-19 Audit engagement](../../data/e-sc11-19-audit-engagement.md) the user may see: to
find, filter, total and act on many audit engagements at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Professional firm › Audit engagements, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "audit engagements" offers this view.
- **AI assistant:** "show the audit engagements that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Audit engagements    Professional firm > Audit engagements   [+ New]                                         |
| [count] [Rotation due] [new this month]   [chart: count by state]                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| signing partner   | [ ] CLIENT   FIRST YEAR   SIGNING PART   ROTATION DAT   STATE                            |
| entity kind       | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Client | client | text | yes |
| First year | first year | text | yes |
| Signing partner | signing partner | text | yes |
| Rotation date | rotation date | date | yes |
| State | state | badge: Proposed, Active, RotationDue, Ended | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Signing partner | each value | the visible rows (D488) |
| Entity kind | each value | the visible rows (D488) |
| State | Proposed, Active, RotationDue, Ended | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Engagement letters of the mandates.
- From the other side: the clients whose letter is signed but whose engagement is not opened.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Rotation due.
- New this month, by rotation date.

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
| New audit engagement | header | the personas whose roles may create it | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

None: no field is editable in a cell.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC11-24 Audit firm](../07-notaries-brokers-officers-and-auditors/s-sc11-24-audit-firm.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 audit engagements of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no audit engagement the user may see yet, with the create action when allowed.
- **Selected:** the bulk bar with the actions allowed on every selected row.
- **Error:** the query failed, with Retry.

## Responsive behaviour

On a phone the table keeps its columns and scrolls sideways, the facet panel becomes a drawer and the KPI strip stays
(VR-14, D491).

## Accessibility

The KPI strip, the facet panel, the toolbar and the table are named landmarks; the result count is announced when the
filters change; each chip has its remove button; the facet drawer returns the focus to its button.

## Example images

Not drawn yet: step S8 draws them from this page, one row per persona and device, light and dark
([D490](../../../../06-decisions/ux/d490-example-images-for-every-persona-that-can-open-a-view.md),
[D500](../../../../06-decisions/ux/d500-images-live-in-the-specs-folders.md)).

| Shows | Device | Light | Dark |
|---|---|---|---|
| Listed, U49, view All | desktop | ![Listed, U49, view All, light](../../images/lists/s-sc11-l19-audit-engagements-u49-statutory-auditor-desktop-light.png) | ![Listed, U49, view All, dark](../../images/lists/s-sc11-l19-audit-engagements-u49-statutory-auditor-desktop-dark.png) |
| Listed, U36, view All | desktop | ![Listed, U36, view All, light](../../images/lists/s-sc11-l19-audit-engagements-u36-professional-desktop-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l19-audit-engagements-u36-professional-desktop-dark.png) |
| Listed, U36, view All | phone | ![Listed, U36, view All, light](../../images/lists/s-sc11-l19-audit-engagements-u36-professional-phone-light.png) | ![Listed, U36, view All, dark](../../images/lists/s-sc11-l19-audit-engagements-u36-professional-phone-dark.png) |
| Listed, U49, view All | phone | ![Listed, U49, view All, light](../../images/lists/s-sc11-l19-audit-engagements-u49-statutory-auditor-phone-light.png) | ![Listed, U49, view All, dark](../../images/lists/s-sc11-l19-audit-engagements-u49-statutory-auditor-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Professional firm › Audit engagements](README.md) |
| Workspaces | [U36](../../../../04-ux/views/u36-professional/workspace.md) |
| Flows | [FL-SC11-07](../../flows/fl-sc11-07-notaries-brokers-officers-and-auditors.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-SC11-L18 Service acts](s-sc11-l18-service-acts.md) · ⬆️ [Up](README.md)
