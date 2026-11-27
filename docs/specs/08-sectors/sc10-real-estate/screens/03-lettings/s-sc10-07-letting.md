🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏘️ [SC10 Real estate](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC10-03 Lettings](README.md) › 🖥️ S-SC10-07 Letting

# 🖥️ S-SC10-07 Letting

**Status:** 🔄 waiting for the owner

## Personas

- [U34 Property manager](../../../../01-users/personas/u34-property-manager.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to let a property ([UC-SC10-07](../../use-cases/03-lettings/uc-sc10-07-let-a-property.md)).

## Entry points

Real estate in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC10-03 step 1, U34 | desktop | ![FL-SC10-03 step 1, U34, light](../../images/03-lettings/u34-property-manager/1-lease-desktop-light.png) | ![FL-SC10-03 step 1, U34, dark](../../images/03-lettings/u34-property-manager/1-lease-desktop-dark.png) |
| FL-SC10-03 step 1, U34 | tablet | ![FL-SC10-03 step 1, U34, light](../../images/03-lettings/u34-property-manager/1-lease-tablet-light.png) | ![FL-SC10-03 step 1, U34, dark](../../images/03-lettings/u34-property-manager/1-lease-tablet-dark.png) |
| Error E1, U34 | desktop | ![Error E1, U34, light](../../images/03-lettings/u34-property-manager/e1-over-cap-desktop-light.png) | ![Error E1, U34, dark](../../images/03-lettings/u34-property-manager/e1-over-cap-desktop-dark.png) |
| Error E1, U34 | tablet | ![Error E1, U34, light](../../images/03-lettings/u34-property-manager/e1-over-cap-tablet-light.png) | ![Error E1, U34, dark](../../images/03-lettings/u34-property-manager/e1-over-cap-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc10-07-letting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc10-07-letting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc10-07-letting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc10-07-letting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc10-07-letting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc10-07-letting-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc10-07-letting-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc10-07-letting-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC10-07 Lease](../../data/e-sc10-07-lease.md), [E-SC10-08 Deposit](../../data/e-sc10-08-deposit.md),
shown as the entity pages list them, with their examples.

## Actions

- Check the file: [UC-SC10-07](../../use-cases/03-lettings/uc-sc10-07-let-a-property.md), step 1.
- Set the rent: [UC-SC10-07](../../use-cases/03-lettings/uc-sc10-07-let-a-property.md), step 2.
- Sign the lease: [UC-SC10-07](../../use-cases/03-lettings/uc-sc10-07-let-a-property.md), step 3.
- Entry inventory: [UC-SC10-07](../../use-cases/03-lettings/uc-sc10-07-let-a-property.md), step 4.

## States

- Normal: the lease, rent cap check, inventory and deposit.
- Empty: "No lease".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, rent over the cap: the rent is refused.
- Read-only: a signed lease is read-only.
- Offline: the inventory is kept on the tablet with its photos and syncs later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC10-06 Agency fees](../02-sales/s-sc10-06-agency-fees.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC10-08 Rents](../04-rents-and-landlords/s-sc10-08-rents.md)
