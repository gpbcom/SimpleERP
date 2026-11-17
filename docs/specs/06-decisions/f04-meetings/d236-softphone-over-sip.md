🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎙️ [Decisions: F4 Meetings](README.md) ›
📜 D236 A softphone over the company's SIP

# 📜 D236 A softphone over the company's SIP

**Status:** ✅ decided

## Context

the benchmarked product provides its own telephony.

## Options

- A softphone over the company's SIP.
- Own numbers too.
- Keep D221.

## Choice

A softphone in the web, desktop and mobile apps registers on the company's own SIP phone system or trunk, with
click-to-call from any record and inbound calls on mobile; numbers come from the company's operator.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Extends D221; simple-ERP sells no telephony.

## Related

- [F4 Meetings](../../02-functional/f04-meetings/README.md)
- [Benchmark](../../05-non-functional/meeting-assistant-benchmark.md)
- [D221](d221-company-phone-system.md)

---

⬅️ [D235 Recruitment: interviews here, the rest in F9](d235-recruitment-split.md) · ⬆️ [Up](README.md) ·
➡️ [D237 Customer support agents](../f16-customer-support-agents/d237-customer-support-agents.md)
