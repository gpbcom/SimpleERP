🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-04 Money and taxes](README.md) › 🖥️ S-F14-18 Publisher dashboard

# 🖥️ S-F14-18 Publisher dashboard

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)

## Purpose

Follow usage and revenue.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-04 step 4, U46 | desktop | ![FL-F14-04 step 4, U46, light](../../images/04-money-and-taxes/u46-plugin-publisher/4-dashboard-desktop-light.png) | ![FL-F14-04 step 4, U46, dark](../../images/04-money-and-taxes/u46-plugin-publisher/4-dashboard-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-18-publisher-dashboard-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-18-publisher-dashboard-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-18-publisher-dashboard-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-18-publisher-dashboard-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-18-publisher-dashboard-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-18-publisher-dashboard-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-18-publisher-dashboard-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-18-publisher-dashboard-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: installs, active companies, revenue and reviews over time.
- Empty: "No install yet": shown for a new plugin.
- Loading: the frame and titles show at once with placeholder rows for the figures; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: The figures last loaded stay visible with their date; nothing refreshes offline. Nothing else is queued: D38
  keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F14-08 Payout](../../data/e-f14-08-payout.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-08 Payout | Sent | Badge "Sent"; a new record starts here; next: Paid or Held (UC-F14-13); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-18-publisher-dashboard-e-f14-08-payout-sent-desktop-{light,dark}.png` |
| E-F14-08 Payout | Paid | Badge "Paid"; next: Reconciled (UC-F14-13); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-18-publisher-dashboard-e-f14-08-payout-paid-desktop-{light,dark}.png` |
| E-F14-08 Payout | Held | Badge "Held"; next: Paid (UC-F14-13); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-18-publisher-dashboard-e-f14-08-payout-held-desktop-{light,dark}.png` |
| E-F14-08 Payout | Reconciled | Badge "Reconciled"; final: read-only, no next state; the history shows how it got here | U46 | `u46-plugin-publisher/s-f14-18-publisher-dashboard-e-f14-08-payout-reconciled-desktop-{light,dark}.png` |

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

- [FL-F14-04 Money and taxes](../../flows/fl-f14-04-money-and-taxes.md)

## Open questions

None.

---

⬅️ [S-F14-17 Refunds](../02-buy-and-licence/s-f14-17-refunds.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-19 Moderation](../05-store-operations/s-f14-19-moderation.md)
