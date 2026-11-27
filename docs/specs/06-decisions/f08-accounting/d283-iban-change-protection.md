🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 📒 [Decisions: F8 Accounting](README.md) ›
📜 D283 Protection against IBAN fraud

# 📜 D283 Protection against IBAN fraud

**Status:** ✅ decided

## Context

What protects payments when a supplier's IBAN changes.

## Options

- Call-back, a second person, a delay.
- A second person only.
- Nothing.

## Choice

A new or changed IBAN is checked with the supplier by a known channel (call-back), approved by a second person, and the
first payment to it waits 48 hours; all logged.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F8-08.

## Related

- [F8 Accounting](../../02-functional/f08-accounting/README.md)

---

⬅️ [D282 F8 use cases and expense threshold](d282-f8-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D284 AI in bookkeeping](d284-ai-in-bookkeeping.md)
