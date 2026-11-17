🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-10 Change safely](README.md) › 🖥️ S-F2-22 Impact analysis

# 🖥️ S-F2-22 Impact analysis

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

List everything that uses an item a draft changes, and what the change does to each.

## Entry points

Publish and versions › Impact; shown before publishing a used item.

## Wireframe

```text
+------------------------------------------------------------------+
| Impact of: rename Site -> Worksite                               |
| Used by                  What happens         Decision           |
| Rule Assign site manager renamed              ok                 |
| Template Delivery note   renamed              ok                 |
| Plugin Planning Pro      breaks (reads Site)  [Accept] [Fix]     |
| API integration EDI      breaks               [Accept] [Fix]     |
|                                         [Publish]                |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-10 step 1, U07 | desktop | ![FL-F2-10 step 1, U07, light](../../images/10-change-safely/u07-administrator/1-impact-analysis-desktop-light.png) | ![FL-F2-10 step 1, U07, dark](../../images/10-change-safely/u07-administrator/1-impact-analysis-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/10-change-safely/u07-administrator/e1-impact-analysis-refused-desktop-light.png) | ![Error E1, U07, dark](../../images/10-change-safely/u07-administrator/e1-impact-analysis-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-22-impact-analysis-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-22-impact-analysis-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-22-impact-analysis-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-22-impact-analysis-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-22-impact-analysis-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-22-impact-analysis-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-22-impact-analysis-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-22-impact-analysis-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Editable |
|---|---|---|
| Used by, what happens, decision | computed from E-F2-10 | decision |

## Actions

| Action | Who | Result |
|---|---|---|
| Accept, fix | configurator | Item settled |
| Publish | configurator | Allowed once all settled |

## States

- Normal: list everything that uses an item a draft changes, and what the change does to each.
- Empty: nothing uses the item: "No impact".
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: a published change's impact, kept with its version.
- Offline: Not available offline: a configuration screen on live, shared settings
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md)); the app shows that it is offline and reloads the
  screen when the network is back.

Shown entities (VD-15): [E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md),
[E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-26 Configuration draft | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-22-impact-analysis-e-f02-26-configuration-draft-active-desktop-{light,dark}.png` |
| E-F2-10 Configuration version | Published | Badge "Published"; a new record starts here; next: Superseded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-22-impact-analysis-e-f02-10-configuration-version-published-desktop-{light,dark}.png` |

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

⬅️ [S-F2-21 Offline form](../09-portals-and-offline-forms/s-f02-21-offline-form.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-23 Test cases](s-f02-23-test-cases.md)
