🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🌾 [SC13 Agriculture and food](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC13-05 Food processing](README.md) › 🖥️ S-SC13-15 HACCP

# 🖥️ S-SC13-15 HACCP

**Status:** ✅ specified

## Personas

- [U20 Production operator](../../../../01-users/personas/u20-production-operator.md)
- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to run HACCP and hygiene records
([UC-SC13-15](../../use-cases/05-food-processing/uc-sc13-15-run-haccp-and-hygiene-records.md)).

## Entry points

Agriculture and food in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC13-05 step 3, U20 | tablet | ![FL-SC13-05 step 3, U20, light](../../images/05-food-processing/u20-production-operator/3-haccp-tablet-light.png) | ![FL-SC13-05 step 3, U20, dark](../../images/05-food-processing/u20-production-operator/3-haccp-tablet-dark.png) |
| Empty | tablet | ![Empty, light](../../images/states/s-sc13-15-haccp-empty-tablet-light.png) | ![Empty, dark](../../images/states/s-sc13-15-haccp-empty-tablet-dark.png) |
| Loading | tablet | ![Loading, light](../../images/states/s-sc13-15-haccp-loading-tablet-light.png) | ![Loading, dark](../../images/states/s-sc13-15-haccp-loading-tablet-dark.png) |
| Read-only | tablet | ![Read-only, light](../../images/states/s-sc13-15-haccp-read-only-tablet-light.png) | ![Read-only, dark](../../images/states/s-sc13-15-haccp-read-only-tablet-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc13-15-haccp-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc13-15-haccp-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC13-13 Hygiene reading](../../data/e-sc13-13-hygiene-reading.md), shown as the entity pages list them,
with their examples.

## Actions

- Take readings: [UC-SC13-15](../../use-cases/05-food-processing/uc-sc13-15-run-haccp-and-hygiene-records.md), step 1.
- Record: [UC-SC13-15](../../use-cases/05-food-processing/uc-sc13-15-run-haccp-and-hygiene-records.md), step 2.
- Correct: [UC-SC13-15](../../use-cases/05-food-processing/uc-sc13-15-run-haccp-and-hygiene-records.md), step 3.
- Review: [UC-SC13-15](../../use-cases/05-food-processing/uc-sc13-15-run-haccp-and-hygiene-records.md), step 4.

## States

- Normal: readings due and done with actions.
- Empty: "No reading due".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, missed: the quality manager is alerted.
- Read-only: past days are read-only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the schedule are kept on the phone; readings wait and sync in order when the network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC13-13 Hygiene reading](../../data/e-sc13-13-hygiene-reading.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC13-13 Hygiene reading | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U20, U27 | `u20-production-operator/s-sc13-15-haccp-e-sc13-13-hygiene-reading-recorded-tablet-{light,dark}.png`, `u27-quality-manager/s-sc13-15-haccp-e-sc13-13-hygiene-reading-recorded-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC13-05 Food processing](../../flows/fl-sc13-05-food-processing.md)

## Open questions

None.

---

⬅️ [S-SC13-14 Traceability](s-sc13-14-traceability.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC13-16 Labels](s-sc13-16-labels.md)
