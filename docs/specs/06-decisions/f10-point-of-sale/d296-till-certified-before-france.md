🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🏪 [Decisions: F10 Point of sale (plugin)](README.md) ›
📜 D296 Till certified before selling in France

# 📜 D296 Till certified before selling in France

**Status:** ✅ decided

## Context

French till software needs a certificate from an accredited body or the publisher's individual attestation (CGI art. 286
I 3° bis; the attestation route was removed in February 2025 and restored in February 2026). Answers Q2.

## Options

- Certify before French sale.
- Certify later, rules now.
- Outside France first.

## Choice

F10 is built to the till rules of the country pack from the first version (inalterability, security, closures,
conservation, archives) and is sold in France only once it holds a certificate from an accredited body (NF525 or
equivalent); the attestation route is not used.

## Decided by

The owner, on 2026-11-10, in the specification interview.

## Consequences

BR-F10-01; the certification audit is a release step of F10; a major version needs a new certificate.

## Related

- [F10 Point of sale](../../02-functional/f10-point-of-sale/README.md)

---

⬅️ [D295 Point of sale coverage](d295-pos-coverage.md) · ⬆️ [Up](README.md) ·
➡️ [D297 Point of sale personas](d297-pos-personas.md)
