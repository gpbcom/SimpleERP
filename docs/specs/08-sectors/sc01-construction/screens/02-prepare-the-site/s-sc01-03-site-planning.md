🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-02 Prepare the site](README.md) › 🖥️ S-SC01-03 Site planning

# 🖥️ S-SC01-03 Site planning

**Status:** ✅ specified

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)

## Purpose

Used to plan the site ([UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md)); to declare works
near networks and keep the safety documents,
[UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-02 step 1, U22 | desktop | ![FL-SC01-02 step 1, U22, light](../../images/02-prepare-the-site/u22-site-manager/1-planning-desktop-light.png) | ![FL-SC01-02 step 1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/1-planning-desktop-dark.png) |
| FL-SC01-02 step 1, U22 | phone | ![FL-SC01-02 step 1, U22, light](../../images/02-prepare-the-site/u22-site-manager/1-planning-phone-light.png) | ![FL-SC01-02 step 1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/1-planning-phone-dark.png) |
| FL-SC01-02 step 1, U22 | tablet | ![FL-SC01-02 step 1, U22, light](../../images/02-prepare-the-site/u22-site-manager/1-planning-tablet-light.png) | ![FL-SC01-02 step 1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/1-planning-tablet-dark.png) |
| Error E1, U22 | desktop | ![Error E1, U22, light](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-desktop-light.png) | ![Error E1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-desktop-dark.png) |
| Error E1, U22 | phone | ![Error E1, U22, light](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-phone-light.png) | ![Error E1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-phone-dark.png) |
| Error E1, U22 | tablet | ![Error E1, U22, light](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-tablet-light.png) | ![Error E1, U22, dark](../../images/02-prepare-the-site/u22-site-manager/e1-no-answer-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-03-site-planning-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-03-site-planning-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-03-site-planning-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-03-site-planning-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-03-site-planning-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-03-site-planning-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-03-site-planning-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-03-site-planning-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-03 Site phase](../../data/e-sc01-03-site-phase.md),
[E-SC01-08 Equipment assignment](../../data/e-sc01-08-equipment-assignment.md),
[E-SC01-09 Works declaration](../../data/e-sc01-09-works-declaration.md), shown as the entity pages list them, with
their examples.

## Actions

- Set the phases: [UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md), step 1.
- Assign crews: [UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md), step 2.
- Book equipment: [UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md), step 3.
- Add subcontractors: [UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md), step 4.
- Publish the plan: [UC-SC01-03](../../use-cases/02-prepare-the-site/uc-sc01-03-plan-the-site.md), step 5.
- Unblock the phase:
  [UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md),
  step 4.

## States

- Normal: the site's timeline: phases as bars, crews, equipment and subcontractors per day, conflicts in red with a
  word.
- Empty: "No phase yet", with Add a phase.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a subcontractor not accepted or without a valid vigilance
  certificate: it cannot be planned and is flagged
  ([BR-SC01-06](../../business-rules/br-sc01-06-subcontractor-documents-before-work.md)).
- Read-only: field workers see only their own days; a published plan changes only by a new publication.
- Offline: the published plan of today and the next days stays readable on the phone; planning waits for the network.

Shown entities (VD-15): [E-SC01-08 Equipment assignment](../../data/e-sc01-08-equipment-assignment.md),
[E-SC01-09 Works declaration](../../data/e-sc01-09-works-declaration.md),
[E-SC01-14 Site safety document](../../data/e-sc01-14-site-safety-document.md),
[E-SC01-03 Site phase](../../data/e-sc01-03-site-phase.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-08 Equipment assignment | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-03-site-planning-e-sc01-08-equipment-assignment-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-09 Works declaration | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-03-site-planning-e-sc01-09-works-declaration-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-14 Site safety document | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-03-site-planning-e-sc01-14-site-safety-document-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-03 Site phase | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-03-site-planning-e-sc01-03-site-phase-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-02 Prepare the site](../../flows/fl-sc01-02-prepare-the-site.md)

## Open questions

None.

---

⬅️ [S-SC01-02 Quote by lots](../01-win-the-work/s-sc01-02-quote-by-lots.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-04 Site time](../03-run-the-site/s-sc01-04-site-time.md)
