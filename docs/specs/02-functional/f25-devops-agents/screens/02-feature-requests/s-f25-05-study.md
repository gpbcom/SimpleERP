🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-02 Feature requests](README.md) › 🖥️ S-F25-05 Study

# 🖥️ S-F25-05 Study

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Study the code and the specs for a feature.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-02 step 1, U47 | desktop | ![FL-F25-02 step 1, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/1-study-desktop-light.png) | ![FL-F25-02 step 1, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/1-study-desktop-dark.png) |
| FL-F25-02 step 1, U47 | phone | ![FL-F25-02 step 1, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/1-study-phone-light.png) | ![FL-F25-02 step 1, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/1-study-phone-dark.png) |
| Error E1, U47 | desktop | ![Error E1, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/e1-silent-desktop-light.png) | ![Error E1, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/e1-silent-desktop-dark.png) |
| Error E1, U47 | phone | ![Error E1, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/e1-silent-phone-light.png) | ![Error E1, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/e1-silent-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-05-study-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-05-study-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-05-study-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-05-study-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-05-study-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-05-study-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-05-study-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-05-study-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: specs and code read with the summary.
- Empty: "No study running".
- Loading: the frame and titles show at once with placeholder rows for the study; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: always read-only.
- Offline: not available offline: online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F25-04 Study note](../../data/e-f25-04-study-note.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-04 Study note | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-05-study-e-f25-04-study-note-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-F25-02 Feature requests](../../flows/fl-f25-02-feature-requests.md)

## Open questions

None.

---

⬅️ [S-F25-04 Duplicates](../01-intake/s-f25-04-duplicates.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-06 Spec pull request](s-f25-06-spec-pull-request.md)
