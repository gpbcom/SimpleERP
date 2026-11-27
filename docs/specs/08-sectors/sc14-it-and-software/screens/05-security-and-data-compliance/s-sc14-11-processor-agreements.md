🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 💻 [SC14 IT and software](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC14-05 Security and data compliance](README.md) ›
🖥️ S-SC14-11 Processor agreements

# 🖥️ S-SC14-11 Processor agreements

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sign data processing agreements,
[UC-SC14-11](../../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md).

## Entry points

IT and software in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC14-05 step 1, U07 | desktop | ![FL-SC14-05 step 1, U07, light](../../images/05-security-and-data-compliance/u07-administrator/1-processor-agreement-desktop-light.png) | ![FL-SC14-05 step 1, U07, dark](../../images/05-security-and-data-compliance/u07-administrator/1-processor-agreement-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc14-11-processor-agreements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc14-11-processor-agreements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc14-11-processor-agreements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc14-11-processor-agreements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc14-11-processor-agreements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc14-11-processor-agreements-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc14-11-processor-agreements-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc14-11-processor-agreements-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC14-10 Processor agreement](../../data/e-sc14-10-processor-agreement.md), shown as the entity pages
list them, with their examples.

## Actions

- Send: [UC-SC14-11](../../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md),
  step 1.
- Sign: [UC-SC14-11](../../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md),
  step 2.
- Keep: [UC-SC14-11](../../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md),
  step 3.
- Update: [UC-SC14-11](../../use-cases/05-security-and-data-compliance/uc-sc14-11-sign-data-processing-agreements.md),
  step 4.

## States

- Normal: agreements per customer with version and signature.
- Empty: "No agreement".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, missing: onboarding is blocked
  ([BR-SC14-06](../../business-rules/br-sc14-06-processor-agreement-per-customer.md)).
- Read-only: signed versions are read-only.
- Offline: not available offline: office work on live subscriptions and customer data. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC14-10 Processor agreement](../../data/e-sc14-10-processor-agreement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC14-10 Processor agreement | Sent | Badge "Sent"; a new record starts here; next: Signed (UC-SC14-11); fields editable within the role | U07, U09 | `u07-administrator/s-sc14-11-processor-agreements-e-sc14-10-processor-agreement-sent-desktop-{light,dark}.png`, `u09-customer/s-sc14-11-processor-agreements-e-sc14-10-processor-agreement-sent-phone-{light,dark}.png` |
| E-SC14-10 Processor agreement | Signed | Badge "Signed"; final: read-only, no next state; the history shows how it got here | U07, U09 | `u07-administrator/s-sc14-11-processor-agreements-e-sc14-10-processor-agreement-signed-desktop-{light,dark}.png`, `u09-customer/s-sc14-11-processor-agreements-e-sc14-10-processor-agreement-signed-phone-{light,dark}.png` |

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

⬅️ [S-SC14-10 Renewals](../02-licences-and-renewals/s-sc14-10-renewals.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC14-12 Vulnerabilities](s-sc14-12-vulnerabilities.md)
