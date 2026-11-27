🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-02 Buy and licence](README.md) › 🖥️ S-F14-05 Purchase

# 🖥️ S-F14-05 Purchase

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Buy a paid plugin or subscription.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-02 step 1, U13 | desktop | ![FL-F14-02 step 1, U13, light](../../images/02-buy-and-licence/u13-owner/1-buy-desktop-light.png) | ![FL-F14-02 step 1, U13, dark](../../images/02-buy-and-licence/u13-owner/1-buy-desktop-dark.png) |
| FL-F14-02 step 1, U13 | phone | ![FL-F14-02 step 1, U13, light](../../images/02-buy-and-licence/u13-owner/1-buy-phone-light.png) | ![FL-F14-02 step 1, U13, dark](../../images/02-buy-and-licence/u13-owner/1-buy-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-05-purchase-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-05-purchase-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-05-purchase-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-05-purchase-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-05-purchase-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-05-purchase-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f14-05-purchase-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f14-05-purchase-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the plan's price, support terms, VAT and payment.
- Empty: "Free plugin": no payment step.
- Loading: the frame and titles show at once with placeholder rows for the plan; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the administrator prepares; the owner approves the purchase.
- Offline: not available offline: payment needs the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-05 Plugin licence](../../data/e-f14-05-plugin-licence.md),
[E-F14-19 Support terms](../../data/e-f14-19-support-terms.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-05 Plugin licence | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f14-05-purchase-e-f14-05-plugin-licence-active-desktop-{light,dark}.png`, `u13-owner/s-f14-05-purchase-e-f14-05-plugin-licence-active-{desktop,phone}-{light,dark}.png` |
| E-F14-19 Support terms | Published | Badge "Published"; a new record starts here; next: Changed (UC-F14-27); fields editable within the role | U07, U13 | `u07-administrator/s-f14-05-purchase-e-f14-19-support-terms-published-desktop-{light,dark}.png`, `u13-owner/s-f14-05-purchase-e-f14-19-support-terms-published-{desktop,phone}-{light,dark}.png` |
| E-F14-19 Support terms | Changed | Badge "Changed"; next: Published (UC-F14-27); fields editable within the role | U07, U13 | `u07-administrator/s-f14-05-purchase-e-f14-19-support-terms-changed-desktop-{light,dark}.png`, `u13-owner/s-f14-05-purchase-e-f14-19-support-terms-changed-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F14-04 Uninstall](../01-find-and-install/s-f14-04-uninstall.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-06 Licences](s-f14-06-licences.md)
