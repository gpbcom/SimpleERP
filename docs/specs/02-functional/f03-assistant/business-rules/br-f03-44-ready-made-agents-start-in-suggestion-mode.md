🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) › 🤖 [F3 Assistant](../README.md) ›
📏 [Business rules](README.md) › 📏 BR-F3-44 Ready-made agents start in suggestion mode

# 📏 BR-F3-44 Ready-made agents start in suggestion mode

**Status:** ✅ specified

## Statement

An agent created from a ready-made template starts in suggestion mode, where it prepares work and a named person
approves each item; it can act alone, within its thresholds, only after a trial of 20 suggestions or 14 days and a
decision of the owner or an administrator.

## Why

A template is written for many companies and knows nothing of this one: the first results must be checked by a person.
The owner's answer: "Ready-made agents"
([D522](../../../06-decisions/f03-assistant/d522-benchmark-gaps-f03-assistant.md)); thresholds follow
[BR-F3-35](br-f03-35-agents-follow-thresholds-and-limits.md).

## Examples

| Case | Result |
|---|---|
| A new Chase overdue invoices agent | drafts reminders, sends none until approved |
| 20 suggestions, 17 accepted | the owner may move it to act alone |
| Day 3 and 4 suggestions | still suggestion mode |
| The administrator asks to skip the trial | refused: the trial is part of the rule |

## Applies to

- [UC-F3-21 Switch on a ready-made agent](../use-cases/13-voice-agents-and-briefings/uc-f03-21-switch-on-a-ready-made-agent.md)
- [E-F3-24 Agent template](../data/e-f03-24-agent-template.md)
- [E-F3-15 Agent](../data/e-f03-15-agent.md)
- [UC-F3-11 Govern AI agents](../use-cases/10-benchmark-additions/uc-f03-11-govern-ai-agents.md)

## Exceptions

None.

## Configurable

Yes: the trial length, within 10 to 100 suggestions and 7 to 60 days.

## Open questions

None.

---

⬅️ [BR-F3-43](br-f03-43-voice-actions-are-confirmed-aloud-before-writing.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F3-45 Add-ins use the user's own rights](br-f03-45-add-ins-use-the-users-own-rights.md)
