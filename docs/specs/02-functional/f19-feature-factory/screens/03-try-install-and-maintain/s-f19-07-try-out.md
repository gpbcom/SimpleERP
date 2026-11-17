🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-03 Try, install and maintain](README.md) › 🖥️ S-F19-07 Try-out

# 🖥️ S-F19-07 Try-out

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Try the feature on a copy of the data.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-03 step 1, U13 | desktop | ![FL-F19-03 step 1, U13, light](../../images/03-try-install-and-maintain/u13-owner/1-try-desktop-light.png) | ![FL-F19-03 step 1, U13, dark](../../images/03-try-install-and-maintain/u13-owner/1-try-desktop-dark.png) |
| FL-F19-03 step 1, U13 | phone | ![FL-F19-03 step 1, U13, light](../../images/03-try-install-and-maintain/u13-owner/1-try-phone-light.png) | ![FL-F19-03 step 1, U13, dark](../../images/03-try-install-and-maintain/u13-owner/1-try-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-07-try-out-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-07-try-out-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-07-try-out-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-07-try-out-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-07-try-out-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-07-try-out-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-07-try-out-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-07-try-out-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the copy company with the feature to try and the accept or change buttons.
- Empty: "No try-out yet".
- Loading: the frame and titles show at once with placeholder rows for the try-out; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: the copy expires on its date.
- Offline: not available offline: the copy runs online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F19-06 Try-out copy](../../data/e-f19-06-try-out-copy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-06 Try-out copy | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f19-07-try-out-e-f19-06-try-out-copy-active-desktop-{light,dark}.png`, `u13-owner/s-f19-07-try-out-e-f19-06-try-out-copy-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F19-03 Try, install and maintain](../../flows/fl-f19-03-try-install-and-maintain.md)

## Open questions

None.

---

⬅️ [S-F19-06 Review](../02-build-and-check/s-f19-06-review.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-08 Install](s-f19-08-install.md)
