🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-11 Trust the answers](README.md) › 🖥️ S-F3-20 Query view

# 🖥️ S-F3-20 Query view

**Status:** ✅ specified

## Personas

- [U05 Accounting](../../../../01-users/personas/u05-accounting.md)
- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U08 External accountant](../../../../01-users/personas/u08-external-accountant.md)

## Purpose

Show the query behind a figure and the records it counted.

## Entry points

A figure in an AI assistant answer.

## Wireframe

```text
+------------------------------------------------------------------+
| 48,200 EUR   Sales of October 2026, Lyon                         |
| In words: posted invoices, Oct 1-31 2026, site Lyon, excl. VAT   |
| Query:    SELECT sum(total_excl_vat) FROM invoices WHERE ...     |
| Records:  312 invoices  [Open the list]                          |
| Covers only what you may see.     [Rerun] [Save as report]       |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-11 step 5, U05 | desktop | ![FL-F3-11 step 5, U05, light](../../images/11-trust-the-answers/u05-accounting/5-query-view-desktop-light.png) | ![FL-F3-11 step 5, U05, dark](../../images/11-trust-the-answers/u05-accounting/5-query-view-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-20-query-view-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-20-query-view-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-20-query-view-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-20-query-view-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-20-query-view-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-20-query-view-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f03-20-query-view-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f03-20-query-view-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Figure, description, query, records | E-F3-02 and the query | filters, then rerun |

## Actions

| Action | Who | Result |
|---|---|---|
| Rerun | the user | New figure beside the old |
| Save as report | the user | Report or tile |

## States

- Normal: show the query behind a figure and the records it counted.
- Empty: never: it opens on a figure.
- Loading: placeholders while the records are counted.
- Error: the error message pattern (D122).
- Read-only: always for the query code; filters can be changed and rerun.
- Offline: Not available offline: it reads live settings and results
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F3-02 Assistant answer](../../data/e-f03-02-assistant-answer.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-02 Assistant answer | Recorded | Badge "Recorded"; a new record starts here; no other state; fields editable within the role | U05 | `u05-accounting/s-f03-20-query-view-e-f03-02-assistant-answer-recorded-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and tablet; on a phone, the description and the records.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-11 Trust the answers](../../flows/fl-f03-11-trust-the-answers.md)

## Open questions

None.

---

⬅️ [S-F3-19 Injection alerts](s-f03-19-injection-alerts.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-21 My assistant memory](../12-personal-cost-aware-and-learning/s-f03-21-my-assistant-memory.md)
