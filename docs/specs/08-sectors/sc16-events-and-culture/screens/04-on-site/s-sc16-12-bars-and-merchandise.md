🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎭 [SC16 Events and culture](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC16-04 On site](README.md) › 🖥️ S-SC16-12 Bars and merchandise

# 🖥️ S-SC16-12 Bars and merchandise

**Status:** 🔄 waiting for the owner

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U43 Event producer](../../../../01-users/personas/u43-event-producer.md)

## Purpose

Used to run bars and merchandise ([UC-SC16-12](../../use-cases/04-on-site/uc-sc16-12-run-bars-and-merchandise.md)).

## Entry points

Events and culture in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC16-04 step 1, U17 | desktop | ![FL-SC16-04 step 1, U17, light](../../images/04-on-site/u17-cashier/1-bar-desktop-light.png) | ![FL-SC16-04 step 1, U17, dark](../../images/04-on-site/u17-cashier/1-bar-desktop-dark.png) |
| FL-SC16-04 step 1, U17 | phone | ![FL-SC16-04 step 1, U17, light](../../images/04-on-site/u17-cashier/1-bar-phone-light.png) | ![FL-SC16-04 step 1, U17, dark](../../images/04-on-site/u17-cashier/1-bar-phone-dark.png) |
| FL-SC16-04 step 1, U17 | tablet | ![FL-SC16-04 step 1, U17, light](../../images/04-on-site/u17-cashier/1-bar-tablet-light.png) | ![FL-SC16-04 step 1, U17, dark](../../images/04-on-site/u17-cashier/1-bar-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc16-12-bars-and-merchandise-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc16-12-bars-and-merchandise-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc16-12-bars-and-merchandise-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc16-12-bars-and-merchandise-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc16-12-bars-and-merchandise-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc16-12-bars-and-merchandise-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc16-12-bars-and-merchandise-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc16-12-bars-and-merchandise-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC16-13 Event till](../../data/e-sc16-13-event-till.md), shown as the entity pages list them, with
their examples.

## Actions

- Open the tills: [UC-SC16-12](../../use-cases/04-on-site/uc-sc16-12-run-bars-and-merchandise.md), step 1.
- Sell: [UC-SC16-12](../../use-cases/04-on-site/uc-sc16-12-run-bars-and-merchandise.md), step 2.
- Close: [UC-SC16-12](../../use-cases/04-on-site/uc-sc16-12-run-bars-and-merchandise.md), step 3.
- Post: [UC-SC16-12](../../use-cases/04-on-site/uc-sc16-12-run-bars-and-merchandise.md), step 4.

## States

- Normal: event tills with sales and licence.
- Empty: "No till open".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a drink outside the licence: it is refused.
- Read-only: closed tills are read-only.
- Offline: tills sell offline,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md).

Shown entities (VD-15): [E-SC16-13 Event till](../../data/e-sc16-13-event-till.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC16-13 Event till | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U17, U43 | `u17-cashier/s-sc16-12-bars-and-merchandise-e-sc16-13-event-till-recorded-{desktop,phone,tablet}-{light,dark}.png`, `u43-event-producer/s-sc16-12-bars-and-merchandise-e-sc16-13-event-till-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC16-04 On site](../../flows/fl-sc16-04-on-site.md)

## Open questions

None.

---

⬅️ [S-SC16-11 Exhibitors](../03-people-and-partners/s-sc16-11-exhibitors.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC16-13 Safety](s-sc16-13-safety.md)
