🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-01 Find and install](README.md) › 🖥️ S-F14-01 Store

# 🖥️ S-F14-01 Store

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Browse and search the store.

## Entry points

Plugin store in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-01 step 1, U07 | desktop | ![FL-F14-01 step 1, U07, light](../../images/01-find-and-install/u07-administrator/1-browse-desktop-light.png) | ![FL-F14-01 step 1, U07, dark](../../images/01-find-and-install/u07-administrator/1-browse-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-01-store-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-01-store-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-01-store-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-01-store-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-01-store-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-01-store-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-01-store-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-01-store-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: plugins and sector packs by category with rating, installs, price and compatibility.
- Empty: "No plugin matches": shown for a search with no result, with the filters to clear.
- Loading: the frame and titles show at once with placeholder rows for the plugins; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the owner browses but cannot install; incompatible plugins are greyed.
- Offline: not available offline: the store is read from its servers. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-01 Store listing](../../data/e-f14-01-store-listing.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-01 Store listing | New | Badge "New"; a new record starts here; next: Paid or Refused (BR-F14-09); fields editable within the role | U13 | `u13-owner/s-f14-01-store-e-f14-01-store-listing-new-{desktop,phone}-{light,dark}.png` |
| E-F14-01 Store listing | Paid | Badge "Paid"; next: Complete or Refused (UC-F14-08, BR-F14-09); fields editable within the role | U13 | `u13-owner/s-f14-01-store-e-f14-01-store-listing-paid-{desktop,phone}-{light,dark}.png` |
| E-F14-01 Store listing | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f14-01-store-e-f14-01-store-listing-refused-{desktop,phone}-{light,dark}.png` |
| E-F14-01 Store listing | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f14-01-store-e-f14-01-store-listing-complete-{desktop,phone}-{light,dark}.png` |

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

- [FL-F14-01 Find and install](../../flows/fl-f14-01-find-and-install.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F14-02 Install](s-f14-02-install.md)
