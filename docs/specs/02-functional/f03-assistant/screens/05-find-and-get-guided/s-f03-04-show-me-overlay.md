🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) › 🤖 [F3 Assistant](../../README.md) ›
🖥️ [Screens](../README.md) › 🖥️ [Screens: FL-F3-05 Find and get guided](README.md) › 🖥️ S-F3-04 Show me overlay

# 🖥️ S-F3-04 Show me overlay

**Status:** ✅ specified

## Personas

Every internal persona (D142): [U01](../../../../01-users/personas/u01-employee.md),
[U02](../../../../01-users/personas/u02-manager.md), [U03](../../../../01-users/personas/u03-sales.md),
[U04](../../../../01-users/personas/u04-purchasing.md), [U05](../../../../01-users/personas/u05-accounting.md),
[U06](../../../../01-users/personas/u06-hr.md), [U07](../../../../01-users/personas/u07-administrator.md),
[U12](../../../../01-users/personas/u12-marketing.md), [U13](../../../../01-users/personas/u13-owner.md),
[U14](../../../../01-users/personas/u14-field-worker.md),
[U15](../../../../01-users/personas/u15-warehouse-operator.md),
[U16](../../../../01-users/personas/u16-office-worker.md).

## Purpose

Show the way on the real screen, one step at a time (D166).

## Entry points

"Show me" under the AI assistant's steps.

## Wireframe

```text
+------------------------------------------------------------------+
| Job J-2026-044                                                    |
|  Status [ In progress v ]  <== highlighted                        |
|          +-------------------------------------+                  |
|          | Step 1 of 3: set the status to      |                  |
|          | Finished.        [Stop]  [Next >]   |                  |
|          +-------------------------------------+                  |
|  (the rest of the screen dimmed)                 [Save]          |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F3-05 step 3, U16 | desktop | ![FL-F3-05 step 3, U16, light](../../images/05-find-and-get-guided/u16-office-worker/3-show-me-desktop-light.png) | ![FL-F3-05 step 3, U16, dark](../../images/05-find-and-get-guided/u16-office-worker/3-show-me-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f03-04-show-me-overlay-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f03-04-show-me-overlay-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f03-04-show-me-overlay-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f03-04-show-me-overlay-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f03-04-show-me-overlay-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f03-04-show-me-overlay-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f03-04-show-me-overlay-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f03-04-show-me-overlay-offline-phone-dark.png) |

## Fields and columns

The step's text, its number, Next and Stop.

## Actions

| Action | Who | Result |
|---|---|---|
| Next | the user | The next step, possibly on another screen |
| Stop | the user | The overlay closes |

## States

- Normal: Show the way on the real screen, one step at a time (D166), as the wireframe shows.
- Empty: never: the overlay opens with its first step.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: the error message pattern (D122).
- Read-only: always: it shows, it never changes data.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.
- A step highlighted.
- Lost: the user went elsewhere; "Restart from step 2?".
- Done.

Shown entities (VD-15): [E-F3-06 Configuration request](../../data/e-f03-06-configuration-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F3-06 Configuration request | Planned | Badge "Planned"; next: Done (UC-F3-05); fields editable within the role | U16 | `u16-office-worker/s-f03-04-show-me-overlay-e-f03-06-configuration-request-planned-{desktop,phone}-{light,dark}.png` |
| E-F3-06 Configuration request | Done | Badge "Done"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f03-04-show-me-overlay-e-f03-06-configuration-request-done-{desktop,phone}-{light,dark}.png` |
| E-F3-06 Configuration request | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U16 | `u16-office-worker/s-f03-04-show-me-overlay-e-f03-06-configuration-request-declined-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop and phone; on a phone the bubble sits under the highlighted element.

## Accessibility

The highlighted element gets focus; the bubble is announced; Escape stops.

## Components

- [C-05 Modal](../../../../04-ux/design-system/components/c-05-modal.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F3-05 Find and get guided](../../flows/fl-f03-05-find-and-get-guided.md)

## Open questions

None.

---

⬅️ [S-F3-03 Writing style settings](../04-summarise-or-draft/s-f03-03-writing-style-settings.md) · ⬆️ [Up](README.md) ·
➡️ [S-F3-05 Configuration requests](s-f03-05-configuration-requests.md)
