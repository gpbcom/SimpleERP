🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-06 Firm management](README.md) › 🖥️ S-SC11-19 Performance

# 🖥️ S-SC11-19 Performance

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to report the firm's performance
([UC-SC11-19](../../use-cases/06-firm-management/uc-sc11-19-report-the-firm-s-performance.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-06 step 4, U13 | desktop | ![FL-SC11-06 step 4, U13, light](../../images/06-firm-management/u13-owner/4-performance-desktop-light.png) | ![FL-SC11-06 step 4, U13, dark](../../images/06-firm-management/u13-owner/4-performance-desktop-dark.png) |
| FL-SC11-06 step 4, U13 | phone | ![FL-SC11-06 step 4, U13, light](../../images/06-firm-management/u13-owner/4-performance-phone-light.png) | ![FL-SC11-06 step 4, U13, dark](../../images/06-firm-management/u13-owner/4-performance-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-19-performance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-19-performance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-19-performance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-19-performance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-19-performance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-19-performance-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc11-19-performance-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc11-19-performance-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC11-07 Fee bill](../../data/e-sc11-07-fee-bill.md),
[E-SC11-14 Partner share](../../data/e-sc11-14-partner-share.md), shown as the entity pages list them, with their
examples.

## Actions

- Open: [UC-SC11-19](../../use-cases/06-firm-management/uc-sc11-19-report-the-firm-s-performance.md), step 1.
- Compare: [UC-SC11-19](../../use-cases/06-firm-management/uc-sc11-19-report-the-firm-s-performance.md), step 2.
- Reconcile: [UC-SC11-19](../../use-cases/06-firm-management/uc-sc11-19-report-the-firm-s-performance.md), step 3.
- Export: [UC-SC11-19](../../use-cases/06-firm-management/uc-sc11-19-report-the-firm-s-performance.md), step 4.

## States

- Normal: fees, time, recovery and clients per area.
- Empty: "No data".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, missing data: it is shown.
- Read-only: partners read only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-14 Partner share](../../data/e-sc11-14-partner-share.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-14 Partner share | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-sc11-19-performance-e-sc11-14-partner-share-active-desktop-{light,dark}.png`, `u13-owner/s-sc11-19-performance-e-sc11-14-partner-share-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-06 Firm management](../../flows/fl-sc11-06-firm-management.md)

## Open questions

None.

---

⬅️ [S-SC11-18 Training](s-sc11-18-training.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-20 Matter assistant](../02-matters-and-documents/s-sc11-20-matter-assistant.md)
