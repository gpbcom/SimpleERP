🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) ›
📜 D208 Meeting sources

# 📜 D208 Meeting sources

**Status:** ✅ decided

## Context

Which meeting sources simple-ERP supports.

## Options

- Teams, Meet, Zoom.
- Self-hosted Jitsi and BigBlueButton.
- In-person recording.
- Phone calls.

## Choice

All four: the platforms' own transcripts and the bot (D7) for Teams, Meet and Zoom; Jitsi and BigBlueButton through the
bot or their recording hooks; in-person meetings recorded with the phone app or a computer's microphone; phone calls
through the company's phone system (SIP).

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Each source is a connection set up by the administrator (F1); the bot is announced (D23).

## Related

- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [D7](../foundations/d07-where-meetings-come-from.md)
- [D23](../foundations/d23-meeting-bot-consent.md)

---

⬅️ [D207](../f15-legal-assistant/d207-copyrighted-standards-register.md) · ⬆️ [Up](README.md) ·
➡️ [D209 What a meeting produces](d209-meeting-outputs.md)
