🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-02 Office suites](README.md) › 🖥️ S-F24-04 Suite files

# 🖥️ S-F24-04 Suite files

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Store and edit documents in the suite.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-02 step 2, U16 | desktop | ![FL-F24-02 step 2, U16, light](../../images/02-office-suites/u16-office-worker/2-files-desktop-light.png) | ![FL-F24-02 step 2, U16, dark](../../images/02-office-suites/u16-office-worker/2-files-desktop-dark.png) |
| FL-F24-02 step 2, U16 | phone | ![FL-F24-02 step 2, U16, light](../../images/02-office-suites/u16-office-worker/2-files-phone-light.png) | ![FL-F24-02 step 2, U16, dark](../../images/02-office-suites/u16-office-worker/2-files-phone-dark.png) |
| Error E1, U16 | desktop | ![Error E1, U16, light](../../images/02-office-suites/u16-office-worker/e1-locked-desktop-light.png) | ![Error E1, U16, dark](../../images/02-office-suites/u16-office-worker/e1-locked-desktop-dark.png) |
| Error E1, U16 | phone | ![Error E1, U16, light](../../images/02-office-suites/u16-office-worker/e1-locked-phone-light.png) | ![Error E1, U16, dark](../../images/02-office-suites/u16-office-worker/e1-locked-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-04-suite-files-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-04-suite-files-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-04-suite-files-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-04-suite-files-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-04-suite-files-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-04-suite-files-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-04-suite-files-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-04-suite-files-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the suite's folders and documents linked to records.
- Empty: "No document linked".
- Loading: the frame and titles show at once with placeholder rows for the documents; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: within the suite's rights.
- Offline: Documents already opened stay readable in the suite's app. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md),
[E-F24-04 Linked document](../../data/e-f24-04-linked-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-03 Suite component | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U16 | `u01-employee/s-f24-04-suite-files-e-f24-03-suite-component-active-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f24-04-suite-files-e-f24-03-suite-component-active-{desktop,phone}-{light,dark}.png` |
| E-F24-04 Linked document | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01, U16 | `u01-employee/s-f24-04-suite-files-e-f24-04-linked-document-active-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f24-04-suite-files-e-f24-04-linked-document-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-F24-02 Office suites](../../flows/fl-f24-02-office-suites.md)

## Open questions

None.

---

⬅️ [S-F24-03 Suite sign-in](s-f24-03-suite-sign-in.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-05 Groupware](s-f24-05-groupware.md)
