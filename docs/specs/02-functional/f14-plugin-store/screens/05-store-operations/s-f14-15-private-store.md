🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-05 Store operations](README.md) › 🖥️ S-F14-15 Private store

# 🖥️ S-F14-15 Private store

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Run a private store.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-05 step 1, U11 | desktop | ![FL-F14-05 step 1, U11, light](../../images/05-store-operations/u11-provider-admin/1-private-store-desktop-light.png) | ![FL-F14-05 step 1, U11, dark](../../images/05-store-operations/u11-provider-admin/1-private-store-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-15-private-store-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-15-private-store-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-15-private-store-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-15-private-store-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-15-private-store-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-15-private-store-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-15-private-store-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-15-private-store-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the private store's plugins and the client companies it serves.
- Empty: "No plugin in the private store yet".
- Loading: the frame and titles show at once with placeholder rows for the private store; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: client administrators see the store, not its settings.
- Offline: not available offline: the store runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F14-10 Private store](../../data/e-f14-10-private-store.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-10 Private store | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U11 | `u11-provider-admin/s-f14-15-private-store-e-f14-10-private-store-active-desktop-{light,dark}.png` |

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

⬅️ [S-F14-14 Seller reports](../04-money-and-taxes/s-f14-14-seller-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-16 Withdrawal](s-f14-16-withdrawal.md)
