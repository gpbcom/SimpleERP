🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
🚛 [SC07 Transport and logistics](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC07-05 Billing and performance](README.md) › 🖥️ S-SC07-13 Transport billing

# 🖥️ S-SC07-13 Transport billing

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U29 Dispatcher](../../../../01-users/personas/u29-dispatcher.md)

## Purpose

Bill a trip with its freight, its energy costs revised by the change in the CNR index between the contract and the
transport, its waiting time and its extras
([UC-SC07-13](../../use-cases/05-billing-and-performance/uc-sc07-13-bill-transport-with-surcharges.md),
[BR-SC07-12](../../business-rules/br-sc07-12-fuel-surcharge-from-the-index.md)).

## Entry points

Transport and logistics in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC07-05 step 2, U05 | desktop | ![FL-SC07-05 step 2, U05, light](../../images/05-billing-and-performance/u05-accounting/2-invoice-desktop-light.png) | ![FL-SC07-05 step 2, U05, dark](../../images/05-billing-and-performance/u05-accounting/2-invoice-desktop-dark.png) |
| Error E1, U05 | desktop | ![Error E1, U05, light](../../images/05-billing-and-performance/u05-accounting/e1-no-proof-desktop-light.png) | ![Error E1, U05, dark](../../images/05-billing-and-performance/u05-accounting/e1-no-proof-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc07-13-transport-billing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc07-13-transport-billing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc07-13-transport-billing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc07-13-transport-billing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc07-13-transport-billing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc07-13-transport-billing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc07-13-transport-billing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc07-13-transport-billing-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC07-13 Transport invoice line](../../data/e-sc07-13-transport-invoice-line.md), shown as the entity
pages list them, with their examples.

## Actions

- Close the trip: [UC-SC07-13](../../use-cases/05-billing-and-performance/uc-sc07-13-bill-transport-with-surcharges.md),
  step 1.
- Compute: [UC-SC07-13](../../use-cases/05-billing-and-performance/uc-sc07-13-bill-transport-with-surcharges.md), step
  2.
- Check: [UC-SC07-13](../../use-cases/05-billing-and-performance/uc-sc07-13-bill-transport-with-surcharges.md), step 3.
- Bill: [UC-SC07-13](../../use-cases/05-billing-and-performance/uc-sc07-13-bill-transport-with-surcharges.md), step 4.

## States

- Normal: the trip's freight, the energy costs line (the CNR index change since the contract, shown on the invoice),
  waiting time, extras and invoice.
- Empty: "Nothing to bill".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, proof missing: the order is held.
- Read-only: a sent invoice is read-only.
- Offline: not available offline: dispatch and office work on live, shared data. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-SC07-05 Billing and performance](../../flows/fl-sc07-05-billing-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC07-12 Chartering](../01-orders-and-planning/s-sc07-12-chartering.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC07-14 Client warehouse](../06-logistics-for-clients/s-sc07-14-client-warehouse.md)
