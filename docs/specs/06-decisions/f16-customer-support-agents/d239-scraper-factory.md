🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎧 [Decisions: F16 Customer support agents](README.md) ›
📜 D239 Connectors and scrapers generated on the fly

# 📜 D239 Connectors and scrapers generated on the fly

**Status:** ✅ decided

## Context

Many back-office tools and websites have no API; writing each connector by hand does not scale.

## Options

- A factory generating them, with tests and review.
- Hand-written only.

## Choice

A scraper and connector factory: a resumable graph (find the target, discover, sample, author with a model tier ladder,
guard, sandbox test, live probe, feedback, review, activate), a cost budget, a progress stream and a Stop button.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

REQ-T12-06 and REQ-T12-13; generated code runs only in the sandbox (REQ-T12-09).

## Related

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)

---

⬅️ [D238 Static workflows or agents](d238-static-or-agentic.md) · ⬆️ [Up](README.md) ·
➡️ [D240 Customers' credentials in a vault](../security-and-compliance/d240-credential-vault.md)
