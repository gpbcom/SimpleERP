🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-12 Personal, cost-aware and learning](README.md) ›
🖥️ S-F3-21 My assistant memory

# 🖥️ S-F3-21 My assistant memory

**Status:** ✅ specified

## Personas

- [U01 Employee](../../../../01-users/personas/u01-employee.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

See, change and erase what the AI assistant keeps about the user's preferences.

## Entry points

The AI assistant panel › My memory.

## Wireframe

```text
+------------------------------------------------------------------+
| My assistant memory (3)                         [Erase all]      |
| my site: Lyon                        2026-11-12  [Edit] [Erase]  |
| drafts in English                    2026-10-02  [Edit] [Erase]  |
| reports as PDF                       2026-09-15  [Edit] [Erase]  |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-12 step 1, U01 | desktop | ![FL-F3-12 step 1, U01, light](../../images/12-personal-cost-aware-and-learning/u01-employee/1-my-assistant-memory-desktop-light.png) | ![FL-F3-12 step 1, U01, dark](../../images/12-personal-cost-aware-and-learning/u01-employee/1-my-assistant-memory-desktop-dark.png) |
| FL-F3-12 step 1, U01 | phone | ![FL-F3-12 step 1, U01, light](../../images/12-personal-cost-aware-and-learning/u01-employee/1-my-assistant-memory-phone-light.png) | ![FL-F3-12 step 1, U01, dark](../../images/12-personal-cost-aware-and-learning/u01-employee/1-my-assistant-memory-phone-dark.png) |
| Error E1, U01 | desktop | ![Error E1, U01, light](../../images/12-personal-cost-aware-and-learning/u01-employee/e1-my-assistant-memory-refused-desktop-light.png) | ![Error E1, U01, dark](../../images/12-personal-cost-aware-and-learning/u01-employee/e1-my-assistant-memory-refused-desktop-dark.png) |
| Error E1, U01 | phone | ![Error E1, U01, light](../../images/12-personal-cost-aware-and-learning/u01-employee/e1-my-assistant-memory-refused-phone-light.png) | ![Error E1, U01, dark](../../images/12-personal-cost-aware-and-learning/u01-employee/e1-my-assistant-memory-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-21-my-assistant-memory-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-21-my-assistant-memory-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-21-my-assistant-memory-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-21-my-assistant-memory-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-21-my-assistant-memory-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-21-my-assistant-memory-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-21-my-assistant-memory-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-21-my-assistant-memory-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Items | E-F3-20 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Edit, erase, erase all | the user | Item changed or gone |

## States

- Normal: see, change and erase what the AI assistant keeps about the user's preferences.
- Empty: "The assistant keeps nothing about you".
- Loading: skeleton rows ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md)).
- Error: the error message pattern (D122).
- Read-only: when the administrator turned memory off: read and erase only.
- Offline: Readable offline from the phone's copy; edits and erasures wait for the network
  ([D182](../../../../06-decisions/f03-assistant/d182-offline-assistant.md)).

Shown entities (VD-15): [E-F3-20 Memory item](../../data/e-f03-20-memory-item.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-20 Memory item | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U01 | `u01-employee/s-f03-21-my-assistant-memory-e-f03-20-memory-item-active-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone.

## Accessibility

Every status is a word, not only a colour; tables have headers; actions are buttons with labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-12 Personal, cost-aware and learning](../../flows/fl-f03-12-personal-cost-aware-and-learning.md)

## Open questions

None.

---

⬅️ [S-F3-20 Query view](../11-trust-the-answers/s-f03-20-query-view.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-22 Cost estimate](s-f03-22-cost-estimate.md)
