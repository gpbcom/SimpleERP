🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-01 Prices and agreements](README.md) › 🖥️ S-SC15-02 Rebates

# 🖥️ S-SC15-02 Rebates

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to manage rebates and year-end discounts,
[UC-SC15-02](../../use-cases/01-prices-and-agreements/uc-sc15-02-manage-rebates-and-year-end-discounts.md).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-01 step 2, U03 | desktop | ![FL-SC15-01 step 2, U03, light](../../images/01-prices-and-agreements/u03-sales/2-rebates-desktop-light.png) | ![FL-SC15-01 step 2, U03, dark](../../images/01-prices-and-agreements/u03-sales/2-rebates-desktop-dark.png) |
| FL-SC15-01 step 2, U03 | phone | ![FL-SC15-01 step 2, U03, light](../../images/01-prices-and-agreements/u03-sales/2-rebates-phone-light.png) | ![FL-SC15-01 step 2, U03, dark](../../images/01-prices-and-agreements/u03-sales/2-rebates-phone-dark.png) |
| FL-SC15-01 step 2, U03 | tablet | ![FL-SC15-01 step 2, U03, light](../../images/01-prices-and-agreements/u03-sales/2-rebates-tablet-light.png) | ![FL-SC15-01 step 2, U03, dark](../../images/01-prices-and-agreements/u03-sales/2-rebates-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-02-rebates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-02-rebates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-02-rebates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-02-rebates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-02-rebates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-02-rebates-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-02-rebates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-02-rebates-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-02 Rebate rule](../../data/e-sc15-02-rebate-rule.md), shown as the entity pages list them, with
their examples.

## Actions

- Set the rule:
  [UC-SC15-02](../../use-cases/01-prices-and-agreements/uc-sc15-02-manage-rebates-and-year-end-discounts.md), step 1.
- Accrue: [UC-SC15-02](../../use-cases/01-prices-and-agreements/uc-sc15-02-manage-rebates-and-year-end-discounts.md),
  step 2.
- Settle: [UC-SC15-02](../../use-cases/01-prices-and-agreements/uc-sc15-02-manage-rebates-and-year-end-discounts.md),
  step 3.
- Post: [UC-SC15-02](../../use-cases/01-prices-and-agreements/uc-sc15-02-manage-rebates-and-year-end-discounts.md), step
  4.

## States

- Normal: rebate rules, accruals and settlements.
- Empty: "No rebate".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the threshold missed: no rebate is due.
- Read-only: settled years are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-02 Rebate rule](../../data/e-sc15-02-rebate-rule.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-02 Rebate rule | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U05 | `u03-sales/s-sc15-02-rebates-e-sc15-02-rebate-rule-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc15-02-rebates-e-sc15-02-rebate-rule-active-desktop-{light,dark}.png` |

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

- [FL-SC15-01 Prices and agreements](../../flows/fl-sc15-01-prices-and-agreements.md)

## Open questions

None.

---

⬅️ [S-SC15-01 Price agreements](s-sc15-01-price-agreements.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-03 Yearly agreement](s-sc15-03-yearly-agreement.md)
