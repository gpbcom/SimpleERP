🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-05 Store operations](README.md) › 🖥️ S-F14-16 Withdrawal

# 🖥️ S-F14-16 Withdrawal

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Withdraw a vulnerable or harmful plugin.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-05 step 2, U11 | desktop | ![FL-F14-05 step 2, U11, light](../../images/05-store-operations/u11-provider-admin/2-withdraw-desktop-light.png) | ![FL-F14-05 step 2, U11, dark](../../images/05-store-operations/u11-provider-admin/2-withdraw-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-16-withdrawal-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-16-withdrawal-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-16-withdrawal-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-16-withdrawal-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-16-withdrawal-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-16-withdrawal-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-16-withdrawal-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-16-withdrawal-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the plugin to withdraw, the reason, the installed copies and the notices.
- Empty: "No withdrawal in progress".
- Loading: the frame and titles show at once with placeholder rows for the withdrawal; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: publishers see the decision and the notice only.
- Offline: not available offline: withdrawals act on the servers. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-11 Plugin withdrawal](../../data/e-f14-11-plugin-withdrawal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-11 Plugin withdrawal | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U11 | `u11-provider-admin/s-f14-16-withdrawal-e-f14-11-plugin-withdrawal-active-desktop-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-05 Store operations](../../flows/fl-f14-05-store-operations.md)

## Open questions

None.

---

⬅️ [S-F14-15 Private store](s-f14-15-private-store.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-17 Refunds](../02-buy-and-licence/s-f14-17-refunds.md)
