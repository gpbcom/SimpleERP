🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-03 People and partners](README.md) › 🖥️ S-SC16-11 Exhibitors

# 🖥️ S-SC16-11 Exhibitors

**Status:** ✅ specified

## Personas

- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell stands to exhibitors
([UC-SC16-11](../../use-cases/03-people-and-partners/uc-sc16-11-sell-stands-to-exhibitors.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-03 step 4, U43 | desktop | ![FL-SC16-03 step 4, U43, light](../../images/03-people-and-partners/u43-event-producer/4-stands-desktop-light.png) | ![FL-SC16-03 step 4, U43, dark](../../images/03-people-and-partners/u43-event-producer/4-stands-desktop-dark.png) |
| FL-SC16-03 step 4, U43 | phone | ![FL-SC16-03 step 4, U43, light](../../images/03-people-and-partners/u43-event-producer/4-stands-phone-light.png) | ![FL-SC16-03 step 4, U43, dark](../../images/03-people-and-partners/u43-event-producer/4-stands-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-11-exhibitors-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-11-exhibitors-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-11-exhibitors-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-11-exhibitors-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-11-exhibitors-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-11-exhibitors-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-11-exhibitors-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-11-exhibitors-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-12 Stand](../../data/e-sc16-12-stand.md),
[E-F2-18 Resource booking](../../../../02-functional/f02-no-code-configuration/data/e-f02-18-resource-booking.md), shown
as the entity pages list them, with their examples.

## Actions

- Sell the stand: [UC-SC16-11](../../use-cases/03-people-and-partners/uc-sc16-11-sell-stands-to-exhibitors.md), step 1.
- Add services: [UC-SC16-11](../../use-cases/03-people-and-partners/uc-sc16-11-sell-stands-to-exhibitors.md), step 2.
- Invoice: [UC-SC16-11](../../use-cases/03-people-and-partners/uc-sc16-11-sell-stands-to-exhibitors.md), step 3.
- Confirm: [UC-SC16-11](../../use-cases/03-people-and-partners/uc-sc16-11-sell-stands-to-exhibitors.md), step 4.

## States

- Normal: the floor plan with stands, exhibitors and services.
- Empty: "No stand".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the stand taken: another is proposed,
  [BR-F2-18](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-18-one-booking-per-resource-and-slot.md).
- Read-only: invoiced stands are read-only.
- Offline: not available offline: office work on budgets, contracts and declarations. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC16-12 Stand](../../data/e-sc16-12-stand.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-12 Stand | Proposed | Badge "Proposed"; a new record starts here; next: Invoiced (UC-SC16-11); fields editable within the role | U09, U43 | `u09-customer/s-sc16-11-exhibitors-e-sc16-12-stand-proposed-phone-{light,dark}.png`, `u43-event-producer/s-sc16-11-exhibitors-e-sc16-12-stand-proposed-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-03 People and partners](../../flows/fl-sc16-03-people-and-partners.md)

## Open questions

None.

---

⬅️ [S-SC16-10 Sponsors](s-sc16-10-sponsors.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-12 Bars and merchandise](../04-on-site/s-sc16-12-bars-and-merchandise.md)
