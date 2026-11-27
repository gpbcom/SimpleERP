🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-03 Review and monitor](README.md) › 🖥️ S-F16-13 Fraud signals

# 🖥️ S-F16-13 Fraud signals

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md), who decides
- [U02 Manager](../../../../01-users/personas/u02-manager.md), who sets thresholds

## Purpose

Show held refunds with their signals and evidence, for a person to clear or confirm.

## Entry points

Support menu, Fraud signals; the held-refund notification.

## Wireframe

```text
Fraud signals                               Held: 3     Thresholds [Edit]
-------------------------------------------------------------------------------
Request  Customer   Signal                     Evidence             Amount
5601     884        refund rate                4 refunds in 60 d    60.00
5622     902        contradicting proof        signed delivery      129.00
-------------------------------------------------------------------------------
[Clear and refund] [Confirm abuse]   reason: [              ]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-03 step 4, U16 | desktop | ![FL-F16-03 step 4, U16, light](../../images/03-review-and-monitor/u16-office-worker/4-fraud-signals-desktop-light.png) | ![FL-F16-03 step 4, U16, dark](../../images/03-review-and-monitor/u16-office-worker/4-fraud-signals-desktop-dark.png) |
| FL-F16-03 step 4, U16 | phone | ![FL-F16-03 step 4, U16, light](../../images/03-review-and-monitor/u16-office-worker/4-fraud-signals-phone-light.png) | ![FL-F16-03 step 4, U16, dark](../../images/03-review-and-monitor/u16-office-worker/4-fraud-signals-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-13-fraud-signals-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-13-fraud-signals-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-13-fraud-signals-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-13-fraud-signals-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-13-fraud-signals-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-13-fraud-signals-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-13-fraud-signals-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-13-fraud-signals-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F16-11 request | number | no | yes |
| Signal | E-F16-11 kind | list | no | yes |
| Evidence | E-F16-11 evidence | text | no | yes |
| Decision | E-F16-11 decision | genuine, abuse | yes | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Clear and refund | row | office worker | refund goes |
| Confirm abuse | row | office worker | refused with the reason |
| Edit thresholds | header | support lead | thresholds saved |

## States

- Normal: held refunds with signals and evidence.
- Empty: "No refund held".
- Loading: the frame and titles show at once with placeholder rows for the held refunds; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a decision without a reason, refused.
- Read-only: the owner reads; decided signals are read-only.
- Offline: not available offline: evidence is read from back-office tools. D38 keeps only today's schedule, time and
  intervention records offline. A banner says the connection is lost; what is on screen stays visible, every action is
  disabled and nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-11 Fraud signal](../../data/e-f16-11-fraud-signal.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-11 Fraud signal | Raised | Badge "Raised"; a new record starts here; next: Cleared or Confirmed (UC-F16-15); fields editable within the role | U02, U16 | `u02-manager/s-f16-13-fraud-signals-e-f16-11-fraud-signal-raised-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f16-13-fraud-signals-e-f16-11-fraud-signal-raised-{desktop,phone}-{light,dark}.png` |
| E-F16-11 Fraud signal | Cleared | Badge "Cleared"; final: read-only, no next state; the history shows how it got here | U02, U16 | `u02-manager/s-f16-13-fraud-signals-e-f16-11-fraud-signal-cleared-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f16-13-fraud-signals-e-f16-11-fraud-signal-cleared-{desktop,phone}-{light,dark}.png` |
| E-F16-11 Fraud signal | Confirmed | Badge "Confirmed"; final: read-only, no next state; the history shows how it got here | U02, U16 | `u02-manager/s-f16-13-fraud-signals-e-f16-11-fraud-signal-confirmed-{desktop,phone}-{light,dark}.png`, `u16-office-worker/s-f16-13-fraud-signals-e-f16-11-fraud-signal-confirmed-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; tablet.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-03 Review and monitor](../../flows/fl-f16-03-review-and-monitor.md)

## Open questions

None.

---

⬅️ [S-F16-12 Intent discovery](../02-automate-an-intent/s-f16-12-intent-discovery.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-14 Work requests](../06-take-in-every-request/s-f16-14-work-requests.md)
