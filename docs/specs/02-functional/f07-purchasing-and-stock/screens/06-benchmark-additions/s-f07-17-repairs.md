🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📦 [F7 Purchasing and stock](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F7-06 Benchmark additions](README.md) › 🖥️ S-F7-17 Repairs

# 🖥️ S-F7-17 Repairs

**Status:** ✅ specified

## Personas

- [U15 Warehouse operator](../../../../01-users/personas/u15-warehouse-operator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Repair products.

## Entry points

Purchasing and stock in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F7-06 step 4, U15 | phone | ![FL-F7-06 step 4, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/4-repairs-phone-light.png) | ![FL-F7-06 step 4, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/4-repairs-phone-dark.png) |
| FL-F7-06 step 4, U15 | tablet | ![FL-F7-06 step 4, U15, light](../../images/06-benchmark-additions/u15-warehouse-operator/4-repairs-tablet-light.png) | ![FL-F7-06 step 4, U15, dark](../../images/06-benchmark-additions/u15-warehouse-operator/4-repairs-tablet-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f07-17-repairs-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f07-17-repairs-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f07-17-repairs-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f07-17-repairs-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f07-17-repairs-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f07-17-repairs-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f07-17-repairs-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f07-17-repairs-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Repair products, as the wireframe shows.
- Empty: No repair order yet, with New repair.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: confirmed moves and posted valuations, corrected by a new move.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F7-14 Repair order](../../data/e-f07-14-repair-order.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F7-14 Repair order | Done | Badge "Done"; next: Invoiced (UC-F7-17); fields editable within the role | U15 | `u15-warehouse-operator/s-f07-17-repairs-e-f07-14-repair-order-done-{phone,tablet}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

⬅️ [S-F7-16 Third-party stock](s-f07-16-third-party-stock.md) · ⬆️ [Up](README.md) ·
➡️ [S-F7-18 Supplier contracts](../07-supplier-agreements-and-performance/s-f07-18-supplier-contracts.md)
