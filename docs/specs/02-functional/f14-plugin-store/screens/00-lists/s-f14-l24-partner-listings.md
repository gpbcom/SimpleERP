🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) › 🗂️ [Views: Plugin store menu](README.md) ›
🗂️ S-F14-L24 Partner listings

# 🗂️ S-F14-L24 Partner listings

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U51 Reseller partner](../../../../01-users/personas/u51-reseller-partner.md) | only the records shared with them | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-F14-24 Partner listing](../../data/e-f14-24-partner-listing.md) the user may see: to
find, filter, total and act on many partner listings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Plugin store › Partner listings, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "partner listings" offers this view.
- **AI assistant:** "show the partner listings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Partner listings    Plugin store > Partner listings   [+ New]                                                |
| [count] [Applied] [new this month]   [chart: count by state]                                                 |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| countries         | [ ] PARTNER   COUNTRIES   LANGUAGES   PROJECTS DEL   SCORE   STATE                       |
| languages         | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Partner | partner | text | yes |
| Countries | countries | number | yes |
| Languages | languages | text | yes |
| Projects delivered | projects delivered | number | yes |
| Score | score | number | yes |
| State | state | badge: Applied, Listed, Declined, Suspended, Withdrawn | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Countries | each value | the visible rows (D488) |
| Languages | each value | the visible rows (D488) |
| Sectors | each value | the visible rows (D488) |
| State | Applied, Listed, Declined, Suspended, Withdrawn | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Listings whose partner has open leads.
- From the other side: the partners with a listing, or none.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Applied.
- New this month, by projects delivered.

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
| New partner listing | header | the personas whose roles may create it | the record's own page (Row opens) |
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

Open › goes to [S-F14-29 Partner directory](../08-trials-instances-and-partners/s-f14-29-partner-directory.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 partner listings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no partner listing the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f14-l24-partner-listings-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f14-l24-partner-listings-u13-owner-desktop-dark.png) |
| Listed, U51, view All | desktop | ![Listed, U51, view All, light](../../images/lists/s-f14-l24-partner-listings-u51-reseller-partner-desktop-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f14-l24-partner-listings-u51-reseller-partner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f14-l24-partner-listings-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f14-l24-partner-listings-u13-owner-phone-dark.png) |
| Listed, U51, view All | phone | ![Listed, U51, view All, light](../../images/lists/s-f14-l24-partner-listings-u51-reseller-partner-phone-light.png) | ![Listed, U51, view All, dark](../../images/lists/s-f14-l24-partner-listings-u51-reseller-partner-phone-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Plugin store › Partner listings](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md) |
| Flows | [FL-F14-08](../../flows/fl-f14-08-trials-instances-and-partners.md) |

## Open questions

This list waits for the owner's confirmation: its entity was created in the benchmark-gap interview of
2026-11-14.

---

⬅️ [S-F14-L23 Trials](s-f14-l23-trials.md) · ⬆️ [Up](README.md) · ➡️ [S-F14-L25 Themes](s-f14-l25-themes.md)
