🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-04 Card

# 🧩 C-04 Card

**Status:** 🔄 waiting for the owner

## Purpose

Groups what belongs together in one block: a widget of the home screen
([D48](../../../06-decisions/ux/d48-home-screen.md)), a figure, an answer or a warning of the legal assistant, an item
of a gallery, a record in a list on a phone.

## Anatomy

```text
+----------------------------------+
| Days off left                    |  <- title
| 12.5                             |  <- content
| Next: 23 Dec to 2 Jan            |
|                 [Request time off]|  <- actions (optional)
+----------------------------------+
```

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-04-card-desktop-light.png) | ![Variants and states, dark](../images/c-04-card-desktop-dark.png) |

## Variants

- **Content card:** a title, its content and up to two actions.
- **Figure card:** a dashboard figure in Plus Jakarta Sans ([Typography](../../visual-identity/typography.md)) with its
  label and change.
- **Selectable card:** (Proposed) a choice among a few, such as a record type model, as on
  [S-F2-05 Record type gallery](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-05-record-type-gallery.md);
  it works as a radio button or a checkbox.
- **Phone card:** a record of a list on a phone, as on
  [S-F2-04 List view settings](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-04-list-view-settings.md).

## States

| State | Look |
|---|---|
| Default | `color-surface`, `color-border` edge, `elevation-1` |
| Hover | (Proposed) For a clickable card only: the edge in `color-border-strong` |
| Focus | The `color-primary` focus ring around the card |
| Selected | (Proposed) A 2 px `color-primary` edge and a check icon |
| Loading | (Proposed) Skeleton lines in place of the content |
| Empty | A short [C-10 Empty state](c-10-empty-state.md) inside the card |
| Error | The [error message pattern](../patterns/error-messages.md), inside the card |

## Tokens

`color-surface`, `color-border`, radius 8 px for cards and `elevation-1` ([Tokens](../tokens.md)); in dark mode,
elevation is a lighter surface. Padding (Proposed): 24 px on a desktop, 16 px on a phone, from the 4 px spacing grid.
The images draw cards with a 12 px radius and 20 px padding; (Proposed) the tokens' 8 px applies when the images are
next regenerated.

## Accessibility

- A card has a heading, so screen-reader users can jump between cards.
- A clickable card holds one link (its title); other actions are separate buttons, never nested in the link.
- A selectable card has the semantics of a radio button or a checkbox.

## Do and don't

- Do keep one subject per card.
- Do put the role's widgets after "My tasks" on the home screen ([D48](../../../06-decisions/ux/d48-home-screen.md)).
- Don't nest cards in cards.
- Don't use cards for long lists on a desktop: use a [C-03 Data table](c-03-data-table.md).

## Used in

25 screens list it, for example
[S-F2-05 Record type gallery](../../../02-functional/f02-no-code-configuration/screens/01-configure-a-record-type/s-f02-05-record-type-gallery.md),
[S-F5-01 Post composer](../../../02-functional/f05-social-media/screens/01-publish-a-post/s-f05-01-post-composer.md),
[S-F15-01 Legal answer](../../../02-functional/f15-legal-assistant/screens/01-ask-a-legal-question/s-f15-01-legal-answer.md)
and
[S-F15-02 Legal warning](../../../02-functional/f15-legal-assistant/screens/02-receive-a-legal-warning/s-f15-02-legal-warning.md);
and every persona's home screen ([Views](../../views/README.md)).

## Open questions

None.

---

⬅️ [Data table](c-03-data-table.md) · ⬆️ [Up](README.md) · ➡️ [Modal](c-05-modal.md)
