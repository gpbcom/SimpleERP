🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-01 Subscriptions and billing](README.md) ›
🖥️ S-SC14-01 Subscriptions

# 🖥️ S-SC14-01 Subscriptions

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell subscriptions with plans and seats,
[UC-SC14-01](../../use-cases/01-subscriptions-and-billing/uc-sc14-01-sell-subscriptions-with-plans-and-seats.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-01 step 1, U03 | desktop | ![FL-SC14-01 step 1, U03, light](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-desktop-light.png) | ![FL-SC14-01 step 1, U03, dark](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-desktop-dark.png) |
| FL-SC14-01 step 1, U03 | phone | ![FL-SC14-01 step 1, U03, light](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-phone-light.png) | ![FL-SC14-01 step 1, U03, dark](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-phone-dark.png) |
| FL-SC14-01 step 1, U03 | tablet | ![FL-SC14-01 step 1, U03, light](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-tablet-light.png) | ![FL-SC14-01 step 1, U03, dark](../../images/01-subscriptions-and-billing/u03-sales/1-subscription-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-01-subscriptions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-01-subscriptions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-01-subscriptions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-01-subscriptions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-01-subscriptions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-01-subscriptions-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-01-subscriptions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-01-subscriptions-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-01 Software subscription](../../data/e-sc14-01-software-subscription.md), shown as the entity
pages list them, with their examples.

## Actions

- Choose a plan:
  [UC-SC14-01](../../use-cases/01-subscriptions-and-billing/uc-sc14-01-sell-subscriptions-with-plans-and-seats.md), step
  1.
- Set seats:
  [UC-SC14-01](../../use-cases/01-subscriptions-and-billing/uc-sc14-01-sell-subscriptions-with-plans-and-seats.md), step
  2.
- Subscribe:
  [UC-SC14-01](../../use-cases/01-subscriptions-and-billing/uc-sc14-01-sell-subscriptions-with-plans-and-seats.md), step
  3.
- Bill:
  [UC-SC14-01](../../use-cases/01-subscriptions-and-billing/uc-sc14-01-sell-subscriptions-with-plans-and-seats.md), step
  4.

## States

- Normal: subscriptions with plan, seats, term and state.
- Empty: "No subscription".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, seats below the minimum: it is refused.
- Read-only: a cancelled subscription is read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-01 Software subscription](../../data/e-sc14-01-software-subscription.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-01 Software subscription | Trial | Badge "Trial"; a new record starts here; next: Active (UC-SC14-01); fields editable within the role | U03, U05, U09 | `u03-sales/s-sc14-01-subscriptions-e-sc14-01-software-subscription-trial-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc14-01-subscriptions-e-sc14-01-software-subscription-trial-desktop-{light,dark}.png`, `u09-customer/s-sc14-01-subscriptions-e-sc14-01-software-subscription-trial-phone-{light,dark}.png` |
| E-SC14-01 Software subscription | Active | Badge "Active"; next: Ended or Suspended (BR-SC14-02); fields editable within the role | U03, U05, U09 | `u03-sales/s-sc14-01-subscriptions-e-sc14-01-software-subscription-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc14-01-subscriptions-e-sc14-01-software-subscription-active-desktop-{light,dark}.png`, `u09-customer/s-sc14-01-subscriptions-e-sc14-01-software-subscription-active-phone-{light,dark}.png` |
| E-SC14-01 Software subscription | Suspended | Badge "Suspended"; next: Ended (BR-SC14-02); fields editable within the role | U03, U05, U09 | `u03-sales/s-sc14-01-subscriptions-e-sc14-01-software-subscription-suspended-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc14-01-subscriptions-e-sc14-01-software-subscription-suspended-desktop-{light,dark}.png`, `u09-customer/s-sc14-01-subscriptions-e-sc14-01-software-subscription-suspended-phone-{light,dark}.png` |

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

- [FL-SC14-01 Subscriptions and billing](../../flows/fl-sc14-01-subscriptions-and-billing.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-SC14-02 Usage](s-sc14-02-usage.md)
