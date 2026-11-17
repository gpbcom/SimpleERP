🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-04 Human agent workspace](README.md) › 🖥️ S-F16-08 Agent workspace

# 🖥️ S-F16-08 Agent workspace

**Status:** ✅ specified

## Personas

- [U16 Office worker](../../../../01-users/personas/u16-office-worker.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Answer the requests routed to people with their history, macros, translations and clocks, one person at a time.

## Entry points

Support menu, Workspace; an assignment notification.

## Wireframe

```text
Workspace   Queues: [Refunds 6] [Spanish 2] [All mine 8]
-------------------------------------------------------------------------------
5512  late-delivery refund  es  40 min left   [Ana answering]
5530  duplicate charge       fr  breached
-------------------------------------------------------------------------------
Request 5512   original (es) | translation (fr)     Agent notes: refund 40 EUR due
History: order 1188, delivered 3 days late
[Macro v] [Refund] [Send] [Resolve]          Customer: Lucia G., 3rd request
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-04 step 2, U16 | desktop | ![FL-F16-04 step 2, U16, light](../../images/04-human-agent-workspace/u16-office-worker/2-agent-workspace-desktop-light.png) | ![FL-F16-04 step 2, U16, dark](../../images/04-human-agent-workspace/u16-office-worker/2-agent-workspace-desktop-dark.png) |
| FL-F16-04 step 2, U16 | phone | ![FL-F16-04 step 2, U16, light](../../images/04-human-agent-workspace/u16-office-worker/2-agent-workspace-phone-light.png) | ![FL-F16-04 step 2, U16, dark](../../images/04-human-agent-workspace/u16-office-worker/2-agent-workspace-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-08-agent-workspace-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-08-agent-workspace-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-08-agent-workspace-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-08-agent-workspace-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-08-agent-workspace-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-08-agent-workspace-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-08-agent-workspace-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-08-agent-workspace-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Request | E-F16-01 | number, intent, language | no | yes |
| Clock | E-F16-05 | time left | no | yes |
| Lock | E-F16-01 | who answers | no | no |
| Answer | E-F16-01 answer | text | yes | yes |
| Macro | E-F16-07 | title | yes | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Open | list | office worker | locked to them |
| Insert macro | answer | office worker | text filled |
| Act | toolbar | office worker | refund or re-send within limits |
| Send and resolve | toolbar | office worker | answer sent, survey goes out |
| Take over | locked request | support lead | lock moved to the lead |

## States

- Normal: queues, the open request with history, notes, translation and clock.
- Empty: "No request waiting": shown when every queue is empty.
- Loading: the frame and titles show at once with placeholder rows for the requests; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a duplicate action refused, or an action above its limit waiting for approval.
- Read-only: a request locked by someone else, or resolved, is read-only.
- Offline: The requests last loaded stay readable; answers are sent only online. Nothing else is queued: D38 keeps only
  today's schedule, time and intervention records offline; a banner says the connection is lost and the actions come
  back with it.

Shown entities (VD-15): [E-F16-01 Customer request](../../data/e-f16-01-customer-request.md),
[E-F16-06 Queue](../../data/e-f16-06-queue.md), [E-F16-07 Macro](../../data/e-f16-07-macro.md),
[E-F16-05 Service-level policy](../../data/e-f16-05-service-level-policy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-01 Customer request | New | Badge "New"; a new record starts here; next: In progress (UC-F16-12); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-01-customer-request-new-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | In progress | Badge "In progress"; next: Resolved or Waiting (UC-F16-01, UC-F16-07); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-01-customer-request-in-progress-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Resolved | Badge "Resolved"; next: Escalated (UC-F16-04); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-01-customer-request-resolved-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Waiting | Badge "Waiting"; next: Resolved (UC-F16-01); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-01-customer-request-waiting-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Escalated | Badge "Escalated"; next: Resolved (UC-F16-01); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-01-customer-request-escalated-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png` |
| E-F16-06 Queue | Open | Badge "Open"; a new record starts here; next: Paused or Closed (UC-F16-08); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-06-queue-open-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-06-queue-open-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-06-queue-open-{desktop,phone}-{light,dark}.png` |
| E-F16-06 Queue | Paused | Badge "Paused"; next: Open (UC-F16-08); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-06-queue-paused-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-06-queue-paused-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-06-queue-paused-{desktop,phone}-{light,dark}.png` |
| E-F16-07 Macro | Active | Badge "Active"; a new record starts here; next: Archived (UC-F16-08); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-07-macro-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-07-macro-active-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-07-macro-active-{desktop,phone}-{light,dark}.png` |
| E-F16-07 Macro | Archived | Badge "Archived"; final: read-only, no next state; the history shows how it got here | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-07-macro-archived-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-07-macro-archived-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-07-macro-archived-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Active | Badge "Active"; a new record starts here; next: Changed or Retired (UC-F16-05); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-05-service-level-policy-active-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-05-service-level-policy-active-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-05-service-level-policy-active-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Changed | Badge "Changed"; next: Active (UC-F16-07); fields editable within the role | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-05-service-level-policy-changed-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-05-service-level-policy-changed-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-05-service-level-policy-changed-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U02, U09, U16 | `u02-manager/s-f16-08-agent-workspace-e-f16-05-service-level-policy-retired-{desktop,phone}-{light,dark}.png`, `u09-customer/s-f16-08-agent-workspace-e-f16-05-service-level-policy-retired-phone-{light,dark}.png`, `u16-office-worker/s-f16-08-agent-workspace-e-f16-05-service-level-policy-retired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; on a phone the list and one request at a time.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-07 Tabs](../../../../04-ux/design-system/components/c-07-tabs.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-11 Chat panel](../../../../04-ux/design-system/components/c-11-chat-panel.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-04 Human agent workspace](../../flows/fl-f16-04-human-agent-workspace.md)

## Open questions

None.

---

⬅️ [S-F16-07 Service levels](s-f16-07-service-levels.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-09 Satisfaction survey](../05-customer-side/s-f16-09-satisfaction-survey.md)
