🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-10 Change safely](README.md) › 🖥️ S-F2-24 Pack upgrade merge

# 🖥️ S-F2-24 Pack upgrade merge

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md)

## Purpose

Compare a pack's new version with the company's changes and decide each conflict.

## Entry points

Packs › Update available.

## Wireframe

```text
+------------------------------------------------------------------+
| Home care pack 2.3 -> 2.4      14 merged, 2 conflicts            |
| Item          Pack 2.3     Pack 2.4      Ours         Decision   |
| Visit form    6 fields     7 fields      8 fields     [Ours v]   |
| Invoice text  mention A    mention B     mention A    pack (lock)|
|                              [Run impact and tests] [Publish]    |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-10 step 3, U07 | desktop | ![FL-F2-10 step 3, U07, light](../../images/10-change-safely/u07-administrator/3-pack-upgrade-merge-desktop-light.png) | ![FL-F2-10 step 3, U07, dark](../../images/10-change-safely/u07-administrator/3-pack-upgrade-merge-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-24-pack-upgrade-merge-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-24-pack-upgrade-merge-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-24-pack-upgrade-merge-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-24-pack-upgrade-merge-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-24-pack-upgrade-merge-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-24-pack-upgrade-merge-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-24-pack-upgrade-merge-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-24-pack-upgrade-merge-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Item, three versions, decision | E-F2-11, E-F2-10 | decision |

## Actions

| Action | Who | Result |
|---|---|---|
| Decide | configurator | Ours, theirs or a mix |
| Publish | configurator | After impact and tests |

## States

- Normal: compare a pack's new version with the company's changes and decide each conflict.
- Empty: no update available: "Your packs are up to date".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: locked legal blocks: always the pack's.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-11 Configuration pack](../../data/e-f02-11-configuration-pack.md),
[E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-11 Configuration pack | Published | Badge "Published"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-24-pack-upgrade-merge-e-f02-11-configuration-pack-published-desktop-{light,dark}.png` |
| E-F2-10 Configuration version | Published | Badge "Published"; a new record starts here; next: Superseded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-24-pack-upgrade-merge-e-f02-10-configuration-version-published-desktop-{light,dark}.png` |

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

⬅️ [S-F2-23 Test cases](s-f02-23-test-cases.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-25 Unused configuration report](s-f02-25-unused-configuration-report.md)
