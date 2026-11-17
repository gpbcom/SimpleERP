🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-01 Intake](README.md) › 🖥️ S-F25-04 Duplicates

# 🖥️ S-F25-04 Duplicates

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Deduplicate against open issues.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-01 step 4, U47 | desktop | ![FL-F25-01 step 4, U47, light](../../images/01-intake/u47-simple-erp-maintainer/4-duplicates-desktop-light.png) | ![FL-F25-01 step 4, U47, dark](../../images/01-intake/u47-simple-erp-maintainer/4-duplicates-desktop-dark.png) |
| FL-F25-01 step 4, U47 | phone | ![FL-F25-01 step 4, U47, light](../../images/01-intake/u47-simple-erp-maintainer/4-duplicates-phone-light.png) | ![FL-F25-01 step 4, U47, dark](../../images/01-intake/u47-simple-erp-maintainer/4-duplicates-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-04-duplicates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-04-duplicates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-04-duplicates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-04-duplicates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-04-duplicates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-04-duplicates-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-04-duplicates-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-04-duplicates-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: candidate duplicates with similarity.
- Empty: "No duplicate".
- Loading: the frame and titles show at once with placeholder rows for the duplicates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: linked ones read-only.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-02 USER feature](../../data/e-f25-02-user-feature.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-02 USER feature | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-04-duplicates-e-f25-02-user-feature-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-01 Intake](../../flows/fl-f25-01-intake.md)

## Open questions

None.

---

⬅️ [S-F25-03 USER ticket](s-f25-03-user-ticket.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-05 Study](../02-feature-requests/s-f25-05-study.md)
