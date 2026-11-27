🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🤲 [SC08 Non-profit association](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC08-03 Grants](README.md) › 🖥️ S-SC08-09 Grant reports

# 🖥️ S-SC08-09 Grant reports

**Status:** ✅ specified

## Personas

- [U31 Treasurer](../../../../01-users/personas/u31-treasurer.md)

## Purpose

Used to report to funders on grants ([UC-SC08-09](../../use-cases/03-grants/uc-sc08-09-report-to-funders-on-grants.md)).

## Entry points

Non-profit association in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC08-03 step 2, U31 | desktop | ![FL-SC08-03 step 2, U31, light](../../images/03-grants/u31-treasurer/2-report-desktop-light.png) | ![FL-SC08-03 step 2, U31, dark](../../images/03-grants/u31-treasurer/2-report-desktop-dark.png) |
| FL-SC08-03 step 2, U31 | phone | ![FL-SC08-03 step 2, U31, light](../../images/03-grants/u31-treasurer/2-report-phone-light.png) | ![FL-SC08-03 step 2, U31, dark](../../images/03-grants/u31-treasurer/2-report-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc08-09-grant-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc08-09-grant-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc08-09-grant-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc08-09-grant-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc08-09-grant-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc08-09-grant-reports-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc08-09-grant-reports-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc08-09-grant-reports-offline-phone-dark.png) |

## Fields and columns

The fields of [E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md),
[E-SC08-09 Grant report](../../data/e-sc08-09-grant-report.md), shown as the entity pages list them, with their
examples.

## Actions

- Gather spending: [UC-SC08-09](../../use-cases/03-grants/uc-sc08-09-report-to-funders-on-grants.md), step 1.
- Fill the report: [UC-SC08-09](../../use-cases/03-grants/uc-sc08-09-report-to-funders-on-grants.md), step 2.
- Sign: [UC-SC08-09](../../use-cases/03-grants/uc-sc08-09-report-to-funders-on-grants.md), step 3.
- Send: [UC-SC08-09](../../use-cases/03-grants/uc-sc08-09-report-to-funders-on-grants.md), step 4.

## States

- Normal: the report's spending per grant and its state.
- Empty: "No report due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, late: the treasurer is reminded.
- Read-only: a sent report is read-only.
- Offline: not available offline: office work on members, gifts and accounts shared by the board. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F8-18 Grant](../../../../02-functional/f08-accounting/data/e-f08-18-grant.md),
[E-SC08-09 Grant report](../../data/e-sc08-09-grant-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-18 Grant | Granted | Badge "Granted"; a new record starts here; next: Received (UC-SC12-19); fields editable within the role | U13, U31 | `u13-owner/s-sc08-09-grant-reports-e-f08-18-grant-granted-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-09-grant-reports-e-f08-18-grant-granted-{desktop,phone}-{light,dark}.png` |
| E-F8-18 Grant | Received | Badge "Received"; next: Closed (UC-F8-22); fields editable within the role | U13, U31 | `u13-owner/s-sc08-09-grant-reports-e-f08-18-grant-received-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-09-grant-reports-e-f08-18-grant-received-{desktop,phone}-{light,dark}.png` |
| E-F8-18 Grant | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U13, U31 | `u13-owner/s-sc08-09-grant-reports-e-f08-18-grant-closed-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-09-grant-reports-e-f08-18-grant-closed-{desktop,phone}-{light,dark}.png` |
| E-SC08-09 Grant report | Sent | Badge "Sent"; a new record starts here; next: Late (UC-SC08-09); fields editable within the role | U13, U31 | `u13-owner/s-sc08-09-grant-reports-e-sc08-09-grant-report-sent-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-09-grant-reports-e-sc08-09-grant-report-sent-{desktop,phone}-{light,dark}.png` |
| E-SC08-09 Grant report | Late | Badge "Late"; next: Sent (UC-SC08-09); fields editable within the role | U13, U31 | `u13-owner/s-sc08-09-grant-reports-e-sc08-09-grant-report-late-{desktop,phone}-{light,dark}.png`, `u31-treasurer/s-sc08-09-grant-reports-e-sc08-09-grant-report-late-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC08-03 Grants](../../flows/fl-sc08-03-grants.md)

## Open questions

None.

---

⬅️ [S-SC08-08 Grants](s-sc08-08-grants.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC08-10 Missions](../04-volunteers/s-sc08-10-missions.md)
