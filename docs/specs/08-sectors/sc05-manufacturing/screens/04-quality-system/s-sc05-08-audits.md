🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏭 [SC05 Manufacturing](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC05-04 Quality system](README.md) › 🖥️ S-SC05-08 Audits

# 🖥️ S-SC05-08 Audits

**Status:** 🔄 waiting for the owner

## Personas

- [U27 Quality manager](../../../../01-users/personas/u27-quality-manager.md)

## Purpose

Used to run internal audits ([UC-SC05-08](../../use-cases/04-quality-system/uc-sc05-08-run-internal-audits.md)).

## Entry points

Manufacturing in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC05-04 step 2, U27 | desktop | ![FL-SC05-04 step 2, U27, light](../../images/04-quality-system/u27-quality-manager/2-audit-desktop-light.png) | ![FL-SC05-04 step 2, U27, dark](../../images/04-quality-system/u27-quality-manager/2-audit-desktop-dark.png) |
| FL-SC05-04 step 2, U27 | tablet | ![FL-SC05-04 step 2, U27, light](../../images/04-quality-system/u27-quality-manager/2-audit-tablet-light.png) | ![FL-SC05-04 step 2, U27, dark](../../images/04-quality-system/u27-quality-manager/2-audit-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc05-08-audits-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc05-08-audits-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc05-08-audits-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc05-08-audits-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc05-08-audits-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc05-08-audits-read-only-desktop-dark.png) |
| Offline | tablet | ![Offline, light](../../images/states/s-sc05-08-audits-offline-tablet-light.png) | ![Offline, dark](../../images/states/s-sc05-08-audits-offline-tablet-dark.png) |

## Fields and columns

The fields of [E-SC05-08 Audit](../../data/e-sc05-08-audit.md),
[E-SC05-09 Quality action](../../data/e-sc05-09-quality-action.md), shown as the entity pages list them, with their
examples.

## Actions

- Plan: [UC-SC05-08](../../use-cases/04-quality-system/uc-sc05-08-run-internal-audits.md), step 1.
- Audit with the tablet: [UC-SC05-08](../../use-cases/04-quality-system/uc-sc05-08-run-internal-audits.md), step 2.
- Record findings: [UC-SC05-08](../../use-cases/04-quality-system/uc-sc05-08-run-internal-audits.md), step 3.
- Close the audit: [UC-SC05-08](../../use-cases/04-quality-system/uc-sc05-08-run-internal-audits.md), step 4.

## States

- Normal: the audit plan, checklists, findings and their actions.
- Empty: "No audit planned".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a finding without action: the audit cannot be closed.
- Read-only: a closed audit is read-only.
- Offline: the shop-floor tablet keeps working without the network,
  [UC-F12-26](../../../../02-functional/f12-manufacturing/use-cases/11-finite-schedule-and-the-tablet/uc-f12-26-keep-working-on-the-tablet-without-the-network.md),
  checklist answers and photos sync in order when it is back,
  [BR-F12-21](../../../../02-functional/f12-manufacturing/business-rules/br-f12-21-tablet-records-sync-in-order.md).

Shown entities (VD-15): [E-SC05-08 Audit](../../data/e-sc05-08-audit.md),
[E-SC05-09 Quality action](../../data/e-sc05-09-quality-action.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC05-08 Audit | Open | Badge "Open"; a new record starts here; next: Closed (UC-SC05-08); fields editable within the role | U27 | `u27-quality-manager/s-sc05-08-audits-e-sc05-08-audit-open-{desktop,tablet}-{light,dark}.png` |
| E-SC05-08 Audit | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U27 | `u27-quality-manager/s-sc05-08-audits-e-sc05-08-audit-closed-{desktop,tablet}-{light,dark}.png` |
| E-SC05-09 Quality action | Done | Badge "Done"; next: Effective (UC-SC05-09); fields editable within the role | U27 | `u27-quality-manager/s-sc05-08-audits-e-sc05-09-quality-action-done-{desktop,tablet}-{light,dark}.png` |
| E-SC05-09 Quality action | Effective | Badge "Effective"; final: read-only, no next state; the history shows how it got here | U27 | `u27-quality-manager/s-sc05-08-audits-e-sc05-09-quality-action-effective-{desktop,tablet}-{light,dark}.png` |

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

- [FL-SC05-04 Quality system](../../flows/fl-sc05-04-quality-system.md)

## Open questions

None.

---

⬅️ [S-SC05-07 Documents](s-sc05-07-documents.md) · ⬆️ [Up](README.md) · ➡️ [S-SC05-09 Actions](s-sc05-09-actions.md)
