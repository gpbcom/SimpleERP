🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-01 Publish a post](README.md) › 🖥️ S-F5-02 Approval

# 🖥️ S-F5-02 Approval

**Status:** ✅ specified

## Personas

- [U13 Owner](../../../../01-users/personas/u13-owner.md)
- [U02 Manager](../../../../01-users/personas/u02-manager.md)

## Purpose

Approve a post.

## Entry points

Social media in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-01 step 2, U13 | desktop | ![FL-F5-01 step 2, U13, light](../../images/01-publish-a-post/u13-owner/2-approve-desktop-light.png) | ![FL-F5-01 step 2, U13, dark](../../images/01-publish-a-post/u13-owner/2-approve-desktop-dark.png) |
| FL-F5-01 step 2, U13 | phone | ![FL-F5-01 step 2, U13, light](../../images/01-publish-a-post/u13-owner/2-approve-phone-light.png) | ![FL-F5-01 step 2, U13, dark](../../images/01-publish-a-post/u13-owner/2-approve-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-02-approval-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-02-approval-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-02-approval-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-02-approval-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-02-approval-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-02-approval-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-02-approval-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-02-approval-offline-phone-dark.png) |

## Fields and columns

As its use case.

## Actions

As its use case's main flow.

## States

- Normal: Approve a post, as the wireframe shows.
- Empty: No post waiting for approval yet, with Nothing waits.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline (D38): on a phone or a computer, the offline banner replaces the actions and nothing is
  changed until the network is back; nothing is queued.

Shown entities (VD-15): [E-F5-01 Post](../../data/e-f05-01-post.md).

Entity states shown (VD-15):

| Entity | State | What changes | Personas | Images |
|---|---|---|---|---|
| E-F5-01 Post | Draft | Badge "Draft"; a new record starts here; next: To approve or Refused (UC-F5-01, UC-F5-02); fields editable within the role | U13 | `u13-owner/s-f05-02-approval-e-f05-01-post-draft-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | To approve | Badge "To approve"; next: Scheduled or Refused (UC-F5-01, UC-F5-02); fields editable within the role | U13 | `u13-owner/s-f05-02-approval-e-f05-01-post-to-approve-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Published | Badge "Published"; next: Held (UC-F5-03); fields editable within the role | U13 | `u13-owner/s-f05-02-approval-e-f05-01-post-published-{desktop,phone}-{light,dark}.png` |
| E-F5-01 Post | Held | Badge "Held"; next: Published (UC-F5-01); fields editable within the role | U13 | `u13-owner/s-f05-02-approval-e-f05-01-post-held-{desktop,phone}-{light,dark}.png` |

State images: each name is a file under the capability's `images/states/` folder, one per device and theme the braces
list; step S8 (36k) draws them, and a system state has none. Rows without a hand-written text are derived from each
entity's Lifecycle (step 36j): the badge is the state's name, the next states are its transitions, and a final state is
read-only.

## Responsive behaviour

Desktop; the inbox and approvals also on the phone.

## Accessibility

Labelled controls; states as text.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F5-01 Publish a post](../../flows/fl-f05-01-publish-a-post.md)

## Open questions

None.

---

⬅️ [S-F5-01 Post composer](s-f05-01-post-composer.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-03 Editorial calendar](../02-automatic-posts/s-f05-03-editorial-calendar.md)
