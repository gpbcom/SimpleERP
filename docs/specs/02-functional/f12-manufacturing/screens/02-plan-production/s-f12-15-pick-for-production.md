🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F12 Manufacturing (plugin)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F12-02 Plan production](README.md) › 🖥️ S-F12-15 Pick for production

# 🖥️ S-F12-15 Pick for production

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)

## Purpose

Pick and stage components.

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F12-02 step 2, U15 | phone | ![FL-F12-02 step 2, U15, light](../../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-phone-light.png) | ![FL-F12-02 step 2, U15, dark](../../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-phone-dark.png) |
| FL-F12-02 step 2, U15 | tablet | ![FL-F12-02 step 2, U15, light](../../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-tablet-light.png) | ![FL-F12-02 step 2, U15, dark](../../images/02-plan-production/u15-warehouse-operator/2-pick-and-stage-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f12-15-pick-for-production-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f12-15-pick-for-production-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f12-15-pick-for-production-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f12-15-pick-for-production-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f12-15-pick-for-production-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f12-15-pick-for-production-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f12-15-pick-for-production-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f12-15-pick-for-production-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Pick and stage components, as the wireframe shows.
- Empty: No component to pick yet, with Nothing to pick.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: done manufacturing orders and recorded checks, corrected by a new record.
- Offline: Works offline in the barcode app
  ([D271](../../../../06-decisions/f07-purchasing-and-stock/d271-warehouse-operations.md)): scans and quantities are
  kept on the device in a queue shown with its count, and sent when the network is back; the stock seen is the one
  loaded before going offline.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F12-02 Plan production](../../flows/fl-f12-02-plan-production.md)

## Open questions

None.

---

⬅️ [S-F12-14 Machine connections](../06-machines-and-oee/s-f12-14-machine-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F12-16 Compliance file](../07-compliance-and-safety/s-f12-16-compliance-file.md)
