🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-02 Prepare the site](README.md) › 🖥️ S-SC01-09 Works declarations

# 🖥️ S-SC01-09 Works declarations

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)

## Purpose

Used to declare works near networks and keep the safety documents,
[UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-02 step 3, U22 | desktop | ![FL-SC01-02 step 3, U22, light](../../images/02-prepare-the-site/u22-site-manager/3-declarations-desktop-light.png) | ![FL-SC01-02 step 3, U22, dark](../../images/02-prepare-the-site/u22-site-manager/3-declarations-desktop-dark.png) |
| FL-SC01-02 step 3, U22 | phone | ![FL-SC01-02 step 3, U22, light](../../images/02-prepare-the-site/u22-site-manager/3-declarations-phone-light.png) | ![FL-SC01-02 step 3, U22, dark](../../images/02-prepare-the-site/u22-site-manager/3-declarations-phone-dark.png) |
| FL-SC01-02 step 3, U22 | tablet | ![FL-SC01-02 step 3, U22, light](../../images/02-prepare-the-site/u22-site-manager/3-declarations-tablet-light.png) | ![FL-SC01-02 step 3, U22, dark](../../images/02-prepare-the-site/u22-site-manager/3-declarations-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-09-works-declarations-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-09-works-declarations-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-09-works-declarations-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-09-works-declarations-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-09-works-declarations-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-09-works-declarations-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-09-works-declarations-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-09-works-declarations-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-09 Works declaration](../../data/e-sc01-09-works-declaration.md), shown as the entity pages list
them, with their examples.

## Actions

- File the declarations:
  [UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md),
  step 1.
- Record the answers:
  [UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md),
  step 2.
- Attach the safety plan:
  [UC-SC01-09](../../use-cases/02-prepare-the-site/uc-sc01-09-declare-works-near-networks-and-keep-the-safety-documents.md),
  step 3.

## States

- Normal: each declaration with its operator, sent date, answers and the phase it blocks.
- Empty: "No declaration", with File a declaration.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, an operator has not answered: the phase stays blocked and the
  site manager is reminded ([BR-SC01-08](../../business-rules/br-sc01-08-declarations-before-digging.md)).
- Read-only: a declaration with all answers is read-only.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-09 Works declaration](../../data/e-sc01-09-works-declaration.md),
[E-SC01-14 Site safety document](../../data/e-sc01-14-site-safety-document.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-09 Works declaration | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-09-works-declarations-e-sc01-09-works-declaration-active-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-14 Site safety document | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U22 | `u22-site-manager/s-sc01-09-works-declarations-e-sc01-14-site-safety-document-active-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-02 Prepare the site](../../flows/fl-sc01-02-prepare-the-site.md)

## Open questions

None.

---

⬅️ [S-SC01-08 Equipment](s-sc01-08-equipment.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-10 Acceptance](../05-hand-over-and-follow-up/s-sc01-10-acceptance.md)
