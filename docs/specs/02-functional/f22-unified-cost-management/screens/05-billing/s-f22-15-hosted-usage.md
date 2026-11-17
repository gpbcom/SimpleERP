🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-05 Billing](README.md) › 🖥️ S-F22-15 Hosted usage

# 🖥️ S-F22-15 Hosted usage

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

See the hosted quota and units billed.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-05 step 1, U13 | desktop | ![FL-F22-05 step 1, U13, light](../../images/05-billing/u13-owner/1-quota-desktop-light.png) | ![FL-F22-05 step 1, U13, dark](../../images/05-billing/u13-owner/1-quota-desktop-dark.png) |
| FL-F22-05 step 1, U13 | phone | ![FL-F22-05 step 1, U13, light](../../images/05-billing/u13-owner/1-quota-phone-light.png) | ![FL-F22-05 step 1, U13, dark](../../images/05-billing/u13-owner/1-quota-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-15-hosted-usage-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-15-hosted-usage-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-15-hosted-usage-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-15-hosted-usage-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-15-hosted-usage-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-15-hosted-usage-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f22-15-hosted-usage-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f22-15-hosted-usage-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: quota used and units billed.
- Empty: "Within the quota".
- Loading: the frame and titles show at once with placeholder rows for the quota; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: Figures last loaded stay visible. Nothing else is queued: D38 keeps only today's schedule, time and
  intervention records offline; a banner says the connection is lost and the actions come back with it.

Shown entities (VD-15): [E-F22-05 Hosted quota](../../data/e-f22-05-hosted-quota.md),
[E-F22-13 Usage invoice](../../data/e-f22-13-usage-invoice.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-05 Hosted quota | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f22-15-hosted-usage-e-f22-05-hosted-quota-active-desktop-{light,dark}.png`, `u13-owner/s-f22-15-hosted-usage-e-f22-05-hosted-quota-active-{desktop,phone}-{light,dark}.png` |
| E-F22-13 Usage invoice | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f22-15-hosted-usage-e-f22-13-usage-invoice-recorded-desktop-{light,dark}.png`, `u13-owner/s-f22-15-hosted-usage-e-f22-13-usage-invoice-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-05 Billing](../../flows/fl-f22-05-billing.md)

## Open questions

None.

---

⬅️ [S-F22-14 Allocation rules](../04-accounting/s-f22-14-allocation-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-16 Client re-billing](s-f22-16-client-re-billing.md)
