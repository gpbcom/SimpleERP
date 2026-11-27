🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-04 Bill and fund](README.md) › 🖥️ S-SC04-09 Tax certificates

# 🖥️ S-SC04-09 Tax certificates

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to issue the yearly tax-credit certificate
([UC-SC04-09](../../use-cases/04-bill-and-fund/uc-sc04-09-issue-the-yearly-tax-credit-certificate.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-04 step 3, U05 | desktop | ![FL-SC04-04 step 3, U05, light](../../images/04-bill-and-fund/u05-accounting/3-certificate-desktop-light.png) | ![FL-SC04-04 step 3, U05, dark](../../images/04-bill-and-fund/u05-accounting/3-certificate-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-09-tax-certificates-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-09-tax-certificates-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-09-tax-certificates-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-09-tax-certificates-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-09-tax-certificates-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-09-tax-certificates-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc04-09-tax-certificates-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc04-09-tax-certificates-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC04-09 Tax-credit certificate](../../data/e-sc04-09-tax-credit-certificate.md), shown as the entity
pages list them, with their examples.

## Actions

- Generate: [UC-SC04-09](../../use-cases/04-bill-and-fund/uc-sc04-09-issue-the-yearly-tax-credit-certificate.md), step
  1.
- Check amounts: [UC-SC04-09](../../use-cases/04-bill-and-fund/uc-sc04-09-issue-the-yearly-tax-credit-certificate.md),
  step 2.
- Send: [UC-SC04-09](../../use-cases/04-bill-and-fund/uc-sc04-09-issue-the-yearly-tax-credit-certificate.md), step 3.
- Keep the copies: [UC-SC04-09](../../use-cases/04-bill-and-fund/uc-sc04-09-issue-the-yearly-tax-credit-certificate.md),
  step 4.

## States

- Normal: the year's certificates per client with amounts and sending state.
- Empty: "No certificate to issue".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, a missing address: the client is listed and the certificate held.
- Read-only: a sent certificate is read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-09 Tax-credit certificate](../../data/e-sc04-09-tax-credit-certificate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-09 Tax-credit certificate | Sent | Badge "Sent"; a new record starts here; next: Held (UC-SC04-09); fields editable within the role | U05 | `u05-accounting/s-sc04-09-tax-certificates-e-sc04-09-tax-credit-certificate-sent-desktop-{light,dark}.png` |
| E-SC04-09 Tax-credit certificate | Held | Badge "Held"; next: Sent (UC-SC04-09); fields editable within the role | U05 | `u05-accounting/s-sc04-09-tax-certificates-e-sc04-09-tax-credit-certificate-held-desktop-{light,dark}.png` |

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

- [FL-SC04-04 Bill and fund](../../flows/fl-sc04-04-bill-and-fund.md)

## Open questions

None.

---

⬅️ [S-SC04-08 Billing](s-sc04-08-billing.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-10 Immediate advance](s-sc04-10-immediate-advance.md)
