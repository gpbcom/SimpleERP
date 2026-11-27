🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-02 Buy and licence](README.md) › 🖥️ S-F14-06 Licences

# 🖥️ S-F14-06 Licences

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Manage licences and seats.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-02 step 2, U07 | desktop | ![FL-F14-02 step 2, U07, light](../../images/02-buy-and-licence/u07-administrator/2-licences-desktop-light.png) | ![FL-F14-02 step 2, U07, dark](../../images/02-buy-and-licence/u07-administrator/2-licences-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-06-licences-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-06-licences-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-06-licences-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-06-licences-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-06-licences-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-06-licences-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-06-licences-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-06-licences-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the company's subscriptions to support, updates and hosting with their renewal dates.
- Empty: "No paid subscription".
- Loading: the frame and titles show at once with placeholder rows for the subscriptions; within 1 second (D408) the
  data replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the administrator reads; the owner renews or stops.
- Offline: not available offline: subscriptions are managed online. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-05 Plugin licence](../../data/e-f14-05-plugin-licence.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-05 Plugin licence | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f14-06-licences-e-f14-05-plugin-licence-active-desktop-{light,dark}.png`, `u13-owner/s-f14-06-licences-e-f14-05-plugin-licence-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F14-05 Purchase](s-f14-05-purchase.md) · ⬆️ [Up](README.md) · ➡️ [S-F14-07 Reviews](s-f14-07-reviews.md)
