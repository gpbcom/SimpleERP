🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-01 See and set up](README.md) › 🖥️ S-F22-05 Payment mode

# 🖥️ S-F22-05 Payment mode

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Bring own keys or use the hosted quota.

## Entry points

Unified platform cost management in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-01 step 4, U07 | desktop | ![FL-F22-01 step 4, U07, light](../../images/01-see-and-set-up/u07-administrator/4-keys-desktop-light.png) | ![FL-F22-01 step 4, U07, dark](../../images/01-see-and-set-up/u07-administrator/4-keys-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-05-payment-mode-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-05-payment-mode-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-05-payment-mode-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-05-payment-mode-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-05-payment-mode-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-05-payment-mode-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-05-payment-mode-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-05-payment-mode-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: own key or hosted quota per provider.
- Empty: "Hosted quota" by default.
- Loading: the frame and titles show at once with placeholder rows for the mode; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner approves.
- Offline: not available offline: set online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F22-04 Paid provider](../../data/e-f22-04-paid-provider.md),
[E-F22-05 Hosted quota](../../data/e-f22-05-hosted-quota.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-04 Paid provider | New | Badge "New"; a new record starts here; next: Paid (UC-F22-04); fields editable within the role | U07, U13 | `u07-administrator/s-f22-05-payment-mode-e-f22-04-paid-provider-new-desktop-{light,dark}.png`, `u13-owner/s-f22-05-payment-mode-e-f22-04-paid-provider-new-{desktop,phone}-{light,dark}.png` |
| E-F22-05 Hosted quota | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f22-05-payment-mode-e-f22-05-hosted-quota-active-desktop-{light,dark}.png`, `u13-owner/s-f22-05-payment-mode-e-f22-05-hosted-quota-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F22-01 See and set up](../../flows/fl-f22-01-see-and-set-up.md)

## Open questions

None.

---

⬅️ [S-F22-04 Providers](s-f22-04-providers.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-06 Budgets](../02-budgets-and-stops/s-f22-06-budgets.md)
