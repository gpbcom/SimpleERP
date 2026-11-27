🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) ›
🌐 [Decisions: F18 Hosted websites and domains (hosted edition)](README.md) ›
📜 D385 Hosted websites and domains coverage

# 📜 D385 Hosted websites and domains coverage

**Status:** ✅ decided

## Context

The owner asked that the fully hosted edition generate each customer's website and its DNS through the cloud providers'
APIs (PLAN D32).

## Options

- Site, domain, DNS and mail records.
- Site and DNS only.
- A SimpleERP sub-domain only.

## Choice

Confirmed and extended by the owner on 2026-11-12: the site built from the company's ERP data and its visual identity,
at least a contact page, a careers page connected to LinkedIn and Indeed through SimpleERP, which synchronises and
aggregates every application, the domain bought, transferred or connected through a registrar's API, the DNS zone, TLS
certificates and mail records (SPF, DKIM, DMARC) managed through the provider's API, behind one interface; European
providers first (for example OVHcloud, Scaleway, Gandi), others later behind the same interface, as for the hosting
(D375), confirmed by the owner on 2026-11-12 (D418).

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

A closed hosted service (D388); twenty use cases (D387).

## Related

- [F18 Hosted websites and domains](../../02-functional/f18-hosted-websites-and-domains/README.md)

---

⬅️ [D384 F17 use cases](../f17-competitive-analysis/d384-f17-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D386 A site is tested before it goes live](d386-website-publication-gate.md)
