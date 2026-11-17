🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-39 Cash-basis books

# 🖥️ S-F8-39 Cash-basis books

**Status:** 🔄 waiting for the owner

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the books of the structures they keep.
- [U36 Professional](../../../../01-users/personas/u36-professional.md): their own receipts and payments.

## Purpose

Categorise bank lines into receipts and payments and produce the journal and the annual summary.

## Entry points

Accounting › Books › Cash-basis book; the bank lines waiting for a category.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Cash-basis book: Cabinet Martin 2026                Receipts 62,400   Payments 31,900 EUR    |
|---------------------------------------------------------------------------------------------|
| DATE        BANK LINE            CATEGORY          RECEIPT   PAYMENT   DOCUMENT              |
| 2026-11-12  Client Roth          Fees received     1,800.00            INV-0412              |
| 2026-11-13  Landlord SCI         Rent                        1,200.00  receipt               |
| Unposted bank lines: 2                              [Categorise] [Annual summary] [Export]   |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-12 step 5, U05 | desktop | ![FL-F8-12 step 5, U05, light](../../images/12-audit-leases-and-special-books/u05-accounting/5-cash-basis-books-desktop-light.png) | ![FL-F8-12 step 5, U05, dark](../../images/12-audit-leases-and-special-books/u05-accounting/5-cash-basis-books-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-39-cash-basis-books-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-39-cash-basis-books-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-39-cash-basis-books-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-39-cash-basis-books-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-39-cash-basis-books-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-39-cash-basis-books-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-39-cash-basis-books-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-39-cash-basis-books-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Date and bank line | E-F8-04 | date and text | no | yes |
| Category | E-F8-01 | list | yes | yes |
| Receipt and payment | E-F8-03 | two amounts | no | yes |
| Document | E-F8-03 | file or link | yes | yes for a payment |
| Unposted lines | E-F8-04 | count | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Categorise | row, bulk bar | professional, accounting | the line is posted on its bank date |
| Annual summary | header | professional, accounting | receipts and payments by category |
| Export | header | professional, external accountant | the journal and the summary as a file |

## States

- Normal: the receipts and payments journal with its balance and the bank lines still to categorise.
- Empty: No bank line yet, with Connect a bank.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused entry
  shows the rule and the bank line concerned.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop only; on a phone, the app asks to continue on a larger screen.

## Accessibility

Every control is reachable by keyboard; states and errors are announced to screen readers and never rely on colour
alone; each field has its visible label.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F8-12](../../flows/fl-f08-12-audit-leases-and-special-books.md)

## Open questions

None.

---

⬅️ [S-F8-38 Business travel](s-f08-38-business-travel.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-L01 Accounts](../00-lists/s-f08-l01-accounts.md)
