🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-06 Firm management](README.md) › 🖥️ S-SC11-18 Training

# 🖥️ S-SC11-18 Training

**Status:** 🔄 waiting for the owner

## Personas

- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to track continuing professional training
([UC-SC11-18](../../use-cases/06-firm-management/uc-sc11-18-track-continuing-professional-training.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-06 step 3, U36 | desktop | ![FL-SC11-06 step 3, U36, light](../../images/06-firm-management/u36-professional/3-training-desktop-light.png) | ![FL-SC11-06 step 3, U36, dark](../../images/06-firm-management/u36-professional/3-training-desktop-dark.png) |
| FL-SC11-06 step 3, U36 | phone | ![FL-SC11-06 step 3, U36, light](../../images/06-firm-management/u36-professional/3-training-phone-light.png) | ![FL-SC11-06 step 3, U36, dark](../../images/06-firm-management/u36-professional/3-training-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-18-training-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-18-training-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-18-training-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-18-training-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-18-training-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-18-training-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-18-training-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-18-training-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-15 Training record](../../data/e-sc11-15-training-record.md), shown as the entity pages list them,
with their examples.

## Actions

- Record: [UC-SC11-18](../../use-cases/06-firm-management/uc-sc11-18-track-continuing-professional-training.md), step 1.
- Follow: [UC-SC11-18](../../use-cases/06-firm-management/uc-sc11-18-track-continuing-professional-training.md), step 2.
- Report: [UC-SC11-18](../../use-cases/06-firm-management/uc-sc11-18-track-continuing-professional-training.md), step 3.
- Plan: [UC-SC11-18](../../use-cases/06-firm-management/uc-sc11-18-track-continuing-professional-training.md), step 4.

## States

- Normal: training hours against the requirement.
- Empty: "No training".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, below the requirement: a reminder is sent.
- Read-only: reported years are read-only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-15 Training record](../../data/e-sc11-15-training-record.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-15 Training record | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U36 | `u36-professional/s-sc11-18-training-e-sc11-15-training-record-recorded-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-06 Firm management](../../flows/fl-sc11-06-firm-management.md)

## Open questions

None.

---

⬅️ [S-SC11-17 Partners](s-sc11-17-partners.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-19 Performance](s-sc11-19-performance.md)
