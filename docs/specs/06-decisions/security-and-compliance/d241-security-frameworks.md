🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🛡️ [Decisions: Security and compliance](README.md) ›
📜 D241 Deployable under security frameworks

# 📜 D241 Deployable under security frameworks

**Status:** ✅ decided

## Context

The owner: the project must be deployable in SecNumCloud, SOC 2 and other security norms.

## Options

- Compliance profiles per deployment.
- One generic deployment.

## Choice

SimpleERP ships compliance deployment profiles and the evidence to obtain or support: SecNumCloud (on a qualified
host), SOC 2 Type II, ISO/IEC 27001 (with 27017, 27018, 27701), HDS, NIS2, DORA, GDPR, the Cyber Resilience Act, and the
national schemes C5 (Germany) and ENS (Spain); PCI DSS by never storing card numbers.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

Constraints on every capability; designed at step 19f.

## Related

- [Security](../../05-non-functional/security.md)
- [Technical security](../../../technical/security/security.md)

---

⬅️ [D240 Customers' credentials in a vault](d240-credential-vault.md) · ⬆️ [Up](README.md) ·
➡️ [D242 Social networks](../f05-social-media/d242-social-networks.md)
