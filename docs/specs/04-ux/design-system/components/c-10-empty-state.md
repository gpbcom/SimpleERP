🏠 [Specs](../../../README.md) › 🎨 [UX](../../README.md) › 📐 [Design system](../README.md) › 🧩 [Components](README.md) ›
🧩 C-10 Empty state

# 🧩 C-10 Empty state

**Status:** 🔄 waiting for the owner

## Purpose

Tells what a list, panel or page will hold and how to start, when it holds nothing yet.

## Anatomy

```text
        [illustration]
   No meetings yet.
   Meetings you record appear here.
   [Record a meeting]
```

A flat illustration in the palette or an icon ([Imagery](../../visual-identity/imagery.md)), one sentence saying what is
missing, one sentence saying what comes here (optional), and the action that starts.

**Example images** (its variants and states, light and dark, D120):

| Shows | Device | Light | Dark |
|---|---|---|---|
| Variants and states | desktop | ![Variants and states, light](../images/c-10-empty-state-desktop-light.png) | ![Variants and states, dark](../images/c-10-empty-state-desktop-dark.png) |

## Variants

- **First use:** nothing created yet; the action creates or imports : "Add your first procedure, or sync a shared
  folder.", as on
  [S-F3-07 Knowledge base](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-07-knowledge-base.md).
- **No result:** search or filters match nothing; the action clears them (Proposed).
- **All done:** nothing waits for the user (Proposed: "Nothing waits for you." on "My tasks",
  [D48](../../../06-decisions/ux/d48-home-screen.md)).
- **Nothing happened:** a log with no entry: "Your provider has not entered SimpleERP.", as on
  [S-F1-11 Provider access log](../../../02-functional/f01-administration/screens/08-provider-and-client-companies/s-f01-11-provider-access-log.md).

## States

Shown, with its action enabled or not according to the user's rights; when the user may not create, the action is hidden
and the sentence says who can (Proposed).

## Tokens

`font-h3` for the sentence and `font-body` for the second (Proposed); `color-text-muted` for the second sentence; the
illustration in the palette ([Imagery](../../visual-identity/imagery.md)); spacing 24 or 32 px from the grid
([Tokens](../tokens.md)).

## Accessibility

- The illustration is decorative and hidden from screen readers; the words carry the meaning.
- The action is a real button, reachable by keyboard.

## Do and don't

- Do use the user's words and say what to do next ([Tone of voice](../../visual-identity/tone-of-voice.md)).
- Do offer the AI assistant when it can help start (Proposed).
- (Proposed) Don't show an empty table with only its headers.
- Don't blame or joke.

## Used in

[S-F3-01 Assistant panel](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-01-assistant-panel.md),
[S-F3-05 Configuration requests](../../../02-functional/f03-assistant/screens/05-find-and-get-guided/s-f03-05-configuration-requests.md),
[S-F3-06 My connections](../../../02-functional/f03-assistant/screens/06-use-an-outside-tool/s-f03-06-my-connections.md),
[S-F3-07 Knowledge base](../../../02-functional/f03-assistant/screens/07-manage-knowledge/s-f03-07-knowledge-base.md),
[S-F3-09 Conversation history](../../../02-functional/f03-assistant/screens/08-manage-and-share-conversations/s-f03-09-conversation-history.md),
[S-F3-13 Assistant usage dashboard](../../../02-functional/f03-assistant/screens/01-ask-the-assistant/s-f03-13-assistant-usage-dashboard.md)
and [S-F4-06 Meetings](../../../02-functional/f04-meetings/screens/04-find-and-reuse-meetings/s-f04-06-meetings.md); and
the empty state of every screen whose States list one.

## Open questions

None.

---

⬅️ [Chart](c-09-chart.md) · ⬆️ [Up](README.md) · ➡️ [Chat panel](c-11-chat-panel.md)
