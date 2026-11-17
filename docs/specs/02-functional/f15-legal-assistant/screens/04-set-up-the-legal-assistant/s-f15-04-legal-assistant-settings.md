🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
⚖️ [F15 Legal assistant](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F15-04 Set up the legal assistant](README.md) › 🖥️ S-F15-04 Legal assistant settings

# 🖥️ S-F15-04 Legal assistant settings

**Status:** ✅ specified

## Personas

U07 Administrator

## Purpose

Set up the legal assistant (FL-F15-04).

## Entry points

Administration › Assistant › Legal.

## Wireframe

```text
+------------------------------------------------------+
| Legal assistant                            [Save]    |
| Law packs   France (shipped)  pulled today [+ Store]  |
| Warnings    [on]  Rest times [on] Contracts [on]      |
|             Thresholds [on] Leave [on]                |
| Provider    Local model (AI settings)                |
| Last refresh  today 04:10, applied                   |
+------------------------------------------------------+
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F15-04 step 1, U07 | desktop | ![FL-F15-04 step 1, U07, light](../../images/04-set-up-the-legal-assistant/u07-administrator/1-law-packs-and-warnings-desktop-light.png) | ![FL-F15-04 step 1, U07, dark](../../images/04-set-up-the-legal-assistant/u07-administrator/1-law-packs-and-warnings-desktop-dark.png) |
| Error E1, U07 | desktop | ![Error E1, U07, light](../../images/04-set-up-the-legal-assistant/u07-administrator/e1-source-unreachable-desktop-light.png) | ![Error E1, U07, dark](../../images/04-set-up-the-legal-assistant/u07-administrator/e1-source-unreachable-desktop-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f15-04-legal-assistant-settings-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f15-04-legal-assistant-settings-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f15-04-legal-assistant-settings-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f15-04-legal-assistant-settings-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f15-04-legal-assistant-settings-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f15-04-legal-assistant-settings-read-only-desktop-dark.png) |
| Offline | desktop | ![Offline, light](../../images/states/s-f15-04-legal-assistant-settings-offline-desktop-light.png) | ![Offline, dark](../../images/states/s-f15-04-legal-assistant-settings-offline-desktop-dark.png) |

## Fields and columns

Law packs with each source's last pull; warnings per kind; provider.

## Actions

As the flow's steps.

## States

- Normal: the countries and law packs installed, warnings on or off, the AI feature setting and links to Law packs and
  Standards.
- An official source unreachable for a day: a banner; the last copy is used.
- Empty: "No law pack installed": France is offered first.
- Loading: the frame and titles show at once with placeholder rows for the settings; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: the error message pattern (D122).
- Read-only: other roles do not see the settings; the AI feature setting is changed in F1.
- Offline: not available offline: settings are on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F15-01 Law pack](../../data/e-f15-01-law-pack.md),
[E-F15-11 Warning trigger](../../data/e-f15-11-warning-trigger.md),
[E-F15-12 Legal source](../../data/e-f15-12-legal-source.md),
[E-F15-04 Standard register entry](../../data/e-f15-04-standard-register-entry.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F15-01 Law pack | Scheduled | Badge "Scheduled"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f15-04-legal-assistant-settings-e-f15-01-law-pack-scheduled-desktop-{light,dark}.png` |
| E-F15-11 Warning trigger | On | Badge "On"; a new record starts here; next: Off (UC-F15-04); fields editable within the role | U07 | `u07-administrator/s-f15-04-legal-assistant-settings-e-f15-11-warning-trigger-on-desktop-{light,dark}.png` |
| E-F15-11 Warning trigger | Off | Badge "Off"; next: On (UC-F15-02); fields editable within the role | U07 | `u07-administrator/s-f15-04-legal-assistant-settings-e-f15-11-warning-trigger-off-desktop-{light,dark}.png` |
| E-F15-12 Legal source | Active | Badge "Active"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f15-04-legal-assistant-settings-e-f15-12-legal-source-active-desktop-{light,dark}.png` |
| E-F15-04 Standard register entry | Open | Badge "Open"; a new record starts here; no other state; fields editable within the role | U07 | `u07-administrator/s-f15-04-legal-assistant-settings-e-f15-04-standard-register-entry-open-desktop-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Citations are links; warnings use an icon and text, never colour alone.

## Components

- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F15-04 Set up the legal assistant](../../flows/fl-f15-04-set-up-the-legal-assistant.md)

## Open questions

None.

---

⬅️ [S-F15-03 Document check](../03-check-a-document-against-the-law/s-f15-03-document-check.md) · ⬆️ [Up](README.md) ·
➡️ [S-F15-05 Law packs refresh](s-f15-05-law-packs-refresh.md)
