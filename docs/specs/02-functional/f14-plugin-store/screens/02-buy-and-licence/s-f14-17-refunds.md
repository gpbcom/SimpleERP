🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-02 Buy and licence](README.md) › 🖥️ S-F14-17 Refunds

# 🖥️ S-F14-17 Refunds

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Handle refunds and disputes.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-02 step 4, U11 | desktop | ![FL-F14-02 step 4, U11, light](../../images/02-buy-and-licence/u11-provider-admin/4-refund-desktop-light.png) | ![FL-F14-02 step 4, U11, dark](../../images/02-buy-and-licence/u11-provider-admin/4-refund-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-17-refunds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-17-refunds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-17-refunds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-17-refunds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-17-refunds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-17-refunds-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-17-refunds-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-17-refunds-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: refund requests with their reasons and decisions.
- Empty: "No refund request".
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner sees the decision; decided refunds are read-only.
- Offline: not available offline: refunds are decided online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-12 Refund](../../data/e-f14-12-refund.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-12 Refund | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U11, U13 | `u11-provider-admin/s-f14-17-refunds-e-f14-12-refund-active-desktop-{light,dark}.png`, `u13-owner/s-f14-17-refunds-e-f14-12-refund-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F14-02 Buy and licence](../../flows/fl-f14-02-buy-and-licence.md)

## Open questions

None.

---

⬅️ [S-F14-16 Withdrawal](../05-store-operations/s-f14-16-withdrawal.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-18 Publisher dashboard](../04-money-and-taxes/s-f14-18-publisher-dashboard.md)
