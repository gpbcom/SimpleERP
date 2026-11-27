🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-03 Try, install and maintain](README.md) › 🖥️ S-F19-11 Cancel

# 🖥️ S-F19-11 Cancel

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Cancel a feature and export its data.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-03 step 5, U13 | desktop | ![FL-F19-03 step 5, U13, light](../../images/03-try-install-and-maintain/u13-owner/5-cancel-desktop-light.png) | ![FL-F19-03 step 5, U13, dark](../../images/03-try-install-and-maintain/u13-owner/5-cancel-desktop-dark.png) |
| FL-F19-03 step 5, U13 | phone | ![FL-F19-03 step 5, U13, light](../../images/03-try-install-and-maintain/u13-owner/5-cancel-phone-light.png) | ![FL-F19-03 step 5, U13, dark](../../images/03-try-install-and-maintain/u13-owner/5-cancel-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-11-cancel-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-11-cancel-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-11-cancel-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-11-cancel-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-11-cancel-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-11-cancel-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f19-11-cancel-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f19-11-cancel-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the cancellation with its month end and the export.
- Empty: never empty: it opens from a feature.
- Loading: the frame and titles show at once with placeholder rows for the cancellation; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: a cancelled feature is read-only.
- Offline: not available offline: cancellation needs the network. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-06 Try-out copy](../../data/e-f19-06-try-out-copy.md),
[E-F19-13 Code handover](../../data/e-f19-13-code-handover.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-06 Try-out copy | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13 | `u13-owner/s-f19-11-cancel-e-f19-06-try-out-copy-active-{desktop,phone}-{light,dark}.png` |
| E-F19-13 Code handover | Available | Badge "Available"; a new record starts here; next: Downloaded (UC-F19-23); fields editable within the role | U13 | `u13-owner/s-f19-11-cancel-e-f19-13-code-handover-available-{desktop,phone}-{light,dark}.png` |
| E-F19-13 Code handover | Downloaded | Badge "Downloaded"; final: read-only, no next state; the history shows how it got here | U13 | `u13-owner/s-f19-11-cancel-e-f19-13-code-handover-downloaded-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F19-10 Defects](s-f19-10-defects.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-12 Promotion](../04-promote/s-f19-12-promotion.md)
