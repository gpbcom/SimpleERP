🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: Security and compliance](README.md) ›
📜 D240 Customers' credentials in a vault

# 📜 D240 Customers' credentials in a vault

**Status:** ✅ decided

## Context

The owner: the credentials customers send must be stored in a safe way.

## Options

- A dedicated vault with envelope encryption and just-in-time use.
- Encrypted columns in the database.

## Choice

A dedicated self-hosted secrets vault: envelope encryption with per-company keys under an HSM or KMS, write-only entry,
decryption only inside the run that needs it, never shown to a model, every use audited, customer-managed keys possible.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

REQ-T12-08; applies to every stored secret of the platform, not only connectors.

## Related

- [F16 Customer support agents](../../02-functional/f16-customer-support-agents/README.md)
- [T12 Connectors and scrapers](../../03-technical/t12-connectors-and-scrapers/README.md)
- [Security](../../05-non-functional/security.md)

---

⬅️ [D239 Connectors and scrapers generated on the fly](../f16-customer-support-agents/d239-scraper-factory.md) ·
⬆️ [Up](README.md) · ➡️ [D241 Deployable under security frameworks](d241-security-frameworks.md)
