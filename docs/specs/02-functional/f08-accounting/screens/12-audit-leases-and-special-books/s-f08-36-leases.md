🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📒 [F8 Accounting](../../README.md) › 🖥️ [Screens](../README.md) › 🖥️ S-F8-36 Leases

# 🖥️ S-F8-36 Leases

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the leases and the entries per book.
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md): the leases and their treatment,
  read-only.

## Purpose

Record a lease and see how each book accounts for it.

## Entry points

Accounting › Leases; a supplier's record; the AI assistant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Lease: Office Lyon 2026-2031                Active    Lessor: SCI Rhone      60 months       |
|---------------------------------------------------------------------------------------------|
| Payment 2,400 EUR monthly    Indexation yearly    Purchase option: none    Deposit 4,800 EUR |
| BOOK            STANDARD       TREATMENT                       FIRST YEAR                    |
| Group IFRS      IFRS 16        liability and right-of-use      interest 3,900 / depr 26,600  |
| Statutory       French GAAP    rent                            rent 28,800                   |
| Discount rate (IFRS): 3.5 percent       [Approve] [Record a modification] [End the lease]     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F8-12 step 2, U05 | desktop | ![FL-F8-12 step 2, U05, light](../../images/12-audit-leases-and-special-books/u05-accounting/2-leases-desktop-light.png) | ![FL-F8-12 step 2, U05, dark](../../images/12-audit-leases-and-special-books/u05-accounting/2-leases-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f08-36-leases-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f08-36-leases-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f08-36-leases-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f08-36-leases-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f08-36-leases-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f08-36-leases-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f08-36-leases-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f08-36-leases-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Lease and lessor | E-F8-41 | text | yes while Draft | yes |
| Term and payments | E-F8-41 schedule | months and amounts | yes while Draft | yes |
| Options and indexation | E-F8-41 | text | yes while Draft | no |
| Book, standard, treatment | E-F8-13 | table | no | yes |
| Discount rate | E-F8-41 | percent | yes while Draft | for an IFRS book |
| Entries | E-F8-03 | list of links | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Approve | header | accounting | the lease is Active and the entries start |
| Record a modification | header | accounting | the lease is remeasured where needed |
| End the lease | header | accounting | the entries stop; derecognition where needed |
| Show the maturity table | header | accounting, external accountant | the payments by year for the notes |

## States

- Normal: the lease terms, how each book treats it and the entries posted.
- Empty: No lease yet, with Add a lease.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a book with no
  standard for leases is shown with a link to set it.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F8-41 Lease](../../data/e-f08-41-lease.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F8-41 Lease | Draft | Badge "Draft"; a new record starts here; next: Active (BR-F8-29); fields editable within the role | U05, U08 | `u05-accounting/s-f08-36-leases-e-f08-41-lease-draft-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-36-leases-e-f08-41-lease-draft-desktop-{light,dark}.png` |
| E-F8-41 Lease | Active | Badge "Active"; next: Modified or Ended (UC-F8-37); fields editable within the role | U05, U08 | `u05-accounting/s-f08-36-leases-e-f08-41-lease-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-36-leases-e-f08-41-lease-active-desktop-{light,dark}.png` |
| E-F8-41 Lease | Modified | Badge "Modified"; next: Active (UC-F8-37); fields editable within the role | U05, U08 | `u05-accounting/s-f08-36-leases-e-f08-41-lease-modified-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-36-leases-e-f08-41-lease-modified-desktop-{light,dark}.png` |
| E-F8-41 Lease | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U05, U08 | `u05-accounting/s-f08-36-leases-e-f08-41-lease-ended-desktop-{light,dark}.png`, `u08-external-accountant/s-f08-36-leases-e-f08-41-lease-ended-desktop-{light,dark}.png` |

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

- [FL-F8-12](../../flows/fl-f08-12-audit-leases-and-special-books.md)

## Open questions

None.

---

⬅️ [S-F8-35 Auditor workspace](s-f08-35-auditor-workspace.md) · ⬆️ [Up](README.md) ·
➡️ [S-F8-37 Peppol](s-f08-37-peppol.md)
