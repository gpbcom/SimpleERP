🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-04 Stay and folio](README.md) › 🖥️ S-SC06-11 Folio

# 🖥️ S-SC06-11 Folio

**Status:** ✅ specified

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)

## Purpose

Used to check guests in and out ([UC-SC06-09](../../use-cases/04-stay-and-folio/uc-sc06-09-check-guests-in-and-out.md));
to merge room, restaurant and bar on one folio,
[UC-SC06-11](../../use-cases/04-stay-and-folio/uc-sc06-11-merge-room-restaurant-and-bar-on-one-folio.md).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-04 step 1, U28 | desktop | ![FL-SC06-04 step 1, U28, light](../../images/04-stay-and-folio/u28-hotel-receptionist/1-check-in-desktop-light.png) | ![FL-SC06-04 step 1, U28, dark](../../images/04-stay-and-folio/u28-hotel-receptionist/1-check-in-desktop-dark.png) |
| FL-SC06-04 step 1, U28 | tablet | ![FL-SC06-04 step 1, U28, light](../../images/04-stay-and-folio/u28-hotel-receptionist/1-check-in-tablet-light.png) | ![FL-SC06-04 step 1, U28, dark](../../images/04-stay-and-folio/u28-hotel-receptionist/1-check-in-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-11-folio-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-11-folio-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-11-folio-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-11-folio-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-11-folio-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-11-folio-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-11-folio-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-11-folio-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC06-08 Room reservation](../../data/e-sc06-08-room-reservation.md),
[E-SC06-09 Folio](../../data/e-sc06-09-folio.md), shown as the entity pages list them, with their examples.

## Actions

- Stay: [UC-SC06-09](../../use-cases/04-stay-and-folio/uc-sc06-09-check-guests-in-and-out.md), step 3.
- Charge to room:
  [UC-SC06-11](../../use-cases/04-stay-and-folio/uc-sc06-11-merge-room-restaurant-and-bar-on-one-folio.md), step 1.
- See the folio:
  [UC-SC06-11](../../use-cases/04-stay-and-folio/uc-sc06-11-merge-room-restaurant-and-bar-on-one-folio.md), step 2.
- Check the folio:
  [UC-SC06-11](../../use-cases/04-stay-and-folio/uc-sc06-11-merge-room-restaurant-and-bar-on-one-folio.md), step 3.
- Settle: [UC-SC06-11](../../use-cases/04-stay-and-folio/uc-sc06-11-merge-room-restaurant-and-bar-on-one-folio.md), step
  4.

## States

- Normal: the folio's charges by outlet, payers and balance.
- Empty: "No charge yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no room ready: the guest goes on a wait list and is told when
  ready.
- Read-only: a settled folio is read-only.
- Offline: not available offline: front-office and back-office work on live bookings and shared figures. Offline work is
  kept for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC06-09 Folio](../../data/e-sc06-09-folio.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-09 Folio | Open | Badge "Open"; a new record starts here; next: Settled (UC-SC06-09); fields editable within the role | U09, U18, U28 | `u09-customer/s-sc06-11-folio-e-sc06-09-folio-open-phone-{light,dark}.png`, `u18-waiter/s-sc06-11-folio-e-sc06-09-folio-open-{phone,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-11-folio-e-sc06-09-folio-open-{desktop,tablet}-{light,dark}.png` |
| E-SC06-09 Folio | Settled | Badge "Settled"; final: read-only, no next state; the history shows how it got here | U09, U18, U28 | `u09-customer/s-sc06-11-folio-e-sc06-09-folio-settled-phone-{light,dark}.png`, `u18-waiter/s-sc06-11-folio-e-sc06-09-folio-settled-{phone,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-11-folio-e-sc06-09-folio-settled-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC06-04 Stay and folio](../../flows/fl-sc06-04-stay-and-folio.md)

## Open questions

None.

---

⬅️ [S-SC06-10 Housekeeping](s-sc06-10-housekeeping.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-12 Tourist tax](../05-taxes-and-performance/s-sc06-12-tourist-tax.md)
