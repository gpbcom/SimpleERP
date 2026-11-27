🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-08 Navigation

# 🧩 C-08 Navigation

**Status:** ✅ specified

## Purpose

The app shell: how a user moves between capabilities. See [D47](../../../06-decisions/ux/d47-app-shell.md).

## Anatomy

```text
+------+--------------------------------------------------+
| logo | [ search...          ] [AI] [bell] [site v] (avatar)|
+------+--------------------------------------------------+
| Home |                                                  |
| ...  |                 page content                     |
| ...  |                                                  |
+------+--------------------------------------------------+
phone: page content + bottom tabs [Home] [Tasks] [Assistant] [Me]
```

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-08-navigation-desktop-light.png) | ![Variants and states, dark](../images/c-08-navigation-desktop-dark.png) |

## Variants

- Desktop: sidebar expanded or collapsed to icons.
- Phone: bottom tab bar.

## States

Item: default, hover, focus, active (current page), with a badge for counts.

## Tokens

`color-primary` for the active item, `color-surface-alt` for the sidebar.

## Accessibility

A `nav` landmark with a name; the current page marked `aria-current`; a "skip to content" link first; every item
reachable by keyboard.

## Do and don't

- Do list only what the role can use.
- Don't hide a capability behind more than one level.

## Used in

Every screen: see [Views](../../views/README.md).

## Open questions

None.

---

⬅️ [Tabs](c-07-tabs.md) · ⬆️ [Up](README.md) · ➡️ [Chart](c-09-chart.md)
