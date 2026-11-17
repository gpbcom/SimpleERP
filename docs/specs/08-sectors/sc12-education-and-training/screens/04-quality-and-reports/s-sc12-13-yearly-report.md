🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🎓 [SC12 Education and training](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC12-04 Quality and reports](README.md) › 🖥️ S-SC12-13 Yearly report

# 🖥️ S-SC12-13 Yearly report

**Status:** 🔄 waiting for the owner

## Personas

- [U38 Training coordinator](../../../../01-users/personas/u38-training-coordinator.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to produce the yearly report
([UC-SC12-13](../../use-cases/04-quality-and-reports/uc-sc12-13-produce-the-yearly-report.md)).

## Entry points

Education and training in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC12-04 step 2, U38 | desktop | ![FL-SC12-04 step 2, U38, light](../../images/04-quality-and-reports/u38-training-coordinator/2-yearly-report-desktop-light.png) | ![FL-SC12-04 step 2, U38, dark](../../images/04-quality-and-reports/u38-training-coordinator/2-yearly-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc12-13-yearly-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc12-13-yearly-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc12-13-yearly-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc12-13-yearly-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc12-13-yearly-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc12-13-yearly-report-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc12-13-yearly-report-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc12-13-yearly-report-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC12-13 Yearly training report](../../data/e-sc12-13-yearly-training-report.md), shown as the entity
pages list them, with their examples.

## Actions

- Compute: [UC-SC12-13](../../use-cases/04-quality-and-reports/uc-sc12-13-produce-the-yearly-report.md), step 1.
- Check income: [UC-SC12-13](../../use-cases/04-quality-and-reports/uc-sc12-13-produce-the-yearly-report.md), step 2.
- Check: [UC-SC12-13](../../use-cases/04-quality-and-reports/uc-sc12-13-produce-the-yearly-report.md), step 3.
- File: [UC-SC12-13](../../use-cases/04-quality-and-reports/uc-sc12-13-produce-the-yearly-report.md), step 4.

## States

- Normal: the yearly report's figures.
- Empty: "No year to report".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, data missing: it is listed.
- Read-only: filed reports are read-only.
- Offline: not available offline: office work on enrolments, funding and billing. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC12-13 Yearly training report](../../data/e-sc12-13-yearly-training-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC12-13 Yearly training report | Prepared | Badge "Prepared"; a new record starts here; next: Filed (UC-SC12-13); fields editable within the role | U05, U38 | `u05-accounting/s-sc12-13-yearly-report-e-sc12-13-yearly-training-report-prepared-desktop-{light,dark}.png`, `u38-training-coordinator/s-sc12-13-yearly-report-e-sc12-13-yearly-training-report-prepared-desktop-{light,dark}.png` |
| E-SC12-13 Yearly training report | Filed | Badge "Filed"; final: read-only, no next state; the history shows how it got here | U05, U38 | `u05-accounting/s-sc12-13-yearly-report-e-sc12-13-yearly-training-report-filed-desktop-{light,dark}.png`, `u38-training-coordinator/s-sc12-13-yearly-report-e-sc12-13-yearly-training-report-filed-desktop-{light,dark}.png` |

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

- [FL-SC12-04 Quality and reports](../../flows/fl-sc12-04-quality-and-reports.md)

## Open questions

None.

---

⬅️ [S-SC12-12 Quality file](s-sc12-12-quality-file.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC12-14 Complaints](s-sc12-14-complaints.md)
