🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-02 Automate an intent](README.md) › 🖥️ S-F16-12 Intent discovery

# 🖥️ S-F16-12 Intent discovery

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Show groups of alike past requests proposed as new intents.

## Entry points

Support menu, Intents, Discovery.

## Wireframe

```text
Intent discovery     Period [last 90 days]        3 210 requests   [Run]
-------------------------------------------------------------------------------
Candidate                       Requests   By people   Status
Change of delivery address      186        92 %        proposed   [Accept] [Merge] [Dismiss]
Gift wrapping question          41         100 %       proposed
-------------------------------------------------------------------------------
Examples of the selected candidate (5)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-02 step 5, U02 | desktop | ![FL-F16-02 step 5, U02, light](../../images/02-automate-an-intent/u02-manager/5-intent-discovery-desktop-light.png) | ![FL-F16-02 step 5, U02, dark](../../images/02-automate-an-intent/u02-manager/5-intent-discovery-desktop-dark.png) |
| FL-F16-02 step 5, U02 | phone | ![FL-F16-02 step 5, U02, light](../../images/02-automate-an-intent/u02-manager/5-intent-discovery-phone-light.png) | ![FL-F16-02 step 5, U02, dark](../../images/02-automate-an-intent/u02-manager/5-intent-discovery-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-12-intent-discovery-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-12-intent-discovery-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-12-intent-discovery-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-12-intent-discovery-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-12-intent-discovery-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-12-intent-discovery-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-12-intent-discovery-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-12-intent-discovery-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Candidate | E-F16-10 label | text | yes | yes |
| Requests | E-F16-10 requests | count | no | yes |
| By people | E-F16-10 share | percent | no | yes |
| Status | E-F16-10 status | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Run | header | support lead | candidates computed |
| Accept | row | support lead | new intent opened in the editor |
| Merge | row | support lead | examples added to an intent's tests |
| Dismiss | row | support lead | candidate hidden |

## States

- Normal: candidates sorted by volume with their examples.
- Empty: "Not enough requests yet": the minimum is shown.
- Loading: the frame and titles show at once with placeholder rows for the candidates; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a run refused below the minimum.
- Read-only: the owner reads; decided candidates are read-only.
- Offline: not available offline: discovery runs on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-02 Intent](../../data/e-f16-02-intent.md),
[E-F16-10 Intent candidate](../../data/e-f16-10-intent-candidate.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-02 Intent | New | Badge "New"; a new record starts here; next: Accepted (UC-F16-14); fields editable within the role | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-02-intent-new-{desktop,phone}-{light,dark}.png` |
| E-F16-02 Intent | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-02-intent-accepted-{desktop,phone}-{light,dark}.png` |
| E-F16-10 Intent candidate | Proposed | Badge "Proposed"; a new record starts here; next: Accepted, Merged or Dismissed (UC-F16-14); fields editable within the role | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-10-intent-candidate-proposed-{desktop,phone}-{light,dark}.png` |
| E-F16-10 Intent candidate | Accepted | Badge "Accepted"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-10-intent-candidate-accepted-{desktop,phone}-{light,dark}.png` |
| E-F16-10 Intent candidate | Merged | Badge "Merged"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-10-intent-candidate-merged-{desktop,phone}-{light,dark}.png` |
| E-F16-10 Intent candidate | Dismissed | Badge "Dismissed"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-12-intent-discovery-e-f16-10-intent-candidate-dismissed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-02 Automate an intent](../../flows/fl-f16-02-automate-an-intent.md)

## Open questions

None.

---

⬅️ [S-F16-11 My requests](../05-customer-side/s-f16-11-my-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-13 Fraud signals](../03-review-and-monitor/s-f16-13-fraud-signals.md)
