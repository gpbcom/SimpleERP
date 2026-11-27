🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › ⚖️ [SC11 Professional firms](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC11-03 Time and billing](README.md) › 🖥️ S-SC11-07 Client funds

# 🖥️ S-SC11-07 Client funds

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U36 Professional](../../../../01-users/personas/u36-professional.md)

## Purpose

Used to hold client funds on trust accounts
([UC-SC11-07](../../use-cases/03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md)).

## Entry points

Professional firms in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC11-03 step 3, U05 | desktop | ![FL-SC11-03 step 3, U05, light](../../images/03-time-and-billing/u05-accounting/3-trust-desktop-light.png) | ![FL-SC11-03 step 3, U05, dark](../../images/03-time-and-billing/u05-accounting/3-trust-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc11-07-client-funds-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc11-07-client-funds-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc11-07-client-funds-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc11-07-client-funds-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc11-07-client-funds-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc11-07-client-funds-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-sc11-07-client-funds-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-sc11-07-client-funds-offline-desktop-dark.png) |

## Fields and columns

The fields of [E-SC11-08 Trust movement](../../data/e-sc11-08-trust-movement.md),
[E-F8-17 Client money ledger](../../../../02-functional/f08-accounting/data/e-f08-17-client-money-ledger.md), shown as
the entity pages list them, with their examples.

## Actions

- Receive: [UC-SC11-07](../../use-cases/03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md), step 1.
- Book to the trust account:
  [UC-SC11-07](../../use-cases/03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md), step 2.
- Release: [UC-SC11-07](../../use-cases/03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md), step 3.
- Pay out: [UC-SC11-07](../../use-cases/03-time-and-billing/uc-sc11-07-hold-client-funds-on-trust-accounts.md), step 4.

## States

- Normal: trust movements per client and matter with balances.
- Empty: "No client fund".
- Loading: the frame and titles show at once with placeholder rows; within 1 second
  ([D408](../../../../06-decisions/technical/d408-performance-and-profiles.md)) the data replaces them, and a longer
  load shows a progress line saying what loads.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)) says what failed
  and what to do; what was typed is kept. For example, to the firm's account: it is refused
  ([BR-SC11-05](../../business-rules/br-sc11-05-client-funds-through-the-trust-account.md)).
- Read-only: professionals read only.
- Offline: not available offline: office work on confidential matters that stay on the server. Offline work is kept for
  the phone forms of the field, [D38](../../../../06-decisions/ux/d38-offline-field-tasks.md),
  [UC-F2-22](../../../../02-functional/f02-no-code-configuration/use-cases/09-portals-and-offline-forms/uc-f02-22-fill-a-form-offline-on-the-phone.md).
  A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-SC11-08 Trust movement](../../data/e-sc11-08-trust-movement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC11-08 Trust movement | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U36 | `u05-accounting/s-sc11-07-client-funds-e-sc11-08-trust-movement-active-desktop-{light,dark}.png`, `u36-professional/s-sc11-07-client-funds-e-sc11-08-trust-movement-active-{desktop,phone}-{light,dark}.png` |

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

- [FL-SC11-03 Time and billing](../../flows/fl-sc11-03-time-and-billing.md)

## Open questions

None.

---

⬅️ [S-SC11-06 Fees](s-sc11-06-fees.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC11-08 Deadlines](../04-deadlines-and-filings/s-sc11-08-deadlines.md)
