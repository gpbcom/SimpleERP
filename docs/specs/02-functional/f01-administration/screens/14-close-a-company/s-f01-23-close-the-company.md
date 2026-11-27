🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🛡️ [F1 Administration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F1-14 Close a company](README.md) › 🖥️ S-F1-23 Close the company

# 🖥️ S-F1-23 Close the company

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Ask to close the company or leave the hosted edition, export everything, confirm.

## Entry points

Administration › Close the company (owner only).

## Wireframe

```text
+------------------------------------------------------------------+
| Close the company       ( ) Close  (x) Leave the hosted edition  |
| 1 Open items   2 unpaid invoices, 1 active subscription [Accept] |
| 2 Export       records CSV/JSON, documents, FEC, audit  [Prepare]|
|                acme-export-2026-11-30.zip  12,400 invoices ...   |
| 3 Confirm      [Confirm with two-factor]                         |
| Read-only until 2026-12-30, then closed.        [Reopen]         |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F1-14 step 1, U13 | desktop | ![FL-F1-14 step 1, U13, light](../../images/14-close-a-company/u13-owner/1-close-the-company-desktop-light.png) | ![FL-F1-14 step 1, U13, dark](../../images/14-close-a-company/u13-owner/1-close-the-company-desktop-dark.png) |
| FL-F1-14 step 1, U13 | phone | ![FL-F1-14 step 1, U13, light](../../images/14-close-a-company/u13-owner/1-close-the-company-phone-light.png) | ![FL-F1-14 step 1, U13, dark](../../images/14-close-a-company/u13-owner/1-close-the-company-phone-dark.png) |
| Error E1, U13 | desktop | ![Error E1, U13, light](../../images/14-close-a-company/u13-owner/e1-close-the-company-refused-desktop-light.png) | ![Error E1, U13, dark](../../images/14-close-a-company/u13-owner/e1-close-the-company-refused-desktop-dark.png) |
| Error E1, U13 | phone | ![Error E1, U13, light](../../images/14-close-a-company/u13-owner/e1-close-the-company-refused-phone-light.png) | ![Error E1, U13, dark](../../images/14-close-a-company/u13-owner/e1-close-the-company-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f01-23-close-the-company-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f01-23-close-the-company-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f01-23-close-the-company-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f01-23-close-the-company-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f01-23-close-the-company-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f01-23-close-the-company-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f01-23-close-the-company-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f01-23-close-the-company-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Kind, open items, export, dates | E-F1-21 | through the steps |

## Actions

| Action | Who | Result |
|---|---|---|
| Prepare the export | owner, administrator | Export built in the background |
| Confirm | owner | Read-only, then closed |
| Reopen | owner | Within the read-only period |

## States

- Normal: the three steps and where the closing stands.
- Empty: nothing asked yet: the choice between close and leave.
- Loading: the export's progress bar.
- Error: an export that failed part way, resumed (D122).
- Read-only: for the administrator, who prepares but cannot confirm.
- Offline: Not available offline: an administration screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F1-21 Company closing](../../data/e-f01-21-company-closing.md),
[E-F8-27 FEC file](../../../f08-accounting/data/e-f08-27-fec-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F1-21 Company closing | Asked | Badge "Asked"; a new record starts here; next: Exported (UC-F1-23); fields editable within the role | U07, U11, U13 | `u07-administrator/s-f01-23-close-the-company-e-f01-21-company-closing-asked-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-23-close-the-company-e-f01-21-company-closing-asked-desktop-{light,dark}.png`, `u13-owner/s-f01-23-close-the-company-e-f01-21-company-closing-asked-{desktop,phone}-{light,dark}.png` |
| E-F1-21 Company closing | Exported | Badge "Exported"; next: Confirmed (UC-F1-23); fields editable within the role | U07, U11, U13 | `u07-administrator/s-f01-23-close-the-company-e-f01-21-company-closing-exported-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-23-close-the-company-e-f01-21-company-closing-exported-desktop-{light,dark}.png`, `u13-owner/s-f01-23-close-the-company-e-f01-21-company-closing-exported-{desktop,phone}-{light,dark}.png` |
| E-F1-21 Company closing | Confirmed | Badge "Confirmed"; next: Reopened or Closed (UC-F1-23); fields editable within the role | U07, U11, U13 | `u07-administrator/s-f01-23-close-the-company-e-f01-21-company-closing-confirmed-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-23-close-the-company-e-f01-21-company-closing-confirmed-desktop-{light,dark}.png`, `u13-owner/s-f01-23-close-the-company-e-f01-21-company-closing-confirmed-{desktop,phone}-{light,dark}.png` |
| E-F1-21 Company closing | Closed | Badge "Closed"; final: read-only, no next state; the history shows how it got here | U07, U11, U13 | `u07-administrator/s-f01-23-close-the-company-e-f01-21-company-closing-closed-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-23-close-the-company-e-f01-21-company-closing-closed-desktop-{light,dark}.png`, `u13-owner/s-f01-23-close-the-company-e-f01-21-company-closing-closed-{desktop,phone}-{light,dark}.png` |
| E-F8-27 FEC file | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07, U11, U13 | `u07-administrator/s-f01-23-close-the-company-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u11-provider-admin/s-f01-23-close-the-company-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u13-owner/s-f01-23-close-the-company-e-f08-27-fec-file-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-13 Stepper](../../../../04-ux/design-system/components/c-13-stepper.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)

## Shown in

- [FL-F1-14 Close a company](../../flows/fl-f01-14-close-a-company.md)

## Open questions

None.

---

⬅️ [S-F1-22 Audit trail](../13-security-and-audit/s-f01-22-audit-trail.md) · ⬆️ [Up](README.md) ·
➡️ [S-F1-24 Access rights dashboard](../09-administration-reports/s-f01-24-access-rights-dashboard.md)
