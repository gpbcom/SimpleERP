🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-04 Volunteers](README.md) › 🖥️ S-SC08-11 Volunteer time

# 🖥️ S-SC08-11 Volunteer time

**Status:** 🔄 waiting for the owner

## Personas

- [U32 Volunteer](../../../../01-users/personas/u32-volunteer.md)
- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to record and value volunteer time
([UC-SC08-11](../../use-cases/04-volunteers/uc-sc08-11-record-and-value-volunteer-time.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-04 step 2, U32 | phone | ![FL-SC08-04 step 2, U32, light](../../images/04-volunteers/u32-volunteer/2-hours-phone-light.png) | ![FL-SC08-04 step 2, U32, dark](../../images/04-volunteers/u32-volunteer/2-hours-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc08-11-volunteer-time-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc08-11-volunteer-time-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc08-11-volunteer-time-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc08-11-volunteer-time-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc08-11-volunteer-time-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc08-11-volunteer-time-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-11-volunteer-time-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-11-volunteer-time-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC08-11 Volunteer hours](../../data/e-sc08-11-volunteer-hours.md),
[E-F8-20 Volunteer contribution](../../../../02-functional/f08-accounting/data/e-f08-20-volunteer-contribution.md),
shown as the entity pages list them, with their examples.

## Actions

- Record hours: [UC-SC08-11](../../use-cases/04-volunteers/uc-sc08-11-record-and-value-volunteer-time.md), step 1.
- Approve: [UC-SC08-11](../../use-cases/04-volunteers/uc-sc08-11-record-and-value-volunteer-time.md), step 2.
- Value if chosen: [UC-SC08-11](../../use-cases/04-volunteers/uc-sc08-11-record-and-value-volunteer-time.md), step 3.
- Repay expenses: [UC-SC08-11](../../use-cases/04-volunteers/uc-sc08-11-record-and-value-volunteer-time.md), step 4.

## States

- Normal: hours per volunteer and mission, values and expenses.
- Empty: "No hours recorded".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, valuation off: only hours are recorded.
- Read-only: approved hours are read-only.
- Offline: hours typed on the phone are kept and sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC08-11 Volunteer hours](../../data/e-sc08-11-volunteer-hours.md),
[E-F8-20 Volunteer contribution](../../../../02-functional/f08-accounting/data/e-f08-20-volunteer-contribution.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC08-11 Volunteer hours | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U31, U32 | `u31-treasurer/s-sc08-11-volunteer-time-e-sc08-11-volunteer-hours-active-{desktop,phone}-{light,dark}.png`, `u32-volunteer/s-sc08-11-volunteer-time-e-sc08-11-volunteer-hours-active-phone-{light,dark}.png` |
| E-F8-20 Volunteer contribution | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U31, U32 | `u31-treasurer/s-sc08-11-volunteer-time-e-f08-20-volunteer-contribution-active-{desktop,phone}-{light,dark}.png`, `u32-volunteer/s-sc08-11-volunteer-time-e-f08-20-volunteer-contribution-active-phone-{light,dark}.png` |

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

- [FL-SC08-04 Volunteers](../../flows/fl-sc08-04-volunteers.md)

## Open questions

None.

---

⬅️ [S-SC08-10 Missions](s-sc08-10-missions.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-12 Events](../05-events/s-sc08-12-events.md)
