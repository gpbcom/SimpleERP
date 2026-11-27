🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-01 Win the work](README.md) › 🖥️ S-SC01-13 Public tenders

# 🖥️ S-SC01-13 Public tenders

**Status:** ✅ specified

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Used to answer public tenders and invoice through Chorus Pro,
[UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md).

## Entry points

Construction in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-01 step 4, U03 | desktop | ![FL-SC01-01 step 4, U03, light](../../images/01-win-the-work/u03-sales/4-public-tender-desktop-light.png) | ![FL-SC01-01 step 4, U03, dark](../../images/01-win-the-work/u03-sales/4-public-tender-desktop-dark.png) |
| FL-SC01-01 step 4, U03 | phone | ![FL-SC01-01 step 4, U03, light](../../images/01-win-the-work/u03-sales/4-public-tender-phone-light.png) | ![FL-SC01-01 step 4, U03, dark](../../images/01-win-the-work/u03-sales/4-public-tender-phone-dark.png) |
| FL-SC01-01 step 4, U03 | tablet | ![FL-SC01-01 step 4, U03, light](../../images/01-win-the-work/u03-sales/4-public-tender-tablet-light.png) | ![FL-SC01-01 step 4, U03, dark](../../images/01-win-the-work/u03-sales/4-public-tender-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-13-public-tenders-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-13-public-tenders-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-13-public-tenders-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-13-public-tenders-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-13-public-tenders-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-13-public-tenders-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-13-public-tenders-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-13-public-tenders-offline-phone-dark.png) |

## Fields and columns

The fields of [E-SC01-12 Public tender](../../data/e-sc01-12-public-tender.md),
[E-SC01-06 Progress bill](../../data/e-sc01-06-progress-bill.md), shown as the entity pages list them, with their
examples.

## Actions

- Record the tender:
  [UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md), step
  1.
- Prepare the answer:
  [UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md), step
  2.
- File before the deadline:
  [UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md), step
  3.
- Mark won and open the site:
  [UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md), step
  4.
- Invoice through Chorus Pro:
  [UC-SC01-13](../../use-cases/01-win-the-work/uc-sc01-13-answer-public-tenders-and-invoice-through-chorus-pro.md), step
  5.

## States

- Normal: the tenders with buyer, reference, deadline, state and the documents asked; for won tenders, the Chorus Pro
  state of each invoice.
- Empty: "No tender followed", with Record a tender.
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, the deadline is near and documents are missing: the tender is
  flagged and sales is reminded.
- Read-only: a closed tender is read-only.
- Offline: not available offline: office work done at a desk on the site's shared figures. Offline work is kept for the
  phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC01-12 Public tender](../../data/e-sc01-12-public-tender.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-12 Public tender | Watching | Badge "Watching"; a new record starts here; next: Answered or Lost (UC-SC01-13); fields editable within the role | U03, U05 | `u03-sales/s-sc01-13-public-tenders-e-sc01-12-public-tender-watching-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-13-public-tenders-e-sc01-12-public-tender-watching-desktop-{light,dark}.png` |
| E-SC01-12 Public tender | Answered | Badge "Answered"; next: Won or Lost (UC-SC01-13); fields editable within the role | U03, U05 | `u03-sales/s-sc01-13-public-tenders-e-sc01-12-public-tender-answered-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-13-public-tenders-e-sc01-12-public-tender-answered-desktop-{light,dark}.png` |
| E-SC01-12 Public tender | Won | Badge "Won"; final: read-only, no next state; the history shows how it got here | U03, U05 | `u03-sales/s-sc01-13-public-tenders-e-sc01-12-public-tender-won-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-sc01-13-public-tenders-e-sc01-12-public-tender-won-desktop-{light,dark}.png` |

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

- [FL-SC01-01 Win the work](../../flows/fl-sc01-01-win-the-work.md)

## Open questions

None.

---

⬅️ [S-SC01-12 Renovation sale](s-sc01-12-renovation-sale.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-14 Site margin](../04-bill-and-subcontract/s-sc01-14-site-margin.md)
