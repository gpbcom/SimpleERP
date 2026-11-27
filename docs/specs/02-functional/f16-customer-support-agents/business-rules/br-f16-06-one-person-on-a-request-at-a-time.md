🏠 [Specs](../../../README.md) › 🧩 [Functional capabilities](../../README.md) ›
🎧 [F16 Customer support agents](../README.md) › 📏 [Business rules](README.md) ›
📏 BR-F16-06 One person on a request at a time

# 📏 BR-F16-06 One person on a request at a time

**Status:** ✅ specified

## Statement

When an office worker opens a request to answer it, the request is locked to them; another person sees who has it and
can only read, until it is released, sent or 15 minutes pass without activity.

## Why

Two people answering the same customer give contradictory answers (D473).

## Examples

| Case | Result |
|---|---|
| Worker A opens request 5512, worker B opens it | B sees "A is answering", read only |
| A idle 16 minutes | lock released |
| Support lead takes over | lead may take the lock, A is told |

## Applies to

- [UC-F16-08 Support requests in the agent workspace](../use-cases/04-human-agent-workspace/uc-f16-08-work-requests-in-the-agent-workspace.md)

## Exceptions

The support lead may take over a locked request.

## Configurable

The idle time 15 minutes.

## Open questions

None.

---

⬅️ [BR-F16-05 Service levels per priority](br-f16-05-service-levels-per-priority.md) · ⬆️ [Up](README.md) ·
➡️ [BR-F16-07 Refund limits per intent](br-f16-07-refund-limits-per-intent.md)
