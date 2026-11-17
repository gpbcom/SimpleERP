🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
🤖 [F25 DevOps agents (hosted edition)](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F25-02 Feature requests](README.md) › 🖥️ S-F25-23 Spec checks

# 🖥️ S-F25-23 Spec checks

**Status:** ✅ specified

## Personas

- [U47 simple-ERP maintainer](../../../../01-users/personas/u47-simple-erp-maintainer.md)

## Purpose

Show the checks of an agent's spec pull request.

## Entry points

The pull request's check; maintainer space.

## Wireframe

```text
Spec checks, PR 418                      Result: back to the agent
-------------------------------------------------------------------------------
Unsourced: "within 48 hours" (uc-f06-04, Main flow 3)
Contradiction: "seats per user" contradicts D443
Tools: links ok, templates ok, prose ok, coverage ok
```

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F25-02 step 4, U47 | desktop | ![FL-F25-02 step 4, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/4-spec-checks-desktop-light.png) | ![FL-F25-02 step 4, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/4-spec-checks-desktop-dark.png) |
| FL-F25-02 step 4, U47 | phone | ![FL-F25-02 step 4, U47, light](../../images/02-feature-requests/u47-simple-erp-maintainer/4-spec-checks-phone-light.png) | ![FL-F25-02 step 4, U47, dark](../../images/02-feature-requests/u47-simple-erp-maintainer/4-spec-checks-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f25-23-spec-checks-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f25-23-spec-checks-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f25-23-spec-checks-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f25-23-spec-checks-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f25-23-spec-checks-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f25-23-spec-checks-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f25-23-spec-checks-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f25-23-spec-checks-offline-phone-dark.png) |

## Fields and columns

| Label | Data | Format | Editable | Required |
|---|---|---|---|---|
| Unsourced | E-F25-13 unsourced | list | no | no |
| Contradictions | E-F25-13 contradictions | list | no | no |
| Tool checks | E-F25-13 tool checks | list | no | yes |

## Actions

| Action | Where | Who | Result |
|---|---|---|---|
| Re-run | header | maintainer | checks run |

## States

- Normal: findings and result.
- Empty: "All checks passed".
- Loading: the frame and titles show at once with placeholder rows for the findings; within 1 second (D408) the data
  replaces them, and a longer load shows a progress line saying what loads.
- Error: a check that could not run, retried.
- Read-only: always read-only.
- Offline: not available offline: checks run online. D38 keeps only today's schedule, time and intervention records
  offline. A banner says the connection is lost; what is on screen stays visible, every action is disabled and nothing
  is queued until the connection is back.

Shown entities (VD-15): [E-F25-05 Agent pull request](../../data/e-f25-05-agent-pull-request.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F25-05 Agent pull request | In review | Badge "In review"; a new record starts here; next: Proposed or Declined (UC-F25-06, UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-23-spec-checks-e-f25-05-agent-pull-request-in-review-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Proposed | Badge "Proposed"; next: Checked or Declined (UC-F25-06, UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-23-spec-checks-e-f25-05-agent-pull-request-proposed-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Declined | Badge "Declined"; final: read-only, no next state; the history shows how it got here | U47 | `u47-simple-erp-maintainer/s-f25-23-spec-checks-e-f25-05-agent-pull-request-declined-{desktop,phone}-{light,dark}.png` |
| E-F25-05 Agent pull request | Checked | Badge "Checked"; next: Open or Declined (UC-F25-23); fields editable within the role | U47 | `u47-simple-erp-maintainer/s-f25-23-spec-checks-e-f25-05-agent-pull-request-checked-{desktop,phone}-{light,dark}.png` |

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
- [C-10 Empty state](../../../../04-ux/design-system/components/c-10-empty-state.md)

## Shown in

- [FL-F25-02 Feature requests](../../flows/fl-f25-02-feature-requests.md)

## Open questions

None.

---

⬅️ [S-F25-22 Vulnerability case](../06-vulnerability-handling/s-f25-22-vulnerability-case.md) · ⬆️ [Up](README.md) ·
➡️ [S-F25-24 Public requests](../05-tell-the-customer/s-f25-24-public-requests.md)
