🏠 [Specs](../../README.md) › ⚙️ [Technical capabilities](../README.md) › 🕸️ [Connectors and scrapers](README.md) ›
🛡️ Security

# 🛡️ Security

**Status:** ✅ specified

## Threats

- Theft of customers' credentials.
- A model tricked by a page or a message into an unwanted action (prompt injection).
- Generated code reaching other systems.
- Over-collection of personal data by scrapers.

## Controls

- The vault (REQ-T12-08): models never see secrets.
- Allow-listed actions per intent, write modes, budgets and step caps (REQ-T12-03); outside content treated as data,
  never as instructions.
- Sandboxes with egress allow-lists (REQ-T12-09).
- Lawful collection (REQ-T12-12).

## Open questions

None.

---

⬅️ [Data](data/README.md) · ⬆️ [Up](README.md) · ➡️ [Operations](operations.md)
