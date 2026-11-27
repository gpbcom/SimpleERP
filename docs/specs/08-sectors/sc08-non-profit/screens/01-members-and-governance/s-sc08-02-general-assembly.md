🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-01 Members and governance](README.md) ›
🖥️ S-SC08-02 General assembly

# 🖥️ S-SC08-02 General assembly

**Status:** 🔄 waiting for the owner

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to run the general assembly
([UC-SC08-02](../../use-cases/01-members-and-governance/uc-sc08-02-run-the-general-assembly.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-01 step 2, U13 | desktop | ![FL-SC08-01 step 2, U13, light](../../images/01-members-and-governance/u13-owner/2-assembly-desktop-light.png) | ![FL-SC08-01 step 2, U13, dark](../../images/01-members-and-governance/u13-owner/2-assembly-desktop-dark.png) |
| FL-SC08-01 step 2, U13 | phone | ![FL-SC08-01 step 2, U13, light](../../images/01-members-and-governance/u13-owner/2-assembly-phone-light.png) | ![FL-SC08-01 step 2, U13, dark](../../images/01-members-and-governance/u13-owner/2-assembly-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/01-members-and-governance/u13-owner/e1-no-quorum-desktop-light.png) | ![Error E1, U13, dark](../../images/01-members-and-governance/u13-owner/e1-no-quorum-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/01-members-and-governance/u13-owner/e1-no-quorum-phone-light.png) | ![Error E1, U13, dark](../../images/01-members-and-governance/u13-owner/e1-no-quorum-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-02-general-assembly-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-02-general-assembly-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-02-general-assembly-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-02-general-assembly-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-02-general-assembly-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-02-general-assembly-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-02-general-assembly-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-02-general-assembly-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-03 Assembly or board meeting](../../data/e-sc08-03-assembly-or-board-meeting.md), shown as the
entity pages list them, with their examples.

## Actions

- Send the notice: [UC-SC08-02](../../use-cases/01-members-and-governance/uc-sc08-02-run-the-general-assembly.md), step
  1.
- Record attendance and proxies:
  [UC-SC08-02](../../use-cases/01-members-and-governance/uc-sc08-02-run-the-general-assembly.md), step 2.
- Vote: [UC-SC08-02](../../use-cases/01-members-and-governance/uc-sc08-02-run-the-general-assembly.md), step 3.
- Write minutes: [UC-SC08-02](../../use-cases/01-members-and-governance/uc-sc08-02-run-the-general-assembly.md), step 4.

## States

- Normal: the assembly's notice, attendance, proxies, quorum, resolutions and votes.
- Empty: "No assembly planned".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the quorum not reached: a second assembly is called as the
  statutes say.
- Read-only: signed minutes are read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC08-03 Assembly or board meeting](../../data/e-sc08-03-assembly-or-board-meeting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-03 Assembly or board meeting | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U31 | `u13-owner/s-sc08-02-general-assembly-e-sc08-03-assembly-or-board-meeting-active-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-02-general-assembly-e-sc08-03-assembly-or-board-meeting-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

(Proposed) Desktop; approvals and receipts also on the phone.

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

⬅️ [S-SC08-01 Members](s-sc08-01-members.md) · ⬆️ [Up](README.md) · ➡️ [S-SC08-03 Board](s-sc08-03-board.md)
