🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Education and training menu](README.md) › 🗂️ S-SC12-L21 Driving lessons

# 🗂️ S-SC12-L21 Driving lessons

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U39 Trainer](../../../../01-users/personas/u39-trainer.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC12-21 Driving lesson](../../data/e-sc12-21-driving-lesson.md) the user may see: to
find, filter, total and act on many driving lessons at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Education and training › Driving lessons, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "driving lessons" offers this view.
- **AI assistant:** "show the driving lessons that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Driving lessons    Education and training > Driving lessons   [+ New]                                        |
| [count] [Booked] [new this month]   [chart: count by state]                                                  |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| instructor        | [ ] LEARNER   INSTRUCTOR   VEHICLE   STARTS AT   HOURS   STATE                           |
| vehicle           | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Learner | learner | text | yes |
| Instructor | instructor | text | yes |
| Vehicle | vehicle | text | yes |
| Starts at | starts at | date and time | yes |
| Hours | hours | number | yes |
| State | state | badge: Booked, Done, Cancelled, Missed | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Instructor | each value | the visible rows (D488) |
| Vehicle | each value | the visible rows (D488) |
| State | Booked, Done, Cancelled, Missed | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Funding lines for lessons paid by a training account.
- From the other side: the instructors with no lesson this week.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Booked.
- New this month, by starts at.

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
| New driving lesson | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| learner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC12-22](../06-apprentices-driving-nurseries-and-canteens/s-sc12-22-driving-school.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 driving lessons of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no driving lesson the user may see yet, with the create action when allowed.
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
| Listed, U38, view All | desktop | ![Listed, U38, view All, light](../../images/lists/s-sc12-l21-driving-lessons-u38-training-coordinator-desktop-light.png) | ![Listed, U38, view All, dark](../../images/lists/s-sc12-l21-driving-lessons-u38-training-coordinator-desktop-dark.png) |
| Listed, U39, view All | phone | ![Listed, U39, view All, light](../../images/lists/s-sc12-l21-driving-lessons-u39-trainer-phone-light.png) | ![Listed, U39, view All, dark](../../images/lists/s-sc12-l21-driving-lessons-u39-trainer-phone-dark.png) |
| Listed, U38, view All | phone | ![Listed, U38, view All, light](../../images/lists/s-sc12-l21-driving-lessons-u38-training-coordinator-phone-light.png) | ![Listed, U38, view All, dark](../../images/lists/s-sc12-l21-driving-lessons-u38-training-coordinator-phone-dark.png) |
| Listed, U39, view All | desktop | ![Listed, U39, view All, light](../../images/lists/s-sc12-l21-driving-lessons-u39-trainer-desktop-light.png) | ![Listed, U39, view All, dark](../../images/lists/s-sc12-l21-driving-lessons-u39-trainer-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Education and training › Driving lessons](README.md) |
| Workspaces | [U38](../../../../04-ux/views/u38-training-coordinator/workspace.md), [U39](../../../../04-ux/views/u39-trainer/workspace.md) |
| Flows | [FL-SC12-06](../../flows/fl-sc12-06-apprentices-driving-nurseries-and-canteens.md) |

## Open questions

None.

---

⬅️ [S-SC12-L20 Apprenticeship contracts](s-sc12-l20-apprenticeship-contracts.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-L22 Childcare places](s-sc12-l22-childcare-places.md)
