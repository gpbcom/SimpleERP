🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-02 Office suites](README.md) › 🖥️ S-F24-05 Groupware

# 🖥️ S-F24-05 Groupware

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Sync mail, calendars and contacts.

## Entry points

Integrations hub in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-02 step 3, U01 | desktop | ![FL-F24-02 step 3, U01, light](../../images/02-office-suites/u01-employee/3-groupware-desktop-light.png) | ![FL-F24-02 step 3, U01, dark](../../images/02-office-suites/u01-employee/3-groupware-desktop-dark.png) |
| FL-F24-02 step 3, U01 | phone | ![FL-F24-02 step 3, U01, light](../../images/02-office-suites/u01-employee/3-groupware-phone-light.png) | ![FL-F24-02 step 3, U01, dark](../../images/02-office-suites/u01-employee/3-groupware-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-05-groupware-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-05-groupware-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-05-groupware-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-05-groupware-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-05-groupware-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-05-groupware-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f24-05-groupware-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f24-05-groupware-offline-phone-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: mail, calendars and contacts synced.
- Empty: "Nothing synced".
- Loading: the frame and titles show at once with placeholder rows for the calendars; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: own only.
- Offline: Calendar entries already synced stay visible; changes wait for sync in the suite's app. Nothing else is
  queued: D38 keeps only today's schedule, time and intervention records offline; a banner says the connection is lost
  and the actions come back with it.

Shown entities (VD-15): [E-F24-03 Suite component](../../data/e-f24-03-suite-component.md),
[E-F24-05 Calendar link](../../data/e-f24-05-calendar-link.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-03 Suite component | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f24-05-groupware-e-f24-03-suite-component-active-{desktop,phone}-{light,dark}.png` |
| E-F24-05 Calendar link | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f24-05-groupware-e-f24-05-calendar-link-active-{desktop,phone}-{light,dark}.png` |

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

⬅️ [S-F24-04 Suite files](s-f24-04-suite-files.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-06 Suite chat](s-f24-06-suite-chat.md)
