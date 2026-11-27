🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-06 Benchmark additions](README.md) › 🖥️ S-F7-16 Third-party stock

# 🖥️ S-F7-16 Third-party stock

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U04 Purchasing](../../../../01-users/personas/u04-purchasing.md)

## Purpose

Work with third-party warehouses and channels.

## Entry points

Purchasing and stock in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-06 step 3, U15 | phone | ![FL-F7-06 step 3, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/3-third-party-stock-phone-light.png) | ![FL-F7-06 step 3, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/3-third-party-stock-phone-dark.png) |
| FL-F7-06 step 3, U15 | tablet | ![FL-F7-06 step 3, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/3-third-party-stock-tablet-light.png) | ![FL-F7-06 step 3, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/3-third-party-stock-tablet-dark.png) |
| Error E1, U15 | phone | ![Error E1, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/e1-variance-phone-light.png) | ![Error E1, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/e1-variance-phone-dark.png) |
| Error E1, U15 | tablet | ![Error E1, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/e1-variance-tablet-light.png) | ![Error E1, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/e1-variance-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-16-third-party-stock-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-16-third-party-stock-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-16-third-party-stock-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-16-third-party-stock-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-16-third-party-stock-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-16-third-party-stock-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-16-third-party-stock-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-16-third-party-stock-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Work with third-party warehouses and channels, as the wireframe shows.
- Empty: No third-party warehouse or channel yet, with Connect one.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and lists also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)

## Shown in

- [FL-F7-06 Benchmark additions](../../flows/fl-f07-06-benchmark-additions.md)

## Open questions

None.

---

⬅️ [S-F7-15 Group trade](s-f07-15-group-trade.md) · ⬆️ [Up](README.md) · ➡️ [S-F7-17 Repairs](s-f07-17-repairs.md)
