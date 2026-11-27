🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-03 Rooms and bookings](README.md) › 🖥️ S-SC06-15 Hospitality assistant

# 🖥️ S-SC06-15 Hospitality assistant

**Status:** 🔄 waiting for the owner

## Personas

- [U28 Hotel receptionist](../../../../01-users/personas/u28-hotel-receptionist.md)
- [U23 Store manager](../../../../01-users/personas/u23-store-manager.md)

## Purpose

Used to ask the AI assistant about the hotel or restaurant,
[UC-SC06-15](../../use-cases/03-rooms-and-bookings/uc-sc06-15-ask-the-assistant-about-the-hotel-or-restaurant.md).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-03 step 3, U28 | desktop | ![FL-SC06-03 step 3, U28, light](../../images/03-rooms-and-bookings/u28-hotel-receptionist/3-assistant-desktop-light.png) | ![FL-SC06-03 step 3, U28, dark](../../images/03-rooms-and-bookings/u28-hotel-receptionist/3-assistant-desktop-dark.png) |
| FL-SC06-03 step 3, U28 | tablet | ![FL-SC06-03 step 3, U28, light](../../images/03-rooms-and-bookings/u28-hotel-receptionist/3-assistant-tablet-light.png) | ![FL-SC06-03 step 3, U28, dark](../../images/03-rooms-and-bookings/u28-hotel-receptionist/3-assistant-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-15-hospitality-assistant-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-15-hospitality-assistant-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-15-hospitality-assistant-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-15-hospitality-assistant-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-15-hospitality-assistant-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-15-hospitality-assistant-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc06-15-hospitality-assistant-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc06-15-hospitality-assistant-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC06-08 Room reservation](../../data/e-sc06-08-room-reservation.md),
[E-SC06-02 Menu dish](../../data/e-sc06-02-menu-dish.md), shown as the entity pages list them, with their examples.

## Actions

- Ask:
  [UC-SC06-15](../../use-cases/03-rooms-and-bookings/uc-sc06-15-ask-the-assistant-about-the-hotel-or-restaurant.md),
  step 1.
- Confirm an action:
  [UC-SC06-15](../../use-cases/03-rooms-and-bookings/uc-sc06-15-ask-the-assistant-about-the-hotel-or-restaurant.md),
  step 4.

## States

- Normal: the conversation with answers, links and prepared actions.
- Empty: suggested questions.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an action beyond the user's rights: the AI assistant refuses and
  says which role can do it.
- Read-only: answers only for roles that cannot act.
- Offline: not available offline: the AI assistant needs the network; the last answers stay readable.

Shown entities (VD-15): [E-SC06-08 Room reservation](../../data/e-sc06-08-room-reservation.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-08 Room reservation | Arrived | Badge "Arrived"; next: Departed or Cancelled (UC-SC06-09, BR-SC06-09); fields editable within the role | U23, U28 | `u23-store-manager/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-arrived-{desktop,phone,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-arrived-{desktop,tablet}-{light,dark}.png` |
| E-SC06-08 Room reservation | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U23, U28 | `u23-store-manager/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-cancelled-{desktop,phone,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-cancelled-{desktop,tablet}-{light,dark}.png` |
| E-SC06-08 Room reservation | Departed | Badge "Departed"; final: read-only, no next state; the history shows how it got here | U23, U28 | `u23-store-manager/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-departed-{desktop,phone,tablet}-{light,dark}.png`, `u28-hotel-receptionist/s-sc06-15-hospitality-assistant-e-sc06-08-room-reservation-departed-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC06-03 Rooms and bookings](../../flows/fl-sc06-03-rooms-and-bookings.md)

## Open questions

None.

---

⬅️ [S-SC06-14 Performance](../05-taxes-and-performance/s-sc06-14-performance.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-16 Campsite](../06-campsites-catering-groups-and-pricing/s-sc06-16-campsite.md)
