🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-05 Security and data compliance](README.md) ›
🖥️ S-SC14-13 Incident reports

# 🖥️ S-SC14-13 Incident reports

**Status:** 🔄 waiting for the owner

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to report security incidents
([UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md)).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-05 step 3, U07 | desktop | ![FL-SC14-05 step 3, U07, light](../../images/05-security-and-data-compliance/u07-administrator/3-incident-report-desktop-light.png) | ![FL-SC14-05 step 3, U07, dark](../../images/05-security-and-data-compliance/u07-administrator/3-incident-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-13-incident-reports-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-13-incident-reports-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-13-incident-reports-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-13-incident-reports-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-13-incident-reports-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-13-incident-reports-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc14-13-incident-reports-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc14-13-incident-reports-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC14-12 Security report](../../data/e-sc14-12-security-report.md), shown as the entity pages list them,
with their examples.

## Actions

- Assess: [UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md), step 1.
- Send the early warning:
  [UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md), step 2.
- Approve: [UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md), step
  3.
- Notify and report:
  [UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md), step 4.

## States

- Normal: incidents with stages and times.
- Empty: "No incident".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, late: the owner is alerted.
- Read-only: sent stages are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-12 Security report](../../data/e-sc14-12-security-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-12 Security report | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U13 | `u07-administrator/s-sc14-13-incident-reports-e-sc14-12-security-report-active-desktop-{light,dark}.png`, `u13-owner/s-sc14-13-incident-reports-e-sc14-12-security-report-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-05 Security and data compliance](../../flows/fl-sc14-05-security-and-data-compliance.md)

## Open questions

None.

---

⬅️ [S-SC14-12 Vulnerabilities](s-sc14-12-vulnerabilities.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-14 Data export](s-sc14-14-data-export.md)
