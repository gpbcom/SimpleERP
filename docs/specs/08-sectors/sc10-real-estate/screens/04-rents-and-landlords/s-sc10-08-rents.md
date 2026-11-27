🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-04 Rents and landlords](README.md) › 🖥️ S-SC10-08 Rents

# 🖥️ S-SC10-08 Rents

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to call rents and issue receipts
([UC-SC10-08](../../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-04 step 1, U34 | desktop | ![FL-SC10-04 step 1, U34, light](../../images/04-rents-and-landlords/u34-property-manager/1-rents-desktop-light.png) | ![FL-SC10-04 step 1, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/1-rents-desktop-dark.png) |
| FL-SC10-04 step 1, U34 | tablet | ![FL-SC10-04 step 1, U34, light](../../images/04-rents-and-landlords/u34-property-manager/1-rents-tablet-light.png) | ![FL-SC10-04 step 1, U34, dark](../../images/04-rents-and-landlords/u34-property-manager/1-rents-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-08-rents-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-08-rents-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-08-rents-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-08-rents-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-08-rents-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-08-rents-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-08-rents-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-08-rents-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-09 Rent call](../../data/e-sc10-09-rent-call.md), shown as the entity pages list them, with their
examples.

## Actions

- Call: [UC-SC10-08](../../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md), step 1.
- Pay: [UC-SC10-08](../../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md), step 2.
- Collect: [UC-SC10-08](../../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md), step 3.
- Receipt: [UC-SC10-08](../../use-cases/04-rents-and-landlords/uc-sc10-08-call-rents-and-issue-receipts.md), step 4.

## States

- Normal: rent calls with paid amounts and receipts.
- Empty: "No rent call".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a partial payment: the balance is kept.
- Read-only: paid calls are read-only.
- Offline: not available offline: office work on leases, accounts and client money. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC10-09 Rent call](../../data/e-sc10-09-rent-call.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC10-09 Rent call | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U34 | `u09-customer/s-sc10-08-rents-e-sc10-09-rent-call-recorded-phone-{light,dark}.png`, `u34-property-manager/s-sc10-08-rents-e-sc10-09-rent-call-recorded-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC10-04 Rents and landlords](../../flows/fl-sc10-04-rents-and-landlords.md)

## Open questions

None.

---

⬅️ [S-SC10-07 Letting](../03-lettings/s-sc10-07-letting.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-09 Indexation](s-sc10-09-indexation.md)
