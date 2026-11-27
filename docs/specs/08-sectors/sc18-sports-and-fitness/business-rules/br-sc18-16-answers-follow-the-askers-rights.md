🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 🏋️ [SC18 Sports and fitness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC18-16 Answers follow the asker's rights

# 📏 BR-SC18-16 Answers follow the asker's rights

**Status:** ✅ specified

## Statement

The AI assistant answers and acts only within the rights of the person who asks, never shows a member's health data to
anyone but the member and their coach, and does an action only after that person confirms it.

## Why

An AI assistant with wider rights than its user would leak health data and act without control. The owner asked for it
in the club ([D562](../../../06-decisions/sectors/d562-benchmark-gaps-sc18-sports-and-fitness.md)). It follows the
shared rule on confirmation
([BR-F3-07](../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md)).

## Examples

| Case | Result |
|---|---|
| Owner asks about classes below their minimum | answered with sources |
| Owner asks for a member's progress | refused |
| Action prepared | done only after confirmation |
| Coach asks about all members' payments | refused |
| No data | the AI assistant says so |

## Applies to

- [UC-SC18-16](../use-cases/04-personal-training/uc-sc18-16-ask-the-assistant-about-the-club.md)
- [E-F3-01 Conversation](../../../02-functional/f03-assistant/data/e-f03-01-conversation.md)

## Exceptions

None.

## Configurable

The topics the AI assistant may answer on, by the administrator.

## Open questions

None.

---

⬅️ [BR-SC18-15 Health data stays with the member and coach](br-sc18-15-health-data-stays-with-the-member-and-coach.md) ·
⬆️ [Up](README.md) ·
➡️ [BR-SC18-17 Members' rates apply only to valid members](br-sc18-17-members-rates-apply-only-to-valid-members.md)
