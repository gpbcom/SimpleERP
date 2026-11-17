🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-04 Money and taxes](README.md) › 🖥️ S-F14-13 Payouts

# 🖥️ S-F14-13 Payouts

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Receive payouts and statements.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-04 step 2, U46 | desktop | ![FL-F14-04 step 2, U46, light](../../images/04-money-and-taxes/u46-plugin-publisher/2-payout-desktop-light.png) | ![FL-F14-04 step 2, U46, dark](../../images/04-money-and-taxes/u46-plugin-publisher/2-payout-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-13-payouts-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-13-payouts-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-13-payouts-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-13-payouts-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-13-payouts-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-13-payouts-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-13-payouts-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-13-payouts-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: payouts per period with sales, refunds, commission, taxes and net.
- Empty: "No payout yet": shown before the first paid sale.
- Loading: the frame and titles show at once with placeholder rows for the statements; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: closed statements are read-only.
- Offline: not available offline: statements are read online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-08 Payout](../../data/e-f14-08-payout.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-08 Payout | Sent | Badge "Sent"; a new record starts here; next: Paid or Held (UC-F14-13); fields editable within the role | U05, U46 | `u05-accounting/s-f14-13-payouts-e-f14-08-payout-sent-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-13-payouts-e-f14-08-payout-sent-desktop-{light,dark}.png` |
| E-F14-08 Payout | Paid | Badge "Paid"; next: Reconciled (UC-F14-13); fields editable within the role | U05, U46 | `u05-accounting/s-f14-13-payouts-e-f14-08-payout-paid-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-13-payouts-e-f14-08-payout-paid-desktop-{light,dark}.png` |
| E-F14-08 Payout | Held | Badge "Held"; next: Paid (UC-F14-13); fields editable within the role | U05, U46 | `u05-accounting/s-f14-13-payouts-e-f14-08-payout-held-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-13-payouts-e-f14-08-payout-held-desktop-{light,dark}.png` |
| E-F14-08 Payout | Reconciled | Badge "Reconciled"; final: read-only, no next state; the history shows how it got here | U05, U46 | `u05-accounting/s-f14-13-payouts-e-f14-08-payout-reconciled-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-13-payouts-e-f14-08-payout-reconciled-desktop-{light,dark}.png` |

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

⬅️ [S-F14-12 Pricing](s-f14-12-pricing.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-14 Seller reports](s-f14-14-seller-reports.md)
