🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
💸 [F22 Unified platform cost management](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F22-07 IT provider re-billing](README.md) › 🖥️ S-F22-26 Client statements

# 🖥️ S-F22-26 Client statements

**Status:** ✅ specified

## Personas

- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)

## Purpose

Review, correct and send each client's usage statement.

## Entry points

Provider space, Statements; the client owner's notification.

## Wireframe

```text
Statements, November 2026                  12 clients   [Send all]
-------------------------------------------------------------------------------
Client              Usage    Billed   Corrections   State
Transport example   80.00    34.50    -5.00         draft
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F22-07 step 2, U11 | desktop | ![FL-F22-07 step 2, U11, light](../../images/07-it-provider-re-billing/u11-provider-admin/2-client-statements-desktop-light.png) | ![FL-F22-07 step 2, U11, dark](../../images/07-it-provider-re-billing/u11-provider-admin/2-client-statements-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f22-26-client-statements-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f22-26-client-statements-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f22-26-client-statements-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f22-26-client-statements-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f22-26-client-statements-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f22-26-client-statements-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f22-26-client-statements-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f22-26-client-statements-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Client | E-F22-18 client | name | no | yes |
| Usage | E-F22-18 usage | EUR | no | yes |
| Billed | E-F22-18 billed | EUR | no | yes |
| Corrections | E-F22-18 corrections | EUR | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Correct | row | IT provider | line corrected |
| Send | row | IT provider | statement and invoice sent |

## States

- Normal: drafts and sent statements.
- Empty: "No statement this month".
- Loading: the frame and titles show at once with placeholder rows for the statements; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a client without rule, flagged.
- Read-only: the client's owner reads their own.
- Offline: not available offline: sent online. D38 keeps only today's schedule, time and intervention records offline. A
  banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing is queued
  until the connection is back.

Shown entities (VD-15): [E-F22-18 Client usage statement](../../data/e-f22-18-client-usage-statement.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F22-18 Client usage statement | Draft | Badge "Draft"; a new record starts here; next: Sent (UC-F22-26); fields editable within the role | U11, U13 | `u11-provider-admin/s-f22-26-client-statements-e-f22-18-client-usage-statement-draft-desktop-{light,dark}.png`, `u13-owner/s-f22-26-client-statements-e-f22-18-client-usage-statement-draft-{desktop,phone}-{light,dark}.png` |
| E-F22-18 Client usage statement | Sent | Badge "Sent"; next: Invoiced (UC-F22-26); fields editable within the role | U11, U13 | `u11-provider-admin/s-f22-26-client-statements-e-f22-18-client-usage-statement-sent-desktop-{light,dark}.png`, `u13-owner/s-f22-26-client-statements-e-f22-18-client-usage-statement-sent-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; clients read on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F22-07 IT provider re-billing](../../flows/fl-f22-07-it-provider-re-billing.md)

## Open questions

None.

---

⬅️ [S-F22-25 Re-billing rules](s-f22-25-re-billing-rules.md) · ⬆️ [Up](README.md) ·
➡️ [S-F22-27 Credit packs](../08-credits-saas-and-carbon/s-f22-27-credit-packs.md)
