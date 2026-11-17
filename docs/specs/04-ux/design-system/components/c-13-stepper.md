🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-13 Stepper

# 🧩 C-13 Stepper

**Status:** 🔄 waiting for the owner

## Purpose

Shows where the user is in a task of several steps, what is done and what is left: the guided setup
([D54](../../../06-decisions/f01-administration/d54-guided-setup.md)).

## Anatomy

```text
(v)---(v)---(3)---(4)---(5)---(6)---(7)
Identity Money Sites Pack Users Import Done
```

One mark per step with its number and name; done steps show a check, the current step is highlighted.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-13-stepper-desktop-light.png) | ![Variants and states, dark](../images/c-13-stepper-desktop-dark.png) |

## Variants

- **Horizontal:** on desktops and tablets, up to seven steps (Proposed).
- **Compact:** on phones, "Step 3 of 7: Sites" with a progress bar (Proposed).

## States

| Step state | Look |
|---|---|
| Done | `color-success` mark with a check (as drawn) |
| Current | `color-primary` mark, label in weight 600 |
| To do | `color-border` mark, `color-text-muted` label |
| With an error | (Proposed) `color-error` mark with the (!) icon |
| Focus | The `color-primary` focus ring on a step that can be opened |

## Tokens

`color-primary`, `color-success`, `color-error`, `color-border`, `color-text-muted`; `font-caption` for labels
(Proposed: as drawn); motion 150 ms ([Motion](../../visual-identity/motion.md)).

## Accessibility

- A list with the current step marked `aria-current`; errors are linked to their field and announced, as on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).
- Done steps say "done" in words, not only by the check.

## Do and don't

- Do let users go back to a done step and keep what they saved, as on
  [S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md).
- Do let users leave and resume ([D54](../../../06-decisions/f01-administration/d54-guided-setup.md)).
- Don't use a stepper for parts that can be done in any order: use [C-07 Tabs](c-07-tabs.md).

## Used in

[S-F1-01 Setup wizard](../../../02-functional/f01-administration/screens/01-guided-setup/s-f01-01-setup-wizard.md); and
the [Wizard pattern](../patterns/wizard.md).

## Open questions

None.

---

⬅️ [File upload](c-12-file-upload.md) · ⬆️ [Up](README.md) · ➡️ [Timeline](c-14-timeline.md)
