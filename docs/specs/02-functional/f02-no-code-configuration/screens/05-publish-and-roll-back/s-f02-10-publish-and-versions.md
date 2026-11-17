🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🔧 [F2 No-code configuration](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F2-05 Publish and roll back](README.md) › 🖥️ S-F2-10 Publish and versions

# 🖥️ S-F2-10 Publish and versions

**Status:** ✅ specified

## Personas

- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)
- Users with the Configurator role (D96, D98)

## Purpose

Review a draft and publish it; see versions and roll back.

## Entry points

Configuration › Publish; Configuration › Versions.

## Wireframe

```text
+------------------------------------------------------------------+
| Publish                          [Preview as v] [Publish]         |
|  + Field Vehicle added to Quotes                                 |
|  ~ Status Waiting for site visit added before Sent               |
|------------------------------------------------------------------|
| Versions                                                         |
|  16  10 Nov 15:02  Marie Dupont   3 changes        [Roll back]   |
|  15  09 Nov 11:40  Claire Martin  1 change         [Roll back]   |
+------------------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F2-05 step 1, U07 | desktop | ![FL-F2-05 step 1, U07, light](../../images/05-publish-and-roll-back/u07-administrator/1-review-and-publish-desktop-light.png) | ![FL-F2-05 step 1, U07, dark](../../images/05-publish-and-roll-back/u07-administrator/1-review-and-publish-desktop-dark.png) |
| Error E2, U07 | desktop | ![Error E2, U07, light](../../images/05-publish-and-roll-back/u07-administrator/e2-records-in-removed-status-desktop-light.png) | ![Error E2, U07, dark](../../images/05-publish-and-roll-back/u07-administrator/e2-records-in-removed-status-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f02-10-publish-and-versions-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f02-10-publish-and-versions-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f02-10-publish-and-versions-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f02-10-publish-and-versions-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f02-10-publish-and-versions-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f02-10-publish-and-versions-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f02-10-publish-and-versions-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f02-10-publish-and-versions-offline-desktop-dark.png) |

## Fields and columns

As [E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md#fields).

## Actions

| Action | Who | Result |
|---|---|---|
| Publish | configurator | UC-F2-09 |
| Roll back | administrator | UC-F2-10 |

## States

- Normal: Review a draft and publish it; see versions and roll back, as the wireframe shows.
- Empty: Nothing to publish: no draft waits.
- Loading: placeholders in the layout of the wireframe; actions are disabled until the record has loaded.
- Error: a draft with problems, each in plain words.
- Read-only: past versions, which can be rolled back to but not edited.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): [E-F2-10 Configuration version](../../data/e-f02-10-configuration-version.md),
[E-F2-26 Configuration draft](../../data/e-f02-26-configuration-draft.md),
[E-F2-25 Request type](../../data/e-f02-25-request-type.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F2-10 Configuration version | Published | Badge "Published"; a new record starts here; next: Superseded (UC-F2-09); fields editable within the role | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-10-configuration-version-published-desktop-{light,dark}.png` |
| E-F2-10 Configuration version | Superseded | Badge "Superseded"; final: read-only, no next state; the history shows how it got here | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-10-configuration-version-superseded-desktop-{light,dark}.png` |
| E-F2-26 Configuration draft | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-26-configuration-draft-active-desktop-{light,dark}.png` |
| E-F2-25 Request type | Draft | Badge "Draft"; a new record starts here; next: Published (UC-F16-16); fields editable within the role | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-25-request-type-draft-desktop-{light,dark}.png` |
| E-F2-25 Request type | Published | Badge "Published"; next: Draft or Retired (UC-F2-30); fields editable within the role | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-25-request-type-published-desktop-{light,dark}.png` |
| E-F2-25 Request type | Retired | Badge "Retired"; next: Published (UC-F2-30); fields editable within the role | U07 | `u07-administrator/s-f02-10-publish-and-versions-e-f02-25-request-type-retired-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Changes are a list with plus and tilde marks spelt out for screen readers.

## Components

- [C-14 Timeline](../../../../04-ux/design-system/components/c-14-timeline.md)

## Shown in

- [FL-F2-05 Publish and roll back](../../flows/fl-f02-05-publish-and-roll-back.md)
- [FL-F2-12 Set up request types](../../flows/fl-f02-12-set-up-request-types.md)

## Open questions

None.

---

⬅️ [S-F2-09 Workflow designer](../04-design-a-visual-workflow/s-f02-09-workflow-designer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F2-11 Packs](../06-share-a-configuration/s-f02-11-packs.md)
