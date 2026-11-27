🏠 [Specs](../../../../README.md) › 🏷️ [Sectors](../../../README.md) › 🏗️ [SC01 Construction](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-SC01-06 Price revision, off-plan sales, BIM and grants](README.md) ›
🖥️ S-SC01-19 Renovation grants

# 🖥️ S-SC01-19 Renovation grants

**Status:** 🔄 waiting for the owner

## Personas

- [U22 Site manager](../../../../01-users/personas/u22-site-manager.md): the grant files of their sites.
- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own file and its documents.

## Purpose

Prepare the grant files of a renovation quote, check the company's label for each domain and follow the file until the
grant is paid.

## Entry points

Construction › Grant files; the quote's Grants tab; the customer portal for the customer.

## Wireframe

```text
+--------------------------------------------------------------------------------------------------+
| Grant file: Quote Q-2026-131, customer Nadia B.                  Draft   [Save] [File request]   |
| Works             Grant             Label domain    Label until   Covered                        |
| Loft insulation   Renovation grant  Insulation      2027-03-31    yes                            |
| Heat pump         CEE premium       Heating         -             NO                             |
| Documents  Tax notice [received]  Technical sheet [missing]  Quote [signed]                      |
| Filing no. -     Works start 2027-01-11     Grant to collect 3,400.00 EUR                        |
+--------------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-SC01-06 step 4, U22 | desktop | ![FL-SC01-06 step 4, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-desktop-light.png) | ![FL-SC01-06 step 4, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-desktop-dark.png) |
| FL-SC01-06 step 4, U22 | phone | ![FL-SC01-06 step 4, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-phone-light.png) | ![FL-SC01-06 step 4, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-phone-dark.png) |
| FL-SC01-06 step 4, U22 | tablet | ![FL-SC01-06 step 4, U22, light](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-tablet-light.png) | ![FL-SC01-06 step 4, U22, dark](../../images/06-revision-developers-bim-and-grants/u22-site-manager/4-renovation-grants-tablet-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-sc01-19-renovation-grants-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-sc01-19-renovation-grants-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-sc01-19-renovation-grants-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-sc01-19-renovation-grants-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-sc01-19-renovation-grants-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-sc01-19-renovation-grants-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-sc01-19-renovation-grants-offline-phone-light.png) | ![Offline, dark](../../images/states/s-sc01-19-renovation-grants-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Quote | E-SC01-18 quote | link | no | yes |
| Customer | E-SC01-18 customer | link | no | yes |
| Works and grants | E-SC01-18 works | work, grant, label domain | yes while Draft | yes |
| Label check | E-SC01-18 label check | domain, end date, covered | no | yes |
| Documents | E-SC01-18 documents | list with status | yes while Draft or Filed | no |
| Filing number and date | E-SC01-18 filing | text and date | yes while Draft | no |
| Grant amount | E-SC01-18 grant amount | amount | yes while Draft or Filed | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Check labels | header | site manager | each domain shown as covered or not |
| File request | header | site manager | the file becomes Filed with its number |
| Record acceptance | file | site manager | the file becomes Accepted |
| Record payment | file | accounting | the file becomes Paid |
| Record refusal | file | site manager | the file becomes Refused with its reason |

## States

- Normal: the works with their grants, the label check per domain, the documents and the filing.
- Empty: No grant file yet, with New grant file.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a label that
  does not cover a domain or a missing document, with what to do.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-SC01-18 Grant file](../../data/e-sc01-18-grant-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-SC01-18 Grant file | Draft | Badge "Draft"; a new record starts here; next: Filed or Refused (BR-SC01-19, UC-SC01-19); fields editable within the role | U22, U09 | `u22-site-manager/s-sc01-19-renovation-grants-e-sc01-18-grant-file-draft-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-19-renovation-grants-e-sc01-18-grant-file-draft-phone-{light,dark}.png` |
| E-SC01-18 Grant file | Filed | Badge "Filed"; next: Accepted or Refused (UC-SC01-19); fields editable within the role | U22, U09 | `u22-site-manager/s-sc01-19-renovation-grants-e-sc01-18-grant-file-filed-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-19-renovation-grants-e-sc01-18-grant-file-filed-phone-{light,dark}.png` |
| E-SC01-18 Grant file | Accepted | Badge "Accepted"; next: Paid (UC-SC01-19); fields editable within the role | U22, U09 | `u22-site-manager/s-sc01-19-renovation-grants-e-sc01-18-grant-file-accepted-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-19-renovation-grants-e-sc01-18-grant-file-accepted-phone-{light,dark}.png` |
| E-SC01-18 Grant file | Refused | Badge "Refused"; final: read-only, no next state; the history shows how it got here | U22, U09 | `u22-site-manager/s-sc01-19-renovation-grants-e-sc01-18-grant-file-refused-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-19-renovation-grants-e-sc01-18-grant-file-refused-phone-{light,dark}.png` |
| E-SC01-18 Grant file | Paid | Badge "Paid"; final: read-only, no next state; the history shows how it got here | U22, U09 | `u22-site-manager/s-sc01-19-renovation-grants-e-sc01-18-grant-file-paid-{desktop,phone,tablet}-{light,dark}.png`, `u09-customer/s-sc01-19-renovation-grants-e-sc01-18-grant-file-paid-phone-{light,dark}.png` |

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

- [FL-SC01-06](../../flows/fl-sc01-06-revision-developers-bim-and-grants.md)

## Open questions

None.

---

⬅️ [S-SC01-18 BIM quantities](s-sc01-18-bim-quantities.md) · ⬆️ [Up](README.md) ·
➡️ [S-SC01-L01 Construction sites](../00-lists/s-sc01-l01-construction-sites.md)
