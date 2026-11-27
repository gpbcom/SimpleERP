🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔌 [F24 Integrations hub](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F24-08 AI connectors, office suites, warehouse and firms](README.md) ›
🖥️ S-F24-29 Accounting firm sync

# 🖥️ S-F24-29 Accounting firm sync

**Status:** ✅ specified

## Personas

- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md): the periods, masters and held
  changes of the clients they serve.
- [U05 Accounting](../../../../01-users/personas/u05-accounting.md): the masters, the held changes and the sync runs.

## Purpose

Sync with the accountant's software, set which side is master of each period and resolve held changes.

## Entry points

Integrations › Accounting firm sync; Accounting › Work with the accountant.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Accounting firm sync   Firm software: connected   Last run 2026-11-14 03:00         [Sync now] |
|---------------------------------------------------------------------------------------------|
| PERIOD     MASTER        LOCKED   HELD CHANGES   STATE                                      |
| 2026-01..10 SimpleERP   yes      1              Conflict                                   |
| 2026-11    SimpleERP    no       0              Active                                     |
| 2025       firm          yes      0              Active                                     |
| HELD: entry 4108 in October, changed by the firm, +120 EUR    [Accept] [Discard] [Open]     |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F24-08 step 4, U08 | desktop | ![FL-F24-08 step 4, U08, light](../../images/08-ai-connectors-suites-and-warehouse/u08-external-accountant/4-accounting-firm-sync-desktop-light.png) | ![FL-F24-08 step 4, U08, dark](../../images/08-ai-connectors-suites-and-warehouse/u08-external-accountant/4-accounting-firm-sync-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f24-29-accounting-firm-sync-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f24-29-accounting-firm-sync-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f24-29-accounting-firm-sync-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f24-29-accounting-firm-sync-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f24-29-accounting-firm-sync-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f24-29-accounting-firm-sync-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f24-29-accounting-firm-sync-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f24-29-accounting-firm-sync-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Period | fiscal period | month or year | no | yes |
| Master | SimpleERP or firm | badge | accounting and the accountant, together | yes |
| Locked | lock date state | yes or no | no | yes |
| Held changes | changes made on the non-master side | count and list | no | no |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Set master | row | accounting, accountant | changes which side masters the period |
| Sync now | header | accounting | runs the sync outside its schedule |
| Accept | held change | accounting, accountant | posts the change as a new entry on the master side |
| Discard | held change | accounting, accountant | drops the change and tells the other side |

## States

- Normal: the periods with master, lock, held changes and state, and the held changes themselves.
- Empty: No firm connected, with the connection to make.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a paused sync
  shows the firm software's error and the books' last matching state.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F24-19 Firm sync](../../data/e-f24-19-firm-sync.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F24-19 Firm sync | Set up | Badge "Set up"; a new record starts here; next: Active (UC-F24-31); fields editable within the role | U08, U05 | `u08-external-accountant/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-set-up-desktop-{light,dark}.png`, `u05-accounting/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-set-up-desktop-{light,dark}.png` |
| E-F24-19 Firm sync | Active | Badge "Active"; next: Conflict, Suspended or Ended (BR-F24-20, UC-F24-16, UC-F24-31); fields editable within the role | U08, U05 | `u08-external-accountant/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-active-desktop-{light,dark}.png`, `u05-accounting/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-active-desktop-{light,dark}.png` |
| E-F24-19 Firm sync | Conflict | Badge "Conflict"; next: Active (UC-F24-31); fields editable within the role | U08, U05 | `u08-external-accountant/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-conflict-desktop-{light,dark}.png`, `u05-accounting/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-conflict-desktop-{light,dark}.png` |
| E-F24-19 Firm sync | Suspended | Badge "Suspended"; next: Active or Ended (UC-F24-16, UC-F24-31); fields editable within the role | U08, U05 | `u08-external-accountant/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-suspended-desktop-{light,dark}.png`, `u05-accounting/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-suspended-desktop-{light,dark}.png` |
| E-F24-19 Firm sync | Ended | Badge "Ended"; final: read-only, no next state; the history shows how it got here | U08, U05 | `u08-external-accountant/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-ended-desktop-{light,dark}.png`, `u05-accounting/s-f24-29-accounting-firm-sync-e-f24-19-firm-sync-ended-desktop-{light,dark}.png` |

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

- [FL-F24-08](../../flows/fl-f24-08-ai-connectors-suites-and-warehouse.md)

## Open questions

None.

---

⬅️ [S-F24-28 Warehouse export](s-f24-28-warehouse-export.md) · ⬆️ [Up](README.md) ·
➡️ [S-F24-L01 Connectors](../00-lists/s-f24-l01-connectors.md)
