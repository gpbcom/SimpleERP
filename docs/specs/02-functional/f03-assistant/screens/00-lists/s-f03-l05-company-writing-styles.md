🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Assistant menu](README.md) › 🗂️ S-F3-L05 Company writing styles

# 🗂️ S-F3-L05 Company writing styles

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U07 Administrator](../../../../01-users/personas/u07-administrator.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | an admin list (D494): settings and technical records |

**Not embedded for:** U01, U02, U03, U04, U05, U06, U12, U14, U15, U16: their use cases work on these records, but a
setting: the owner confirmed it for U07 and U13 only (D519).

## Purpose

The aggregated list of every [E-F3-05 Company writing style](../../data/e-f03-05-company-writing-style.md) the user may
see: to find, filter, total and act on many company writing styles at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Administration › Company writing styles, in the Administration menu (D494).
- **Workspaces:** 2 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "company writing styles" offers this view.
- **AI assistant:** "show the company writing styles that need attention" opens it with the filter as editable chips
  (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Company writing styles    Administration › Company writing styles   [+ New]                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] TONE   STATE   WORDS TO USE   WORDS TO AVOID                                         |
| words to use      | [ ] ...                                                  Open >                          |
| words to avoid    | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Tone | tone | label | yes |
| State | state | badge: Active | yes |
| Words to use | words to use | text | yes |
| Words to avoid | words to avoid | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Words to use | each value | the visible rows (D488) |
| Words to avoid | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

None: company writing styles link to no other record type in their fields.

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
| New company writing style | header | U07 and the administration roles | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- words to use: editable in its cell unless the record's state locks it.
- words to avoid: editable in its cell unless the record's state locks it.

## Hidden fields

| Field | Why | Shown to | Hidden for |
|---|---|---|---|
| sample texts | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-F3-03 Writing style settings](../04-summarise-or-draft/s-f03-03-writing-style-settings.md).

The records also show on: [S-F3-01 Assistant panel](../01-ask-the-assistant/s-f03-01-assistant-panel.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 company writing styles of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no company writing style the user may see yet, with the create action when allowed.
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
| Listed, U07, view All | desktop | ![Listed, U07, view All, light](../../images/lists/s-f03-l05-company-writing-styles-u07-administrator-desktop-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l05-company-writing-styles-u07-administrator-desktop-dark.png) |
| Listed, U07, view All | phone | ![Listed, U07, view All, light](../../images/lists/s-f03-l05-company-writing-styles-u07-administrator-phone-light.png) | ![Listed, U07, view All, dark](../../images/lists/s-f03-l05-company-writing-styles-u07-administrator-phone-dark.png) |
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f03-l05-company-writing-styles-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l05-company-writing-styles-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f03-l05-company-writing-styles-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f03-l05-company-writing-styles-u13-owner-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Administration › Company writing styles](README.md) |
| Workspaces | [U07](../../../../04-ux/views/u07-administrator/workspace.md), [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F3-04](../../flows/fl-f03-04-summarise-or-draft.md) |

## Open questions

None.

---

⬅️ [S-F3-L04 Assistant change batches](s-f03-l04-assistant-change-batches.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-L06 Configuration requests](s-f03-l06-configuration-requests.md)
