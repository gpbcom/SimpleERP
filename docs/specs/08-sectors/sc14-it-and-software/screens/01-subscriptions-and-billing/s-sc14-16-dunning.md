🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-01 Subscriptions and billing](README.md) › 🖥️ S-SC14-16 Dunning

# 🖥️ S-SC14-16 Dunning

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to handle failed payments and dunning,
[UC-SC14-16](../../use-cases/01-subscriptions-and-billing/uc-sc14-16-handle-failed-payments-and-dunning.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-01 step 5, U05 | desktop | ![FL-SC14-01 step 5, U05, light](../../images/01-subscriptions-and-billing/u05-accounting/5-dunning-desktop-light.png) | ![FL-SC14-01 step 5, U05, dark](../../images/01-subscriptions-and-billing/u05-accounting/5-dunning-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-16-dunning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-16-dunning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-16-dunning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-16-dunning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-16-dunning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-16-dunning-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc14-16-dunning-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc14-16-dunning-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC14-14 Dunning case](../../data/e-sc14-14-dunning-case.md), shown as the entity pages list them, with
their examples.

## Actions

- Retry: [UC-SC14-16](../../use-cases/01-subscriptions-and-billing/uc-sc14-16-handle-failed-payments-and-dunning.md),
  step 1.
- Remind: [UC-SC14-16](../../use-cases/01-subscriptions-and-billing/uc-sc14-16-handle-failed-payments-and-dunning.md),
  step 2.
- Warn: [UC-SC14-16](../../use-cases/01-subscriptions-and-billing/uc-sc14-16-handle-failed-payments-and-dunning.md),
  step 3.
- Suspend: [UC-SC14-16](../../use-cases/01-subscriptions-and-billing/uc-sc14-16-handle-failed-payments-and-dunning.md),
  step 4.

## States

- Normal: dunning cases with step and amount.
- Empty: "No failed payment".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, suspended: access is read-only.
- Read-only: closed cases are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-14 Dunning case](../../data/e-sc14-14-dunning-case.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-14 Dunning case | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-sc14-16-dunning-e-sc14-14-dunning-case-active-desktop-{light,dark}.png` |

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

- [FL-SC14-01 Subscriptions and billing](../../flows/fl-sc14-01-subscriptions-and-billing.md)

## Open questions

None.

---

⬅️ [S-SC14-15 EU VAT](s-sc14-15-eu-vat.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-17 Customer portal](../06-portal-and-metrics/s-sc14-17-customer-portal.md)
