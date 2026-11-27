🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) ›
📦 [SC15 Wholesale and distribution](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-SC15-05 Sales force and performance](README.md) › 🖥️ S-SC15-14 Visits

# 🖥️ S-SC15-14 Visits

**Status:** ✅ specified

## Personas

- [U42 Sales representative](../../../../01-users/personas/u42-sales-representative.md)
- [U03 Sales](../../../../01-users/personas/u03-sales.md)

## Purpose

Used to follow sales reps' visits, routes and targets,
[UC-SC15-14](../../use-cases/05-sales-force-and-performance/uc-sc15-14-follow-sales-reps-visits-routes-and-targets.md).

## Entry points

Wholesale and distribution in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC15-05 step 1, U42 | phone | ![FL-SC15-05 step 1, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-phone-light.png) | ![FL-SC15-05 step 1, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-phone-dark.png) |
| FL-SC15-05 step 1, U42 | desktop | ![FL-SC15-05 step 1, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-desktop-light.png) | ![FL-SC15-05 step 1, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-desktop-dark.png) |
| FL-SC15-05 step 1, U42 | tablet | ![FL-SC15-05 step 1, U42, light](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-tablet-light.png) | ![FL-SC15-05 step 1, U42, dark](../../images/05-sales-force-and-performance/u42-sales-representative/1-visits-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc15-14-visits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc15-14-visits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc15-14-visits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc15-14-visits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc15-14-visits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc15-14-visits-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc15-14-visits-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc15-14-visits-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC15-11 Visit report](../../data/e-sc15-11-visit-report.md),
[E-F9-26 Round](../../../../02-functional/f09-hr-and-projects/data/e-f09-26-round.md),
[E-F6-18 Commission plan and target](../../../../02-functional/f06-customers-and-sales/data/e-f06-18-commission-plan-and-target.md),
shown as the entity pages list them, with their examples.

## Actions

- Plan the route:
  [UC-SC15-14](../../use-cases/05-sales-force-and-performance/uc-sc15-14-follow-sales-reps-visits-routes-and-targets.md),
  step 1.
- Visit and report:
  [UC-SC15-14](../../use-cases/05-sales-force-and-performance/uc-sc15-14-follow-sales-reps-visits-routes-and-targets.md),
  step 2.
- Take orders:
  [UC-SC15-14](../../use-cases/05-sales-force-and-performance/uc-sc15-14-follow-sales-reps-visits-routes-and-targets.md),
  step 3.
- Follow targets:
  [UC-SC15-14](../../use-cases/05-sales-force-and-performance/uc-sc15-14-follow-sales-reps-visits-routes-and-targets.md),
  step 4.

## States

- Normal: the rep's route, visits, reports and targets.
- Empty: "No visit planned".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, no consent: no location is recorded.
- Read-only: reps see their own.
- Offline: the week's route and customers stay on the tablet; reports sync later,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).

Shown entities (VD-15): [E-SC15-11 Visit report](../../data/e-sc15-11-visit-report.md),
[E-F6-18 Commission plan and target](../../../../02-functional/f06-customers-and-sales/data/e-f06-18-commission-plan-and-target.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC15-11 Visit report | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U42 | `u03-sales/s-sc15-14-visits-e-sc15-11-visit-report-active-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-14-visits-e-sc15-11-visit-report-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Draft | Badge "Draft"; a new record starts here; next: Active (UC-F6-25); fields editable within the role | U03, U42 | `u03-sales/s-sc15-14-visits-e-f06-18-commission-plan-and-target-draft-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-14-visits-e-f06-18-commission-plan-and-target-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Active | Badge "Active"; next: Closed (UC-SC11-17); fields editable within the role | U03, U42 | `u03-sales/s-sc15-14-visits-e-f06-18-commission-plan-and-target-active-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-14-visits-e-f06-18-commission-plan-and-target-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-F6-18 Commission plan and target | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U03, U42 | `u03-sales/s-sc15-14-visits-e-f06-18-commission-plan-and-target-closed-{desktop,phone,tablet}-{light,dark}.png`, `u42-sales-representative/s-sc15-14-visits-e-f06-18-commission-plan-and-target-closed-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC15-05 Sales force and performance](../../flows/fl-sc15-05-sales-force-and-performance.md)

## Open questions

None.

---

⬅️ [S-SC15-13 EU statistics](../04-import-and-suppliers/s-sc15-13-eu-statistics.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC15-15 Margins](s-sc15-15-margins.md)
