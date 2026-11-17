🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛟 [F20 Hosted support assistant (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F20-07 Employees' help](README.md) › 🖥️ S-F20-27 Report a problem

# 🖥️ S-F20-27 Report a problem

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)

## Purpose

Report a problem from the screen where it happened, with its context.

## Entry points

"Report a problem" in every screen's menu; an error message's button.

## Wireframe

```text
Report a problem
-------------------------------------------------------------------------------
Page: Expenses   Time: 10:02   Error: could not save
What happened? [                                   ]
[x] Add a masked screenshot                     [Send]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F20-07 step 3, U01 | desktop | ![FL-F20-07 step 3, U01, light](../../images/07-employees-help/u01-employee/3-report-a-problem-desktop-light.png) | ![FL-F20-07 step 3, U01, dark](../../images/07-employees-help/u01-employee/3-report-a-problem-desktop-dark.png) |
| FL-F20-07 step 3, U01 | phone | ![FL-F20-07 step 3, U01, light](../../images/07-employees-help/u01-employee/3-report-a-problem-phone-light.png) | ![FL-F20-07 step 3, U01, dark](../../images/07-employees-help/u01-employee/3-report-a-problem-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f20-27-report-a-problem-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f20-27-report-a-problem-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f20-27-report-a-problem-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f20-27-report-a-problem-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f20-27-report-a-problem-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f20-27-report-a-problem-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f20-27-report-a-problem-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f20-27-report-a-problem-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Page, time, error | E-F20-01 | text | no | yes |
| Description | E-F20-01 | text | yes | no |
| Screenshot | E-F20-03 | yes, no | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Send | footer | employee | request sent |

## States

- Normal: the context filled and the description.
- Empty: never empty: context is always filled.
- Loading: the frame and titles show at once with placeholder rows for the context; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a known incident, linked.
- Read-only: sent reports are read-only in My requests.
- Offline: The report form stays filled; sending waits for the network and is not queued. Nothing else is queued: D38
  keeps only today's schedule, time and intervention records offline; a banner says the connection is lost and the
  actions come back with it.

Shown entities (VD-15): [E-F20-01 Support request](../../data/e-f20-01-support-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F20-01 Support request | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f20-27-report-a-problem-e-f20-01-support-request-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone and desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F20-07 Employees' help](../../flows/fl-f20-07-employees-help.md)

## Open questions

None.

---

⬅️ [S-F20-26 Help on the phone](s-f20-26-help-on-the-phone.md) · ⬆️ [Up](README.md) ·
➡️ [S-F20-28 Incident handling](../03-incidents/s-f20-28-incident-handling.md)
