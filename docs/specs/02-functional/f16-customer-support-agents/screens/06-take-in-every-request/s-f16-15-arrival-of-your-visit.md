🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-06 Take in every request](README.md) › 🖥️ S-F16-15 Arrival of your visit

# 🖥️ S-F16-15 Arrival of your visit

**Status:** 🔄 draft (GH-2 step S4b, from VD-20, VD-21 / D502, D503)

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md): their own visit only.

## Purpose

Tell the customer the day and window of their visit, then, during the window, the expected arrival time.

## Entry points

The link in the scheduling message (email or SMS); the customer portal › My requests › the request.

## Wireframe

A customer-facing page; the exception to the map right by nature (VD-20). The map follows
[C-17 Map](../../../../04-ux/design-system/components/c-17-map.md) and shows a small map near the customer's address
(D517);
the employee's position and route are never drawn.

```text
Phone, before the window:              Phone, during the window:
+--------------------------------+     +--------------------------------+
| Your visit                     |     | Your visit                     |
| Bathing help                   |     | Bathing help                   |
| Tuesday 9 December             |     | Arriving at about 08:20        |
| between 08:00 and 09:00        |     | (window 08:00 to 09:00)        |
| Lea will come                  |     | [ map: your address only ]     |
| [Change the time] [Cancel]     |     | [Call us]                      |
+--------------------------------+     +--------------------------------+
After check-in: "Arrived at 08:22".  After check-out: "Done at 09:05".
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F9-12 step 10, U09 | phone | ![FL-F9-12 step 10, U09, light](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u09-customer/10-arrival-of-your-visit-phone-light.png) | ![FL-F9-12 step 10, U09, dark](../../../f09-hr-and-projects/images/12-schedule-customer-requests/u09-customer/10-arrival-of-your-visit-phone-dark.png) |
| Error E4, U09 | phone | ![Error E4, U09, light](../../images/06-take-in-every-request/u09-customer/e4-the-arrival-link-has-expired-phone-light.png) | ![Error E4, U09, dark](../../images/06-take-in-every-request/u09-customer/e4-the-arrival-link-has-expired-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-15-arrival-of-your-visit-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-15-arrival-of-your-visit-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-15-arrival-of-your-visit-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-15-arrival-of-your-visit-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-15-arrival-of-your-visit-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-15-arrival-of-your-visit-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-15-arrival-of-your-visit-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-15-arrival-of-your-visit-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Service | E-F16-12 request type | name | no | yes |
| Day and window | E-F16-12 scheduled window | day, times | through "Change the time" | yes |
| Arrival time | computed from E-F9-26 and E-F9-32 | "about hh:mm" | no | during the window only |
| Person coming | E-F16-12 assigned person | first name (D517) | no | no |
| State | E-F16-12 state | Scheduled, Arrived, Done, Cancelled | no | yes |

## Actions

| Action | Where | Who may use it | Result |
|---|---|---|---|
| Change the time | before the window | the customer | message to the planner; re-planned (UC-F9-35) |
| Cancel | before the window | the customer | work request cancelled, round ordered again |
| Call us | always | the customer | the company's phone number |

## States

- Normal: the day and the window; during the window, the arrival time.
- Empty: not used; a link always concerns one visit.
- Loading: the frame with the day shows at once; the arrival time follows.
- Error: an expired or wrong link shows the visit's state only, with the sign-in to the portal (D122).
- Read-only: after check-out, "Done"; no action.
- Offline: not available offline: a page served live
  ([D407](../../../../06-decisions/technical/d407-front-end.md)).

Shown entities (VD-15): [E-F16-12 Work request](../../data/e-f16-12-work-request.md),
[E-F9-32 Live position](../../../f09-hr-and-projects/data/e-f09-32-live-position.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-12 Work request | Scheduled, before the window | Day and window; Change the time, Cancel | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f16-12-work-request-scheduled-before-the-window-phone-{light,dark}.png` |
| E-F16-12 Work request | Scheduled, during the window | Arrival time, the map of the address; Call us only | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f16-12-work-request-scheduled-during-the-window-phone-{light,dark}.png` |
| E-F16-12 Work request | In progress | "Arrived at hh:mm" | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f16-12-work-request-in-progress-phone-{light,dark}.png` |
| E-F16-12 Work request | Done | "Done at hh:mm"; read-only | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f16-12-work-request-done-phone-{light,dark}.png` |
| E-F16-12 Work request | Cancelled | "Cancelled", the date; read-only | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f16-12-work-request-cancelled-phone-{light,dark}.png` |
| E-F9-32 Live position | Sharing, Paused or Off | Not shown; only the arrival time's precision changes | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f09-32-live-position-sharing-paused-or-off-phone-{light,dark}.png` |
| E-F9-32 Live position | Off | Badge "Off"; a new record starts here; next: Sharing or Erased (BR-F9-30, BR-F9-31); fields editable within the role | U09 | `u09-customer/s-f16-15-arrival-of-your-visit-e-f09-32-live-position-off-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first (D34); on desktop the same card, centred.

## Accessibility

The arrival time is text, announced when it changes; the map is decorative and has a text alternative (the address);
buttons have labels.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-17 Map](../../../../04-ux/design-system/components/c-17-map.md)
- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)

## Shown in

- [FL-F16-06 Take in every request](../../flows/fl-f16-06-take-in-every-request.md)
- [FL-F9-12 Schedule customer requests](../../../f09-hr-and-projects/flows/fl-f09-12-schedule-customer-requests.md)

## Open questions

None.

---

⬅️ [S-F16-14 Work requests](s-f16-14-work-requests.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-16 Forum](../07-live-chat-voice-and-contracts/s-f16-16-forum.md)
