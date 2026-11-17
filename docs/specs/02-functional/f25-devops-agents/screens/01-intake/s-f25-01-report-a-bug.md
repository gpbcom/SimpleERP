🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-01 Intake](README.md) › 🖥️ S-F25-01 Report a bug

# 🖥️ S-F25-01 Report a bug

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Report a bug from simple-ERP.

## Entry points

DevOps agents in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-01 step 1, U07 | desktop | ![FL-F25-01 step 1, U07, light](../../images/01-intake/u07-administrator/1-bug-desktop-light.png) | ![FL-F25-01 step 1, U07, dark](../../images/01-intake/u07-administrator/1-bug-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/06-vulnerability-handling/u07-administrator/e1-report-a-bug-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/06-vulnerability-handling/u07-administrator/e1-report-a-bug-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-01-report-a-bug-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-01-report-a-bug-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-01-report-a-bug-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-01-report-a-bug-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-01-report-a-bug-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-01-report-a-bug-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f25-01-report-a-bug-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f25-01-report-a-bug-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: the report form with optional masked screenshot.
- Empty: never empty: the form.
- Loading: the frame and titles show at once with placeholder rows for the report; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: sent reports read-only.
- Offline: The form stays filled; sending needs the network and is not queued. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F25-01 Bug or feature request](../../data/e-f25-01-bug-or-feature-request.md),
[E-F25-12 Vulnerability case](../../data/e-f25-12-vulnerability-case.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-01 Bug or feature request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-f25-01-report-a-bug-e-f25-01-bug-or-feature-request-active-desktop-{light,dark}.png`, `u13-owner/s-f25-01-report-a-bug-e-f25-01-bug-or-feature-request-active-{desktop,phone}-{light,dark}.png` |
| E-F25-12 Vulnerability case | Reported | Badge "Reported"; a new record starts here; next: Confirmed or Closed (UC-F25-01, UC-F25-22); fields editable within the role | U07 | `u07-administrator/s-f25-01-report-a-bug-e-f25-12-vulnerability-case-reported-desktop-{light,dark}.png` |
| E-F25-12 Vulnerability case | Confirmed | Badge "Confirmed"; next: Fixed (UC-F25-22); fields editable within the role | U07 | `u07-administrator/s-f25-01-report-a-bug-e-f25-12-vulnerability-case-confirmed-desktop-{light,dark}.png` |
| E-F25-12 Vulnerability case | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f25-01-report-a-bug-e-f25-12-vulnerability-case-closed-desktop-{light,dark}.png` |
| E-F25-12 Vulnerability case | Fixed | Badge "Fixed"; next: Disclosed (UC-F25-22); fields editable within the role | U07 | `u07-administrator/s-f25-01-report-a-bug-e-f25-12-vulnerability-case-fixed-desktop-{light,dark}.png` |

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

⬆️ [Up](README.md) · ➡️ [S-F25-02 Request a feature](s-f25-02-request-a-feature.md)
