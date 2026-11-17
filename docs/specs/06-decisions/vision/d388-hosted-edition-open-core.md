🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎯 [Decisions: Vision](README.md) ›
📜 D388 Hosted edition: closed services around the open core

# 📜 D388 Hosted edition: closed services around the open core

**Status:** ✅ decided

## Context

The owner asked that the fully hosted parts (F18 websites and domains, F19 feature factory, F20 support assistant) not
be open source; simple-ERP is AGPL-3.0 with no dual licence (D9, D376).

## Options

- Open core: separate closed services talking to simple-ERP only through its public API and MCP.
- Change the project's licence.
- Keep everything AGPL.

## Choice

Open core, confirmed by the owner on 2026-11-12: the AGPL product stays whole and open; the hosted-only parts are
separate programs run by the publisher, which reach simple-ERP only through its public API (T5) and MCP (T6), never
linking or copying AGPL code. What they produce inside a company's simple-ERP (a plugin, a page, a configuration)
follows the product's licence (D377). A lawyer confirms the boundary before launch.

## Decided by

The owner, on 2026-11-12, in the specification interview.

## Consequences

D9 unchanged; the vision's licence and business model pages name the hosted edition; no AGPL code in the closed services
(checked at each release).

Revised by D440 on 2026-11-12: the closed services use only the hosted edition's listed providers.

Clarified on 2026-11-12 after the review (R10, the owner's yes): besides the public API (T5) and MCP (T6), the support
assistant (F20) reads a customer's Kubernetes namespace (logs, events, metrics) through a read-only, audited, masked
service account and runs approved, scripted runbook operations; the DevOps agents (F25) read a masked copy of the
customer's company and write branches, pull requests and issues through their GitHub App; the websites service (F18)
drives DNS, registrar and CDN APIs; the feature factory (F19) builds plugins with the plugin SDK and publishes them
through the store's signing. None links or copies AGPL code; the lawyer reviews these interfaces.

## Related

- [Licence](../../00-vision/business/licence.md)
- [Business model](../../00-vision/business/business-model.md)

---

⬅️ [D387 F18 use cases](../f18-hosted-websites-and-domains/d387-f18-use-cases.md) · ⬆️ [Up](README.md) ·
➡️ [D389 Generated features are plugins](../f19-feature-factory/d389-generated-features-are-plugins.md)
