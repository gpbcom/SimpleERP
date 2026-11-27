🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-03 Lettings](README.md) › 🖥️ S-SC10-10 Deposits

# 🖥️ S-SC10-10 Deposits

**Status:** ✅ specified

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to manage deposits and their return
([UC-SC10-10](../../use-cases/03-lettings/uc-sc10-10-manage-deposits-and-their-return.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-03 step 2, U34 | desktop | ![FL-SC10-03 step 2, U34, light](../../images/03-lettings/u34-property-manager/2-deposit-desktop-light.png) | ![FL-SC10-03 step 2, U34, dark](../../images/03-lettings/u34-property-manager/2-deposit-desktop-dark.png) |
| FL-SC10-03 step 2, U34 | tablet | ![FL-SC10-03 step 2, U34, light](../../images/03-lettings/u34-property-manager/2-deposit-tablet-light.png) | ![FL-SC10-03 step 2, U34, dark](../../images/03-lettings/u34-property-manager/2-deposit-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-10-deposits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-10-deposits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-10-deposits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-10-deposits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-10-deposits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-10-deposits-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-10-deposits-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-10-deposits-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-08 Deposit](../../data/e-sc10-08-deposit.md), shown as the entity pages list them, with their
examples.

## Actions

- Exit inventory: [UC-SC10-10](../../use-cases/03-lettings/uc-sc10-10-manage-deposits-and-their-return.md), step 1.
- Compute deductions: [UC-SC10-10](../../use-cases/03-lettings/uc-sc10-10-manage-deposits-and-their-return.md), step 2.
- Return: [UC-SC10-10](../../use-cases/03-lettings/uc-sc10-10-manage-deposits-and-their-return.md), step 3.
- Receive the statement: [UC-SC10-10](../../use-cases/03-lettings/uc-sc10-10-manage-deposits-and-their-return.md), step
  4.

## States

- Normal: the deposit, inventories compared, deductions and return date.
- Empty: "No deposit to return".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, late: the penalty is computed
  ([BR-SC10-04](../../business-rules/br-sc10-04-deposit-within-the-cap.md)).
- Read-only: a returned deposit is read-only.
- Offline: the exit inventory is kept on the tablet and syncs later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC10-03 Lettings](../../flows/fl-sc10-03-lettings.md)

## Open questions

None.

---

⬅️ [S-SC10-09 Indexation](../04-rents-and-landlords/s-sc10-09-indexation.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-11 Charges](../04-rents-and-landlords/s-sc10-11-charges.md)
