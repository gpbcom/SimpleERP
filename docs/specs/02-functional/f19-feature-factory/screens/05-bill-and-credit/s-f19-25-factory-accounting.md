🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🏭 [F19 Feature factory (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F19-05 Bill and credit](README.md) › 🖥️ S-F19-25 Factory accounting

# 🖥️ S-F19-25 Factory accounting

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Post the factory's invoices, credits and refunds to F8 and reconcile their payments.

## Entry points

Factory billing, Accounting; the month's close.

## Wireframe

```text
Factory accounting, November 2026            [Post to F8]
-------------------------------------------------------------------------------
Document      Kind          Revenue   VAT     Posted       Paid
F-2026-0311   invoice       300.00    60.00   2026-12-01   matched
AV-2026-0042  credit note  -150.00   -30.00   2026-12-01   -
F-2026-0340   invoice       300.00    60.00   2026-12-01   reminder sent
-------------------------------------------------------------------------------
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F19-05 step 4, U05 | desktop | ![FL-F19-05 step 4, U05, light](../../images/05-bill-and-credit/u05-accounting/4-factory-accounting-desktop-light.png) | ![FL-F19-05 step 4, U05, dark](../../images/05-bill-and-credit/u05-accounting/4-factory-accounting-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f19-25-factory-accounting-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f19-25-factory-accounting-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f19-25-factory-accounting-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f19-25-factory-accounting-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f19-25-factory-accounting-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f19-25-factory-accounting-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f19-25-factory-accounting-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f19-25-factory-accounting-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Document | E-F19-15 document | number | no | yes |
| Kind | E-F19-09 kind | invoice, credit note, refund | no | yes |
| Amounts | E-F19-15 amounts | EUR | no | yes |
| Posted | E-F19-15 posted | date | no | no |
| Paid | E-F19-15 reconciled | matched, reminder | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Post to F8 | header | accounting | postings sent |
| Confirm match | row | accounting | payment matched |
| Send reminder | row | accounting | owner reminded |

## States

- Normal: the month's documents with posting and payment state.
- Empty: "Nothing to post this month".
- Loading: the frame and titles show at once with placeholder rows for the documents; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a closed period or a missing account, with the fix.
- Read-only: the owner reads; posted entries are read-only (CR-FR-003).
- Offline: not available offline: posting needs F8 online. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F19-09 Hosted invoice](../../data/e-f19-09-hosted-invoice.md),
[E-F19-15 Factory posting](../../data/e-f19-15-factory-posting.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F19-09 Hosted invoice | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U13 | `u05-accounting/s-f19-25-factory-accounting-e-f19-09-hosted-invoice-active-desktop-{light,dark}.png`, `u13-owner/s-f19-25-factory-accounting-e-f19-09-hosted-invoice-active-{desktop,phone}-{light,dark}.png` |
| E-F19-15 Factory posting | Prepared | Badge "Prepared"; a new record starts here; next: Posted (UC-F19-15); fields editable within the role | U05, U13 | `u05-accounting/s-f19-25-factory-accounting-e-f19-15-factory-posting-prepared-desktop-{light,dark}.png`, `u13-owner/s-f19-25-factory-accounting-e-f19-15-factory-posting-prepared-{desktop,phone}-{light,dark}.png` |
| E-F19-15 Factory posting | Posted | Badge "Posted"; next: Reconciled (UC-F19-25); fields editable within the role | U05, U13 | `u05-accounting/s-f19-25-factory-accounting-e-f19-15-factory-posting-posted-desktop-{light,dark}.png`, `u13-owner/s-f19-25-factory-accounting-e-f19-15-factory-posting-posted-{desktop,phone}-{light,dark}.png` |
| E-F19-15 Factory posting | Reconciled | Badge "Reconciled"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f19-25-factory-accounting-e-f19-15-factory-posting-reconciled-desktop-{light,dark}.png`, `u13-owner/s-f19-25-factory-accounting-e-f19-15-factory-posting-reconciled-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F19-05 Bill and credit](../../flows/fl-f19-05-bill-and-credit.md)

## Open questions

None.

---

⬅️ [S-F19-24 Security and privacy](../02-build-and-check/s-f19-24-security-and-privacy.md) · ⬆️ [Up](README.md) ·
➡️ [S-F19-26 Similar features](../07-catalogue-and-co-funding/s-f19-26-similar-features.md)
