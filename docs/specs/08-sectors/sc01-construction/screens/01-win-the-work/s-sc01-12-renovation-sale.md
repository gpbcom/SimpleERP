🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-01 Win the work](README.md) › 🖥️ S-SC01-12 Renovation sale

# 🖥️ S-SC01-12 Renovation sale

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U09 Customer](../../../../01-users/personas/u09-customer.md)

## Purpose

Used to sell renovation to consumers
([UC-SC01-12](../../use-cases/01-win-the-work/uc-sc01-12-sell-renovation-to-consumers.md)).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-01 step 2, U03 | phone | ![FL-SC01-01 step 2, U03, light](../../images/01-win-the-work/u03-sales/2-renovation-phone-light.png) | ![FL-SC01-01 step 2, U03, dark](../../images/01-win-the-work/u03-sales/2-renovation-phone-dark.png) |
| FL-SC01-01 step 2, U03 | desktop | ![FL-SC01-01 step 2, U03, light](../../images/01-win-the-work/u03-sales/2-renovation-desktop-light.png) | ![FL-SC01-01 step 2, U03, dark](../../images/01-win-the-work/u03-sales/2-renovation-desktop-dark.png) |
| FL-SC01-01 step 2, U03 | tablet | ![FL-SC01-01 step 2, U03, light](../../images/01-win-the-work/u03-sales/2-renovation-tablet-light.png) | ![FL-SC01-01 step 2, U03, dark](../../images/01-win-the-work/u03-sales/2-renovation-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-12-renovation-sale-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-12-renovation-sale-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-12-renovation-sale-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-12-renovation-sale-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-12-renovation-sale-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-12-renovation-sale-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-12-renovation-sale-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-12-renovation-sale-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md), shown as the entity pages list them, with their
examples.

## Actions

- Quote at the customer's home:
  [UC-SC01-12](../../use-cases/01-win-the-work/uc-sc01-12-sell-renovation-to-consumers.md), step 1.
- Add the VAT certificate: [UC-SC01-12](../../use-cases/01-win-the-work/uc-sc01-12-sell-renovation-to-consumers.md),
  step 2.
- Sign quote and certificate: [UC-SC01-12](../../use-cases/01-win-the-work/uc-sc01-12-sell-renovation-to-consumers.md),
  step 3.
- Plan after the withdrawal end:
  [UC-SC01-12](../../use-cases/01-win-the-work/uc-sc01-12-sell-renovation-to-consumers.md), step 4.

## States

- Normal: the renovation quote, the VAT certificate to sign, the withdrawal period and the earliest start.
- Empty: "No renovation quote yet", with New quote.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the customer does not sign the certificate: the lines go to the
  normal VAT rate and the total is shown again before signing.
- Read-only: a signed quote is read-only.
- Offline: the quote being built at the customer's home stays on the tablet and is sent when the network is back;
  signing needs the network.

Shown entities (VD-15): [E-SC01-02 Quote lot](../../data/e-sc01-02-quote-lot.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-02 Quote lot | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U03, U09 | `u03-sales/s-sc01-12-renovation-sale-e-sc01-02-quote-lot-active-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-12-renovation-sale-e-sc01-02-quote-lot-active-phone-{light,dark}.png` |

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

- [FL-SC01-01 Win the work](../../flows/fl-sc01-01-win-the-work.md)

## Open questions

None.

---

⬅️ [S-SC01-11 Warranties](../05-hand-over-and-follow-up/s-sc01-11-warranties.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-13 Public tenders](s-sc01-13-public-tenders.md)
