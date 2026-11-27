🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-08 Trials, test instances, partners and themes](README.md) › 🖥️ S-F14-27 Test instances

# 🖥️ S-F14-27 Test instances

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md): their own instances.

## Purpose

Create a test instance with demo data, install a plugin build on it, extend or remove it.

## Entry points

Plugin store › Publisher portal › Test instances.

## Wireframe

```text
+---------------------------------------------------------------------------------------------+
| Test instances                                              2 of 3 running      [+ New]    |
|---------------------------------------------------------------------------------------------|
| PLUGIN           BUILD   DEMO DATA        ADDRESS                    ENDS         STATE      |
| Garden planner   1.4.1   Services demo    t-4821.test.example        2026-12-12   Running    |
| Garden planner   1.3.0   Retail demo      t-4712.test.example        2026-11-20   Running    |
| [Open] [Install build] [Reset] [Extend] [Remove]                                            |
+---------------------------------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-08 step 1, U46 | desktop | ![FL-F14-08 step 1, U46, light](../../images/08-trials-instances-and-partners/u46-plugin-publisher/1-test-instances-desktop-light.png) | ![FL-F14-08 step 1, U46, dark](../../images/08-trials-instances-and-partners/u46-plugin-publisher/1-test-instances-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-27-test-instances-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-27-test-instances-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-27-test-instances-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-27-test-instances-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-27-test-instances-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-27-test-instances-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-27-test-instances-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-27-test-instances-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Plugin and build | E-F14-22 plugin, build | text | yes, by installing | yes |
| Demo data | E-F14-22 demo dataset | list of sector examples | while Requested | yes |
| SimpleERP version | E-F14-22 platform version | version | while Requested | yes |
| Address and users | E-F14-22 address | link | no | no |
| Ends | E-F14-22 end date | date | once by Extend | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| New instance | header | publisher | an instance is created with demo data only |
| Install build | row | publisher | a build of the plugin is installed on the instance |
| Reset | row | publisher | the demo data is reloaded |
| Extend | row | publisher | the end date moves once by 14 days |
| Remove | row | publisher | the instance and its data are deleted |

## States

- Normal: the publisher's instances with plugin, build, demo data, address and end date.
- Empty: No test instance yet, with New instance.
- Loading: the headings and the table as placeholders; the values follow.
- Error: the error message pattern ([D122](../../../../06-decisions/ux/d122-error-message-standard.md)); a refused
  request shows the limit or the reason.
- Read-only: the record in a locked state: values shown, no action offered.
- Offline: Not available offline: a back-office screen on live, shared data
  ([D38](../../../../06-decisions/ux/d38-offline-field-tasks.md): only today's schedule, time and intervention records
  work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F14-22 Test instance](../../data/e-f14-22-test-instance.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-22 Test instance | Requested | Badge "Requested"; a new record starts here; next: Running (UC-F14-29); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-27-test-instances-e-f14-22-test-instance-requested-desktop-{light,dark}.png` |
| E-F14-22 Test instance | Running | Badge "Running"; next: Expired or Removed (UC-F14-29); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-27-test-instances-e-f14-22-test-instance-running-desktop-{light,dark}.png` |
| E-F14-22 Test instance | Expired | Badge "Expired"; next: Removed (BR-F14-24); fields editable within the role | U46 | `u46-plugin-publisher/s-f14-27-test-instances-e-f14-22-test-instance-expired-desktop-{light,dark}.png` |
| E-F14-22 Test instance | Removed | Badge "Removed"; final: read-only, no next state; the history shows how it got here | U46 | `u46-plugin-publisher/s-f14-27-test-instances-e-f14-22-test-instance-removed-desktop-{light,dark}.png` |

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

- [FL-F14-08](../../flows/fl-f14-08-trials-instances-and-partners.md)

## Open questions

None.

---

⬅️ [S-F14-26 Version history](../06-release-channels-and-rollback/s-f14-26-version-history.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-28 Free trials](s-f14-28-free-trials.md)
