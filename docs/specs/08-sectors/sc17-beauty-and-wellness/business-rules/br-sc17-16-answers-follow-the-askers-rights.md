🏠 [Specs](../../../README.md) › 🏷️ [Sectors](../../README.md) › 💇 [SC17 Beauty and wellness](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-SC17-16 Answers follow the asker's rights

# 📏 BR-SC17-16 Answers follow the asker's rights

**Status:** 🔄 waiting for the owner

## Statement

The AI assistant answers and acts only within the rights of the person who asks: it reads only the records that person
may read and prepares only the actions that person may do, and an action is done only after that person confirms it.

## Why

An AI assistant with wider rights than its user would leak data and act without control. The owner asked for it in the
salon ([D561](../../../06-decisions/sectors/d561-benchmark-gaps-sc17-beauty-and-wellness.md)). It follows the shared
rule on confirmation
([BR-F3-07](../../../02-functional/f03-assistant/business-rules/br-f03-07-no-deletes-no-irreversible-acts.md)).

## Examples

| Case | Result |
|---|---|
| Manager asks about tomorrow's deposits | answered with sources |
| Beautician asks about payroll | refused |
| Action prepared | done only after confirmation |
| Question on another salon | answered if the manager has that right |
| No data | the AI assistant says so |

## Applies to

- [UC-SC17-16](../use-cases/04-commissions-and-tips/uc-sc17-16-ask-the-assistant-about-the-salon.md)
- [E-F3-01 Conversation](../../../02-functional/f03-assistant/data/e-f03-01-conversation.md)

## Exceptions

None.

## Configurable

The topics the AI assistant may answer on, by the administrator.

## Open questions

None.

---

⬅️ [BR-SC17-15](br-sc17-15-targets-are-seen-by-the-staff-member-and-the-manager.md) · ⬆️ [Up](README.md) ·
➡️ [BR-SC17-17](br-sc17-17-renters-keep-their-own-bookings-and-invoices.md)
