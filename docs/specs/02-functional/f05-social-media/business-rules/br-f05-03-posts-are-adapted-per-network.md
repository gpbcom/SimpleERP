🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
📣 [F5 Social media and marketing](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F5-03 Posts are adapted per network

# 📏 BR-F5-03 Posts are adapted per network

**Status:** ✅ specified

## Statement

One post is prepared once and adapted per network: length limits, formats and ratios, hashtags, mentions, link previews;
a format a network's API does not allow is flagged before scheduling.

## Why

Each network has its own limits. See [D243](../../../06-decisions/f05-social-media/d243-social-formats.md).

## Examples

| Case | Result |
|---|---|
| A 2,000-character text to X | Shortened version proposed |
| A story for a network whose API refuses stories | Flagged |

## Applies to

Every F5 use case.

## Exceptions

None.

## Configurable

No.

## Open questions

None.

---

⬅️ [BR-F5-02 Automatic posts follow their event rule](br-f05-02-automatic-posts-follow-their-event-rule.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F5-04 AI content is marked](br-f05-04-ai-content-is-marked.md)
