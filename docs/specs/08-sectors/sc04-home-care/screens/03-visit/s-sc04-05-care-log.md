🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-03 Visit](README.md) › 🖥️ S-SC04-05 Care log

# 🖥️ S-SC04-05 Care log

**Status:** ✅ specified

## Personas

- [U26 Carer](../../../../01-users/personas/u26-carer.md)
- [U25 Care coordinator](../../../../01-users/personas/u25-care-coordinator.md)

## Purpose

Used to keep the care log and report incidents
([UC-SC04-05](../../use-cases/03-visit/uc-sc04-05-keep-the-care-log-and-report-incidents.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-03 step 2, U26 | phone | ![FL-SC04-03 step 2, U26, light](../../images/03-visit/u26-carer/2-care-log-phone-light.png) | ![FL-SC04-03 step 2, U26, dark](../../images/03-visit/u26-carer/2-care-log-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc04-05-care-log-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc04-05-care-log-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc04-05-care-log-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc04-05-care-log-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc04-05-care-log-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc04-05-care-log-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc04-05-care-log-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc04-05-care-log-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC04-06 Care log entry](../../data/e-sc04-06-care-log-entry.md),
[E-SC04-07 Care incident](../../data/e-sc04-07-care-incident.md), shown as the entity pages list them, with their
examples.

## Actions

- Write the log: [UC-SC04-05](../../use-cases/03-visit/uc-sc04-05-keep-the-care-log-and-report-incidents.md), step 1.
- Report an incident: [UC-SC04-05](../../use-cases/03-visit/uc-sc04-05-keep-the-care-log-and-report-incidents.md), step
  2.
- Read and act: [UC-SC04-05](../../use-cases/03-visit/uc-sc04-05-keep-the-care-log-and-report-incidents.md), step 3.

## States

- Normal: the visit's log, the shared part, and incidents with seriousness and actions.
- Empty: "No note yet".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a serious incident: the family contact is told at once too
  ([BR-SC04-08](../../business-rules/br-sc04-08-incidents-reach-the-coordinator.md)).
- Read-only: the family reads the shared part only.
- Offline: works offline,
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md),
  the visit's earlier notes are kept on the phone; new notes and incidents wait in the queue and sync in order when the
  network is back,
  [BR-F2-21](../../../../02-functional/f02-no-code-configuration/business-rules/br-f02-21-offline-forms-keep-only-what-is-needed-and-sync-in-order.md).

Shown entities (VD-15): [E-SC04-06 Care log entry](../../data/e-sc04-06-care-log-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-06 Care log entry | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U09, U25, U26 | `u09-customer/s-sc04-05-care-log-e-sc04-06-care-log-entry-recorded-phone-{light,dark}.png`, `u25-care-coordinator/s-sc04-05-care-log-e-sc04-06-care-log-entry-recorded-{desktop,phone}-{light,dark}.png`, `u26-carer/s-sc04-05-care-log-e-sc04-06-care-log-entry-recorded-phone-{light,dark}.png` |

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

- [FL-SC04-03 Visit](../../flows/fl-sc04-03-visit.md)

## Open questions

None.

---

⬅️ [S-SC04-04 Visit](../02-plan-the-rounds/s-sc04-04-visit.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-06 Replacements](../02-plan-the-rounds/s-sc04-06-replacements.md)
