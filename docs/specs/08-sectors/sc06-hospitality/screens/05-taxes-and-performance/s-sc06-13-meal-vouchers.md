🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🍽️ [SC06 Restaurant and hospitality](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC06-05 Taxes and performance](README.md) › 🖥️ S-SC06-13 Meal vouchers

# 🖥️ S-SC06-13 Meal vouchers

**Status:** 🔄 waiting for the owner

## Personas

- [U17 Cashier](../../../../01-users/personas/u17-cashier.md)
- [U18 Waiter](../../../../01-users/personas/u18-waiter.md)

## Purpose

Used to accept meal vouchers
([UC-SC06-13](../../use-cases/05-taxes-and-performance/uc-sc06-13-accept-meal-vouchers.md)).

## Entry points

Restaurant and hospitality in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC06-05 step 2, U17 | desktop | ![FL-SC06-05 step 2, U17, light](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-desktop-light.png) | ![FL-SC06-05 step 2, U17, dark](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-desktop-dark.png) |
| FL-SC06-05 step 2, U17 | phone | ![FL-SC06-05 step 2, U17, light](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-phone-light.png) | ![FL-SC06-05 step 2, U17, dark](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-phone-dark.png) |
| FL-SC06-05 step 2, U17 | tablet | ![FL-SC06-05 step 2, U17, light](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-tablet-light.png) | ![FL-SC06-05 step 2, U17, dark](../../images/05-taxes-and-performance/u17-cashier/2-meal-voucher-tablet-dark.png) |
| Error E1, U17 | desktop | ![Error E1, U17, light](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-desktop-light.png) | ![Error E1, U17, dark](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-desktop-dark.png) |
| Error E1, U17 | phone | ![Error E1, U17, light](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-phone-light.png) | ![Error E1, U17, dark](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-phone-dark.png) |
| Error E1, U17 | tablet | ![Error E1, U17, light](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-tablet-light.png) | ![Error E1, U17, dark](../../images/05-taxes-and-performance/u17-cashier/e1-voucher-limit-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc06-13-meal-vouchers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc06-13-meal-vouchers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc06-13-meal-vouchers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc06-13-meal-vouchers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc06-13-meal-vouchers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc06-13-meal-vouchers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc06-13-meal-vouchers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc06-13-meal-vouchers-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC06-12 Meal voucher payment](../../data/e-sc06-12-meal-voucher-payment.md), shown as the entity pages
list them, with their examples.

## Actions

- Scan the voucher: [UC-SC06-13](../../use-cases/05-taxes-and-performance/uc-sc06-13-accept-meal-vouchers.md), step 1.
- Check the limit: [UC-SC06-13](../../use-cases/05-taxes-and-performance/uc-sc06-13-accept-meal-vouchers.md), step 2.
- Pay the rest: [UC-SC06-13](../../use-cases/05-taxes-and-performance/uc-sc06-13-accept-meal-vouchers.md), step 3.
- Match the issuer: [UC-SC06-13](../../use-cases/05-taxes-and-performance/uc-sc06-13-accept-meal-vouchers.md), step 4.

## States

- Normal: the voucher scanned, limit, eligible amount and rest.
- Empty: "No voucher".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over the daily limit: the rest is asked.
- Read-only: a paid order is read-only.
- Offline: the till takes vouchers offline as it allows,
  [UC-F10-14](../../../../02-functional/f10-point-of-sale/use-cases/06-mobile-and-delivery/uc-f10-14-sell-on-the-move-and-offline.md);
  checks with the issuer wait.

Shown entities (VD-15): [E-SC06-12 Meal voucher payment](../../data/e-sc06-12-meal-voucher-payment.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC06-12 Meal voucher payment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U17, U18 | `u05-accounting/s-sc06-13-meal-vouchers-e-sc06-12-meal-voucher-payment-active-desktop-{light,dark}.png`, `u17-cashier/s-sc06-13-meal-vouchers-e-sc06-12-meal-voucher-payment-active-{desktop,phone,tablet}-{light,dark}.png`, `u18-waiter/s-sc06-13-meal-vouchers-e-sc06-12-meal-voucher-payment-active-{phone,tablet}-{light,dark}.png` |

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

- [FL-SC06-05 Taxes and performance](../../flows/fl-sc06-05-taxes-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC06-12 Tourist tax](s-sc06-12-tourist-tax.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC06-14 Performance](s-sc06-14-performance.md)
