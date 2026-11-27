🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-05 Security and data compliance](README.md) ›
🖥️ S-SC14-14 Data export

# 🖥️ S-SC14-14 Data export

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Used to let customers switch and export their data,
[UC-SC14-14](../../use-cases/05-security-and-data-compliance/uc-sc14-14-let-customers-switch-and-export-their-data.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-05 step 4, U09 | phone | ![FL-SC14-05 step 4, U09, light](../../images/05-security-and-data-compliance/u09-customer/4-export-phone-light.png) | ![FL-SC14-05 step 4, U09, dark](../../images/05-security-and-data-compliance/u09-customer/4-export-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-sc14-14-data-export-empty-phone-light.png) | ![Empty, dark](../../images/states/s-sc14-14-data-export-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-sc14-14-data-export-loading-phone-light.png) | ![Loading, dark](../../images/states/s-sc14-14-data-export-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-sc14-14-data-export-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-sc14-14-data-export-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc14-14-data-export-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc14-14-data-export-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC14-13 Data export](../../data/e-sc14-13-data-export.md), shown as the entity pages list them, with
their examples.

## Actions

- Request:
  [UC-SC14-14](../../use-cases/05-security-and-data-compliance/uc-sc14-14-let-customers-switch-and-export-their-data.md),
  step 1.
- Export:
  [UC-SC14-14](../../use-cases/05-security-and-data-compliance/uc-sc14-14-let-customers-switch-and-export-their-data.md),
  step 2.
- Download:
  [UC-SC14-14](../../use-cases/05-security-and-data-compliance/uc-sc14-14-let-customers-switch-and-export-their-data.md),
  step 3.
- Close:
  [UC-SC14-14](../../use-cases/05-security-and-data-compliance/uc-sc14-14-let-customers-switch-and-export-their-data.md),
  step 4.

## States

- Normal: export requests with scope, format and state.
- Empty: "No request".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a charge after the end date: it is refused.
- Read-only: done ones are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-13 Data export](../../data/e-sc14-13-data-export.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-13 Data export | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U09 | `u07-administrator/s-sc14-14-data-export-e-sc14-13-data-export-active-desktop-{light,dark}.png`, `u09-customer/s-sc14-14-data-export-e-sc14-13-data-export-active-phone-{light,dark}.png` |

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

⬅️ [S-SC14-13 Incident reports](s-sc14-13-incident-reports.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-15 EU VAT](../01-subscriptions-and-billing/s-sc14-15-eu-vat.md)
