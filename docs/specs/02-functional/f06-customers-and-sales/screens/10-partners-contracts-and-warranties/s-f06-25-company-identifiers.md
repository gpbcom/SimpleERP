🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛒 [F6 Customers and sales](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F6-25 Company identifiers

# 🖥️ S-F6-25 Company identifiers

**Status:** 🔄 waiting for the owner

## Personas

- [U03 Sales](../../../../01-users/personas/u03-sales.md): the identifiers of the companies they sell to.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the identifiers on invoices and filings.

## Purpose

Keep every identifier of a company with its scheme, its check and the use it serves.

## Entry points

Customers and sales › a company › Identifiers; a supplier's or partner's record.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Bois et Fils: identifiers                                              [+ Add an identifier] |
|---------------------------------------------------------------------------------------------|
| SCHEME             VALUE              CHECK           CHECKED ON    DEFAULT FOR             |
| National number    552 081 317        Valid           2026-11-14    invoice                 |
| Establishment      552 081 317 00021  Valid           2026-11-14    -                       |
| VAT number         FR12 552081317     Active          2026-11-14    invoice, customs        |
| E-invoicing addr.  0225:552081317     Entered         -             e-invoice               |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F6-10 step 2, U03 | desktop | ![FL-F6-10 step 2, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-desktop-light.png) | ![FL-F6-10 step 2, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-desktop-dark.png) |
| FL-F6-10 step 2, U03 | phone | ![FL-F6-10 step 2, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-phone-light.png) | ![FL-F6-10 step 2, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-phone-dark.png) |
| FL-F6-10 step 2, U03 | tablet | ![FL-F6-10 step 2, U03, light](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-tablet-light.png) | ![FL-F6-10 step 2, U03, dark](../../images/10-partners-contracts-and-warranties/u03-sales/2-company-identifiers-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f06-25-company-identifiers-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f06-25-company-identifiers-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f06-25-company-identifiers-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f06-25-company-identifiers-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f06-25-company-identifiers-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f06-25-company-identifiers-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f06-25-company-identifiers-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f06-25-company-identifiers-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Scheme | E-F6-24 scheme | list | yes while Entered | yes |
| Value | E-F6-24 value | text without spaces | yes while Entered | yes |
| Check | E-F6-24 state | badge | no | yes |
| Checked on | E-F6-24 checked on | date | no | no |
| Default for | E-F6-24 uses | list of uses | yes | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Add an identifier | header | sales, accounting | a new identifier, checked at once |
| Check again | row | sales, accounting | the scheme's check and the register are asked again |
| Retire | row | sales, accounting | the identifier stops being used on new documents |
| Set as default | row | sales, accounting | documents of that use take this identifier |

## States

- Normal: the company's identifiers with their check and the use each serves.
- Empty: No identifier yet, with Add an identifier.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  identifier shows the scheme's rule and what was typed.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F6-24 Company identifier](../../data/e-f06-24-company-identifier.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F6-24 Company identifier | Entered | Badge "Entered"; a new record starts here; next: Valid or Invalid (BR-F6-20); fields editable within the role | U03, U05 | `u03-sales/s-f06-25-company-identifiers-e-f06-24-company-identifier-entered-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-25-company-identifiers-e-f06-24-company-identifier-entered-desktop-{light,dark}.png` |
| E-F6-24 Company identifier | Valid | Badge "Valid"; next: Invalid or Retired (BR-F6-20, UC-F6-28); fields editable within the role | U03, U05 | `u03-sales/s-f06-25-company-identifiers-e-f06-24-company-identifier-valid-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-25-company-identifiers-e-f06-24-company-identifier-valid-desktop-{light,dark}.png` |
| E-F6-24 Company identifier | Invalid | Badge "Invalid"; next: Entered (UC-F6-28); fields editable within the role | U03, U05 | `u03-sales/s-f06-25-company-identifiers-e-f06-24-company-identifier-invalid-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-25-company-identifiers-e-f06-24-company-identifier-invalid-desktop-{light,dark}.png` |
| E-F6-24 Company identifier | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U03, U05 | `u03-sales/s-f06-25-company-identifiers-e-f06-24-company-identifier-retired-{desktop,phone,tablet}-{light,dark}.png`, `u05-accounting/s-f06-25-company-identifiers-e-f06-24-company-identifier-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

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

- [FL-F6-10](../../flows/fl-f06-10-partners-contracts-and-warranties.md)

## Open questions

None.

---

⬅️ [S-F6-24 Partner programme](s-f06-24-partner-programme.md) · ⬆️ [Up](README.md) ·
➡️ [S-F6-26 Frame contracts](s-f06-26-frame-contracts.md)
