🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-04 Rents and landlords](README.md) ›
🖥️ S-SC10-12 Landlord statements

# 🖥️ S-SC10-12 Landlord statements

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to pay landlords and send statements
([UC-SC10-12](../../use-cases/04-rents-and-landlords/uc-sc10-12-pay-landlords-and-send-statements.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-04 step 4, U34 | desktop | ![FL-SC10-04 step 4, U34, light](../../images/04-rents-and-landlords/u34-property-manager/4-landlord-desktop-light.png) | ![FL-SC10-04 step 4, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/4-landlord-desktop-dark.png) |
| FL-SC10-04 step 4, U34 | tablet | ![FL-SC10-04 step 4, U34, light](../../images/04-rents-and-landlords/u34-property-manager/4-landlord-tablet-light.png) | ![FL-SC10-04 step 4, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/4-landlord-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-12-landlord-statements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-12-landlord-statements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-12-landlord-statements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-12-landlord-statements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-12-landlord-statements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-12-landlord-statements-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-12-landlord-statements-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-12-landlord-statements-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-11 Landlord statement](../../data/e-sc10-11-landlord-statement.md),
[E-F8-17 Client money ledger](../../../../02-functional/f08-accounting/data/e-f08-17-client-money-ledger.md), shown as
the entity pages list them, with their examples.

## Actions

- Close the period:
  [UC-SC10-12](../../use-cases/04-rents-and-landlords/uc-sc10-12-pay-landlords-and-send-statements.md), step 1.
- Deduct fees and expenses:
  [UC-SC10-12](../../use-cases/04-rents-and-landlords/uc-sc10-12-pay-landlords-and-send-statements.md), step 2.
- Pay: [UC-SC10-12](../../use-cases/04-rents-and-landlords/uc-sc10-12-pay-landlords-and-send-statements.md), step 3.
- Send the statement:
  [UC-SC10-12](../../use-cases/04-rents-and-landlords/uc-sc10-12-pay-landlords-and-send-statements.md), step 4.

## States

- Normal: per landlord: rents, fees, expenses and payment.
- Empty: "Nothing to pay".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a rent unpaid: it shows on the statement.
- Read-only: a paid statement is read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-11 Landlord statement](../../data/e-sc10-11-landlord-statement.md),
[E-F8-17 Client money ledger](../../../../02-functional/f08-accounting/data/e-f08-17-client-money-ledger.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-11 Landlord statement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U34 | `u05-accounting/s-sc10-12-landlord-statements-e-sc10-11-landlord-statement-active-desktop-{light,dark}.png`, `u34-property-manager/s-sc10-12-landlord-statements-e-sc10-11-landlord-statement-active-{desktop,tablet}-{light,dark}.png` |
| E-F8-17 Client money ledger | Open | Badge "Open"; a new record starts here; next: Closed (UC-F8-21); fields editable within the role | U05, U34 | `u05-accounting/s-sc10-12-landlord-statements-e-f08-17-client-money-ledger-open-desktop-{light,dark}.png`, `u34-property-manager/s-sc10-12-landlord-statements-e-f08-17-client-money-ledger-open-{desktop,tablet}-{light,dark}.png` |
| E-F8-17 Client money ledger | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U05, U34 | `u05-accounting/s-sc10-12-landlord-statements-e-f08-17-client-money-ledger-closed-desktop-{light,dark}.png`, `u34-property-manager/s-sc10-12-landlord-statements-e-f08-17-client-money-ledger-closed-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC10-04 Rents and landlords](../../flows/fl-sc10-04-rents-and-landlords.md)

## Open questions

None.

---

⬅️ [S-SC10-11 Charges](s-sc10-11-charges.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-13 Diagnostics](../03-lettings/s-sc10-13-diagnostics.md)
