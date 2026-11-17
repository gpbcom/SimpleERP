🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-04 Bill and subcontract](README.md) › 🖥️ S-SC01-14 Site margin

# 🖥️ S-SC01-14 Site margin

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Used to follow site profitability
([UC-SC01-14](../../use-cases/04-bill-and-subcontract/uc-sc01-14-follow-site-profitability.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-04 step 3, U22 | desktop | ![FL-SC01-04 step 3, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-desktop-light.png) | ![FL-SC01-04 step 3, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-desktop-dark.png) |
| FL-SC01-04 step 3, U22 | phone | ![FL-SC01-04 step 3, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-phone-light.png) | ![FL-SC01-04 step 3, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-phone-dark.png) |
| FL-SC01-04 step 3, U22 | tablet | ![FL-SC01-04 step 3, U22, light](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-tablet-light.png) | ![FL-SC01-04 step 3, U22, dark](../../images/04-bill-and-subcontract/u22-site-manager/3-margin-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-14-site-margin-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-14-site-margin-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-14-site-margin-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-14-site-margin-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-14-site-margin-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-14-site-margin-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-14-site-margin-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-14-site-margin-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-06 Progress bill](../../data/e-sc01-06-progress-bill.md), shown as the entity pages list them, with their
examples.

## Actions

- Open the site's margin: [UC-SC01-14](../../use-cases/04-bill-and-subcontract/uc-sc01-14-follow-site-profitability.md),
  step 1.
- Update the estimate to complete:
  [UC-SC01-14](../../use-cases/04-bill-and-subcontract/uc-sc01-14-follow-site-profitability.md), step 2.
- Compare the sites: [UC-SC01-14](../../use-cases/04-bill-and-subcontract/uc-sc01-14-follow-site-profitability.md), step
  3.
- Act on alerts: [UC-SC01-14](../../use-cases/04-bill-and-subcontract/uc-sc01-14-follow-site-profitability.md), step 4.

## States

- Normal: per lot: budget, actual, estimate to complete and margin at completion, with alerts.
- Empty: "No cost yet on this site".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the margin at completion below the threshold: the site manager
  and the owner are alerted.
- Read-only: the owner and accounting read; only the site manager edits the estimate.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-01 Construction site](../../data/e-sc01-01-construction-site.md),
[E-SC01-06 Progress bill](../../data/e-sc01-06-progress-bill.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-01 Construction site | Planned | Badge "Planned"; a new record starts here; next: Running (UC-SC01-01); fields editable within the role | U13, U22 | `u13-owner/s-sc01-14-site-margin-e-sc01-01-construction-site-planned-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-sc01-14-site-margin-e-sc01-01-construction-site-planned-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Running | Badge "Running"; next: Accepted (UC-SC01-01); fields editable within the role | U13, U22 | `u13-owner/s-sc01-14-site-margin-e-sc01-01-construction-site-running-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-sc01-14-site-margin-e-sc01-01-construction-site-running-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-01 Construction site | Accepted | Badge "Accepted"; next: Closed (UC-SC01-14); fields editable within the role | U13, U22 | `u13-owner/s-sc01-14-site-margin-e-sc01-01-construction-site-accepted-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-sc01-14-site-margin-e-sc01-01-construction-site-accepted-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-06 Progress bill | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-SC01-06); fields editable within the role | U13, U22 | `u13-owner/s-sc01-14-site-margin-e-sc01-06-progress-bill-draft-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-sc01-14-site-margin-e-sc01-06-progress-bill-draft-{desktop,phone,tablet}-{light,dark}.png` |
| E-SC01-06 Progress bill | Sent | Badge "Sent"; next: Paid (UC-SC01-13); fields editable within the role | U13, U22 | `u13-owner/s-sc01-14-site-margin-e-sc01-06-progress-bill-sent-{desktop,phone}-{light,dark}.png`, `u22-site-manager/s-sc01-14-site-margin-e-sc01-06-progress-bill-sent-{desktop,phone,tablet}-{light,dark}.png` |

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

- [FL-SC01-04 Bill and subcontract](../../flows/fl-sc01-04-bill-and-subcontract.md)

## Open questions

None.

---

⬅️ [S-SC01-13 Public tenders](../01-win-the-work/s-sc01-13-public-tenders.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-15 Site assistant](../03-run-the-site/s-sc01-15-site-assistant.md)
