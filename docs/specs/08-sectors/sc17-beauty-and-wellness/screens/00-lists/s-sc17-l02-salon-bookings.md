🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💇 [SC17 Beauty and wellness](../../README.md) ›
🖥️ [Screens](../README.md) › 🗂️ [Views: Beauty and wellness menu](README.md) › 🗂️ S-SC17-L02 Salon bookings

# 🗂️ S-SC17-L02 Salon bookings

**Status:** ✅ specified

## Personas

| Persona | Rows they see | What differs |
|---|---|---|
| [U09 Customer](../../../../01-users/personas/u09-customer.md) | only the records shared with them | columns, facets and actions as their roles' field rules allow (D488) |
| [U23 Store manager](../../../../01-users/personas/u23-store-manager.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |
| [U52 Beautician](../../../../01-users/personas/u52-beautician.md) | the records their roles' record rules allow (T2) | columns, facets and actions as their roles' field rules allow (D488) |

## Purpose

The aggregated list of every [E-SC17-02 Salon booking](../../data/e-sc17-02-salon-booking.md) the user may see: to find,
filter, total and act on many salon bookings at once
([D484](../../../../06-decisions/ux/d484-aggregated-list-view-per-record-type-and-persona-workspaces.md),
[D485](../../../../06-decisions/ux/d485-every-entity-has-an-aggregated-view.md)). Written from the
[list view template](../../../../_templates/list-view.md) and the
[aggregated list view pattern](../../../../04-ux/design-system/patterns/aggregated-list-view.md).

## Entry points

- **Menu:** Beauty and wellness › Salon bookings, in the capability's menu (D495).
- **Workspaces:** the persona workspaces embed it, each on its persona's default saved view (D493): see Shown in.
- **Global search:** typing "salon bookings" offers this view.
- **AI assistant:** "show the salon bookings that need attention" opens it with the filter as editable chips (D486).

## Wireframe

```text
+--------------------------------------------------------------------------------------------------------------+
| Salon bookings    Beauty and wellness > Salon bookings   [+ New]                                             |
| [count] [Held] [new this month]   [chart: count by state]                                                    |
| [View: All v] [* Describe what you want to see...] [Filter] [Chart] [Export] [Ask about this list]           |
| FACETS            | (chips)                                              n of N results                      |
| staff member      | [ ] CUSTOMER   STAFF MEMBER   CABIN   STARTS AT   STATE                                  |
| channel           | [ ] ...                                              Open >                              |
| Related records   | [ ] ...                                              Open >                              |
| Counts, totals, facets and the chart use only the records you may see.                                       |
+--------------------------------------------------------------------------------------------------------------+
```

## Columns

| Label | Field | Format | Sortable |
|---|---|---|---|
| Customer | customer | text | yes |
| Staff member | staff member | text | yes |
| Cabin | cabin | text | yes |
| Starts at | starts at | date and time | yes |
| State | state | badge: Held, Confirmed, Cancelled, Arrived, Done, NoShow | yes |

Secrets are never a column (VR-4).

## Facets

| Facet | Values | Counted on |
|---|---|---|
| Staff member | each value | the visible rows (D488) |
| Channel | each value | the visible rows (D488) |
| State | Held, Confirmed, Cancelled, Arrived, Done, NoShow | the visible rows (D488) |

Eligible for: None: these records are neither people who can be scheduled nor work to schedule (D511).

## Related-record filters

- Booking deposits of the bookings.
- From the other side: the cabins used.

## KPI strip

- Count of the visible rows.
- Needs attention: count in the state Held.
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
| New salon booking | header | the personas whose roles may create it | the record's own page (Row opens) |
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
| customer | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |
| owner | personal data | the roles whose field rules may read it, and the person concerned | the other personas of this list: never a column, a facet, a filter, a chart axis or a plain-words filter target |

## Row opens

Open › goes to [S-SC17-02 Online booking](../01-book-staff-and-cabins/s-sc17-02-online-booking.md).

## States

- **Loading:** the KPI strip, the facets and the table as placeholders.
- **Listed:** the first 50 salon bookings of the saved view, with the KPI strip and the facet counts.
- **Filtered:** the chips of the filter or the plain words, and the result count.
- **No result:** "Nothing matches these filters", with Clear filters.
- **Empty:** no salon booking the user may see yet, with the create action when allowed.
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
| Listed, U09, view All | phone | ![Listed, U09, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u09-customer-phone-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u09-customer-phone-dark.png) |
| Listed, U23, view All | desktop | ![Listed, U23, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u23-store-manager-desktop-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u23-store-manager-desktop-dark.png) |
| Listed, U23, view All | phone | ![Listed, U23, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u23-store-manager-phone-light.png) | ![Listed, U23, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u23-store-manager-phone-dark.png) |
| Listed, U52, view All | desktop | ![Listed, U52, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u52-beautician-desktop-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u52-beautician-desktop-dark.png) |
| Listed, U52, view All | phone | ![Listed, U52, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u52-beautician-phone-light.png) | ![Listed, U52, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u52-beautician-phone-dark.png) |
| Listed, U09, view All | desktop | ![Listed, U09, view All, light](../../images/lists/s-sc17-l02-salon-bookings-u09-customer-desktop-light.png) | ![Listed, U09, view All, dark](../../images/lists/s-sc17-l02-salon-bookings-u09-customer-desktop-dark.png) |

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-15 Facet panel](../../../../04-ux/design-system/components/c-15-facet-panel.md)
- [C-16 KPI strip](../../../../04-ux/design-system/components/c-16-kpi-strip.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)

## Shown in

| Where | Pages |
|---|---|
| Menu | [Beauty and wellness › Salon bookings](README.md) |
| Workspaces | [U09](../../../../04-ux/views/u09-customer/workspace.md), [U23](../../../../04-ux/views/u23-store-manager/workspace.md), [U52](../../../../04-ux/views/u52-beautician/workspace.md) |
| Flows | [FL-SC17-01](../../flows/fl-sc17-01-book-staff-and-cabins.md) |

## Open questions

None.

---

⬅️ [S-SC17-L01 Cabins](s-sc17-l01-cabins.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC17-L03 Booking deposits](s-sc17-l03-booking-deposits.md)
