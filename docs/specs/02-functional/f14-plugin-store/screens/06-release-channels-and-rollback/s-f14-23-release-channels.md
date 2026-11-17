🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🧰 [F14 Plugin store](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F14-06 Release channels and rollback](README.md) › 🖥️ S-F14-23 Release channels

# 🖥️ S-F14-23 Release channels

**Status:** ✅ specified

## Personas

- [U46 Plugin publisher](../../../../01-users/personas/u46-plugin-publisher.md), who publishes betas and runs rollouts
- [U11 IT provider administrator](../../../../01-users/personas/u11-provider-admin.md), who can stop a rollout
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md), who opts into betas

## Purpose

Publish versions to the beta channel and roll them out in stages, with install reports.

## Entry points

The publisher portal's releases; an administrator's plugin page ("Join the beta").

## Wireframe

```text
Gate Booking, release channels
-------------------------------------------------------------------------------
Beta     2.4.0-beta.1   12 companies   0 failures      [Promote to stable]
Stable   2.4.0          stage 25 % of 1 240   failures 2.9 %   PAUSED
Stages:  [5 %] -> [25 %] -> [100 %]                 [Resume] [Stop] (operator)
-------------------------------------------------------------------------------
Failure reports grouped by cause
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F14-06 step 1, U46 | desktop | ![FL-F14-06 step 1, U46, light](../../images/06-release-channels-and-rollback/u46-plugin-publisher/1-release-channels-desktop-light.png) | ![FL-F14-06 step 1, U46, dark](../../images/06-release-channels-and-rollback/u46-plugin-publisher/1-release-channels-desktop-dark.png) |
| Error E1, U46 | desktop | ![Error E1, U46, light](../../images/06-release-channels-and-rollback/u46-plugin-publisher/e1-release-channels-refused-desktop-light.png) | ![Error E1, U46, dark](../../images/06-release-channels-and-rollback/u46-plugin-publisher/e1-release-channels-refused-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f14-23-release-channels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f14-23-release-channels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f14-23-release-channels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f14-23-release-channels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f14-23-release-channels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f14-23-release-channels-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f14-23-release-channels-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f14-23-release-channels-offline-desktop-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Channel | E-F14-17 channel | beta, stable | yes | yes |
| Stages | E-F14-17 stages | percentages | yes (publisher) | yes |
| Current stage | E-F14-17 current stage | percent | no | yes |
| Failure rate | E-F14-17 failure rate | percent | no | yes |
| Status | E-F14-17 status | running, paused, done, stopped | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Publish to beta | header | publisher | beta offered to opted-in companies |
| Promote | beta row | publisher | rollout starts |
| Resume | stable row | publisher | next stage after a fix |
| Stop | stable row | store operator | rollout stopped |
| Join the beta | plugin page | administrator | company opted in |

## States

- Normal: each channel's version, reach, failures and the rollout's stage.
- Empty: "No release in progress": shown when every company has the latest version.
- Loading: the frame and titles show at once with placeholder rows for the channels; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a paused rollout with its failure rate, or an unsigned version refused.
- Read-only: administrators see only their opt-in; a finished rollout is read-only.
- Offline: not available offline: releases are run on the store's servers. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F14-17 Rollout](../../data/e-f14-17-rollout.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F14-17 Rollout | Beta | Badge "Beta"; a new record starts here; next: Running (UC-F14-24); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-23-release-channels-e-f14-17-rollout-beta-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-23-release-channels-e-f14-17-rollout-beta-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-23-release-channels-e-f14-17-rollout-beta-desktop-{light,dark}.png` |
| E-F14-17 Rollout | Running | Badge "Running"; next: Paused, Done or Stopped (UC-F14-25); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-23-release-channels-e-f14-17-rollout-running-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-23-release-channels-e-f14-17-rollout-running-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-23-release-channels-e-f14-17-rollout-running-desktop-{light,dark}.png` |
| E-F14-17 Rollout | Paused | Badge "Paused"; next: Running (UC-F14-24); fields editable within the role | U07, U11, U46 | `u07-administrator/s-f14-23-release-channels-e-f14-17-rollout-paused-desktop-{light,dark}.png`, `u11-provider-admin/s-f14-23-release-channels-e-f14-17-rollout-paused-desktop-{light,dark}.png`, `u46-plugin-publisher/s-f14-23-release-channels-e-f14-17-rollout-paused-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet in one column.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-09 Chart](../../../../04-ux/design-system/components/c-09-chart.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F14-06 Release channels and rollback](../../flows/fl-f14-06-release-channels-and-rollback.md)

## Open questions

None.

---

⬅️ [S-F14-22 Plugin lifecycle](../07-plugin-end-of-life/s-f14-22-plugin-lifecycle.md) · ⬆️ [Up](README.md) ·
➡️ [S-F14-24 Translations](../03-publish/s-f14-24-translations.md)
