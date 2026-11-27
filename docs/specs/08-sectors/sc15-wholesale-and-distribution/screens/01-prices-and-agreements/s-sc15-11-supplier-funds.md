🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-01 Prices and agreements](README.md) › 🖥️ S-SC15-11 Supplier funds

# 🖥️ S-SC15-11 Supplier funds

**Status:** ✅ specified

## Personas

- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to run supplier promotions and listing fees,
[UC-SC15-11](../../use-cases/01-prices-and-agreements/uc-sc15-11-run-supplier-promotions-and-listing-fees.md).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-01 step 4, U04 | desktop | ![FL-SC15-01 step 4, U04, light](../../images/01-prices-and-agreements/u04-purchasing/4-supplier-funds-desktop-light.png) | ![FL-SC15-01 step 4, U04, dark](../../images/01-prices-and-agreements/u04-purchasing/4-supplier-funds-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-11-supplier-funds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-11-supplier-funds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-11-supplier-funds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-11-supplier-funds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-11-supplier-funds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-11-supplier-funds-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-11-supplier-funds-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-11-supplier-funds-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC15-08 Supplier fund](../../data/e-sc15-08-supplier-fund.md), shown as the entity pages list them,
with their examples.

## Actions

- Record: [UC-SC15-11](../../use-cases/01-prices-and-agreements/uc-sc15-11-run-supplier-promotions-and-listing-fees.md),
  step 1.
- Execute:
  [UC-SC15-11](../../use-cases/01-prices-and-agreements/uc-sc15-11-run-supplier-promotions-and-listing-fees.md), step 2.
- Prove: [UC-SC15-11](../../use-cases/01-prices-and-agreements/uc-sc15-11-run-supplier-promotions-and-listing-fees.md),
  step 3.
- Invoice the supplier:
  [UC-SC15-11](../../use-cases/01-prices-and-agreements/uc-sc15-11-run-supplier-promotions-and-listing-fees.md), step 4.

## States

- Normal: supplier funds with execution proof and invoicing.
- Empty: "No supplier fund".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, not executed: it is not invoiced.
- Read-only: invoiced ones are read-only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC15-08 Supplier fund](../../data/e-sc15-08-supplier-fund.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-08 Supplier fund | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U04 | `u03-sales/s-sc15-11-supplier-funds-e-sc15-08-supplier-fund-active-{desktop,phone,tablet}-{light,dark}.png`, `u04-purchasing/s-sc15-11-supplier-funds-e-sc15-08-supplier-fund-active-desktop-{light,dark}.png` |

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

- [FL-SC15-01 Prices and agreements](../../flows/fl-sc15-01-prices-and-agreements.md)

## Open questions

None.

---

⬅️ [S-SC15-10 Returns](../03-warehouse/s-sc15-10-returns.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-12 Imports](../04-import-and-suppliers/s-sc15-12-imports.md)
