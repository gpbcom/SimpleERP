🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-14 Flagged posts are moderated before publication

# 📏 BR-F16-14 Flagged posts are moderated before publication

**Status:** ✅ specified, ⚖️ lawyer review before launch (D574)

## Statement

A post flagged by the checks (spam, abuse, personal data, forbidden links) is not visible to anyone but the author and
the moderators until a moderator publishes it, with or without edits; a published post reported by a reader is hidden
until reviewed.

## Why

A public forum shows the company's name next to every post, and a post with another person's data or abuse cannot be
undone once read. The owner asked for a community forum
([D535](../../../06-decisions/f16-customer-support-agents/d535-benchmark-gaps-f16-customer-support-agents.md)).
(⚖️ lawyer review before launch, D574) The France-pack rule on moderation is still to write: to read the LCEN (loi
2004-575) art. 6 and Regulation (EU) 2022/2065 (Digital Services Act), art. 16.

## Examples

| Case | Result |
|---|---|
| A clean question | published at once |
| A reply with an email address | held, the moderator removes the address |
| A reported post | hidden until reviewed |
| A removed post | the author is told the reason and may appeal once |
| An AI answer | visible only after a moderator accepts it, marked as AI |

## Applies to

- [UC-F16-18](../use-cases/07-live-chat-voice-and-contracts/uc-f16-18-run-the-community-forum.md)
- [E-F16-13 Forum post](../data/e-f16-13-forum-post.md)
- [E-F16-13 Forum post](../data/e-f16-13-forum-post.md)

## Exceptions

None.

## Configurable

The checks' strictness and the forbidden terms, by the owner.

## Open questions

None.

---

⬅️ [BR-F16-13 Every customer request becomes one work request](br-f16-13-every-request-becomes-a-work-request.md) ·
⬆️ [Up](README.md) · ➡️ [BR-F16-15](br-f16-15-the-ai-hands-over-to-a-person-with-the-full-history.md)
