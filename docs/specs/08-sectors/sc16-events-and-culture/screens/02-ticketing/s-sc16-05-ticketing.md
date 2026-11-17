🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-02 Ticketing](README.md) › 🖥️ S-SC16-05 Ticketing

# 🖥️ S-SC16-05 Ticketing

**Status:** 🔄 waiting for the owner

## Personas

- [U44 Box-office agent](../../../../01-users/personas/u44-box-office-agent.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell tickets with seat maps and price categories,
[UC-SC16-05](../../use-cases/02-ticketing/uc-sc16-05-sell-tickets-with-seat-maps-and-price-categories.md).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-02 step 1, U44 | desktop | ![FL-SC16-02 step 1, U44, light](../../images/02-ticketing/u44-box-office-agent/1-sell-desktop-light.png) | ![FL-SC16-02 step 1, U44, dark](../../images/02-ticketing/u44-box-office-agent/1-sell-desktop-dark.png) |
| FL-SC16-02 step 1, U44 | phone | ![FL-SC16-02 step 1, U44, light](../../images/02-ticketing/u44-box-office-agent/1-sell-phone-light.png) | ![FL-SC16-02 step 1, U44, dark](../../images/02-ticketing/u44-box-office-agent/1-sell-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-05-ticketing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-05-ticketing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-05-ticketing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-05-ticketing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-05-ticketing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-05-ticketing-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-05-ticketing-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-05-ticketing-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md),
[E-SC16-08 Admission ticket](../../data/e-sc16-08-admission-ticket.md),
[E-F5-12 Event ticket](../../../../02-functional/f05-social-media/data/e-f05-12-event-ticket.md), shown as the entity
pages list them, with their examples.

## Actions

- Set the sale:
  [UC-SC16-05](../../use-cases/02-ticketing/uc-sc16-05-sell-tickets-with-seat-maps-and-price-categories.md), step 1.
- Choose seats:
  [UC-SC16-05](../../use-cases/02-ticketing/uc-sc16-05-sell-tickets-with-seat-maps-and-price-categories.md), step 2.
- Pay: [UC-SC16-05](../../use-cases/02-ticketing/uc-sc16-05-sell-tickets-with-seat-maps-and-price-categories.md), step
  3.
- Get the ticket:
  [UC-SC16-05](../../use-cases/02-ticketing/uc-sc16-05-sell-tickets-with-seat-maps-and-price-categories.md), step 4.

## States

- Normal: the seat map with categories, prices, held and sold seats.
- Empty: "Sale not open".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a seat taken meanwhile: it is refused.
- Read-only: a past show is read-only.
- Offline: not available offline: seats are held live across channels.

Shown entities (VD-15):
[E-F5-12 Event ticket](../../../../02-functional/f05-social-media/data/e-f05-12-event-ticket.md),
[E-SC16-07 Ticket order](../../data/e-sc16-07-ticket-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-12 Event ticket | Sold | Badge "Sold"; a new record starts here; next: Scanned or Refunded (UC-F5-18, UC-SC08-12); fields editable within the role | U09, U44 | `u09-customer/s-sc16-05-ticketing-e-f05-12-event-ticket-sold-phone-{light,dark}.png`, `u44-box-office-agent/s-sc16-05-ticketing-e-f05-12-event-ticket-sold-{desktop,phone}-{light,dark}.png` |
| E-SC16-07 Ticket order | Paid | Badge "Paid"; a new record starts here; next: Refunded (UC-SC16-17); fields editable within the role | U09, U44 | `u09-customer/s-sc16-05-ticketing-e-sc16-07-ticket-order-paid-phone-{light,dark}.png`, `u44-box-office-agent/s-sc16-05-ticketing-e-sc16-07-ticket-order-paid-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC16-02 Ticketing](../../flows/fl-sc16-02-ticketing.md)

## Open questions

None.

---

⬅️ [S-SC16-04 Performers](../01-plan-and-book/s-sc16-04-performers.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-06 Access control](s-sc16-06-access-control.md)
