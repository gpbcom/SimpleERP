🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-03 Bugs](README.md) › 🖥️ S-F25-09 Root cause

# 🖥️ S-F25-09 Root cause

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Find the cause in the code.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-03 step 2, U47 | desktop | ![FL-F25-03 step 2, U47, light](../../images/03-bugs/u47-simple-erp-maintainer/2-cause-desktop-light.png) | ![FL-F25-03 step 2, U47, dark](../../images/03-bugs/u47-simple-erp-maintainer/2-cause-desktop-dark.png) |
| FL-F25-03 step 2, U47 | phone | ![FL-F25-03 step 2, U47, light](../../images/03-bugs/u47-simple-erp-maintainer/2-cause-phone-light.png) | ![FL-F25-03 step 2, U47, dark](../../images/03-bugs/u47-simple-erp-maintainer/2-cause-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-09-root-cause-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-09-root-cause-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-09-root-cause-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-09-root-cause-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-09-root-cause-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-09-root-cause-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-09-root-cause-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-09-root-cause-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the trace and the cause.
- Empty: "No cause yet".
- Loading: the frame and titles show at once with placeholder rows for the cause; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; approvals and receipts also on the phone.

## Accessibility

Labelled controls; amounts and states as text.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F25-03 Bugs](../../flows/fl-f25-03-bugs.md)

## Open questions

None.

---

⬅️ [S-F25-08 Reproduce](s-f25-08-reproduce.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-10 Fix pull request](s-f25-10-fix-pull-request.md)
