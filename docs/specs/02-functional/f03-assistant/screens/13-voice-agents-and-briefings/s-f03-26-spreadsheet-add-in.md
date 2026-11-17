🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-13 Voice, agents and briefings](README.md) ›
🖥️ S-F3-26 Spreadsheet add-in

# 🖥️ S-F3-26 Spreadsheet add-in

**Status:** ✅ specified

## Personas

- - [U05 Accounting](../../../../01-users/personas/u05-accounting.md): reports and ledgers.
- - [U13 Owner](../../../../01-users/personas/u13-owner.md): figures of the company.

## Purpose

Pick data to pull into the spreadsheet, refresh it, and see the connection's state.

## Entry points

The add-in pane of the spreadsheet application; Assistant › Add-ins (the connection list).

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| simple-ERP add-in            Connected as Claire P.             [Refresh all] [Disconnect]  |
| ------------------------------------------------------------------------------------------- |
| DATA                         WHERE          LAST READ       ROWS                            |
| Trial balance, Nov 2026      Sheet1!A1      09:12           184                             |
| Open invoices                Sheet2!A1      09:12           37                              |
| Ask: What were sales in Lyon last month?  [Insert as formula]        Source: invoices       |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-13 step 3, U05 | desktop | ![FL-F3-13 step 3, U05, light](../../images/13-voice-agents-and-briefings/u05-accounting/3-spreadsheet-add-in-desktop-light.png) | ![FL-F3-13 step 3, U05, dark](../../images/13-voice-agents-and-briefings/u05-accounting/3-spreadsheet-add-in-desktop-dark.png) |
| FL-F3-13 step 3, U05 | desktop | ![FL-F3-13 step 3, U05, light](../../images/13-voice-agents-and-briefings/u05-accounting/3-spreadsheet-add-in-desktop-light.png) | ![FL-F3-13 step 3, U05, dark](../../images/13-voice-agents-and-briefings/u05-accounting/3-spreadsheet-add-in-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-26-spreadsheet-add-in-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-26-spreadsheet-add-in-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-26-spreadsheet-add-in-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-26-spreadsheet-add-in-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-26-spreadsheet-add-in-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-26-spreadsheet-add-in-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-26-spreadsheet-add-in-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-26-spreadsheet-add-in-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Data | E-F3-25 list or report | text | yes | yes |
| Where | cell range | reference | yes | yes |
| Last read | E-F3-25 last used | time | no | yes |
| Rows | rows read | number | no | yes |
| Connection | E-F3-25 state | badge | disconnect | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Connect | pane | the user | the sign-in opens and a connection is made |
| Refresh all | header | the user | the data is read again with the user's rights |
| Insert | list | the user | a list or report is put in the cells |
| Disconnect | header | the user | the token is revoked |

## States

- Normal: the connection, the data pulled into the workbook and the question box.
- Empty: Nothing pulled yet. Choose a list or a report.
- Loading: The data is read and the cells fill with a progress count.
- Error: the error message pattern (D122); an expired sign-in asks to sign in again.
- Read-only: a revoked connection: the last values with a Not refreshed mark.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F3-25 Add-in connection](../../data/e-f03-25-add-in-connection.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-25 Add-in connection | Connected | Badge "Connected"; a new record starts here; next: Expired or Revoked (BR-F3-45, UC-F3-22); fields editable within the role | U05, U13 | `u05-accounting/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-connected-desktop-{light,dark}.png`, `u13-owner/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-connected-{desktop,phone}-{light,dark}.png` |
| E-F3-25 Add-in connection | Expired | Badge "Expired"; next: Connected or Revoked (UC-F3-22); fields editable within the role | U05, U13 | `u05-accounting/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-expired-desktop-{light,dark}.png`, `u13-owner/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-expired-{desktop,phone}-{light,dark}.png` |
| E-F3-25 Add-in connection | Revoked | Badge "Revoked"; final: read-only, no next state; the history shows how it got here | U05, U13 | `u05-accounting/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-revoked-desktop-{light,dark}.png`, `u13-owner/s-f03-26-spreadsheet-add-in-e-f03-25-add-in-connection-revoked-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

The add-in pane is narrow by design and works in the spreadsheet's mobile apps that allow add-ins; otherwise desktop
only.

## Accessibility

The pane follows the spreadsheet application's own accessibility; messages are text; keyboard: next data, insert.

## Components

- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-13 Voice, agents and briefings](../../flows/fl-f03-13-voice-agents-and-briefings.md)

## Open questions

None.

---

⬅️ [S-F3-25 Agent catalogue](s-f03-25-agent-catalogue.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-27 Daily briefing](s-f03-27-daily-briefing.md)
