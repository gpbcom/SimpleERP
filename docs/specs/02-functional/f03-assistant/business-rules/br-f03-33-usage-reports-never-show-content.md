🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-33 Usage reports never show content

# 📏 BR-F3-33 Usage reports never show content

**Status:** ✅ specified

## Statement

The AI assistant usage dashboard counts by role or team, feature, day, provider and connection; it never shows a
question, an answer or a conversation, nor a person's own counts; feedback reasons are shown without their author.

## Why

Conversations are private by default (D141). See
[D185](../../../06-decisions/f03-assistant/d185-assistant-usage-dashboard.md).

## Examples

| Case | Result |
|---|---|
| "Questions per team this month" | Sales 412, HR 96 |
| An administrator wants Paul's questions | Not available |
| A thumbs down "out of date" | Counted; the knowledge item's owner is told which item, not who rated |

## Applies to

- [UC-F3-01](../use-cases/01-ask-the-assistant/uc-f03-01-ask-a-question-about-the-company-s-data.md),
  [UC-F3-07](../use-cases/07-manage-knowledge/uc-f03-07-manage-the-company-knowledge-base.md),
  [UC-F3-08](../use-cases/08-manage-and-share-conversations/uc-f03-08-manage-and-share-conversations.md)

## Exceptions

A team of fewer than 3 people is shown with its parent team.

The call log tab of the dashboard is the audit list of outside calls ([E-F3-08](../data/e-f03-08-outside-call.md)),
shown to the administrator only (D517): it names the user of each call, never its content.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F3-32 Retry before an error](br-f03-32-retry-before-an-error.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-34 All capabilities via the AI assistant](br-f03-34-every-capability-is-reachable-from-the-assistant.md)
