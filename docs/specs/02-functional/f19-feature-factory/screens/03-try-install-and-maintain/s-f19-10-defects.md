🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-03 Try, install and maintain](README.md) › 🖥️ S-F19-10 Defects

# 🖥️ S-F19-10 Defects

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Report a defect.

## Entry points

Feature factory in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-03 step 4, U07 | desktop | ![FL-F19-03 step 4, U07, light](../../images/03-try-install-and-maintain/u07-administrator/4-defect-desktop-light.png) | ![FL-F19-03 step 4, U07, dark](../../images/03-try-install-and-maintain/u07-administrator/4-defect-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-10-defects-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-10-defects-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-10-defects-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-10-defects-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-10-defects-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-10-defects-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f19-10-defects-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f19-10-defects-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: defects with their state and fix dates against the limit.
- Empty: "No defect reported".
- Loading: the frame and titles show at once with placeholder rows for the defects; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: fixed defects are read-only.
- Offline: not available offline: reports are sent online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-16 Feature defect](../../data/e-f19-16-feature-defect.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-16 Feature defect | Active | Badge "Active"; a new record starts here; next: Fixed or Credited (UC-F19-10, UC-F19-22); fields editable within the role | U07 | `u07-administrator/s-f19-10-defects-e-f19-16-feature-defect-active-desktop-{light,dark}.png` |
| E-F19-16 Feature defect | Fixed | Badge "Fixed"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f19-10-defects-e-f19-16-feature-defect-fixed-desktop-{light,dark}.png` |
| E-F19-16 Feature defect | Credited | Badge "Credited"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f19-10-defects-e-f19-16-feature-defect-credited-desktop-{light,dark}.png` |

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

⬅️ [S-F19-09 Changes](s-f19-09-changes.md) · ⬆️ [Up](README.md) · ➡️ [S-F19-11 Cancel](s-f19-11-cancel.md)
