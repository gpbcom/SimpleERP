🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔭 [F17 Competitive analysis](../../README.md) › 🖥️ [Screens](../README.md) ›
🗂️ [Views: Competitive analysis menu](README.md) › 🗂️ S-F17-L01 Competitors

# 🗂️ S-F17-L01 Competitors

**Status:** ✅ specified, reviewed by the owner on 2026-11-13 (D519); example images in step S8

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U13 Owner](../../../../01-users/personas/u13-owner.md) | as the permissions row "Competitors, signals": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U12 Marketing and communication](../../../../01-users/personas/u12-marketing.md) | as the permissions row "Competitors, signals": ✅ | actions as [permissions](../../permissions.md) gives them |
| [U03 Sales](../../../../01-users/personas/u03-sales.md) | as the permissions row "Competitors, signals": read | actions as [permissions](../../permissions.md) gives them |

## Purpose

The aggregated list of every [E-F17-01 Competitor](../../data/e-f17-01-competitor.md) the user may see: to find, filter,
total and act on many competitors at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Competitive analysis › Competitors, in the capability's menu (D495).
- **Workspaces:** 3 persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "competitors" offers this view.
- **AI assistant:** "show the competitors that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Competitors    Competitive analysis › Competitors   [+ New]                                                  |
| [count]   [chart: count by state]                                                                            |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                                  n of N results                  |
| state             | [ ] NAME   STATE   WEBSITE   FOLLOWED SIGNALS                                            |
| website           | [ ] ...                                                  Open >                          |
| followed signals  | [ ] ...                                                  Open >                          |
| Related records   |                                                                                          |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Name | name | link to the record | yes |
| State | state | badge: Active | yes |
| Website | website | link to the record | yes |
| Followed signals | followed signals | text | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| State | Active | the visible rows (D488) |
| Website | each linked website | the visible rows (D488) |
| Followed signals | each value | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Competitors of a chosen website, or of the websites that match a filter.
- From the other side: the websites that have competitors, or none.

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
| New competitor | header | the personas whose roles may create it | the record's own page (Row opens) |
| Tag | bulk bar | every persona of the list | tags the selected rows; audited |
| Delete | bulk bar | when the record's rules and the role allow | deleted; audited |
| Export | toolbar, bulk bar | every persona of the list | CSV or XLSX of the visible rows and columns; audited (T3) |
| Ask about this list | toolbar | every persona of the list | an answer from the visible rows only, with its sources (D489) |
| Chart | toolbar | every persona of the list | a C-09 chart of the filtered rows, pinnable |
| Open › | row | every persona of the list | the record's own page (Row opens) |

Each action is offered within the role and checked again on the server (VR-10).

## Inline edit

- followed signals: editable in its cell unless the record's state locks it.

## Hidden fields

None: no personal data and no secret among its fields.

## Row opens

Open › goes to [S-F17-01 Competitors](../01-set-up-and-profiles/s-f17-01-competitors.md).

The records also show on: [S-F17-02 Competitor profile](../01-set-up-and-profiles/s-f17-02-competitor-profile.md),
[S-F17-20 Competitor assistant](../03-analyse-and-arm-sales/s-f17-20-competitor-assistant.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 competitors of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no competitor the user may see yet, with the create action when allowed.
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
| Listed, U13, view All | desktop | ![Listed, U13, view All, light](../../images/lists/s-f17-l01-competitors-u13-owner-desktop-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l01-competitors-u13-owner-desktop-dark.png) |
| Listed, U13, view All | phone | ![Listed, U13, view All, light](../../images/lists/s-f17-l01-competitors-u13-owner-phone-light.png) | ![Listed, U13, view All, dark](../../images/lists/s-f17-l01-competitors-u13-owner-phone-dark.png) |
| Listed, U12, view All | desktop | ![Listed, U12, view All, light](../../images/lists/s-f17-l01-competitors-u12-marketing-desktop-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f17-l01-competitors-u12-marketing-desktop-dark.png) |
| Listed, U12, view All | phone | ![Listed, U12, view All, light](../../images/lists/s-f17-l01-competitors-u12-marketing-phone-light.png) | ![Listed, U12, view All, dark](../../images/lists/s-f17-l01-competitors-u12-marketing-phone-dark.png) |
| Listed, U03, view All | desktop | ![Listed, U03, view All, light](../../images/lists/s-f17-l01-competitors-u03-sales-desktop-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l01-competitors-u03-sales-desktop-dark.png) |
| Listed, U03, view All | phone | ![Listed, U03, view All, light](../../images/lists/s-f17-l01-competitors-u03-sales-phone-light.png) | ![Listed, U03, view All, dark](../../images/lists/s-f17-l01-competitors-u03-sales-phone-dark.png) |

## Components

[C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md),
[C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md),
[C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md),
[C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md).

## Shown in

| Where | Pages |
|---|---|
| Menu | [Competitive analysis › Competitors](README.md) |
| Workspaces | [U13](../../../../04-ux/views/u13-owner/workspace.md), [U12](../../../../04-ux/views/u12-marketing/workspace.md), [U03](../../../../04-ux/views/u03-sales/workspace.md) |
| Flows | [FL-F17-01](../../flows/fl-f17-01-set-up-and-profiles.md), [FL-F17-03](../../flows/fl-f17-03-analyse-and-arm-sales.md), [FL-F17-05](../../flows/fl-f17-05-tender-watch.md), [FL-F17-07](../../flows/fl-f17-07-sales-enablement.md) |

## Open questions

None.

---

⬅️ [S-F17-28 Technology detection](../08-ads-pages-search-and-tech/s-f17-28-tech-detection.md) · ⬆️ [Up](README.md) ·
➡️ [S-F17-L02 Company facts](s-f17-l02-company-facts.md)
