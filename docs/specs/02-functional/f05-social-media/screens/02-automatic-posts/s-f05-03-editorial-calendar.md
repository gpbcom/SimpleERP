🏠 [Specs](../../../../README.md) › 🧩 [Functional capabilities](../../../README.md) ›
📣 [F5 Social media and marketing](../../README.md) › 🖥️ [Screens](../README.md) ›
🖥️ [Screens: FL-F5-02 Automatic posts](README.md) › 🖥️ S-F5-03 Editorial calendar

# 🖥️ S-F5-03 Editorial calendar

**Status:** ✅ specified

## Personas

- [U12 Marketing](../../../../01-users/personas/u12-marketing.md)
- [U07 Administrator](../../../../01-users/personas/u07-administrator.md)

## Purpose

Set up automatic posts.

## Entry points

Social media in the menu.

## Wireframe

See the images in the flow page (D120).

**Example images** (as drawn in its flow, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| FL-F5-02 step 1, U12 | desktop | ![FL-F5-02 step 1, U12, light](../../images/02-automatic-posts/u12-marketing/1-automatic-rule-desktop-light.png) | ![FL-F5-02 step 1, U12, dark](../../images/02-automatic-posts/u12-marketing/1-automatic-rule-desktop-dark.png) |
| Error E1, U12 | desktop | ![Error E1, U12, light](../../images/02-automatic-posts/u12-marketing/e1-held-blocked-word-desktop-light.png) | ![Error E1, U12, dark](../../images/02-automatic-posts/u12-marketing/e1-held-blocked-word-desktop-dark.png) |
| Error E1, U12 | phone | ![Error E1, U12, light](../../images/02-automatic-posts/u12-marketing/e1-held-blocked-word-phone-light.png) | ![Error E1, U12, dark](../../images/02-automatic-posts/u12-marketing/e1-held-blocked-word-phone-dark.png) |
| Empty | desktop | ![Empty, light](../../images/states/s-f05-03-editorial-calendar-empty-desktop-light.png) | ![Empty, dark](../../images/states/s-f05-03-editorial-calendar-empty-desktop-dark.png) |
| Loading | desktop | ![Loading, light](../../images/states/s-f05-03-editorial-calendar-loading-desktop-light.png) | ![Loading, dark](../../images/states/s-f05-03-editorial-calendar-loading-desktop-dark.png) |
| Read-only | desktop | ![Read-only, light](../../images/states/s-f05-03-editorial-calendar-read-only-desktop-light.png) | ![Read-only, dark](../../images/states/s-f05-03-editorial-calendar-read-only-desktop-dark.png) |
| Offline | phone | ![Offline, light](../../images/states/s-f05-03-editorial-calendar-offline-phone-light.png) | ![Offline, dark](../../images/states/s-f05-03-editorial-calendar-offline-phone-dark.png) |

## Fields and columns

As its use case.

## Actions

As its use case's main flow.

## States

- Normal: Set up automatic posts, as the wireframe shows.
- Empty: No post planned this month yet, with Plan a post.
- Loading: skeleton rows in place of the list ([C-03](../../../../04-ux/design-system/components/c-03-data-table.md));
  actions are disabled until it has loaded.
- Error: the error message pattern (D122).
- Read-only: for users without the marketing right; published items.
- Offline: Not available offline: a back-office screen on live, shared data (D38: only today's schedule, time and
  intervention records work offline). The app shows that it is offline and reloads the screen when the network is back.

Shown entities (VD-15): none; no flow's Entities and screens table names an entity on this screen.

## Responsive behaviour

Desktop; the inbox and approvals also on the phone.

## Accessibility

Labelled controls; states as text.

## Components

- [C-04 Card](../../../../04-ux/design-system/components/c-04-card.md)
- [C-03 Data table](../../../../04-ux/design-system/components/c-03-data-table.md)

## Shown in

- [FL-F5-02 Automatic posts](../../flows/fl-f05-02-automatic-posts.md)

## Open questions

None.

---

⬅️ [S-F5-02 Approval](../01-publish-a-post/s-f05-02-approval.md) · ⬆️ [Up](README.md) ·
➡️ [S-F5-04 Automatic post rules](../01-publish-a-post/s-f05-04-automatic-post-rules.md)
