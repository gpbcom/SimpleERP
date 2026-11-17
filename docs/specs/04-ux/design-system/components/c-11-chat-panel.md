🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-11 Chat panel

# 🧩 C-11 Chat panel

**Status:** ✅ specified

## Purpose

The AI assistant's panel (F3, F15), on any screen. See [D49](../../../06-decisions/ux/d49-assistant-side-panel.md).

## Anatomy

```text
+---------------------------------+
| Assistant      [legal] [x]      |
| About: Invoice INV-2026-00042   |
|---------------------------------|
| answers, with sources            |
|                                 |
|---------------------------------|
| [ Ask about this invoice...   ] |
+---------------------------------+
```

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-11-chat-panel-desktop-light.png) | ![Variants and states, dark](../images/c-11-chat-panel-desktop-dark.png) |

## Variants

- Desktop: a right panel, about a third of the width.
- Phone: full screen.

## States

Closed, open, thinking, answered, error, offline (on a field worker's phone).

## Tokens

`color-surface`, `elevation-2`, `font-body`.

## Accessibility

Answers are announced to screen readers as they arrive; the panel traps focus only on phones, where it is full screen;
Escape closes it.

## Do and don't

- Do show what the AI assistant is looking at ("About: ...").
- Don't let it show anything the user's permissions forbid (D12).

## Used in

Every screen: see [Views](../../views/README.md).

## Open questions

None.

---

⬅️ [Empty state](c-10-empty-state.md) · ⬆️ [Up](README.md) · ➡️ [File upload](c-12-file-upload.md)
