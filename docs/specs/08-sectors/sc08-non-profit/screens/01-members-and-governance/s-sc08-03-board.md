🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-01 Members and governance](README.md) › 🖥️ S-SC08-03 Board

# 🖥️ S-SC08-03 Board

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to run the board and its decisions
([UC-SC08-03](../../use-cases/01-members-and-governance/uc-sc08-03-run-the-board-and-its-decisions.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-01 step 3, U13 | desktop | ![FL-SC08-01 step 3, U13, light](../../images/01-members-and-governance/u13-owner/3-board-desktop-light.png) | ![FL-SC08-01 step 3, U13, dark](../../images/01-members-and-governance/u13-owner/3-board-desktop-dark.png) |
| FL-SC08-01 step 3, U13 | phone | ![FL-SC08-01 step 3, U13, light](../../images/01-members-and-governance/u13-owner/3-board-phone-light.png) | ![FL-SC08-01 step 3, U13, dark](../../images/01-members-and-governance/u13-owner/3-board-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-03-board-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-03-board-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-03-board-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-03-board-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-03-board-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-03-board-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-03-board-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-03-board-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-03 Assembly or board meeting](../../data/e-sc08-03-assembly-or-board-meeting.md), shown as the
entity pages list them, with their examples.

## Actions

- Convene: [UC-SC08-03](../../use-cases/01-members-and-governance/uc-sc08-03-run-the-board-and-its-decisions.md), step
  1.
- Meet: [UC-SC08-03](../../use-cases/01-members-and-governance/uc-sc08-03-run-the-board-and-its-decisions.md), step 2.
- Decide: [UC-SC08-03](../../use-cases/01-members-and-governance/uc-sc08-03-run-the-board-and-its-decisions.md), step 3.
- Record: [UC-SC08-03](../../use-cases/01-members-and-governance/uc-sc08-03-run-the-board-and-its-decisions.md), step 4.

## States

- Normal: board meetings, decisions and their actions.
- Empty: "No board meeting".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a member not on the board: cannot vote.
- Read-only: recorded decisions are read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC08-03 Assembly or board meeting](../../data/e-sc08-03-assembly-or-board-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-03 Assembly or board meeting | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U31 | `u13-owner/s-sc08-03-board-e-sc08-03-assembly-or-board-meeting-active-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-03-board-e-sc08-03-assembly-or-board-meeting-active-{desktop,phone}-{light,dark}.png` |

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

## Shown in

- [FL-SC08-01 Members and governance](../../flows/fl-sc08-01-members-and-governance.md)

## Open questions

None.

---

⬅️ [S-SC08-02 General assembly](s-sc08-02-general-assembly.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-04 Donations](../02-donations-and-receipts/s-sc08-04-donations.md)
