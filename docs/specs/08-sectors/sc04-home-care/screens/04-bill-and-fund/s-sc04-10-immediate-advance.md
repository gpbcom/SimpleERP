🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏠 [SC04 Home care](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC04-04 Bill and fund](README.md) › 🖥️ S-SC04-10 Immediate advance

# 🖥️ S-SC04-10 Immediate advance

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Send each invoice of a client who joined the immediate advance as a request, follow its validation within 48 hours
(by the client, or by URSSAF automatically once they have passed) and match URSSAF's payment of the whole service
([UC-SC04-10](../../use-cases/04-bill-and-fund/uc-sc04-10-use-the-immediate-advance.md),
[CR-FR-104](../../../../10-country-packs/france/tax-and-vat/cr-fr-104-immediate-advance-of-tax-credit.md)).

## Entry points

Home care in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC04-04 step 2, U05 | desktop | ![FL-SC04-04 step 2, U05, light](../../images/04-bill-and-fund/u05-accounting/2-advance-desktop-light.png) | ![FL-SC04-04 step 2, U05, dark](../../images/04-bill-and-fund/u05-accounting/2-advance-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc04-10-immediate-advance-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc04-10-immediate-advance-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc04-10-immediate-advance-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc04-10-immediate-advance-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc04-10-immediate-advance-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc04-10-immediate-advance-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc04-10-immediate-advance-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc04-10-immediate-advance-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC04-08 Care invoice](../../data/e-sc04-08-care-invoice.md) and
[E-SC04-13 Immediate advance claim](../../data/e-sc04-13-immediate-advance-claim.md), shown as the entity pages list
them, with their examples. The client's validation screen reads: URSSAF pays the whole 260.00 EUR to the provider and
debits you 130.00 EUR, your share after the tax credit; validate within 48 hours, after which URSSAF validates it
automatically.

## Actions

- Join: [UC-SC04-10](../../use-cases/04-bill-and-fund/uc-sc04-10-use-the-immediate-advance.md), step 1.
- Record the payment: [UC-SC04-10](../../use-cases/04-bill-and-fund/uc-sc04-10-use-the-immediate-advance.md), step 4.

## States

- Normal: the clients who joined, the requests sent, their validation state (by the client within 48 hours, or
  automatic after them) and URSSAF's payments of the whole service.
- Empty: "No client uses the immediate advance".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, URSSAF refuses a request: its reason shows and accounting corrects and sends it again; only a request
  that cannot be corrected is billed to the client in full outside the advance. A request the client does not answer is
  never an error: URSSAF validates it automatically after 48 hours.
- Read-only: a validated request is read-only.
- Offline: not available offline: office work at the agency on shared planning and billing data. Offline work is kept
  for the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC04-13 Immediate advance claim](../../data/e-sc04-13-immediate-advance-claim.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC04-13 Immediate advance claim | Sent | Badge "Sent"; a new record starts here; next: Refused, Validated or Cancelled (UC-SC04-10, BR-SC04-13); fields editable within the role | U05, U09 | `u05-accounting/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-sent-desktop-{light,dark}.png`, `u09-customer/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-sent-phone-{light,dark}.png` |
| E-SC04-13 Immediate advance claim | Refused | Badge "Refused"; next: Sent (UC-SC04-10); fields editable within the role | U05, U09 | `u05-accounting/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-refused-desktop-{light,dark}.png`, `u09-customer/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-refused-phone-{light,dark}.png` |
| E-SC04-13 Immediate advance claim | Validated | Badge "Validated"; next: Paid (UC-SC04-10); fields editable within the role | U05, U09 | `u05-accounting/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-validated-desktop-{light,dark}.png`, `u09-customer/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-validated-phone-{light,dark}.png` |
| E-SC04-13 Immediate advance claim | Cancelled | Badge "Cancelled"; final: read-only, no next state; the history shows how it got here | U05, U09 | `u05-accounting/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-cancelled-desktop-{light,dark}.png`, `u09-customer/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-cancelled-phone-{light,dark}.png` |
| E-SC04-13 Immediate advance claim | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U05, U09 | `u05-accounting/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-paid-desktop-{light,dark}.png`, `u09-customer/s-sc04-10-immediate-advance-e-sc04-13-immediate-advance-claim-paid-phone-{light,dark}.png` |

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

⬅️ [S-SC04-09 Tax certificates](s-sc04-09-tax-certificates.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC04-11 Travel time](s-sc04-11-travel-time.md)
