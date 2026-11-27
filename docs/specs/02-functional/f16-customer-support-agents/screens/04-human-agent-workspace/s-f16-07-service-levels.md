🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🎧 [F16 Customer support agents](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F16-04 Human agent workspace](README.md) › 🖥️ S-F16-07 Service levels

# 🖥️ S-F16-07 Service levels

**Status:** ✅ specified

## Personas

- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Define service-level policies and see requests near or past their targets.

## Entry points

Support settings, Service levels; the breach notification.

## Wireframe

```text
Service levels                                               [New policy]
-------------------------------------------------------------------------------
Policy    Priority   First response   Resolution   Hours            Met (30 d)
Normal    normal     4 h              16 h         Mon-Fri 9-18     94 %
Urgent    urgent     1 h              8 h          Mon-Sun 8-20     88 %
-------------------------------------------------------------------------------
Near breach: 5512 (40 min), 5530 (breached 1 h ago)
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F16-04 step 1, U02 | desktop | ![FL-F16-04 step 1, U02, light](../../images/04-human-agent-workspace/u02-manager/1-service-levels-desktop-light.png) | ![FL-F16-04 step 1, U02, dark](../../images/04-human-agent-workspace/u02-manager/1-service-levels-desktop-dark.png) |
| FL-F16-04 step 1, U02 | phone | ![FL-F16-04 step 1, U02, light](../../images/04-human-agent-workspace/u02-manager/1-service-levels-phone-light.png) | ![FL-F16-04 step 1, U02, dark](../../images/04-human-agent-workspace/u02-manager/1-service-levels-phone-dark.png) |
| Error E1, U02 | desktop | ![Error E1, U02, light](../../images/04-human-agent-workspace/u02-manager/e1-service-levels-refused-desktop-light.png) | ![Error E1, U02, dark](../../images/04-human-agent-workspace/u02-manager/e1-service-levels-refused-desktop-dark.png) |
| Error E1, U02 | phone | ![Error E1, U02, light](../../images/04-human-agent-workspace/u02-manager/e1-service-levels-refused-phone-light.png) | ![Error E1, U02, dark](../../images/04-human-agent-workspace/u02-manager/e1-service-levels-refused-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f16-07-service-levels-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f16-07-service-levels-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f16-07-service-levels-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f16-07-service-levels-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f16-07-service-levels-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f16-07-service-levels-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f16-07-service-levels-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f16-07-service-levels-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Policy | E-F16-05 name | text | yes | yes |
| Priority | E-F16-05 priority | list | yes | yes |
| First response | E-F16-05 first response | duration | yes | yes |
| Resolution | E-F16-05 resolution | duration | yes | yes |
| Hours | E-F16-05 business hours | text | yes | yes |
| Met | computed | percent | no | no |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| New policy | header | support lead | policy created |
| Edit | row | support lead | new targets from a date |
| Open request | near-breach list | support lead | the request in the workspace |

## States

- Normal: policies with their targets and share met, and the requests near breach.
- Empty: "No service level yet": requests have no clock until a policy exists.
- Loading: the frame and titles show at once with placeholder rows for the policies; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a resolution target shorter than the first response, next to the field.
- Read-only: office workers and the owner read policies; only the lead edits.
- Offline: not available offline: policies are set on the server. D38 keeps only today's schedule, time and intervention
  records offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and
  nothing is queued until the connection is back.

Shown entities (VD-15): [E-F16-01 Customer request](../../data/e-f16-01-customer-request.md),
[E-F16-05 Service-level policy](../../data/e-f16-05-service-level-policy.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F16-01 Customer request | New | Badge "New"; a new record starts here; next: In progress (UC-F16-12); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-01-customer-request-new-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | In progress | Badge "In progress"; next: Resolved or Waiting (UC-F16-01, UC-F16-07); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-01-customer-request-in-progress-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Resolved | Badge "Resolved"; next: Escalated (UC-F16-04); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-01-customer-request-resolved-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Waiting | Badge "Waiting"; next: Resolved (UC-F16-01); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-01-customer-request-waiting-{desktop,phone}-{light,dark}.png` |
| E-F16-01 Customer request | Escalated | Badge "Escalated"; next: Resolved (UC-F16-01); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-01-customer-request-escalated-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Active | Badge "Active"; a new record starts here; next: Changed or Retired (UC-F16-05); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-05-service-level-policy-active-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Changed | Badge "Changed"; next: Active (UC-F16-07); fields editable within the role | U02 | `u02-manager/s-f16-07-service-levels-e-f16-05-service-level-policy-changed-{desktop,phone}-{light,dark}.png` |
| E-F16-05 Service-level policy | Retired | Badge "Retired"; final: read-only, no next state; the history shows how it got here | U02 | `u02-manager/s-f16-07-service-levels-e-f16-05-service-level-policy-retired-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the near-breach list on a phone.

## Accessibility

Keyboard order follows the reading order; every control has a visible label; amounts, states and icons are also given as
text; status changes are announced to screen readers.

## Components

- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)
- [C-02 Form field](../../../../04-ux/design-system/components/c-02-form-field.md)
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F16-04 Human agent workspace](../../flows/fl-f16-04-human-agent-workspace.md)

## Open questions

None.

---

⬅️ [S-F16-06 Support connections](../01-resolve-a-request/s-f16-06-support-connections.md) · ⬆️ [Up](README.md) ·
➡️ [S-F16-08 Agent workspace](s-f16-08-agent-workspace.md)
