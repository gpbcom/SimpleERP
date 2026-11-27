🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-05 Security and data compliance](README.md) ›
🖥️ S-SC14-12 Vulnerabilities

# 🖥️ S-SC14-12 Vulnerabilities

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)

## Purpose

Used to keep the software bill of materials and handle vulnerabilities,
[UC-SC14-12](../../use-cases/05-security-and-data-compliance/uc-sc14-12-keep-the-software-bill-of-materials-and-handle-vulnerabilities.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-05 step 2, U16 | desktop | ![FL-SC14-05 step 2, U16, light](../../images/05-security-and-data-compliance/u16-office-worker/2-vulnerabilities-desktop-light.png) | ![FL-SC14-05 step 2, U16, dark](../../images/05-security-and-data-compliance/u16-office-worker/2-vulnerabilities-desktop-dark.png) |
| FL-SC14-05 step 2, U16 | phone | ![FL-SC14-05 step 2, U16, light](../../images/05-security-and-data-compliance/u16-office-worker/2-vulnerabilities-phone-light.png) | ![FL-SC14-05 step 2, U16, dark](../../images/05-security-and-data-compliance/u16-office-worker/2-vulnerabilities-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-12-vulnerabilities-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-12-vulnerabilities-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-12-vulnerabilities-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-12-vulnerabilities-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-12-vulnerabilities-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-12-vulnerabilities-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-12-vulnerabilities-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-12-vulnerabilities-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-11 Component](../../data/e-sc14-11-component.md), shown as the entity pages list them, with their
examples.

## Actions

- Import:
  [UC-SC14-12](../../use-cases/05-security-and-data-compliance/uc-sc14-12-keep-the-software-bill-of-materials-and-handle-vulnerabilities.md),
  step 1.
- Match:
  [UC-SC14-12](../../use-cases/05-security-and-data-compliance/uc-sc14-12-keep-the-software-bill-of-materials-and-handle-vulnerabilities.md),
  step 2.
- Fix:
  [UC-SC14-12](../../use-cases/05-security-and-data-compliance/uc-sc14-12-keep-the-software-bill-of-materials-and-handle-vulnerabilities.md),
  step 3.
- Notify:
  [UC-SC14-12](../../use-cases/05-security-and-data-compliance/uc-sc14-12-keep-the-software-bill-of-materials-and-handle-vulnerabilities.md),
  step 4.

## States

- Normal: releases, components and vulnerabilities.
- Empty: "No bill of materials".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, exploited: the reporting clock starts,
  [BR-SC14-07](../../business-rules/br-sc14-07-vulnerabilities-reported-in-time.md),
  [UC-SC14-13](../../use-cases/05-security-and-data-compliance/uc-sc14-13-report-security-incidents.md).
- Read-only: imported lists are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-11 Component](../../data/e-sc14-11-component.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-11 Component | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U16 | `u16-office-worker/s-sc14-12-vulnerabilities-e-sc14-11-component-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC14-05 Security and data compliance](../../flows/fl-sc14-05-security-and-data-compliance.md)

## Open questions

None.

---

⬅️ [S-SC14-11 Processor agreements](s-sc14-11-processor-agreements.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-13 Incident reports](s-sc14-13-incident-reports.md)
