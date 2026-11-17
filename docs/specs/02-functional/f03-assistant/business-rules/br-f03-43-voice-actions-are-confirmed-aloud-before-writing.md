🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-43 Voice actions are confirmed aloud before writing

# 📏 BR-F3-43 Voice actions are confirmed aloud before writing

**Status:** ✅ specified

## Statement

When the user speaks to the AI assistant, any action that would write to the company's data is read back with its key
values and saved only after the user says confirm or taps Confirm; silence for 10 seconds or the word cancel saves
nothing; what the AI assistant cannot do by voice (deletes, sending out, payments) opens the confirmation card on
screen.

## Why

Speech recognition makes mistakes, especially on names, amounts and dates. The owner's answer: "Hands-free voice"
([D522](../../../06-decisions/f03-assistant/d522-benchmark-gaps-f03-assistant.md));
[BR-F3-28](br-f03-28-hands-free-confirmations-are-spoken.md) already speaks the confirmation in the phone app, and this
rule makes it the rule for every voice entry.

## Examples

| Case | Result |
|---|---|
| Create a visit report for Dupont tomorrow at nine | read back with the customer and the time, saved after confirm |
| The user says nothing for 10 seconds after the read-back | nothing is saved |
| Delete the Dupont quote | refused by voice, the card opens on screen ([BR-F3-07](br-f03-07-no-deletes-no-irreversible-acts.md)) |
| A question without a change | answered at once, no confirmation |
| Pay the supplier invoice | refused by voice |

## Applies to

- [UC-F3-20 Talk to the AI assistant hands-free](../use-cases/13-voice-agents-and-briefings/uc-f03-20-talk-to-the-assistant-hands-free.md)
- [UC-F3-09 Use the AI assistant on a phone](../use-cases/09-assistant-on-a-phone/uc-f03-09-use-the-assistant-on-a-phone.md)
- [S-F3-24 Voice mode](../screens/13-voice-agents-and-briefings/s-f03-24-voice-mode.md)

## Exceptions

None.

## Configurable

No: the list of actions that never run by voice is part of [BR-F3-07](br-f03-07-no-deletes-no-irreversible-acts.md).

## Open questions

None.

---

⬅️ [BR-F3-42 Unanswered topics hold no names](br-f03-42-unanswered-topics-hold-no-names.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-44 Ready-made agents start in suggestion mode](br-f03-44-ready-made-agents-start-in-suggestion-mode.md)
