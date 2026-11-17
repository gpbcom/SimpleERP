🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-18 Plan

# 🧩 C-18 Plan

**Status:** 🔄 draft (GH-2 step S4b, from VD-19 / D501)

## Purpose

Shows places inside a building or a site, floors, rooms, bins, seats and venues, with the records in them and their
state: the floor and venue plans of
[D501](../../../06-decisions/ux/d501-maps-planning-list-views-record-pages-dashboards-in-four-domains.md).

## Anatomy

```text
+-------------------------------------------------------------------------+
| [Floor: 2 v]  [Show: rooms v]                     [+] [-]  [List view]   |
|                                                                         |
|  +--------+--------+--------+   +-----------------+                     |
|  | 201    | 202    | 203    |   | 210             |                     |
|  | Clean  | To do  | Busy   |   | Out of order    |                     |
|  +--------+--------+--------+   +-----------------+                     |
|                                                                         |
| Legend: Clean  To do  Busy  Out of order                                 |
+-------------------------------------------------------------------------+
| Room 202 · To do · Next arrival 15:00                       [Open >]    |
+-------------------------------------------------------------------------+
```

1. **Controls:** the floor or area, what to show, zoom, and **List view**, which shows the same items as a table.
2. **Plan:** the drawing of the floor or site
   [REQ-T13-08](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-08-floor-and-venue-plans.md), with
   each place as a shape.
3. **Items:** each place carries its name, its state word and an icon.
4. **Legend** and the selected item's **card** with **Open ›**.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-18-plan-desktop-light.png) | ![Variants and states, dark](../images/c-18-plan-desktop-dark.png) |

## Variants

- **Warehouse:** bins, locations and zones for picking and counts (F7, SC15).
- **Rooms by floor:** hotel rooms for housekeeping and reception (SC06); consulting rooms.
- **Restaurant floor:** tables and their service state, as on [S-F10-09
  Floor](../../../02-functional/f10-point-of-sale/screens/04-restaurant-service/s-f10-09-floor.md) (F10).
- **Venue:** rooms, areas and staff posts of a venue or a festival site (SC16).
- **Shop floor:** work centres and their operations (F12, SC05).
- **Seat map:** (Proposed) the seat map of [E-F5-11 Ticket type and seat
  map](../../../02-functional/f05-social-media/data/e-f05-11-ticket-type-and-seat-map.md) becomes one of its uses, as on
  [S-F5-17 Ticketing
  setup](../../../02-functional/f05-social-media/screens/07-events-and-ticketing/s-f05-17-ticketing-setup.md).
- **List layout:** the Plan side of an [aggregated list view](../patterns/aggregated-list-view.md) whose record type has
  places inside a building.

## States

| State | Look |
|---|---|
| No plan yet | [C-10](c-10-empty-state.md): "No plan for this floor yet"; "Draw or import a plan" for a configurator |
| Loading | (Proposed) The frame and the floor picker |
| Normal | The items and their states |
| Selected | The item outlined and its card open |
| Editing the plan | (Proposed) A configurator moves, adds or names places; the records keep their place |
| Error | The [error message pattern](../patterns/error-messages.md) |

## Tokens

Shapes on `color-surface` with `color-border-strong` outlines; states with `color-success`, `color-warning`,
`color-error` or `color-text-muted` and always their word and icon ([Colours](../../visual-identity/colours.md),
[Iconography](../../visual-identity/iconography.md)); names in `font-label`, states in `font-caption`
([Typography](../../visual-identity/typography.md)); the card as [C-04 Card](c-04-card.md).

## Accessibility

- "List view" shows the same places as a table with the same states: the plan is never the only way.
- Each place is a button named after its name and state ("Room 202, to do"); arrow keys move between neighbours
  (Proposed).
- States show by word and icon, never by colour alone.
- Zoom controls are labelled; no animation when reduced motion is asked ([Motion](../../visual-identity/motion.md)).

## Do and don't

- Do show only the records and fields the user may see
  [D12](../../../06-decisions/foundations/d12-permissions-model.md),
  [REQ-T13-06](../../../03-technical/t13-maps-and-geodata/requirements/req-t13-06-map-queries-respect-permissions.md).
- Do keep the plan's drawing apart from the records: moving a shape never changes a record.
- Don't draw a person's position on a plan.

## Used in

[S-F10-09 Floor](../../../02-functional/f10-point-of-sale/screens/04-restaurant-service/s-f10-09-floor.md) (today drawn
without this component), the plan layout of the [aggregated list view](../patterns/aggregated-list-view.md), and the
floor and venue screens to write in step S4b for F7, SC15, SC06, SC16, F12 and SC05.

## Open questions

None. Answered on 2026-11-13
([D517](../../../06-decisions/foundations/d517-the-drafts-open-points-answered-on-2026-11-13.md)): the map right
of [D502](../../../06-decisions/ux/d502-records-on-a-map-for-planners-and-managers-only.md) does not limit plans.
A plan that is a screen's own work tool, such as [S-F10-09
Floor](../../../02-functional/f10-point-of-sale/screens/04-restaurant-service/s-f10-09-floor.md) for U18 Waiter and the
seat
map for buyers, stays with that screen's personas and rights; the map right applies to the plan layout of
list views.

---

⬅️ [Map](c-17-map.md) · ⬆️ [Up](README.md)

