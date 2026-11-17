🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧭 [F21 Onboarding and module activation](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F21-05 Migration from another tool](README.md) › 🖥️ S-F21-22 Opening balance check

# 🖥️ S-F21-22 Opening balance check

**Status:** ✅ specified

## Personas

- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)

## Purpose

Compare opening balances with last year's FEC and post the opening entry.

## Entry points

Guide, Accounting; the accountant's client list.

## Wireframe

```text
Opening balances vs FEC 2025        186 accounts   1 difference
-------------------------------------------------------------------------------
Account   Opening      FEC closing   Difference   Reason
411       48 210.00    48 210.00     -
512       12 000.00    12 040.00     40.00        [bank fees]
-------------------------------------------------------------------------------
[Post the opening entry]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F21-05 step 2, U08 | desktop | ![FL-F21-05 step 2, U08, light](../../images/05-migration-from-another-tool/u08-external-accountant/2-opening-balance-check-desktop-light.png) | ![FL-F21-05 step 2, U08, dark](../../images/05-migration-from-another-tool/u08-external-accountant/2-opening-balance-check-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f21-22-opening-balance-check-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f21-22-opening-balance-check-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f21-22-opening-balance-check-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f21-22-opening-balance-check-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f21-22-opening-balance-check-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f21-22-opening-balance-check-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f21-22-opening-balance-check-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f21-22-opening-balance-check-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Account | E-F21-15 | number | no | yes |
| Opening, FEC | E-F21-15 | EUR | no | yes |
| Difference | E-F21-15 differences | EUR | no | no |
| Reason | E-F21-15 differences | text | yes | if different |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Upload FEC | header | accountant | balances compared |
| Explain | row | accountant | reason saved |
| Post | footer | accountant | opening entry posted |

## States

- Normal: accounts with balances and differences.
- Empty: "Upload last year's FEC".
- Loading: the frame and titles show at once with placeholder rows for the accounts; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an invalid FEC with its line.
- Read-only: posted check read-only.
- Offline: not available offline: the comparison runs on the server. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F21-15 Opening balance check](../../data/e-f21-15-opening-balance-check.md),
[E-F8-27 FEC file](../../../f08-accounting/data/e-f08-27-fec-file.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F21-15 Opening balance check | Compared | Badge "Compared"; a new record starts here; next: Equal or Differences (UC-F21-22); fields editable within the role | U05, U08 | `u05-accounting/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-compared-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-compared-desktop-{light,dark}.png` |
| E-F21-15 Opening balance check | Equal | Badge "Equal"; final: read-only, no next state; the history shows how it got here | U05, U08 | `u05-accounting/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-equal-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-equal-desktop-{light,dark}.png` |
| E-F21-15 Opening balance check | Differences | Badge "Differences"; next: Explained (UC-F21-22); fields editable within the role | U05, U08 | `u05-accounting/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-differences-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-22-opening-balance-check-e-f21-15-opening-balance-check-differences-desktop-{light,dark}.png` |
| E-F8-27 FEC file | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U05, U08 | `u05-accounting/s-f21-22-opening-balance-check-e-f08-27-fec-file-active-desktop-{light,dark}.png`, `u08-external-accountant/s-f21-22-opening-balance-check-e-f08-27-fec-file-active-desktop-{light,dark}.png` |

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
- [C-12 File upload](../../../../04-ux/design-system/components/c-12-file-upload.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F21-05 Migration from another tool](../../flows/fl-f21-05-migration-from-another-tool.md)

## Open questions

None.

---

⬅️ [S-F21-21 Migration](s-f21-21-migration.md) · ⬆️ [Up](README.md) ·
➡️ [S-F21-23 Invite your accountant](../03-team-and-data/s-f21-23-invite-your-accountant.md)
