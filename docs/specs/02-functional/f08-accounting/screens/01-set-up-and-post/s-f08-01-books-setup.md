🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F8-01 Set up and post](README.md) ›
🖥️ S-F8-01 Books setup

# 🖥️ S-F8-01 Books setup

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set up the books.

## Entry points

Accounting in the menu; the AI assistant (BR-F3-34).

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-01 step 1, U05 | desktop | ![FL-F8-01 step 1, U05, light](../../images/01-set-up-and-post/u05-accounting/1-set-up-the-books-desktop-light.png) | ![FL-F8-01 step 1, U05, dark](../../images/01-set-up-and-post/u05-accounting/1-set-up-the-books-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-01-books-setup-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-01-books-setup-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-01-books-setup-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-01-books-setup-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-01-books-setup-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-01-books-setup-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-01-books-setup-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-01-books-setup-offline-desktop-dark.png) |

## Fields and columns

As its entities.

## Actions

As its use case's main flow.

## States

- Normal: Set up the books, as the wireframe shows.
- Empty: No journal besides the defaults yet for the period, with Add a journal.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: posted entries and closed periods (CR-FR-003).
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-01 Account](../../data/e-f08-01-account.md),
[E-F8-02 Journal](../../data/e-f08-02-journal.md), [E-F8-33 Tax rate](../../data/e-f08-33-tax-rate.md),
[E-F8-27 FEC file](../../data/e-f08-27-fec-file.md),
[E-F8-29 Entry annotation](../../data/e-f08-29-entry-annotation.md),
[E-F8-10 Fiscal period](../../data/e-f08-10-fiscal-period.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-01 Account | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-01-account-active-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-01-account-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-01-account-active-desktop-{light,dark}.png` |
| E-F8-02 Journal | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-02-journal-recorded-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-02-journal-recorded-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-02-journal-recorded-desktop-{light,dark}.png` |
| E-F8-33 Tax rate | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-33-tax-rate-active-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-33-tax-rate-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-33-tax-rate-active-desktop-{light,dark}.png` |
| E-F8-27 FEC file | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-27-fec-file-active-desktop-{light,dark}.png` |
| E-F8-29 Entry annotation | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-29-entry-annotation-active-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-29-entry-annotation-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-29-entry-annotation-active-desktop-{light,dark}.png` |
| E-F8-10 Fiscal period | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U07, U08 | `u05-accounting/s-f08-01-books-setup-e-f08-10-fiscal-period-active-desktop-{light,dark}.png`, `u07-administrator/s-f08-01-books-setup-e-f08-10-fiscal-period-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-01-books-setup-e-f08-10-fiscal-period-active-desktop-{light,dark}.png` |

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

- [FL-F8-01 Set up and post](../../flows/fl-f08-01-set-up-and-post.md)

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [S-F8-02 Journal entries](s-f08-02-journal-entries.md)
