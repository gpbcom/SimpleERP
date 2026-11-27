🏠 [Specs](../../README.md) › 📜 [Decisions](../README.md) › 🎯 [Decisions: Vision](README.md) ›
📜 D373 Sovereign, AI-native, one suite that replaces the rest

# 📜 D373 Sovereign, AI-native, one suite that replaces the rest

**Status:** ✅ decided

## Context

SimpleERP competes with AI meeting assistants, support-agent platforms, classic ERPs and AI-native ERPs. Its stance
against them had to be chosen.

## Options

- One suite replaces all.
- An Odoo alternative with AI.
- AI-native first.
- Sovereign AI-native.

## Choice

Sovereign, AI-native and one fully integrated suite that replaces them all. Meetings and tickets land on the ERP's own
records; the AI acts through the ERP's own API and permissions; the company's data is never copied to a third party. The
agents also act on outside systems (customer back offices, other tools) through MCP, A2A and connectors, and through
browser automation where a tool has no API (T12).

## Decided by

The owner, on 2026-11-11, in the specification interview.

## Consequences

The claim is "your own data is never scraped or copied to a third party", not "no scraping": T12 drives outside tools
without an API. The named benchmark keeps the claim honest.

Revised by D440 on 2026-11-12: the promise is reworded to what is true: the company's data stays on its servers by
default and goes outside only to a provider an administrator chose; customers' data never goes into GitHub.

Revised by D447 on 2026-11-12: the hosted-only services are named plainly: F18, F19, F20 and F25.

## Related

[🧭 Positioning](../../00-vision/product/positioning.md) · [⚖️ Benchmark](../../00-vision/benchmark/benchmark.md)

---

⬅️ [D372 The problem and who has it](d372-problem-and-targets.md) · ⬆️ [Up](README.md) ·
➡️ [D374 Revenue and pricing](d374-revenue-and-pricing.md)
