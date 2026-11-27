🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-01 Button

# 🧩 C-01 Button

**Status:** 🔄 waiting for the owner

## Purpose

Starts an action. Its label is a verb, in the user's business words: "Send quote", "Approve"
([Tone of voice](../../visual-identity/tone-of-voice.md)).

## Anatomy

```text
+------------------------------+
| [icon]  Send quote           |
+------------------------------+
```

1. **Label:** a verb and, when needed, its object.
2. **Icon:** optional, a Lucide icon at 20 px before the label ([Iconography](../../visual-identity/iconography.md)).

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-01-button-desktop-light.png) | ![Variants and states, dark](../images/c-01-button-desktop-dark.png) |

## Variants

- **Primary:** `color-primary` fill and white text (6.44:1, [Colours](../../visual-identity/colours.md)); the main
  action of a view or a dialog, such as the action that fixes an error in the
  [error message pattern](../patterns/error-messages.md). (Proposed) One primary button per view or dialog.
- **Secondary:** `color-surface` with a `color-border-strong` edge; the other actions, such as "Cancel".
- **Danger:** `color-error` text and edge on `color-surface`, for destructive actions; (Proposed) it always opens a
  confirmation ([C-05 Modal](c-05-modal.md)).
- **Ghost:** (Proposed) `color-primary` text with no edge, as drawn, for minor actions in tables and cards.
- **Icon only:** for toolbars; it always has an accessible name ([Iconography](../../visual-identity/iconography.md)).
- **Phone:** (Proposed) full width, as drawn; in a stack, the primary action comes first, on top.

## States

| State | Look |
|---|---|
| Default | As its variant |
| Hover | (Proposed) The fill or edge 8 % darker in light mode and 8 % lighter in dark mode |
| Focus | A 2 px focus ring in `color-primary` (the colour's stated use), offset 2 px (Proposed) |
| Active | (Proposed) Pressed: the hover look, without elevation |
| Disabled | (Proposed) `color-text-muted` on `color-surface-alt`; a tooltip says why when the reason is not visible |
| Error | A button has no error state; the error shows on the field or in the message ([error message pattern](../patterns/error-messages.md)) |
| Loading | (Proposed) A spinner replaces the icon, the label stays, and the button cannot be pressed twice |

## Tokens

`color-primary`, `color-surface`, `color-border-strong`, `color-error`, `color-text`, `color-text-muted`; height
`field-height` (44 px comfortable, 32 px compact, [Tokens](../tokens.md)) (Proposed: buttons as high as fields); radius
8 px (Proposed: as fields); `font-label` (Inter 14 / 20 px, weight 500,
[Typography](../../visual-identity/typography.md)); motion 150 ms ([Motion](../../visual-identity/motion.md)).

## Accessibility

- A native button (or a link when it opens a page), activated with Enter and Space.
- Its name is its label; an icon-only button has an accessible name
  ([Iconography](../../visual-identity/iconography.md)).
- A button that acts on several records states how many: "Confirm 12 changes", as on
  [S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md).
- The focus ring is always visible; white on `color-primary` meets AA ([Colours](../../visual-identity/colours.md)).
- Touch targets: 44 px high on phones (phones always comfortable,
  [D42](../../../06-decisions/ux/d42-density-per-role.md)); the field worker's phone screens use large touch targets
  ([D50](../../../06-decisions/ux/d50-field-screens-for-rare-users.md)).

## Do and don't

- Do write the action on the button: "Hand over and deactivate", not "OK", as on
  [S-F1-05 Offboarding](../../../02-functional/f01-administration/screens/03-user-lifecycle/s-f01-05-offboarding.md).
- Do put "Cancel" before the primary action, on the right of a dialog (Proposed: as drawn).
- Don't use the accent colour for a button's text: accent is never text on white
  ([Colours](../../visual-identity/colours.md)).
- Don't show colour as the only difference between two buttons: their words differ.

## Used in

Every screen and every error message ([error message pattern](../patterns/error-messages.md)); listed by name in
[S-F3-02 Change confirmation card](../../../02-functional/f03-assistant/screens/03-act-through-the-assistant/s-f03-02-change-confirmation-card.md),
[S-F3-04 Show me overlay](../../../02-functional/f03-assistant/screens/05-find-and-get-guided/s-f03-04-show-me-overlay.md),
[S-F3-06 My connections](../../../02-functional/f03-assistant/screens/06-use-an-outside-tool/s-f03-06-my-connections.md)
and
[S-F4-03 Phone recorder](../../../02-functional/f04-meetings/screens/02-record-in-person-or-by-phone/s-f04-03-phone-recorder.md).

## Open questions

None.

---

⬆️ [Up](README.md) · ➡️ [Form field](c-02-form-field.md)
