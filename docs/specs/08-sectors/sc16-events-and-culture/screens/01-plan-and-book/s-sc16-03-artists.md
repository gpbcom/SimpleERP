🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-01 Plan and book](README.md) › 🖥️ S-SC16-03 Artists

# 🖥️ S-SC16-03 Artists

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to contract artists and manage riders
([UC-SC16-03](../../use-cases/01-plan-and-book/uc-sc16-03-contract-artists-and-manage-riders.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-01 step 3, U43 | desktop | ![FL-SC16-01 step 3, U43, light](../../images/01-plan-and-book/u43-event-producer/3-artists-desktop-light.png) | ![FL-SC16-01 step 3, U43, dark](../../images/01-plan-and-book/u43-event-producer/3-artists-desktop-dark.png) |
| FL-SC16-01 step 3, U43 | phone | ![FL-SC16-01 step 3, U43, light](../../images/01-plan-and-book/u43-event-producer/3-artists-phone-light.png) | ![FL-SC16-01 step 3, U43, dark](../../images/01-plan-and-book/u43-event-producer/3-artists-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-03-artists-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-03-artists-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-03-artists-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-03-artists-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-03-artists-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-03-artists-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-03-artists-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-03-artists-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-04 Artist contract](../../data/e-sc16-04-artist-contract.md),
[E-SC16-05 Rider item](../../data/e-sc16-05-rider-item.md), shown as the entity pages list them, with their examples.

## Actions

- Offer: [UC-SC16-03](../../use-cases/01-plan-and-book/uc-sc16-03-contract-artists-and-manage-riders.md), step 1.
- Sign: [UC-SC16-03](../../use-cases/01-plan-and-book/uc-sc16-03-contract-artists-and-manage-riders.md), step 2.
- Turn the rider into tasks:
  [UC-SC16-03](../../use-cases/01-plan-and-book/uc-sc16-03-contract-artists-and-manage-riders.md), step 3.
- Check: [UC-SC16-03](../../use-cases/01-plan-and-book/uc-sc16-03-contract-artists-and-manage-riders.md), step 4.

## States

- Normal: artists' contracts and rider tasks.
- Empty: "No artist".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a rider item missing: it stays on the checklist.
- Read-only: signed contracts are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-04 Artist contract](../../data/e-sc16-04-artist-contract.md),
[E-SC16-05 Rider item](../../data/e-sc16-05-rider-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-04 Artist contract | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U09, U43 | `u09-customer/s-sc16-03-artists-e-sc16-04-artist-contract-active-phone-{light,dark}.png`, `u43-event-producer/s-sc16-03-artists-e-sc16-04-artist-contract-active-{desktop,phone}-{light,dark}.png` |
| E-SC16-05 Rider item | Checked | Badge "Checked"; a new record starts here; next: Done (BR-SC16-07); fields editable within the role | U09, U43 | `u09-customer/s-sc16-03-artists-e-sc16-05-rider-item-checked-phone-{light,dark}.png`, `u43-event-producer/s-sc16-03-artists-e-sc16-05-rider-item-checked-{desktop,phone}-{light,dark}.png` |
| E-SC16-05 Rider item | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U09, U43 | `u09-customer/s-sc16-03-artists-e-sc16-05-rider-item-done-phone-{light,dark}.png`, `u43-event-producer/s-sc16-03-artists-e-sc16-05-rider-item-done-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-SC16-02 Venues](s-sc16-02-venues.md) · ⬆️ [Up](README.md) · ➡️ [S-SC16-04 Performers](s-sc16-04-performers.md)
