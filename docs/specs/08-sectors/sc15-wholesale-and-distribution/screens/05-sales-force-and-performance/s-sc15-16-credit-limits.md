🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-05 Sales force and performance](README.md) › 🖥️ S-SC15-16 Credit limits

# 🖥️ S-SC15-16 Credit limits

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to manage customer credit limits,
[UC-SC15-16](../../use-cases/05-sales-force-and-performance/uc-sc15-16-manage-customer-credit-limits.md).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-05 step 3, U05 | desktop | ![FL-SC15-05 step 3, U05, light](../../images/05-sales-force-and-performance/u05-accounting/3-credit-desktop-light.png) | ![FL-SC15-05 step 3, U05, dark](../../images/05-sales-force-and-performance/u05-accounting/3-credit-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-16-credit-limits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-16-credit-limits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-16-credit-limits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-16-credit-limits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-16-credit-limits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-16-credit-limits-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc15-16-credit-limits-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc15-16-credit-limits-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-F6-12 Credit limit](../../../../02-functional/f06-customers-and-sales/data/e-f06-12-credit-limit.md),
shown as the entity pages list them, with their examples.

## Actions

- Set the limit:
  [UC-SC15-16](../../use-cases/05-sales-force-and-performance/uc-sc15-16-manage-customer-credit-limits.md), step 1.
- Order: [UC-SC15-16](../../use-cases/05-sales-force-and-performance/uc-sc15-16-manage-customer-credit-limits.md), step
  2.
- Approve: [UC-SC15-16](../../use-cases/05-sales-force-and-performance/uc-sc15-16-manage-customer-credit-limits.md),
  step 3.
- Release: [UC-SC15-16](../../use-cases/05-sales-force-and-performance/uc-sc15-16-manage-customer-credit-limits.md),
  step 4.

## States

- Normal: limits, used and held orders.
- Empty: "No limit set".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, over the limit: the order is held.
- Read-only: sales read only.
- Offline: not available offline: office work on agreements, accounts and statistics. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15):
[E-F6-12 Credit limit](../../../../02-functional/f06-customers-and-sales/data/e-f06-12-credit-limit.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-12 Credit limit | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U05 | `u03-sales/s-sc15-16-credit-limits-e-f06-12-credit-limit-active-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc15-16-credit-limits-e-f06-12-credit-limit-active-desktop-{light,dark}.png` |

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

- [FL-SC15-05 Sales force and performance](../../flows/fl-sc15-05-sales-force-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC15-15 Margins](s-sc15-15-margins.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-17 Buying](../04-import-and-suppliers/s-sc15-17-buying.md)
