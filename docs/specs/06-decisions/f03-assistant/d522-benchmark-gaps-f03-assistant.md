🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🤖 [Decisions: F3 Assistant](README.md) ›
📜 D522 Benchmark gaps of F3 Assistant

# 📜 D522 Benchmark gaps of F3 Assistant

**Status:** ✅ specified

## Context

The 2026-11-14 benchmark-gaps interview compared the specifications with the voice, agent and briefing features of the
benchmarked suites and offered each gap as an option
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "F3 Assistant").

## Options

- Take each gap as a use case of F3 in a new flow, or leave it out.
- Voice is a use case with a business rule and no entity of its own, since the spoken turns are saved as text in the
  conversation.

## Choice

The owner selected all five gaps; each becomes a use case of F3, drawn in
[FL-F3-13 Voice, agents and briefings](../../02-functional/f03-assistant/flows/fl-f03-13-voice-agents-and-briefings.md).

| Gap | Use case | The owner's answer |
|---|---|---|
| G35 | [UC-F3-20 Talk to the AI assistant hands-free](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-20-talk-to-the-assistant-hands-free.md) | "Hands-free voice" |
| G36 | [UC-F3-21 Switch on a ready-made agent](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-21-switch-on-a-ready-made-agent.md) | "Ready-made agents" |
| G37 | [UC-F3-22 Use ERP data in a spreadsheet add-in](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-22-use-erp-data-in-a-spreadsheet-add-in.md) | "Spreadsheet add-ins" |
| G38 | [UC-F3-23 Read the daily briefing](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-23-read-the-daily-briefing.md) | "Daily briefing" |
| G13 | [UC-F3-24 Keep personal to-dos and memos](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-24-keep-personal-to-dos-and-memos.md) | "Personal to-dos and memos" |

## Decided by

The owner, on 2026-11-14, in the benchmark-gaps interview
(interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository), section "Block by block").

## Consequences

- Use cases
  [UC-F3-20 Talk to the AI assistant hands-free](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-20-talk-to-the-assistant-hands-free.md)
  to
  [UC-F3-24 Keep personal to-dos and memos](../../02-functional/f03-assistant/use-cases/13-voice-agents-and-briefings/uc-f03-24-keep-personal-to-dos-and-memos.md),
  screens
  [S-F3-24 Voice mode](../../02-functional/f03-assistant/screens/13-voice-agents-and-briefings/s-f03-24-voice-mode.md)
  to [S-F3-28 My to-dos](../../02-functional/f03-assistant/screens/13-voice-agents-and-briefings/s-f03-28-my-to-dos.md),
  rules
  [BR-F3-43 Voice actions are confirmed aloud before writing](../../02-functional/f03-assistant/business-rules/br-f03-43-voice-actions-are-confirmed-aloud-before-writing.md)
  to
  [BR-F3-47 To-dos are private unless shared](../../02-functional/f03-assistant/business-rules/br-f03-47-to-dos-are-private-unless-shared.md),
  entities [E-F3-24 Agent template](../../02-functional/f03-assistant/data/e-f03-24-agent-template.md) to
  [E-F3-27 To-do](../../02-functional/f03-assistant/data/e-f03-27-to-do.md) and their lists
  [S-F3-L24 Agent templates](../../02-functional/f03-assistant/screens/00-lists/s-f03-l24-agent-templates.md) to
  [S-F3-L27 To-dos](../../02-functional/f03-assistant/screens/00-lists/s-f03-l27-to-dos.md).
- Voice never identifies a person by their voice
  ([BR-F4-02 No voice prints](../../02-functional/f04-meetings/business-rules/br-f04-02-no-voice-prints.md)).
- Ready-made agents follow the thresholds of
  [BR-F3-35 Agents follow thresholds and amount limits](../../02-functional/f03-assistant/business-rules/br-f03-35-agents-follow-thresholds-and-limits.md)
  and the audit agent of
  [BR-F3-36 An audit agent checks the agents](../../02-functional/f03-assistant/business-rules/br-f03-36-an-audit-agent-checks-agents.md).

## Related

- [FL-F3-13 Voice, agents and briefings](../../02-functional/f03-assistant/flows/fl-f03-13-voice-agents-and-briefings.md)
- [D460 F3 Assistant: gaps and improvements](d460-f03-gaps-and-improvements.md)
- Interview record (the owner's interview of 2026-11-14 on the benchmark gaps, not kept in the repository)

---

⬅️ [D521](../f02-no-code-configuration/d521-benchmark-gaps-f02-no-code-configuration.md) · ⬆️ [Up](README.md) ·
➡️ [D523 Benchmark gaps of F4 Meetings](../f04-meetings/d523-benchmark-gaps-f04-meetings.md)
