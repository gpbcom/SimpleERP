🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-05 Customer side](README.md) › 🖥️ S-F16-09 Satisfaction survey

# 🖥️ S-F16-09 Satisfaction survey

**Status:** ✅ specified

## Personas

- [U09 Customer](../../../../01-users/personas/u09-customer.md), who rates
- [U02 Manager](../../../../01-users/personas/u02-manager.md), who reads the results on the dashboard

## Purpose

Let the customer rate a resolved request in one tap.

## Entry points

The link in the resolution message; the chat after the answer.

## Wireframe

```text
How did we do with your request 5512?
-------------------------------------------------------------------------------
[1] [2] [3] [4] [5]
Tell us more (optional): [                                         ]
                                                               [Send]
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-05 step 4, U09 | phone | ![FL-F16-05 step 4, U09, light](../../images/05-customer-side/u09-customer/4-satisfaction-survey-phone-light.png) | ![FL-F16-05 step 4, U09, dark](../../images/05-customer-side/u09-customer/4-satisfaction-survey-phone-dark.png) |
| Empty | phone | ![Empty, light](../../images/states/s-f16-09-satisfaction-survey-empty-phone-light.png) | ![Empty, dark](../../images/states/s-f16-09-satisfaction-survey-empty-phone-dark.png) |
| Loading | phone | ![Loading, light](../../images/states/s-f16-09-satisfaction-survey-loading-phone-light.png) | ![Loading, dark](../../images/states/s-f16-09-satisfaction-survey-loading-phone-dark.png) |
| Read-only | phone | ![Read-only, light](../../images/states/s-f16-09-satisfaction-survey-read-only-phone-light.png) | ![Read-only, dark](../../images/states/s-f16-09-satisfaction-survey-read-only-phone-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-09-satisfaction-survey-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-09-satisfaction-survey-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Score | E-F16-08 score | 1 to 5 | yes | yes |
| Comment | E-F16-08 comment | text, 500 characters | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Send | footer | customer | rating recorded |

## States

- Normal: the five scores and the comment field.
- Empty: never empty: it opens from a resolved request.
- Loading: the frame and titles show at once with placeholder rows for the survey; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: an expired link, with "nothing was recorded".
- Read-only: a rating already sent shows read-only with "Thank you".
- Offline: The survey stays on screen; sending needs the network. Nothing else is queued: D38 keeps only today's
  schedule, time and intervention records offline; a banner says the connection is lost and the actions come back with
  it.

Shown entities (VD-15): [E-F16-08 Satisfaction rating](../../data/e-f16-08-satisfaction-rating.md),
[E-F16-01 Customer request](../../data/e-f16-01-customer-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-08 Satisfaction rating | Asked | Badge "Asked"; a new record starts here; next: Answered or Expired (UC-F16-01, UC-F16-09); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-08-satisfaction-rating-asked-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-08-satisfaction-rating-asked-phone-{light,dark}.png` |
| E-F16-01 Customer request | New | Badge "New"; a new record starts here; next: In progress (UC-F16-12); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-01-customer-request-new-phone-{light,dark}.png` |
| E-F16-01 Customer request | In progress | Badge "In progress"; next: Resolved or Waiting (UC-F16-01, UC-F16-07); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-01-customer-request-in-progress-phone-{light,dark}.png` |
| E-F16-01 Customer request | Resolved | Badge "Resolved"; next: Escalated (UC-F16-04); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-01-customer-request-resolved-phone-{light,dark}.png` |
| E-F16-01 Customer request | Waiting | Badge "Waiting"; next: Resolved (UC-F16-01); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-01-customer-request-waiting-phone-{light,dark}.png` |
| E-F16-01 Customer request | Escalated | Badge "Escalated"; next: Resolved (UC-F16-01); fields editable within the role | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-01-customer-request-escalated-phone-{light,dark}.png` |
| E-F16-08 Satisfaction rating | Expired | Badge "Expired"; final: read-only, no next state; the history shows how it got here | U02, U09 | `u02-manager/s-f16-09-satisfaction-survey-e-f16-08-satisfaction-rating-expired-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-09-satisfaction-survey-e-f16-08-satisfaction-rating-expired-phone-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Phone first; same layout on desktop.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-01 Button](../../../../04-ux/design-system/components/c-01-button.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-05 Customer side](../../flows/fl-f16-05-customer-side.md)

## Open questions

None.

---

⬅️ [S-F16-08 Agent workspace](../04-human-agent-workspace/s-f16-08-agent-workspace.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-10 Help centre](s-f16-10-help-centre.md)
