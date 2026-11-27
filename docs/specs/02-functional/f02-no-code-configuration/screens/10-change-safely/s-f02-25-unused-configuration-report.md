🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-10 Change safely](README.md) › 🖥️ S-F2-25 Unused configuration report

# 🖥️ S-F2-25 Unused configuration report

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

List the configuration nobody used in a period and archive it.

## Entry points

Reports › Unused configuration.

## Wireframe

```text
+------------------------------------------------------------------+
| Unused configuration   [Last 6 months v]                         |
| Item                 Kind       Uses   Still referred by          |
| Fax                  field      0      template Quote             |
| Old discount rule    rule       0      -                          |
| Map of depots        view       0      -                          |
|                                    [Archive selected]            |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-10 step 4, U07 | desktop | ![FL-F2-10 step 4, U07, light](../../images/10-change-safely/u07-administrator/4-unused-configuration-report-desktop-light.png) | ![FL-F2-10 step 4, U07, dark](../../images/10-change-safely/u07-administrator/4-unused-configuration-report-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-25-unused-configuration-report-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-25-unused-configuration-report-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-25-unused-configuration-report-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-25-unused-configuration-report-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-25-unused-configuration-report-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-25-unused-configuration-report-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-25-unused-configuration-report-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-25-unused-configuration-report-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Item, kind, uses, references | computed | selection |

## Actions

| Action | Who | Result |
|---|---|---|
| Archive selected | administrator | One draft archiving them |

## States

- Normal: list the configuration nobody used in a period and archive it.
- Empty: "Everything was used in this period".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for configurators: they read, administrators archive.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-10 Configuration version | Published | Badge "Published"; a new record starts here; next: Superseded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-25-unused-configuration-report-e-f02-10-configuration-version-published-desktop-{light,dark}.png` |

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

⬅️ [S-F2-24 Pack upgrade merge](s-f02-24-pack-upgrade-merge.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-26](../11-rights-translations-and-approvals/s-f02-26-field-rights-and-validation.md)
