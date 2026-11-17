🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-10 Change safely](README.md) › 🖥️ S-F2-23 Test cases

# 🖥️ S-F2-23 Test cases

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Write, run and read the test cases of a rule or workflow.

## Entry points

A rule or workflow › Test cases.

## Wireframe

```text
+------------------------------------------------------------------+
| Purchase approval › Test cases (3)              [+ Case] [Run]   |
| Case                         Expected      Last run              |
| Purchase 3,200 EUR           manager       passed                |
| Purchase 6,000 EUR           owner         failed: got manager   |
| Purchase from new supplier   buyer first   passed                |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-10 step 2, U07 | desktop | ![FL-F2-10 step 2, U07, light](../../images/10-change-safely/u07-administrator/2-test-cases-desktop-light.png) | ![FL-F2-10 step 2, U07, dark](../../images/10-change-safely/u07-administrator/2-test-cases-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-23-test-cases-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-23-test-cases-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-23-test-cases-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-23-test-cases-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-23-test-cases-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-23-test-cases-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-23-test-cases-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-23-test-cases-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Sample record, expected, last result | E-F2-21 | yes |

## Actions

| Action | Who | Result |
|---|---|---|
| Run | configurator | Results per case |
| Add a case | configurator | Case saved |

## States

- Normal: write, run and read the test cases of a rule or workflow.
- Empty: no case yet: Add a case, or ask the AI assistant to propose some.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: cases of a published rule for non-configurators.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-08 Automation rule](../../data/e-f02-08-automation-rule.md),
[E-F2-21 Test case](../../data/e-f02-21-test-case.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-08 Automation rule | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-23-test-cases-e-f02-08-automation-rule-draft-desktop-{light,dark}.png` |
| E-F2-08 Automation rule | Published | Badge "Published"; next: Paused (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-23-test-cases-e-f02-08-automation-rule-published-desktop-{light,dark}.png` |
| E-F2-08 Automation rule | Paused | Badge "Paused"; next: Published (UC-F2-07); fields editable within the role | U07 | `u07-administrator/s-f02-23-test-cases-e-f02-08-automation-rule-paused-desktop-{light,dark}.png` |
| E-F2-21 Test case | Active | Badge "Active"; a new record starts here; next: Archived (UC-F2-24); fields editable within the role | U07 | `u07-administrator/s-f02-23-test-cases-e-f02-21-test-case-active-desktop-{light,dark}.png` |
| E-F2-21 Test case | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-23-test-cases-e-f02-21-test-case-archived-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Every status is a word, not only a colour; drag and drop has a keyboard equivalent; fields have labels.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F2-10 Change safely](../../flows/fl-f02-10-change-safely.md)

## Open questions

None.

---

⬅️ [S-F2-22 Impact analysis](s-f02-22-impact-analysis.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-24 Pack upgrade merge](s-f02-24-pack-upgrade-merge.md)
