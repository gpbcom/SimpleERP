🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-05 Suppliers and customers](README.md) › 🖥️ S-SC05-11 Complaints 8D

# 🖥️ S-SC05-11 Complaints 8D

**Status:** ✅ specified

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to analyse customer complaints
([UC-SC05-11](../../use-cases/05-suppliers-and-customers/uc-sc05-11-analyse-customer-complaints.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-05 step 2, U27 | desktop | ![FL-SC05-05 step 2, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/2-complaint-8d-desktop-light.png) | ![FL-SC05-05 step 2, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/2-complaint-8d-desktop-dark.png) |
| FL-SC05-05 step 2, U27 | tablet | ![FL-SC05-05 step 2, U27, light](../../images/05-suppliers-and-customers/u27-quality-manager/2-complaint-8d-tablet-light.png) | ![FL-SC05-05 step 2, U27, dark](../../images/05-suppliers-and-customers/u27-quality-manager/2-complaint-8d-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-11-complaints-8d-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-11-complaints-8d-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-11-complaints-8d-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-11-complaints-8d-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-11-complaints-8d-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-11-complaints-8d-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-11-complaints-8d-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-11-complaints-8d-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-11 8D report](../../data/e-sc05-11-8d-report.md), shown as the entity pages list them, with their
examples.

## Actions

- Record: [UC-SC05-11](../../use-cases/05-suppliers-and-customers/uc-sc05-11-analyse-customer-complaints.md), step 1.
- Analyse in eight steps:
  [UC-SC05-11](../../use-cases/05-suppliers-and-customers/uc-sc05-11-analyse-customer-complaints.md), step 2.
- Answer: [UC-SC05-11](../../use-cases/05-suppliers-and-customers/uc-sc05-11-analyse-customer-complaints.md), step 3.
- Open the actions: [UC-SC05-11](../../use-cases/05-suppliers-and-customers/uc-sc05-11-analyse-customer-complaints.md),
  step 4.

## States

- Normal: the complaint and its eight steps with dates.
- Empty: "No complaint".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a step late: the quality manager is alerted.
- Read-only: a sent report is read-only.
- Offline: not available offline: office work on shared quality and planning records. Offline work is kept for the phone
  forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC05-11 8D report](../../data/e-sc05-11-8d-report.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-11 8D report | Sent | Badge "Sent"; a new record starts here; next: Complete (UC-SC05-11); fields editable within the role | U03, U27 | `u03-sales/s-sc05-11-complaints-8d-e-sc05-11-8d-report-sent-{desktop,phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc05-11-complaints-8d-e-sc05-11-8d-report-sent-{desktop,tablet}-{light,dark}.png` |
| E-SC05-11 8D report | Complete | Badge "Complete"; final: read-only, no next state; the history shows how it got here | U03, U27 | `u03-sales/s-sc05-11-complaints-8d-e-sc05-11-8d-report-complete-{desktop,phone,tablet}-{light,dark}.png`, `u27-quality-manager/s-sc05-11-complaints-8d-e-sc05-11-8d-report-complete-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC05-05 Suppliers and customers](../../flows/fl-sc05-05-suppliers-and-customers.md)

## Open questions

None.

---

⬅️ [S-SC05-10 Supplier quality](s-sc05-10-supplier-quality.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC05-12 Calibration](../04-quality-system/s-sc05-12-calibration.md)
