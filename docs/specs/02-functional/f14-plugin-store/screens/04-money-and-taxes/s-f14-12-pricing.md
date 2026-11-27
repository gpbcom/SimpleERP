🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-04 Money and taxes](README.md) › 🖥️ S-F14-12 Pricing

# 🖥️ S-F14-12 Pricing

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md)

## Purpose

Set prices and plans.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-04 step 1, U46 | desktop | ![FL-F14-04 step 1, U46, light](../../images/04-money-and-taxes/u46-plugin-publisher/1-prices-desktop-light.png) | ![FL-F14-04 step 1, U46, dark](../../images/04-money-and-taxes/u46-plugin-publisher/1-prices-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-12-pricing-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-12-pricing-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-12-pricing-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-12-pricing-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-12-pricing-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-12-pricing-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-12-pricing-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-12-pricing-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: plans, prices, trials and discount codes.
- Empty: "No plan": the plugin is free until a plan is added.
- Loading: the frame and titles show at once with placeholder rows for the plans; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a price change already announced to buyers is locked until its date.
- Offline: not available offline: prices are set online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F14-04 Plugin price plan](../../data/e-f14-04-plugin-price-plan.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-04 Plugin price plan | Published | Badge "Published"; a new record starts here; next: Paid (UC-F14-05); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-12-pricing-e-f14-04-plugin-price-plan-published-desktop-{light,dark}.png` |
| E-F14-04 Plugin price plan | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U46 | `u46-plugin-publisher/s-f14-12-pricing-e-f14-04-plugin-price-plan-paid-desktop-{light,dark}.png` |

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

⬅️ [S-F14-11 Releases](../03-publish/s-f14-11-releases.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-13 Payouts](s-f14-13-payouts.md)
