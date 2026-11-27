🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-01 Plan and book](README.md) › 🖥️ S-SC16-02 Venues

# 🖥️ S-SC16-02 Venues

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Used to book venues and rooms ([UC-SC16-02](../../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-01 step 2, U43 | desktop | ![FL-SC16-01 step 2, U43, light](../../images/01-plan-and-book/u43-event-producer/2-venue-desktop-light.png) | ![FL-SC16-01 step 2, U43, dark](../../images/01-plan-and-book/u43-event-producer/2-venue-desktop-dark.png) |
| FL-SC16-01 step 2, U43 | phone | ![FL-SC16-01 step 2, U43, light](../../images/01-plan-and-book/u43-event-producer/2-venue-phone-light.png) | ![FL-SC16-01 step 2, U43, dark](../../images/01-plan-and-book/u43-event-producer/2-venue-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-02-venues-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-02-venues-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-02-venues-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-02-venues-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-02-venues-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-02-venues-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-02-venues-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-02-venues-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-03 Venue room](../../data/e-sc16-03-venue-room.md),
[E-F2-18 Resource booking](../../../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md), shown
as the entity pages list them, with their examples.

For a cinema venue, a Cinema card adds:

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| CNC ticketing approval number | E-SC16-03 CNC ticketing approval number | text | yes | for a cinema, before any ticket is sold |
| Delivery and installation declared on | E-SC16-03 delivery and installation declared on | date, not in the future | yes | for a cinema, before any ticket is sold |

Until both are recorded, the cinema sells no ticket at the box office or online
([BR-SC16-17](../../business-rules/br-sc16-17-box-office-figures-are-reported-to-the-cnc.md),
[D575](../../../../06-decisions/foundations/d575-answers-of-2026-11-27-on-the-last-open-points.md) point 13).

## Actions

- Find a venue: [UC-SC16-02](../../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md), step 1.
- Check capacity: [UC-SC16-02](../../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md), step 2.
- Book: [UC-SC16-02](../../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md), step 3.
- Confirm: [UC-SC16-02](../../use-cases/01-plan-and-book/uc-sc16-02-book-venues-and-rooms.md), step 4.

## States

- Normal: venues and rooms with capacity and bookings.
- Empty: "No room".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, capacity too small: the producer is warned.
- Read-only: past bookings are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-03 Venue room](../../data/e-sc16-03-venue-room.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-03 Venue room | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U43 | `u43-event-producer/s-sc16-02-venues-e-sc16-03-venue-room-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC16-01 Plan and book](../../flows/fl-sc16-01-plan-and-book.md)

## Open questions

None.

---

⬅️ [S-SC16-01 Event plan](s-sc16-01-event-plan.md) · ⬆️ [Up](README.md) · ➡️ [S-SC16-03 Artists](s-sc16-03-artists.md)
