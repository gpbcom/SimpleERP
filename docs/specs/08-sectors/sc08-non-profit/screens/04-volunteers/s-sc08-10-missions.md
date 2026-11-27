🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-04 Volunteers](README.md) › 🖥️ S-SC08-10 Missions

# 🖥️ S-SC08-10 Missions

**Status:** ✅ specified

## Personas

- [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to recruit and register volunteers for missions
([UC-SC08-10](../../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-04 step 1, U32 | phone | ![FL-SC08-04 step 1, U32, light](../../images/04-volunteers/u32-volunteer/1-missions-phone-light.png) | ![FL-SC08-04 step 1, U32, dark](../../images/04-volunteers/u32-volunteer/1-missions-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc08-10-missions-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc08-10-missions-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc08-10-missions-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc08-10-missions-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc08-10-missions-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc08-10-missions-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-10-missions-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-10-missions-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-10 Mission](../../data/e-sc08-10-mission.md), shown as the entity pages list them, with their
examples.

## Actions

- Publish: [UC-SC08-10](../../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md), step
  1.
- Sign up: [UC-SC08-10](../../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md), step
  2.
- Confirm: [UC-SC08-10](../../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md), step
  3.
- Remind: [UC-SC08-10](../../use-cases/04-volunteers/uc-sc08-10-recruit-and-register-volunteers-for-missions.md), step
  4.

## States

- Normal: missions with places, volunteers and the waiting list.
- Empty: "No mission".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the mission full: the volunteer goes on the waiting list.
- Read-only: volunteers see their own sign-ups.
- Offline: the mission list stays readable on the phone; sign-ups wait for the network.

Shown entities (VD-15): [E-SC08-10 Mission](../../data/e-sc08-10-mission.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-10 Mission | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U13, U32 | `u13-owner/s-sc08-10-missions-e-sc08-10-mission-active-{desktop,phone}-{light,dark}.png`, `u32-volunteer/s-sc08-10-missions-e-sc08-10-mission-active-phone-{light,dark}.png` |

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

- [FL-SC08-04 Volunteers](../../flows/fl-sc08-04-volunteers.md)

## Open questions

None.

---

⬅️ [S-SC08-09 Grant reports](../03-grants/s-sc08-09-grant-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-11 Volunteer time](s-sc08-11-volunteer-time.md)
