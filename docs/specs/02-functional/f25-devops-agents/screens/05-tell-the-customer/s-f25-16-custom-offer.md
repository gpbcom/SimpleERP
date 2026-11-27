🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-05 Tell the customer](README.md) › 🖥️ S-F25-16 Custom offer

# 🖥️ S-F25-16 Custom offer

**Status:** ✅ specified

## Personas

- [U47 SimpleERP maintainer](../../../../01-users/personas/u47-simpleerp-maintainer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Offer the feature factory for a custom need.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-05 step 3, U47 | desktop | ![FL-F25-05 step 3, U47, light](../../images/05-tell-the-customer/u47-simpleerp-maintainer/3-factory-desktop-light.png) | ![FL-F25-05 step 3, U47, dark](../../images/05-tell-the-customer/u47-simpleerp-maintainer/3-factory-desktop-dark.png) |
| FL-F25-05 step 3, U47 | phone | ![FL-F25-05 step 3, U47, light](../../images/05-tell-the-customer/u47-simpleerp-maintainer/3-factory-phone-light.png) | ![FL-F25-05 step 3, U47, dark](../../images/05-tell-the-customer/u47-simpleerp-maintainer/3-factory-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-16-custom-offer-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-16-custom-offer-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-16-custom-offer-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-16-custom-offer-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-16-custom-offer-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-16-custom-offer-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-16-custom-offer-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-16-custom-offer-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the feature-factory offer with its price.
- Empty: never empty.
- Loading: the frame and titles show at once with placeholder rows for the offer; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner chooses.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-01 Bug or feature request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U47 | `u13-owner/s-f25-16-custom-offer-e-f25-01-bug-or-feature-request-active-{desktop,phone}-{light,dark}.png`, `u47-simpleerp-maintainer/s-f25-16-custom-offer-e-f25-01-bug-or-feature-request-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-05 Tell the customer](../../flows/fl-f25-05-tell-the-customer.md)

## Open questions

None.

---

⬅️ [S-F25-15 Shipped](s-f25-15-shipped.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-17 Agent rights](../04-approve-and-govern/s-f25-17-agent-rights.md)
