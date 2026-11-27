🏠 [Specs](../../../README.md) › 🌍 [Country packs](../../README.md) › 🇫🇷 [France](../README.md) ›
🔒 [Data protection](README.md) › ⚖️ CR-FR-052 Personal data kept no longer than needed

# ⚖️ CR-FR-052 Personal data kept no longer than needed

**Status:** ✅ specified

## Statement

Personal data has a retention period and is deleted at its end.

## Values

- Leaver's private AI assistant history: deleted at deactivation.
- Unused assistant conversation: 12 months by default.
- Meeting audio and video: deleted once the transcript is checked, 7 days by default.
- Leads: 3 years after the last contact (CNIL).
- Activity drafts: 7 days.

## Legal references

- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) art. 5(1)(e).
- [CNIL guidance](https://www.cnil.fr/fr/professionnels).

## Effective dates

Since 2018-05-25.

## Enforced by

- [BR-F1-10 A leaver's AI assistant history is deleted](../../../02-functional/f01-administration/business-rules/br-f01-10-leavers-assistant-history-deleted.md)
- [BR-F3-27 Conversation retention](../../../02-functional/f03-assistant/business-rules/br-f03-27-conversation-retention.md)
- [BR-F4-03 Recordings are deleted once checked](../../../02-functional/f04-meetings/business-rules/br-f04-03-recordings-are-deleted-once-checked.md)
- [Data](../../../02-functional/f06-customers-and-sales/data/README.md)
- [BR-F9-07 Activity drafts stay private](../../../02-functional/f09-hr-and-projects/business-rules/br-f09-07-activity-drafts-stay-private.md)
- [Data retention](../../../05-non-functional/data-retention.md)
- [UC-SC07-23 Run last-mile rounds](../../../08-sectors/sc07-transport/use-cases/07-passengers-removals-courier-and-freight/uc-sc07-23-run-last-mile-rounds.md)

## When the law changes

Watched in the law corpus: GDPR art. 5. A change flags this rule and warns the administrators; the corrected rule ships
in a pack update (D294).

## Penalty

Up to 20 000 000 EUR or 4 % of turnover (GDPR art. 83(5)).

## Exceptions

None.

## Open questions

A company may choose "never" for conversations (BR-F3-27) and extend recordings with no cap (BR-F4-03): the
pack sets a maximum for each, to be confirmed by the owner.

---

⬅️ [CR-FR-051 Access and erasure requests](cr-fr-051-access-and-erasure.md) · ⬆️ [Up](README.md) ·
➡️ [CR-FR-053 No biometric voice prints](cr-fr-053-no-biometric-voice-prints.md)
