🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: No-code configuration menu](README.md) › 🗂️ S-F2-L10 Configuration versions

# 🗂️ S-F2-L10 Configuration versions

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

## Purpose

The aggregated list of every [E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md) the user may
see: to find, filter, total and act on many configuration versions at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Configuration versions, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "configuration versions" offers this view.
- **AI assistant:** "show the configuration versions that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Configuration versions    Administration › Configuration versions   [+ New]                                  |
| [count] [new this month]   [chart: count by state]                                                           |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NUMBER   STATE   PUBLISHED BY   PUBLISHED AT                                         |
| published by      | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Number | number | number, right-aligned | yes |
| State | state | badge: Published, Superseded | yes |
| Published by | published by | person's name | yes |
| Published at | published at | date and time | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Published, Superseded | the visible rows (D488) |
| Published by | each person, the user first | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: configuration versions link to no other record type in their fields.

## KPI strip

- Count of the visible rows.
- New this month, by published at.

Recomputed on the filtered visible rows (D487, C-16).

## Default chart

Count by state (VR-8); the Chart button turns the filtered list into a chart the user can pin to their home screen
(C-09).

## Saved views

- All.
- Mine: published by.
- Recently changed.

Each persona's default saved view is set in its workspace (see Shown in).

## Map layout

None: no place.

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New configuration version | header | U07 and the administration roles | the record's own page (Row opens) |
| Change state | bulk bar | the personas whose roles may change it | allowed transitions only; audited (T3) |
| Assign | bulk bar | the personas whose roles may assign | sets the published by; audited |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- published at: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| published by | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F2-10 Publish and versions](../05-publish-and-roll-back/s-f02-10-publish-and-versions.md).

The records also show on: [S-F2-11 Packs](../06-share-a-configuration/s-f02-11-packs.md),
[S-F2-22 Impact analysis](../10-change-safely/s-f02-22-impact-analysis.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 configuration versions of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no configuration version the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f02-l10-configuration-versions-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f02-l10-configuration-versions-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f02-l10-configuration-versions-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f02-l10-configuration-versions-u07-administrator-phone-dark.png) |
| Listed, U11, view All | desktop | ![Listed, U11, view All, light](../../images/lists/s-f02-l10-configuration-versions-u11-provider-admin-desktop-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f02-l10-configuration-versions-u11-provider-admin-desktop-dark.png) |
| Listed, U11, view All | phone | ![Listed, U11, view All, light](../../images/lists/s-f02-l10-configuration-versions-u11-provider-admin-phone-light.png) | ![Listed, U11, view All, dark](../../images/lists/s-f02-l10-configuration-versions-u11-provider-admin-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Configuration versions](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U11](../../../../04-ux/views/u11-provider-admin/workspace.md) |
| Flows | [FL-F1-08](../../../f01-administration/flows/fl-f01-08-provider-and-client-companies.md), [FL-F2-01](../../flows/fl-f02-01-configure-a-record-type.md), [FL-F2-05](../../flows/fl-f02-05-publish-and-roll-back.md), [FL-F2-10](../../flows/fl-f02-10-change-safely.md), [FL-F2-12](../../flows/fl-f02-12-set-up-request-types.md) |

## Open questions

None.

---

⬅️ [S-F2-L09 Workflows](s-f02-l09-workflows.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-L11 Configuration packs](s-f02-l11-configuration-packs.md)
